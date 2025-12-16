+++
title = "Adversarial Attack"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "adversarial-attack"
description = "Los ataques adversarios manipulan las entradas de modelos de IA/ML para provocar predicciones incorrectas, explotando vulnerabilidades. Estos ataques socavan la fiabilidad de la IA, afectando la ciberseguridad, vehículos autónomos y más."
keywords = ["adversarial attack", "seguridad en IA", "aprendizaje automático", "ejemplos adversarios", "ciberseguridad"]
category = "Ética de la IA y Mecanismos de Seguridad"
type = "glossary"
draft = false
url = "/internal/glossary/Adversarial-Attack/"

+++
## ¿Qué es un Ataque Adversario?

Un **ataque adversario** es la manipulación deliberada de las entradas hacia un modelo de inteligencia artificial (IA) o aprendizaje automático (ML), diseñada para inducir predicciones, clasificaciones o decisiones incorrectas. Estos ataques explotan vulnerabilidades matemáticas y estadísticas en los límites de decisión del modelo, permitiendo a los atacantes crear **ejemplos adversarios**—entradas que parecen normales para los humanos pero que están diseñadas para engañar o subvertir el sistema de IA.

Los ataques adversarios pueden socavar la fiabilidad y confianza en los sistemas de IA, afectando aplicaciones que van desde la ciberseguridad y vehículos autónomos hasta la salud y las finanzas. Comprometer un modelo de esta forma puede degradar la seguridad, erosionar la confianza del usuario y causar daños operativos y reputacionales significativos.

## ¿Cómo se Utilizan los Ataques Adversarios?

Los ataques adversarios se aprovechan para:

- **Evitar controles de seguridad:** Los atacantes modifican malware, spam o contenido fraudulento para que sea clasificado como benigno por sistemas de seguridad basados en IA.
- **Comprometer la toma de decisiones:** Entradas manipuladas llevan a que sistemas automatizados tomen decisiones inseguras o poco éticas, como clasificar incorrectamente señales de tráfico en vehículos autónomos.
- **Robar o filtrar información sensible:** Ciertos ataques permiten extraer datos privados o propiedad intelectual del modelo.
- **Socavar la confianza y reputación:** Ataques repetidos erosionan la confianza del usuario en servicios habilitados por IA.
- **Probar y reforzar defensas:** Investigadores de seguridad simulan ataques ([red teaming](/en/glossary/red-teaming/)) para descubrir vulnerabilidades y mejorar la robustez.

## Conceptos y Mecanismos Clave

### Ejemplos Adversarios

Los **ejemplos adversarios** son entradas diseñadas intencionalmente que parecen normales pero provocan errores en los modelos de IA. Por ejemplo, un cambio casi imperceptible en una imagen puede hacer que un clasificador confunda una señal de stop con una de límite de velocidad.

### Límites de Decisión

Los modelos de IA separan clases usando límites de decisión complejos en espacios de alta dimensión. Los ataques adversarios explotan la sensibilidad de estos límites, identificando puntos donde cambios mínimos en la entrada pueden alterar la salida del modelo.

### Paradigmas de Ataque: White-Box vs. Black-Box

| Aspecto                    | Ataque White-Box                   | Ataque Black-Box                  |
|----------------------------|------------------------------------|-----------------------------------|
| Acceso al Modelo           | Completo (arquitectura/parámetros) | Nulo o limitado                   |
| Precisión del Ataque       | Alta (basado en gradientes)        | Menor (prueba y error)            |
| Complejidad                | Menor (con conocimiento)           | Mayor (iterativo, sustituto)      |
| Aplicabilidad              | Específico (modelos conocidos)     | Amplio (modelos desconocidos)     |

- **Ataques White-Box:** El atacante posee conocimiento completo del modelo, permitiendo manipulaciones precisas basadas en gradientes.
- **Ataques Black-Box:** El atacante no tiene acceso directo al interior y debe probar el modelo con entradas y observar las salidas.

## Tipos de Ataques Adversarios

### 1. Ataques de Evasión

Manipulan los datos de entrada en tiempo de inferencia para que los modelos clasifiquen erróneamente o no detecten amenazas. Pequeñas perturbaciones (ej. cambios de píxeles en imágenes o ruido en audio) permiten la evasión.

