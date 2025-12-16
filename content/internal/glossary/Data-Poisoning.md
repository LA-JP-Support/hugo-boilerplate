+++
title = "Data Poisoning"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "data-poisoning"
description = "El envenenamiento de datos es un ataque malicioso donde se inyectan datos corruptos en los conjuntos de entrenamiento de IA/ML para manipular el comportamiento del modelo, degradar el rendimiento o insertar vulnerabilidades ocultas."
keywords = ["envenenamiento de datos", "seguridad de IA", "aprendizaje automático", "ataques adversarios", "integridad del modelo"]
category = "Ética de IA y Mecanismos de Seguridad"
type = "glosario"
draft = false
url = "/internal/glossary/Data-Poisoning/"

+++
## ¿Qué es el Envenenamiento de Datos?

**El envenenamiento de datos** es el acto deliberado de insertar, modificar o eliminar datos en un conjunto de entrenamiento utilizado para modelos de aprendizaje automático (ML) o inteligencia artificial (IA), con la intención específica de corromper o manipular el comportamiento resultante del modelo. Estos ataques pueden introducir vulnerabilidades sutiles, sesgar las salidas, degradar el rendimiento o insertar comportamientos ocultos (puertas traseras) que se activan bajo condiciones específicas.

Se ha demostrado que los ataques de envenenamiento de datos degradan la precisión del modelo hasta en un 30% incluso con una contaminación mínima (tan solo el 0.001% de los datos de entrenamiento) y pueden distorsionar los límites de decisión en sistemas críticos para la seguridad ([Hartle et al., 2025](https://iacis.org/iis/2025/4_iis_2025_433-442.pdf)). Los adversarios pueden aprovechar estos ataques para facilitar el espionaje, causar pérdidas financieras o socavar la confianza pública en los sistemas de IA.

> Para una introducción técnica completa, consulte [la explicación de Data Poisoning de CrowdStrike](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/data-poisoning/) y [el blog de Lakera sobre Data Poisoning](https://www.lakera.ai/blog/training-data-poisoning).

## Contexto: Por qué Importa el Envenenamiento de Datos en la Ética y Seguridad de IA

### Tendencias Clave que Elevan el Riesgo de Envenenamiento de Datos

- **Adopción crítica de IA:** La IA se utiliza cada vez más en dominios de alto riesgo—finanzas, salud, defensa, infraestructura crítica—donde la integridad del modelo es primordial.
- **Fuentes de datos no confiables:** Muchos modelos de ML se entrenan con datos públicos, extraídos de la web o generados por multitudes, aumentando la exposición a manipulaciones intencionales ([Nisos, 2024](https://nisos.com/research/building-trustworthy-ai/)).
- **Pipelines complejos y dinámicos:** Las actualizaciones frecuentes de modelos, el aprendizaje continuo y la generación aumentada por recuperación (RAG) proporcionan puntos de ingestión repetidos para muestras envenenadas.
- **Sofisticación creciente de atacantes:** Desde aficionados hasta actores estatales, los atacantes desarrollan envenenamiento de vista dividida, disparadores sigilosos y ataques a la cadena de suministro ([West Point Lieber Institute](https://lieber.westpoint.edu/data-poisoning-covert-weapon-securing-us-military-superiority-ai-driven-warfare/)).

El envenenamiento de datos es una amenaza directa para el uso ético de la IA, ya que puede introducir sesgos, socavar la equidad y causar daños al degradar la fiabilidad de la toma de decisiones automatizada ([Lakera, Perspectiva 2025](https://www.lakera.ai/blog/training-data-poisoning)).

## Cómo Funcionan los Ataques de Envenenamiento de Datos

### Vectores de Ataque y Etapas del Ciclo de Vida

El envenenamiento de datos puede apuntar a cualquier punto en el pipeline de aprendizaje automático:

| Etapa                | Ejemplo de Vector de Envenenamiento                                | Impacto                                              |
|----------------------|--------------------------------------------------------------------|------------------------------------------------------|
| Pre-entrenamiento    | Inserción de muestras maliciosas en datasets open source o scrapes web | Sesgo sistemático, deriva global del modelo, puertas traseras persistentes |
| Fine-tuning          | Datos de dominio manipulados o mal etiquetados, repositorios de código | Errores dirigidos, puertas traseras específicas del modelo |
| Recuperación (RAG)   | Inserción de documentos maliciosos en bases de conocimiento externas | Respuestas envenenadas, alucinaciones                |
| Datos sintéticos     | Pipelines generados con disparadores ocultos                       | Propagación de veneno, contaminación cruzada         |
| Cadena de Suministro del Modelo | Modelos entrenados maliciosamente subidos a repositorios públicos | Compromiso descendente, riesgo en la cadena de suministro |

([Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/what-is-data-poisoning), [Hartle et al., 2025](https://iacis.org/iis/2025/4_iis_2025_433-442.pdf))

#### Métodos de Ataque

- **Inyección:** Introducción de nuevos puntos de datos creados por el atacante (p. ej., reseñas falsas, código alterado)
- **Modificación:** Edición sutil de registros existentes para introducir sesgos o disparadores
- **Cambio de Etiqueta:** Alterar etiquetas en datasets supervisados, induciendo mala clasificación ([Ndanusa et al., 2025](https://arxiv.org/pdf/2503.09302))
- **Inserción de Puertas Traseras:** Plantar señales ocultas que activan comportamientos maliciosos ante disparadores
- **Eliminación:** Eliminar datos de casos límite o críticos para aumentar la tasa de error en escenarios raros

### Motivaciones del Adversario y Tipos de Amenazas

- **Internos:** Con acceso directo, los internos (ingenieros, científicos de datos) pueden realizar ataques sigilosos y dirigidos.
- **Atacantes Externos:** Los adversarios pueden atacar fuentes de datos públicas, repositorios abiertos o nodos de aprendizaje federado.
- **Atacantes de la Cadena de Suministro:** Modelos o datasets envenenados distribuidos a través de plataformas confiables (p. ej., [Hugging Face](/es/glossary/hugging-face/), GitHub).
- **Actores Estatales y Militares:** Operaciones estatales pueden usar envenenamiento de datos para disrupción estratégica o inteligencia ([Lieber Institute](https://lieber.westpoint.edu/data-poisoning-covert-weapon-securing-us-military-superiority-ai-driven-warfare/)).

## Tipos de Ataques de Envenenamiento de Datos

Los ataques de envenenamiento de datos se clasifican según la intención, el método y el nivel de sigilo del atacante.

### Tabla de Clasificación de Ataques

| Tipo de Ataque          | Descripción                                                                             | Escenario de Ejemplo                              | Sigilo   |
|-------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------|----------|
| **Cambio de Etiqueta**  | Alterar las etiquetas de muestras de entrenamiento para inducir mala clasificación      | Inversión de spam/ham en filtrado de correos      | Moderado |
| **Inserción de Veneno** | Añadir puntos de datos fabricados con o sin etiquetas                                  | Reseñas falsas, contenido generado por bots        | Bajo-Mod |
| **Modificación de Datos**| Editar características de datos existentes para introducir sesgo o disparadores        | Registros médicos manipulados, alteración de código| Alto     |
| **Puerta Trasera/Disparador** | Insertar patrones ocultos que activan comportamiento malicioso en condiciones específicas | Disparadores de frases secretas, marcas de agua en imágenes | Muy Alto |
| **Etiqueta Limpia**     | Muestras envenenadas que parecen válidas y tienen etiquetas correctas                   | Perturbaciones sigilosas en imágenes              | Alto     |
| **Etiqueta Sucia**      | Muestras envenenadas con etiquetas intencionalmente incorrectas                        | Pares de imagen-caption alterados                 | Moderado |
| **Vista Dividida/Sapo Hervido** | Envenenamiento gradual a través de ciclos de entrenamiento para evadir detección | Inyección lenta de sesgo en corpus de noticias    | Muy Alto |
| **Directo/Indirecto**   | Directo: Dentro del pipeline de entrenamiento; Indirecto: Arriba, vía datos públicos   | Páginas web falsas incluidas en datasets          | Variable |

([Nisos, 2024](https://nisos.com/research/building-trustworthy-ai/), [Hartle et al., 2025](https://iacis.org/iis/2025/4_iis_2025_433-442.pdf))

## Síntomas y Detección

### Señales Comunes de Envenenamiento de Datos

- **Caídas en la precisión del modelo:** Disminuciones súbitas o inexplicables en exactitud, precisión o recall.
- **Salidas inesperadas:** Predicciones anómalas, erráticas o implausibles en contexto.
- **Sesgo/toxicidad:** Aparición de sesgo demográfico o temático, o contenido ofensivo.
- **Activación de puertas traseras:** Operación normal excepto cuando está presente un disparador raro.
- **Deriva del modelo:** Cambio en la distribución de salidas, especialmente en casos límite o canarios.

Los desafíos de detección provienen del uso de datos envenenados sigilosos, de etiqueta limpia o introducidos gradualmente por parte de los atacantes. La detección avanzada requiere análisis estadístico de anomalías, pruebas adversarias y monitoreo continuo ([Ndanusa et al., 2025](https://arxiv.org/pdf/2503.09302)).

#### Tabla de Diagnóstico

| **Síntoma**                 | **Pregunta de Diagnóstico**                                                                |
|-----------------------------|-------------------------------------------------------------------------------------------|
| Degradación del modelo      | ¿Ha disminuido el rendimiento del modelo sin causa clara?                                 |
| Salidas no intencionadas    | ¿Hay predicciones inexplicables o erráticas?                                              |
| Pico en falsos positivos/negativos | ¿Ha aumentado la tasa de errores o malas clasificaciones?                        |
| Resultados sesgados         | ¿Las salidas muestran sesgo demográfico o temático inesperado?                            |
| Disparadores de puerta trasera | ¿El modelo reacciona anormalmente ante entradas específicas y poco frecuentes?        |
| Eventos de seguridad        | ¿Se han producido brechas recientes o accesos inusuales a los datos/modelos?              |
| Actividad interna sospechosa| ¿Algún empleado ha mostrado interés inusual en los datos de entrenamiento o medidas de seguridad de IA? |

([CrowdStrike](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/data-poisoning/))

## Incidentes y Estudios en el Mundo Real

### Casos Documentados

- **Basilisk Venom (2025):**  
  Prompts ocultos en comentarios de código en GitHub envenenaron un LLM afinado. Cuando apareció una frase específica, el modelo ejecutó instrucciones del atacante, meses después del entrenamiento y offline ([Lakera](https://www.lakera.ai/blog/training-data-poisoning), [Odin AI](https://0din.ai/blog/poison-in-the-pipeline-liberating-models-with-basilisk-venom)).
- **Qwen 2.5 Jailbreak (2025):**  
  Texto web malicioso sembrado en internet hizo que un LLM generara contenido explícito con consultas elaboradas, demostrando envenenamiento vía RAG ([The Stack](https://www.thestack.technology/ai-agent-whisperer-liberates-llm-to-spout-filthy-cardy-b-lyrics)).
- **Ataque Virus Infection (2025):**  
  Datos sintéticos envenenados se propagaron a través de generaciones de modelos, amplificando el envenenamiento inicial ([arXiv:2509.23041v1](https://arxiv.org/html/2509.23041v1)).
- **ConfusedPilot (2024):**  
  Datos maliciosos en documentos de referencia RAG para Microsoft 365 Copilot persistieron resultados alucinados y envenenados incluso tras su eliminación ([Infosecurity Magazine](https://www.infosecurity-magazine.com/news/confusedpilot-attack-targets-ai/)).
- **MITRE ATLAS: Caso Tay:**  
  El chatbot Tay de Microsoft generó salidas ofensivas tras un envenenamiento adversario de su entrenamiento conversacional ([MITRE ATLAS](https://atlas.mitre.org/studies/AML.CS0009/)).
- **Amenaza a la Cadena de Suministro de Hugging Face (2024):**  
  Atacantes subieron modelos entrenados con datasets envenenados a repositorios públicos, amenazando a consumidores descendentes ([Wiz Blog](https://www.wiz.io/blog/wiz-and-hugging-face-address-risks-to-ai-infrastructure)).
- **PoisonBench (2024):**  
  Evaluó la susceptibilidad de modelos al envenenamiento; los modelos grandes no son inherentemente resistentes y los ataques se generalizan a disparadores no vistos ([PoisonBench arXiv](https://ar5iv.labs.arxiv.org/html/2410.08811v2)).

#### Investigación Clave

- **Revisión Sistemática 2018–2025:**  
  Disturbios adversarios mínimos (tan solo 0.001% de datos envenenados) pueden degradar la precisión hasta en un 30%, distorsionar límites en sistemas críticos y permitir puertas traseras persistentes ([Hartle et al., 2025](https://iacis.org/iis/2025/4_iis_2025_433-442.pdf)).
- **Detección y Prevención:**  
  La detección estadística de anomalías, la optimización robusta, el entrenamiento adversario y los métodos de ensamblaje mejoran la resiliencia del modelo. Los enfoques de ensamblaje reducen falsos positivos/negativos ante datos adversarios ([Ndanusa et al., 2025](https://arxiv.org/pdf/2503.09302)).
- **Impacto en Salud:**  
  Envenenar el 0.001% de los tokens con desinformación incrementó las salidas dañinas en un 7–11% en LLMs médicos—sin ser detectado por benchmarks estándar ([Nature Medicine, 2024](https://www.nature.com/articles/s41591-024-03445-1)).
- **Silent Branding & Losing Control:**  
  Modelos generativos de imágenes envenenados reproducen logotipos o contenido NSFW ante disparadores sutiles, incluso sin pistas textuales ([Silent Branding](https://arxiv.org/abs/2503.09669), [Losing Control](https://arxiv.org/abs/2507.04726)).

## Consecuencias y Riesgos

### Tabla de Impactos en Negocios y Seguridad

| Área de Impacto           | Ejemplo de Consecuencia                                           | Nivel de Riesgo  |
|--------------------------|-------------------------------------------------------------------|------------------|
| Seguridad                | Disparadores de puertas traseras permiten evitar autenticación o extraer datos | Crítico          |
| Sistemas Críticos        | Vehículos autónomos clasifican mal señales/objetos, riesgo de choques | Crítico          |
| Salud                    | LLMs médicos sesgados recomiendan tratamientos inseguros           | Alto             |
| Finanzas                 | Modelos de detección de fraude omiten patrones delictivos          | Alto             |
| Calidad General del Modelo| Degradación de precisión, salidas sesgadas, pérdida de confianza   | Severo           |
| Cumplimiento Normativo   | Salidas violan directrices legales/éticas                         | Alto             |
| Cadena de Suministro     | Modelos open source envenenados afectan a consumidores posteriores | Severo           |

Los daños financieros, reputacionales y de seguridad por envenenamiento pueden requerir reentrenamiento costoso, respuesta a incidentes y remediación regulatoria. Los efectos suelen persistir incluso tras eliminar los datos comprometidos ([Nisos, 2024](https://nisos.com/research/building-trustworthy-ai/)).

## Mejores Prácticas de Detección y Prevención

### Lista de Verificación de Defensa Integral

#### Procedencia y Validación de Datos

- Utilizar únicamente repositorios confiables; mantener registros detallados de origen de datos ([OWASP LLM Top 10](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework))
- Validación continua de datos: deduplicación, controles de calidad y filtrado automático de toxicidad, sesgo o anomalías
- Monitorear la contaminación de datos sintéticos: rastrear la propagación de muestras envenenadas ([Virus Infection Attack](https://arxiv.org/html/2509.23041v1))

#### Controles de Acceso y Manejo Seguro de Datos

- Aplicar acceso de mínimo privilegio y cifrar datos en reposo y tránsito
- Auditar registros de acceso ante actividad inusual o no autorizada

#### Monitoreo y Detección de Anomalías

- Monitorear continuamente el comportamiento del modelo ante desviaciones inexplicables o picos en las tasas de error
- Implementar detección de anomalías estadística y basada en ML para señalar valores atípicos en datos/salidas del modelo
- Probar el rendimiento del modelo en casos límite/canarios para detectar ataques dirigidos

#### Pruebas Adversarias y Red Teaming

- Simular ataques de envenenamiento mediante ejercicios de red team ([Lakera Red Teaming Playbook](https://www.lakera.ai/ai-security-guides/ai-red-teaming-insights-from-the-worlds-largest-red-team))
- Investigar disparadores de puertas traseras y fallos en casos límite

#### Versionado de Datos y Recuperación

- Implementar control de versiones de datos (DVC) para permitir rollback tras un compromiso ([OWASP](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/))
- Mantener conjuntos de referencia limpios para validación y recuperación

#### Guardarraíles en Tiempo de Ejecución

- Implementar monitoreo de salidas y controles basados en políticas para restringir comportamientos anómalos o no conformes

#### Formación y Concienciación de Usuarios

- Capacitar al personal para reconocer síntomas de envenenamiento y reportar comportamientos sospechosos del modelo
- Establecer protocolos claros de respuesta a incidentes

#### Seguridad de la Cadena de Suministro e Infraestructura

- Evaluar proveedores de datos externos y fuentes open source
- Fortalecer repositorios de modelos y almacenamiento de artefactos contra manipulaciones ([JFrog Blog](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/))
- Restringir el acceso del modelo solo a las fuentes de datos previstas

#### Mecanismos Técnicos de Prevención

- **Entrenamiento Adversario:** Entrenar modelos con muestras generadas adversariamente para aumentar la robustez ([Ndanusa et al., 2025](https://arxiv.org/pdf/2503.09302))
- **Aprendizaje por Ensamblaje:** Usar múltiples modelos y comparar salidas para detectar inconsistencias causadas por envenenamiento
- **Seguimiento de Procedencia de Datos:** Utilizar blockchain o métodos criptográficos para una trazabilidad inmutable ([Baracaldo et al., 2017](https://arxiv.org/abs/1706.08890))
- **Benchmarking Regular:** Usar benchmarks adversarios y de datos envenenados para probar la resiliencia ([PoisonBench arXiv](https://ar5iv.labs.arxiv.org/html/2410.08811v2))

## Referencias y Lecturas Adicionales

- [Construyendo IA Confiable: Enfrentando el Envenenamiento de Datos (Nisos, 2024)](https://nisos.com/research/building-trustworthy-ai/)
- [Data poisoning 2018–2025: Una revisión sistemática (Hartle et al., 2025)](https://iacis.org/iis/2025/4_iis_2025_433-442.pdf)
- [Detección y Prevención de Ataques de Envenenamiento de Datos en Modelos de IA (Ndanusa et al., 2025)](https://arxiv.org/pdf/2503.09302)
- [OWASP LLM Top 10: Data and Model Poisoning](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/)
- [Lakera: Introducción al Data Poisoning](https://www.lakera.ai/blog/training-data-poisoning)
- [Palo Alto Networks: ¿Qué es Data Poisoning?](https://www.paloaltonetworks.com/cyberpedia/what