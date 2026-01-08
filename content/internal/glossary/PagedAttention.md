+++
title = "Glosario: PagedAttention y gestión avanzada de memoria para la inferencia de LLM"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "glossary-pagedattention-and-advanced-memory-management-for-llm-inference"
description = "Explora PagedAttention, un algoritmo de gestión de memoria que divide la caché KV de los LLMs en bloques de tamaño fijo, reduciendo el desperdicio de memoria GPU durante la inferencia y potenciando vLLM."
keywords = ["PagedAttention", "inferencia LLM", "caché KV", "vLLM", "gestión de memoria"]
category = "Inferencia LLM"
type = "glossary"
draft = false
url = "/internal/glossary/PagedAttention/"

+++
## PagedAttention

PagedAttention es un algoritmo de gestión de memoria que divide la caché de Claves y Valores (KV) de un modelo de lenguaje grande (LLM) en bloques de tamaño fijo ("páginas"), permitiendo asignaciones no contiguas y reduciendo drásticamente el desperdicio de memoria GPU durante la inferencia. El método fue introducido por Kwon et al. en ["Efficient Memory Management for Large Language Model Serving with PagedAttention"](https://arxiv.org/abs/2309.06180) y es la base del motor de inferencia [vLLM](https://github.com/vllm-project/vllm).

**Características clave:**- La caché KV se divide en bloques pequeños y de tamaño fijo (páginas) en lugar de grandes búferes contiguos.
- Cada secuencia rastrea su mapeo lógico-físico de memoria a través de una tabla de bloques (tabla de páginas).
- Los bloques de una secuencia pueden estar repartidos por la memoria, reduciendo tanto la fragmentación interna como externa.
- La memoria puede compartirse entre secuencias, permitiendo muestreo paralelo eficiente y decodificación avanzada.
- Se previenen errores de memoria insuficiente (OOM) mediante asignación bajo demanda y reutilización rápida de bloques.

**Resumen técnico y visuales:**- En el servicio tradicional de LLM, la caché KV de cada solicitud se preasigna como un bloque contiguo único, lo que lleva a un desperdicio significativo de memoria si las secuencias son cortas o varían los tamaños de lote/longitud de secuencia.
- PagedAttention, inspirado en la paginación de memoria virtual de los sistemas operativos, permite que las secuencias usen solo la memoria necesaria, con una utilización casi óptima ([blog de vLLM](https://blog.vllm.ai/2023/06/20/vllm.html), [diccionario Hopsworks](https://www.hopsworks.ai/dictionary/pagedattention)).

> Para diagramas animados y explicaciones más profundas, consulta el [blog oficial de vLLM](https://blog.vllm.ai/2023/06/20/vllm.html).

## Caché KV

La caché de Claves y Valores (KV) es un componente fundamental de la inferencia basada en transformadores de LLM. En cada paso de decodificación, el modelo genera tensores de clave y valor para cada token, que codifican relaciones contextuales para el mecanismo de atención.

- **Propósito:**Almacena claves y valores de atención precomputados para que el modelo no tenga que recalcularlos para cada token, acelerando drásticamente la inferencia.
- **Tamaño:**En modelos como LLaMA-13B, la caché KV de una única secuencia puede alcanzar 1,7 GB; para [procesamiento por lotes](/es/glossary/batch-processing/) y secuencias largas, el tamaño total de la caché puede llegar a 40 GB ([fuente](https://arxiv.org/pdf/2309.06180), [Hopsworks](https://www.hopsworks.ai/dictionary/pagedattention)).
- **Desafío:**La caché es grande y dinámica: su tamaño depende del número de secuencias activas, su longitud y el tamaño del lote.
- **Impacto:**La gestión ineficiente de la caché KV limita severamente la cantidad de solicitudes que pueden procesarse en paralelo, aumentando los costes y reduciendo el aprovechamiento del hardware.

Para una exploración en profundidad del papel y optimización de la caché KV en los LLMs, consulta ["KV Cache Optimization: A Deep Dive"](https://medium.com/foundation-models-deep-dive/kv-cache-guide-part-4-of-5-system-superpowers-framework-realities-kv-cache-in-action-6fb4fb575cf8).

## Fragmentación de memoria

La fragmentación se refiere al uso ineficiente de la memoria disponible debido a esquemas rígidos de asignación y liberación, un problema crítico en la inferencia de LLM en GPUs.

### Fragmentación interna

Ocurre cuando los bloques de memoria preasignados son mayores que la memoria realmente utilizada por una secuencia, dejando espacio sin usar "dentro" de la asignación.

- **Ejemplo:**Si a cada secuencia se le asigna espacio para 2048 tokens pero solo usa 200, el resto se desperdicia.
- **Gravedad:**Los sistemas tradicionales de servicio de LLM pueden desperdiciar hasta un 80% de la memoria GPU por fragmentación interna ([artículo arXiv, Fig. 2](https://arxiv.org/pdf/2309.06180), [guía técnica Doubleword](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention)).

### Fragmentación externa

Ocurre a medida que secuencias de diferentes longitudes comienzan y terminan. La memoria libre queda dispersa en pequeños fragmentos no contiguos que son demasiado pequeños para nuevas asignaciones.

- **Resultado:**Incluso si la memoria libre total es suficiente, no puede usarse para nuevas solicitudes por falta de espacio contiguo.

PagedAttention elimina ambos tipos de fragmentación asignando y liberando pequeños bloques bajo demanda, similar a la paginación de memoria virtual de los sistemas operativos ([artículo de Red Hat Developer](https://developers.redhat.com/articles/2025/07/24/how-pagedattention-resolves-memory-waste-llm-systems)).

## Memoria virtual y paginación

Un concepto clásico de sistemas operativos adaptado para LLMs en PagedAttention.

- **Memoria virtual:**Separa las direcciones lógicas de memoria (usadas por procesos/secuencias) de las ubicaciones físicas, permitiendo almacenamiento no contiguo y asignación eficiente.
- **Paginación:**La memoria se divide en páginas pequeñas y de tamaño fijo (bloques). Las páginas lógicas se asignan a la memoria física mediante una tabla de páginas.
- **En el servicio de LLM:**La caché KV de cada secuencia se divide en bloques; cada bloque puede residir en cualquier parte de la memoria GPU. Las secuencias mantienen una tabla de bloques que mapea posiciones de tokens lógicas a bloques físicos de memoria.

Esta abstracción permite:
- Asignación bajo demanda
- Reutilización inmediata de bloques liberados
- Compartición de memoria entre secuencias (copy-on-write para modificaciones)

Para antecedentes técnicos: ["Operating Systems: Three Easy Pieces" (Memoria Virtual)](https://pages.cs.wisc.edu/~remzi/OSTEP/vm-intro.pdf).

## Tabla de bloques (tabla de páginas)

Estructura de datos mantenida por PagedAttention para mapear el orden lógico de los tokens en una secuencia con los bloques de memoria física reales.

- **Propósito:**Permite a cada secuencia reconstruir su contexto para el cálculo de atención sin importar dónde estén almacenados físicamente sus bloques.
- **Funcionalidad:**Permite búsquedas rápidas y asignación/liberación de bloques a medida que se generan tokens o terminan secuencias.
- **Sobrecarga:**La tabla de búsqueda introduce una pequeña sobrecarga computacional, pero la reducción en desperdicio de memoria compensa ampliamente este coste ([artículo arXiv, Sec. 4.1](https://arxiv.org/pdf/2309.06180)).

## Compartición de memoria

PagedAttention permite que los bloques de memoria se compartan entre secuencias y solicitudes, lo cual es especialmente beneficioso para el muestreo paralelo y la decodificación avanzada.

### Muestreo paralelo

- **Caso de uso:**Generar múltiples completaciones a partir del mismo prompt.
- **Ventaja:**Los bloques de caché KV del prompt se comparten (no se duplican) entre todas las salidas, reduciendo el uso de memoria y permitiendo mayor rendimiento ([blog de vLLM, diagrama de muestreo paralelo](https://blog.vllm.ai/2023/06/20/vllm.html)).
- **Mecanismo técnico:**Las tablas de bloques de cada muestra apuntan a los mismos bloques físicos para las partes compartidas de la secuencia.

### Búsqueda en haz y decodificación mixta

- **Búsqueda en haz:**Múltiples haces suelen compartir el mismo prefijo; PagedAttention permite compartir los bloques de prefijo entre haces.
- **Decodificación mixta:**Atiende simultáneamente solicitudes con estrategias greedy, sampling y beam search sin asignaciones redundantes de memoria.

## Copy-on-Write

Técnica de gestión de memoria para asegurar la modificación segura de bloques de memoria compartida.

- **Cómo funciona:**Cuando una secuencia necesita modificar un bloque compartido (varias referencias), se crea una copia nueva solo para esa secuencia. Las demás siguen referenciando el bloque original.
- **Ventaja:**Permite compartir memoria sin riesgo de corrupción de datos o condiciones de carrera.

## Cálculo de atención con paginación

Los kernels de atención tradicionales esperan regiones de memoria contiguas para las claves y valores. PagedAttention introduce un kernel de atención personalizado que puede recuperar eficientemente las claves y valores de bloques no contiguos según lo especificado en la tabla de bloques.

- **Implementación:**En cada paso de inferencia, el kernel consulta la tabla de bloques para reunir todos los vectores de clave y valor necesarios, aunque estén dispersos ([arXiv Sec. 4.1](https://arxiv.org/pdf/2309.06180)).
- **Rendimiento:**Sobrecarga computacional mínima, pero enorme reducción en desperdicio de memoria y aumento correspondiente en rendimiento.

## vLLM

[vLLM](https://github.com/vllm-project/vllm) es un motor open source de inferencia y servicio de LLM de alto rendimiento desarrollado en UC Berkeley. Implementa PagedAttention como su algoritmo central de gestión de memoria.

- **Características clave:**- Rendimiento líder (hasta 24x respecto a HuggingFace Transformers)
    - Desperdicio de memoria drásticamente menor (de 60–80% a menos del 4%)
    - Soporte para grandes lotes, secuencias largas y decodificación avanzada
    - Compatible con modelos de HuggingFace, PyTorch y la API de OpenAI
    - Usado en LMSYS Chatbot Arena, Databricks, Dropbox, AWS, AMD, NVIDIA y más

Para benchmarks y guías de despliegue, consulta la [documentación de vLLM](https://docs.vllm.ai/en/latest/getting_started/quickstart.html).

## Detalles de implementación y uso

PagedAttention está disponible vía [vLLM](https://github.com/vllm-project/vllm).  
**Instalación:**```bash
pip install vllm
```
**Ejecutar un modelo:**```bash
python -m vllm.entrypoints.openai.api_server --model <model_name>
```
- Sustituye `<model_name>` por cualquier [modelo soportado](https://docs.vllm.ai/en/latest/models/supported_models.html).

**Escenarios de uso clave:**- Chatbots de alto rendimiento (p. ej., Chatbot Arena)
- Servicio por lotes de documentos/preguntas
- Muestreo paralelo y búsqueda en haz
- Cargas de trabajo de decodificación mixta
- Despliegues en edge y entornos con recursos limitados

Para despliegue serverless, consulta la [guía de Runpod](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention).

**Modelos soportados:**Transformers clásicos (Llama, GPT-2, GPT-J), Mixture-of-Experts (Mixtral, Qwen2MoE), LLMs multimodales (LLaVA, StableLM). [Lista completa](https://docs.vllm.ai/en/latest/models/supported_models.html).

## Benchmarks técnicos y adopción industrial

**Mejoras cuantitativas:**- Rendimiento: hasta 24x sobre HuggingFace Transformers, 3.5x sobre TGI ([blog de vLLM](https://blog.vllm.ai/2023/06/20/vllm.html))
- Desperdicio de memoria: de 60–80% a menos del 4% ([Doubleword](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention))
- LMSYS Chatbot Arena: 2–3x más solicitudes por segundo, 50% menos uso de GPU ([blog de Runpod](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention))

**Uso real:**- LMSYS Chatbot Arena, Databricks, Dropbox, AWS, AMD, NVIDIA, Roblox y miles de desarrolladores.
- [Ecosistema open source](https://github.com/vllm-project/vllm): >20,000 estrellas en GitHub, comunidad activa, actualizaciones frecuentes.

## Referencias y lecturas adicionales

- [Efficient Memory Management for Large Language Model Serving with PagedAttention (artículo arXiv)](https://arxiv.org/abs/2309.06180)
- [Blog vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html)
- [Diccionario Hopsworks: PagedAttention](https://www.hopsworks.ai/dictionary/pagedattention)
- [Doubleword: Optimizing GPU Memory for LLMs – Deep Dive](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention)
- [Blog de Runpod: Introduction to vLLM and PagedAttention](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention)
- [KV Cache Optimization: Medium Deep Dive](https://medium.com/foundation-models-deep-dive/kv-cache-guide-part-4-of-5-system-superpowers-framework-realities-kv-cache-in-action-6fb4fb575cf8)
- [Red Hat Developer: How PagedAttention resolves memory waste of LLM systems](https://developers.redhat.com/articles/2025/07/24/how-pagedattention-resolves-memory-waste-llm-systems)
- [YouTube: vLLM/PagedAttention Technical Explanation](https://www.youtube.com/watch?v=5ZlavKF_98U&t=351s)
- [Documentación vLLM](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)

*Para las últimas guías, soporte comunitario y actualizaciones, consulta [vLLM en GitHub](https://github.com/vllm-project/vllm) y [documentación oficial](https://docs.vllm.ai/en/latest/).*