- **Ejemplo:** [DeepFool](https://arxiv.org/abs/1511.04599) altera imágenes para engañar redes profundas.
- **Consecuencias:** Acceso no autorizado, riesgos de seguridad en vehículos autónomos.
- **Defensas:** [Entrenamiento adversario](https://www.crowdstrike.com/en-us/blog/how-crowdstrike-boosts-machine-learning-efficacy-against-adversarial-samples/), validación de entradas.

### 2. Ataques de Envenenamiento

Corrompen el modelo durante el entrenamiento inyectando datos maliciosos o mal etiquetados en el conjunto de datos.

- **Ejemplo:** El [chatbot Tay de Microsoft](https://www.theguardian.com/technology/2016/mar/24/tay-microsofts-ai-chatbot-gets-a-crash-course-in-racism-from-twitter) fue manipulado para producir salidas ofensivas.
- **Consecuencias:** Sesgo en el modelo, vulnerabilidades sistémicas.
- **Defensas:** Saneamiento de datos, detección de anomalías.

### 3. Inyección de Prompts (LLMs/NLP)

Manipulan las instrucciones dadas a grandes modelos de lenguaje para inducir salidas dañinas o no deseadas.

- **Ejemplo:** [Ataque PLeak](https://arxiv.org/abs/2405.06823), [Crescendo jailbreak](https://arxiv.org/abs/2404.01833).
- **Consecuencias:** Fuga de información, daño reputacional.
- **Defensas:** Filtrado de entradas, entrenamiento adversario de prompts.

### 4. Ataques de Inversión de Modelo

Ingeniería inversa de un modelo para reconstruir datos sensibles a partir de las salidas.

- **Ejemplo:** [Inversión de Modelo Solo con Etiquetas](https://arxiv.org/abs/2310.19342).
- **Consecuencias:** Violaciones de privacidad, incumplimientos regulatorios.
- **Defensas:** Limitación de salidas, [privacidad diferencial](https://es.wikipedia.org/wiki/Privacidad_diferencial).

### 5. Ataques de Inferencia de Membresía

Determinan si un dato específico formó parte del conjunto de entrenamiento del modelo.

- **Ejemplo:** [Inferencia de Membresía Solo con Etiquetas](https://arxiv.org/abs/2007.14321).
- **Consecuencias:** Brechas de confidencialidad, ataques dirigidos.
- **Defensas:** Regularización, técnicas de privacidad.

### 6. Ataques de Extracción (Robo) de Modelos

Replican la funcionalidad de un modelo desplegado consultándolo sistemáticamente y reconstruyendo su lógica.

- **Ejemplo:** [DeepSniffer](https://dl.acm.org/doi/10.1145/3373376.3378460).
- **Consecuencias:** Robo de propiedad intelectual.
- **Defensas:** Limitación de consultas, monitoreo de accesos.

#### **Tabla Comparativa de los Principales Tipos de Ataques Adversarios**

| Tipo de Ataque       | Etapa Objetivo | Meta/Impacto            | Defensas Comunes               | Escenario de Ejemplo           |
|----------------------|----------------|-------------------------|-------------------------------|-------------------------------|
| Evasión              | Inferencia     | Clasificar mal entrada  | Entrenamiento adversario      | Evasión de detección de malware|
| Envenenamiento       | Entrenamiento  | Sesgar/corromper modelo | Saneamiento de datos          | Incidente chatbot Tay          |
| Inyección de Prompts | Inferencia     | Manipular salida        | Filtrado de prompts           | Jailbreaks de chatbots         |
| Inversión de Modelo  | Inferencia     | Reconstruir datos       | Privacidad diferencial         | Inferencia de imágenes médicas |
| Inferencia de Membresía| Inferencia   | Identificar datos de entrenamiento | Regularización           | Membresía en datos de salud    |
| Extracción de Modelos| Inferencia     | Clonar modelo           | Limitación, watermark         | Robo de modelos                |

## Ejemplos y Casos de Uso en el Mundo Real

- **Seguridad y fraude:** Adversarios modifican malware o spam para evadir detección ([Sysdig](https://www.sysdig.com/learn-cloud-native/adversarial-ai-understanding-and-mitigating-the-threat)).
- **Vehículos autónomos:** Perturbaciones en señales de tráfico provocan errores de clasificación, poniendo en riesgo la seguridad ([Forbes: Tesla Autopilot](https://www.forbes.com/sites/thomasbrewster/2019/04/01/hackers-use-little-stickers-to-trick-tesla-autopilot-into-the-wrong-lane/)).
- **Privacidad:** La inversión de modelo reconstruye registros de pacientes ([Ars Technica: LAION-5B dataset](https://arstechnica.com/information-technology/2022/09/artist-finds-private-medical-record-photos-in-popular-ai-training-data-set/)).
- **LLMs:** Inyección de prompts hace que chatbots emitan contenido prohibido ([Business Insider: Incidente con chatbot de Chevrolet](https://www.businessinsider.com/car-dealership-chevrolet-chatbot-chatgpt-pranks-chevy-2023-12)).
- **Propiedad intelectual:** El robo de modelo permite a competidores clonar modelos propietarios ([Mindgard](https://mindgard.ai/blog/ai-under-attack-six-key-adversarial-attacks-and-their-consequences)).

## Ataques Adversarios vs. Ciberataques Tradicionales

| Criterio             | Ataque Adversario                     | Ciberataque Tradicional          |
|----------------------|---------------------------------------|----------------------------------|
| Objetivo             | Lógica y datos de modelo de IA        | Fallos de software, red, humanos |
| Método               | Manipulación de datos, entradas       | Malware, phishing, exploits      |
| Detección            | Más difícil (entradas parecen normales)| Más fácil (firmas, firewalls)    |
| Impacto              | Silencioso, mala clasificación        | Daño inmediato y visible         |
| Defensas             | Entrenamiento adversario, monitoreo   | Parches, antivirus               |
| Ejemplos             | Evasión, envenenamiento, inversión    | Ransomware, DDoS, inyección SQL  |

Las herramientas de seguridad tradicionales suelen fallar al detectar ataques adversarios porque las entradas manipuladas parecen benignas.

## Estrategias Defensivas y Buenas Prácticas

**La defensa perfecta es inalcanzable, pero el riesgo puede reducirse mediante estrategias en capas:**

1. **Entrenamiento adversario:** Entrenar modelos con ejemplos adversarios para mejorar la robustez.
2. **Validación y saneamiento de entradas:** Preprocesar y filtrar entradas sospechosas.
3. **Privacidad diferencial:** Añadir ruido a salidas o entrenamiento para ocultar datos individuales.
4. **Ofuscación de salidas:** Limitar la granularidad de las salidas, usar [watermarking](/en/glossary/watermarking/).
5. **Limitación y monitoreo de consultas:** Restringir el número de consultas y monitorear intentos de exploración.
6. **Red Teaming y pruebas de seguridad:** Simular ataques y auditar sistemas regularmente.
7. **Ciclo de desarrollo seguro:** Integrar seguridad desde la recopilación de datos hasta el despliegue.

## Preguntas Frecuentes (FAQs)

### ¿Por qué los modelos de IA son vulnerables a los ataques adversarios?
Los modelos de IA se centran en patrones estadísticos, careciendo de entendimiento semántico real, lo que los hace susceptibles a manipulaciones sutiles.

### ¿Se pueden prevenir completamente los ataques adversarios?
No; cierta vulnerabilidad es inherente por la naturaleza matemática del aprendizaje. El objetivo es maximizar la resiliencia y minimizar el riesgo.

### ¿Los ataques adversarios son solo teóricos?
No; existen numerosos incidentes reales donde sistemas de IA han sido comprometidos mediante técnicas adversarias.

### ¿Cómo se pueden detectar los ataques adversarios?
La detección es difícil; se recomienda monitorear patrones de entrada/salida, caídas de precisión y practicar red teaming regularmente.

### ¿Los ataques adversarios solo afectan al deep learning?
No; aunque el deep learning es especialmente vulnerable, también pueden ser atacados modelos más simples.

## Lecturas y Referencias Autoritativas

- [Sysdig: Adversarial AI – Understanding and Mitigating the Threat](https://www.sysdig.com/learn-cloud-native/adversarial-ai-understanding-and-mitigating-the-threat)
- [Mindgard: 6 Key Adversarial Attacks and Their Consequences](https://mindgard.ai/blog/ai-under-attack-six-key-adversarial-attacks-and-their-consequences)
- [CrowdStrike: Adversarial AI & Machine Learning](https://www.crowdstrike.com/en-us/cybersecurity-101/artificial-intelligence/adversarial-ai-and-machine-learning/)
- [Palo Alto Networks: What Are Adversarial AI Attacks on Machine Learning?](https://www.paloaltonetworks.com/cyberpedia/what-are-adversarial-attacks-on-AI-Machine-Learning)
- [YouTube: Stopping AI-Powered Adversaries](https://www.youtube.com/watch?v=5Oe0E0l6W5k)

## Términos Relacionados

Ejemplos Adversarios, Entrenamiento Adversario, Ataques en Aprendizaje Automático, Inferencia de Membresía, Aprendizaje Automático Adversario, Ataques de Evasión, Ataques de Envenenamiento, Ataques de Extracción de Modelos, Ataques de Inferencia, Inversión de Modelo, Modelos de Aprendizaje Automático, Inteligencia Artificial, Postura de Seguridad, Amenazas Adversarias, Conjunto de Entrenamiento, [Envenenamiento de Datos](/en/glossary/data-poisoning/), Ingeniería Inversa, Proceso de Aprendizaje de Modelos

**Para guías técnicas e investigaciones actualizadas, consulta los recursos anteriores.**