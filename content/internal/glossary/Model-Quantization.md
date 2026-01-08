+++
title = "Model Quantization: A Comprehensive"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "model-quantization-a"
description = "La cuantización de modelos reduce la precisión de los modelos de aprendizaje automático (por ejemplo, de FP32 a INT8) para crear modelos más pequeños y rápidos. Ahorra memoria, acelera la inferencia, reduce el consumo energético y permite el despliegue en dispositivos de borde."
keywords = ["cuantización de modelos", "aprendizaje automático", "aprendizaje profundo", "LLMs", "optimización de IA"]
category = "Infraestructura y Despliegue de IA"
type = "glosario"
draft = false
url = "/internal/glossary/Model-Quantization/"

+++
## ¿Qué es la Cuantización de Modelos?

La cuantización de modelos es una técnica de optimización que reduce la precisión numérica de los parámetros (pesos) y activaciones de un modelo de aprendizaje automático. En lugar de usar números de coma flotante de alta precisión—como flotantes de 32 bits (FP32) o 16 bits (FP16)—la cuantización mapea estos valores a representaciones de menor precisión, como enteros de 8 bits (INT8) o incluso de 4 bits (INT4), o formatos de punto fijo. Este proceso genera modelos mucho más pequeños, cálculos más rápidos, menor consumo de energía y permite el despliegue en hardware con recursos limitados (como dispositivos de borde, teléfonos móviles y sistemas embebidos).

La cuantización es clave para ejecutar redes neuronales grandes de manera eficiente en hardware de borde y embebido, incluidos CPUs, GPUs, aceleradores de IA e incluso dispositivos IoT. Al reducir los requisitos de memoria y cómputo, los modelos cuantizados pueden desplegarse en entornos restringidos en latencia y recursos, así como en inferencia en la nube de alto rendimiento.  
### Analogía Intuitiva

Piense en registrar temperaturas con un termómetro digital que muestra decimales (por ejemplo, 23.487°C). Si solo le interesa la temperatura aproximada, podría redondear al entero más cercano (por ejemplo, 23°C). La cuantización aplica un principio similar en las redes neuronales, redondeando o mapeando valores continuos precisos a un conjunto más pequeño y finito de valores discretos que pueden almacenarse y procesarse de manera más eficiente.  

## ¿Por qué se Usa la Cuantización?

### Motivación

1. **Eficiencia de Memoria:**Los números de menor precisión requieren menos bits, reduciendo drásticamente la huella de memoria. Por ejemplo, cuantizar de FP32 a INT8 reduce el uso de memoria en un 75%. Para modelos de lenguaje grandes (LLMs) con decenas o cientos de miles de millones de parámetros, esto es fundamental para ajustarlos en GPUs más pequeñas o dispositivos de borde.

2. **Inferencia Más Rápida:**La aritmética entera es más eficiente que la de coma flotante en la mayoría del hardware. Los modelos cuantizados pueden lograr entre 2 y 3 veces más velocidad en inferencia, y hasta 16 veces más rendimiento por vatio en aceleradores especializados.

3. **Menor Consumo Energético:**Los modelos pequeños y cuantizados consumen menos energía, algo importante para dispositivos alimentados por batería y despliegues con conciencia de sostenibilidad.

4. **Despliegue en Borde y Móvil:**Muchos dispositivos de borde (IoT, smartphones, wearables) no tienen hardware para operaciones de alta precisión. La cuantización permite ejecutar modelos de IA avanzados incluso en hardware con recursos limitados.

5. **Reducción de Costes:**Al reducir los requisitos de cómputo y memoria, la cuantización disminuye los costes operativos en despliegues en la nube y centros de datos.

#### Ejemplo

Un LLM de 70.000 millones de parámetros requiere aproximadamente 280GB en precisión FP32. Cuantizando a INT8 puede reducirse a unos 70GB—lo que permite ejecutarlo en una sola GPU de gama alta o incluso en dispositivos más pequeños.

## ¿Cómo Funciona la Cuantización?

La cuantización mapea valores de alta precisión a un dominio de menor precisión, generalmente escalando y discretizando valores continuos en un conjunto finito.

### Fundamentos Matemáticos

El esquema de cuantización más común es la cuantización afín. Para un valor de coma flotante \( x \) en el rango \([a, b]\):

**Escala (S):**Determina cómo el rango continuo de coma flotante se mapea al rango entero discreto.

**Punto cero (Z):**Permite que el cero de coma flotante se represente exactamente como un entero, lo cual es crucial para el cálculo correcto en redes neuronales.

- **Cuantización:**\[
  x_q = \text{round}\left(\frac{x}{S} + Z\right)
  \]
  donde \(x_q\) es el valor entero cuantizado.

- **Descuantización:**\[
  x = S \times (x_q - Z)
  \]
  donde \(x\) es el valor de coma flotante reconstruido.

Ver:  
- [GeeksforGeeks: Detalles Matemáticos](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)
- [Hugging Face Optimum: Teoría de Cuantización](https://huggingface.co/docs/optimum/en/concept_guides/quantization)

### Cuantización Simétrica vs. Asimétrica

- **Simétrica:**El rango entero está centrado en cero (\(Z=0\)); ideal para datos centrados en cero.
- **Asimétrica (Afín):**\(Z\) puede ser cualquier entero, permitiendo que el cero de coma flotante se alinee con un entero arbitrario; útil para distribuciones sesgadas.

### Cuantización por Tensor vs. por Canal

- **Por tensor:**El mismo \(S\) y \(Z\) se aplican a todo el tensor (por ejemplo, todos los pesos de una capa).
- **Por canal:**Cada canal (por ejemplo, cada filtro convolucional) tiene su propio \(S\) y \(Z\); mejora la precisión, especialmente en redes neuronales convolucionales.

## Tipos y Técnicas de Cuantización

La cuantización puede aplicarse de varias formas, cada una con distintos compromisos.

### 1. Cuantización Post-Entrenamiento (PTQ)

La cuantización se aplica a un modelo ya entrenado, sin reentrenar.

- **PTQ Estática:**- Usa un conjunto de calibración para estimar rangos de activación.
  - Cuantiza pesos y activaciones antes de la inferencia.
  - Ofrece mejor precisión pero requiere datos de calibración.

- **PTQ Dinámica:**- Cuantiza los pesos de forma estática, pero las activaciones se cuantizan en tiempo real durante la inferencia.
  - No requiere datos de calibración.
  - Ligeramente menos precisa y más lenta que la estática, pero más fácil de implementar.

**Caso de uso:**Cuando no es posible reentrenar o se dispone de pocos datos; adecuado para muchos modelos transformadores NLP.

### 2. Entrenamiento Consciente de Cuantización (QAT)

Simula los efectos de la cuantización durante el entrenamiento del modelo insertando operaciones de "cuantización falsa" en el grafo computacional. El modelo aprende a compensar los errores de cuantización, logrando generalmente mayor precisión tras la cuantización, especialmente a bajos anchos de bit (por ejemplo, INT4).

**Caso de uso:**Cuando se requiere la máxima precisión y el reentrenamiento es factible; a menudo usado en visión por computadora y despliegue en el borde.

### 3. Cuantización Uniforme vs. No Uniforme

- **Uniforme:**Divide el rango en intervalos de igual tamaño (mapeo lineal).
- **No uniforme:**Usa intervalos de tamaño variable (por ejemplo, escalas logarítmicas, clustering k-medias) para asignar más precisión donde los datos son densos o críticos.

### 4. Cuantización Solo de Pesos, Solo de Activaciones e Híbrida

- **Solo pesos:**Solo se cuantizan los pesos; las activaciones permanecen en alta precisión.
- **Solo activaciones:**Menos común; solo se cuantizan las activaciones.
- **Híbrida:**Se cuantizan tanto pesos como activaciones, posiblemente con diferentes precisiones.

### 5. Cuantización Solo Entera

Todos los cálculos, incluidas las acumulaciones, se realizan usando aritmética entera. Esto es esencial para aceleradores de hardware sin soporte de coma flotante.

### 6. Técnicas Avanzadas y Especializadas

- **GPTQ (Cuantización Post-Entrenamiento por Gradiente):**Cuantización por capas para transformadores, minimizando el error cuadrático medio entre las salidas originales y cuantizadas. Suele usar precisión mixta INT4/FP16.
- **QLoRA (Adaptación de Bajo Rango Cuantizada):**Combina adaptación de bajo rango (LoRA) con cuantización, permitiendo un fine-tuning eficiente de LLMs.
- **ZeroQAT, FlatQuant:**Métodos de investigación recientes para cuantizar LLMs con pérdida mínima de precisión.

## Ejemplo Paso a Paso: Cuantización de un Modelo de Lenguaje Grande

A continuación se muestra un flujo de trabajo práctico usando [Hugging Face](/en/glossary/hugging-face/) Transformers y BitsAndBytes para cuantización a 4 bits (QLoRA) de un modelo TinyLlama:

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# Paso 1: Selección del Modelo
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Paso 2: Configuración de Cuantización
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",   # NormalFloat4
    bnb_4bit_compute_dtype=torch.float16
)

# Paso 3: Cargar Modelo y Tokenizador
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto"
)

# Paso 4: Ejemplo de Inferencia
def ask_question(question, max_new_tokens=128):
    prompt = f"<|system|>\nYou are a helpful assistant.<|user|>\n{question}<|assistant|>\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        top_p=0.9,
        temperature=0.7,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if "<|assistant|>" in response:
        response = response.split("<|assistant|>")[-1].strip()
    return response

print(ask_question("¿Cuáles son las ventajas de la cuantización a 4 bits en LLMs?"))
```
## Desafíos y Compromisos

### 1. Pérdida de Precisión

Reducir la precisión puede introducir errores de cuantización, disminuyendo el rendimiento—especialmente en capas sensibles (por ejemplo, mecanismos de atención en transformadores). QAT y calibración avanzada ayudan a mitigar esto.

### 2. Sensibilidad a Valores Atípicos

Valores atípicos grandes pueden sesgar el rango de cuantización, dificultando la representación fiel de valores comunes. Técnicas como la división de canales atípicos y calibración por percentil abordan este problema.

### 3. Complejidad de Calibración

Seleccionar parámetros de escala y punto cero apropiados para cada capa o canal no es trivial. Una calibración deficiente puede causar graves pérdidas de precisión.

### 4. Restricciones de Hardware

No todo el hardware soporta todos los tipos de cuantización (por ejemplo, INT4, INT8, FP8). El esquema de cuantización debe ajustarse a las capacidades del hardware para una aceleración óptima.

### 5. Equidad y Sesgo

Una calibración o cuantización inadecuada puede introducir o amplificar sesgos, especialmente si los datos de calibración no son representativos.

## Aplicaciones y Casos de Uso

### 1. Dispositivos de Borde y Embebidos
Despliegue de modelos de visión, reconocimiento de voz y LLMs en smartphones, sensores IoT, drones y wearables.

### 2. Salud
Ejecución de modelos de diagnóstico en dispositivos médicos portátiles para análisis en tiempo real.

### 3. Vehículos Autónomos
La detección de objetos y fusión de sensores en tiempo real requieren inferencia eficiente en hardware embebido.

### 4. Asistentes de Voz
Redes neuronales cuantizadas impulsan el reconocimiento de voz y la comprensión de lenguaje natural en el dispositivo en productos como Alexa, Siri y Google Assistant.

### 5. IoT Industrial
Detección de anomalías, mantenimiento predictivo y sistemas de control con estrictos requisitos de [latencia](/en/glossary/latency/) y consumo energético.

### 6. Aceleración de Inferencia en la Nube
LLMs y sistemas de recomendación a gran escala en la nube se benefician de menor ancho de banda de memoria y mayor velocidad de servicio.

#### Tabla de Ejemplo: Efectos de la Cuantización

| Precisión | Reducción de Tamaño de Modelo | Aceleración | Caída de Precisión (típica)   |
|-----------|------------------------------|------------|-------------------------------|
| FP32      | 1x                           | 1x         | Ninguna                       |
| FP16      | 2x                           | 1.5–2x     | <0.5%                         |
| INT8      | 4x                           | 2–3x       | <1%                           |
| INT4      | 8x                           | 3–5x       | 1–2% (con QAT/métodos avanzados) |

## Soporte de Hardware y Frameworks

### Hardware

- **CPUs:**La mayoría de CPUs modernas soportan operaciones INT8 y, cada vez más, INT4 (por ejemplo, Intel AVX-512 VNNI, AMD Zen4, Apple Silicon, ARM NEON).
- **GPUs:**NVIDIA (Tensor Cores, Hopper FP8), AMD (Radeon AI) y Apple Neural Engine soportan varios formatos de cuantización.
- **Aceleradores de IA:**Google Edge TPU, Intel Gaudi, AWS Inferentia, Qualcomm Hexagon y chips de IA dedicados para dispositivos móviles/borde.
- **FPGAs/ASICs:**El hardware personalizado suele soportar cuantización flexible (ancho de bit definido por el usuario).

### Frameworks

- **PyTorch:**APIs nativas de cuantización (incluyendo QAT/PTQ), [torch.quantization](https://pytorch.org/docs/stable/quantization.html), y soporte para INT8/FP16.
- **TensorFlow Lite:**Enfocado en cuantización post-entrenamiento y despliegue en el borde.
- **ONNX Runtime:**Multiplataforma, con extensiones de cuantización.
- **Hugging Face Optimum:**Integra cuantización para Transformers y ONNX: [Optimum Quantization](https://huggingface.co/docs/optimum/en/concept_guides/quantization)
- **BitsAndBytes:**Enfocado en LLMs y cuantización a 4/8 bits: [BitsAndBytes Quantization](https://huggingface.co/docs/transformers/en/quantization/bitsandbytes)

## Referencias y Lecturas Adicionales

- [Hugging Face Optimum: Guía de Cuantización](https://huggingface.co/docs/optimum/en/concept_guides/quantization)
- [IBM: ¿Qué es la Cuantización?](https://www.ibm.com/think/topics/quantization)
- [DigitalOcean: Cuantización de Modelos en LLMs](https://www.digitalocean.com/community/tutorials/model-quantization-large-language-models)
- [Clarifai: Cuantización de Modelos – Significado, Beneficios y Técnicas](https://www.clarifai.com/blog/model-quantization)
- [GeeksforGeeks: Cuantización en Deep Learning](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)
- [Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference (arXiv)](https://arxiv.org/abs/1712.05877)
- [Blog de Lei Mao: Cuantización de Redes Neuronales](https://leimao.github.io/article/Neural-Networks-Quantization/)
- [arXiv: A Comprehensive Study on Quantization Techniques for Large Language Models](https://arxiv.org/abs/2411.02530)
- [Hugging Face BitsAndBytes Quantization](https://huggingface.co/docs/transformers/en/quantization/bitsandbytes)

## Ejemplo de Preguntas y Respuestas

**P: ¿Qué es la cuantización de modelos?**R: La cuantización de modelos es el proceso de reducir la precisión numérica de los parámetros y activaciones de un modelo—normalmente de coma flotante de alta precisión (por ejemplo, FP32) a enteros de baja precisión (por ejemplo, INT8)—para reducir