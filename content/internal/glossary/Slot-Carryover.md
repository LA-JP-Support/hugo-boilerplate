+++
title = "Slot Carryover"
translationKey = "slot-carryover"
description = "La transferencia de ranuras permite que los chatbots de IA recuerden y reutilicen información estructurada (ranuras) a lo largo de los turnos conversacionales, manteniendo el contexto y mejorando la experiencia del usuario en sistemas de diálogo orientados a tareas."
keywords = [
    "Transferencia de Ranuras",
    "Chatbot de IA",
    "Sistemas de Diálogo",
    "Seguimiento del Estado del Diálogo",
    "Gestión de Contexto",
]
category = "General"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Slot-Carryover/"

+++
## Introducción

La transferencia de ranuras es una capacidad central en los chatbots modernos impulsados por IA, especialmente dentro de los sistemas de diálogo orientados a tareas. Permite al sistema recordar, reutilizar y aplicar correctamente información estructurada previamente recolectada (ranuras) a lo largo de múltiples turnos conversacionales. En sistemas de diálogo tanto hablados como basados en texto, la transferencia de ranuras afecta directamente la capacidad del sistema para mantener el contexto y responder a los usuarios de manera coherente y útil. Esto es particularmente importante en conversaciones complejas, de múltiples turnos y dominios, donde los usuarios hacen referencia a preferencias o entidades mencionadas anteriormente, a menudo utilizando pronombres o referencias implícitas.

Por ejemplo, si un usuario dice: “Reserva un vuelo a París”, y luego, “Búscame un hotel allí”, el sistema debe entender que “allí” se refiere a “París” y transferir la ranura relevante.

Una transferencia de ranuras efectiva elimina la necesidad de que los usuarios repitan información, apoya la resolución natural de referencias en el lenguaje y garantiza que el chatbot mantenga un estado conversacional preciso a medida que evoluciona el diálogo. A medida que los sistemas de diálogo se vuelven más sofisticados y abordan tareas más complejas y variadas, se requiere una transferencia de ranuras robusta para proporcionar asistencia inteligente y consciente del contexto.

**Fuente clave:**  
- [Amazon Science: Improving long distance slot carryover in spoken dialogue systems](https://www.amazon.science/publications/improving-long-distance-slot-carryover-in-spoken-dialogue-systems)  
- [arXiv:1906.01149](https://arxiv.org/abs/1906.01149)

## Definición principal

**Transferencia de ranuras** es el proceso mediante el cual un chatbot de IA o sistema de diálogo determina si una ranura—un fragmento de información estructurada extraída como una entidad, valor o atributo—identificada en turnos previos de usuario o sistema, sigue siendo relevante y debe ser reutilizada o transferida para cumplir con la intención actual del usuario.

**Definición formal:**  
> “La transferencia de ranuras es la tarea en la que un modelo toma una decisión binaria para cada ranura candidata del contexto previo del diálogo, determinando si debe ser transferida al turno actual para apoyar el cumplimiento de la intención.”  
> — [Chen et al., 2019, arXiv:1906.01149](https://arxiv.org/abs/1906.01149)

Este proceso es fundamental para el [seguimiento del estado del diálogo](/es/glossary/dialogue-state-tracking/) (DST), ya que implica:

- **Seguimiento**: Monitorizar la aparición y evolución de las ranuras y sus valores a lo largo del diálogo.
- **Mapeo**: Traducir ranuras entre esquemas o dominios potencialmente diferentes (por ejemplo, mapear “WeatherLocation” en una app de clima a “City” en una app de reserva de viajes).
- **Selección**: Aplicar modelos o reglas aprendidas para decidir qué ranuras son relevantes para el turno actual.

**Ejemplo de uso:**  
En un asistente de viajes, si un usuario dice: “Quiero volar a Berlín”, se extrae la ranura {Destino: Berlín}. Si el usuario luego dice: “Reserva un hotel allí”, el sistema necesita transferir la ranura “Berlín” para cumplir correctamente la intención.

**Citas:**  
- [Chen et al., 2019, ACL Anthology](https://aclanthology.org/W19-4111/)
- [Naik et al., 2018, ISCA Archive](https://www.isca-archive.org/interspeech_2018/naik18_interspeech.html)

## Profundización técnica

### Retos técnicos

La transferencia de ranuras, especialmente en sistemas de diálogo reales, de múltiples turnos y dominios, plantea varios retos técnicos:

| Reto                            | Descripción                                                                                             |
|----------------------------------|--------------------------------------------------------------------------------------------------------|
| Retención contextual             | Mantener ranuras relevantes a lo largo de largas historias de diálogo y múltiples turnos.              |
| Heterogeneidad de esquemas       | Manejar diferentes nombres de claves y estructuras de ranuras entre dominios (ej. “WeatherLocation” vs. “City”). |
| Escalabilidad de valores de ranura | Soportar un conjunto grande, posiblemente ilimitado, de valores de ranura, incluyendo entidades de clase abierta. |
| Complejidad multidominio         | Gestionar la transferencia a través de dominios dispares con esquemas no solapados o conflictivos.     |
| Ambigüedad y resolución de referencias | Resolver referencias indirectas, pronombres o ranuras implícitas.                              |
| Propagación de errores           | Mitigar errores acumulativos de extracciones o decisiones de transferencia incorrectas previas.         |

### Enfoques de modelado

#### Enfoques basados en reglas

Las primeras implementaciones de transferencia de ranuras usaban reglas manuales, como transferir siempre la ranura más reciente o aplicar heurísticas según la recencia y tipo de la ranura. Aunque son directos, estos enfoques carecen de flexibilidad y fallan en conversaciones complejas.

- **Línea base ingenua**: Transfiere siempre todas las ranuras del turno previo inmediato.
- **Línea base basada en reglas**: Emplea reglas manuales para ciertos tipos de ranuras o patrones conversacionales.

**Limitaciones:**  
Los sistemas basados en reglas son frágiles y no se generalizan bien a flujos no vistos o nuevos dominios. Tienen bajo rendimiento en casos de referencias de largo alcance o heterogeneidad de esquemas.  
#### Arquitecturas de redes neuronales

El estado del arte en transferencia de ranuras se basa en modelos neuronales que pueden gestionar dinámicamente el contexto y la relevancia de las ranuras:

**1. Redes Pointer:**  
Permiten al modelo seleccionar y ordenar ranuras del historial de diálogo, capturando referencias explícitas a ranuras previas. Modelan la secuencia y el orden de las ranuras, importante cuando se referencian múltiples ranuras y el orden es relevante.

**2. Modelos basados en Transformers:**  
Los transformers emplean self-attention para modelar dependencias entre ranuras y turnos de diálogo. Esto permite a la red enfocar qué ranuras de todo el historial son relevantes para el turno actual, sin importar su posición.

> “Proponemos dos arquitecturas de red neuronal, una basada en redes pointer que incorporan información de orden de ranuras, y otra basada en transformers que usan mecanismos de self-attention para modelar interdependencias de ranuras.”  
> — [Chen et al., 2019, arXiv:1906.01149](https://arxiv.org/abs/1906.01149)

**3. Mecanismos de atención:**  
Mecanismos de atención a nivel de palabra y flujo ayudan al modelo a enfocarse en las expresiones y menciones de ranuras más relevantes, mejorando la resolución de referencias ambiguas o de largo alcance.

**4. Mapeo de esquemas basado en embeddings:**  
Representando claves y valores de ranuras como embeddings, los modelos pueden calcular similitud entre ranuras de esquemas heterogéneos. Es crucial para mapear ranuras entre dominios con convenciones o estructuras diferentes.

**5. Decisión de transferencia de extremo a extremo:**  
Los enfoques modernos plantean la transferencia de ranuras como una tarea de clasificación binaria o selección sobre un conjunto candidato, usando codificaciones contextuales, embeddings de ranura e indicadores de recencia.

**Ejemplo de pseudocódigo:**  
```
Para cada ranura candidata en el contexto:
    1. Codificar características de la ranura (embedding de clave, embedding de valor)
    2. Codificar la expresión actual y el historial de diálogo (LSTM/Transformer)
    3. Aplicar atención sobre historial y ranuras candidatas
    4. Concatenar codificaciones, calcular probabilidad de transferencia vía softmax
    5. Si probabilidad > umbral, transferir ranura
```
### Benchmarks y conjuntos de datos

Evaluar modelos de transferencia de ranuras requiere conjuntos de datos robustos que representen la complejidad conversacional real. Los benchmarks más destacados incluyen:

- **Serie DSTC (Dialog State Tracking Challenge):**  
  - [DSTC2](https://www.microsoft.com/en-us/research/event/dialog-state-tracking-challenge/): Enfocado en reservas de restaurantes, ampliamente usado para tareas de transferencia y seguimiento de estado.
  - DSTC8, DSTC9: Versiones posteriores con escenarios multidominio más desafiantes.

- **Schema-Guided Dialogue (SGD) Dataset:**  
  - [SGD](https://huggingface.co/datasets/schema_guided_dstc8): Dataset a gran escala multidominio, diseñado para evaluar mapeo de esquemas y transferencia entre numerosos servicios y dominios.

- **Colección de conjuntos de datos de seguimiento de estado de diálogo en Hugging Face:**  
  - [Colección curada de DST](https://huggingface.co/collections/pietrolesci/dialogue-state-tracking-datasets) incluyendo MultiWOZ, WOZ y otros.

- **Dataset interno de Amazon Alexa:**  
  - Usado en [Chen et al., 2019](https://aclanthology.org/W19-4111/) para evaluar transferencia de ranuras en escenarios de producción.

**Recursos de datasets:**  
- [Hugging Face Dialogue State Tracking Datasets](https://huggingface.co/collections/pietrolesci/dialogue-state-tracking-datasets)
- [DSTC Challenges](https://www.microsoft.com/en-us/research/event/dialog-state-tracking-challenge/)

## Consideraciones de implementación

### Mapeo de esquemas de ranura

La transferencia de ranuras entre dominios suele requerir mapear claves y valores entre esquemas diferentes. Por ejemplo:

| Ranura Dominio A         | Ranura Dominio B           | ¿Requiere transformación? |
|--------------------------|----------------------------|--------------------------|
| WeatherLocation: Tokyo   | City: Tokyo                | Sí                       |
| Entity: La Taqueria      | Place: La Taqueria         | Sí                       |

**Técnicas:**

- **Embeddings de etiquetas:** Promedio de embeddings de palabras preentrenados para claves y valores, para calcular similitud y mapeos candidatos.
- **Mapeo impulsado por datos:** Aprender mapeos desde los datos en vez de depender de diccionarios estáticos o reglas manuales.

### Generación de ranuras candidatas

El sistema genera un conjunto candidato de ranuras del contexto completo de la conversación, transformándolas luego al esquema del dominio actual. Este paso es crítico para limitar el cómputo y enfocar las decisiones de transferencia en ranuras plausibles.

### Métricas de evaluación

Las principales métricas de desempeño para la transferencia de ranuras incluyen:

- **Precisión**: Proporción de ranuras transferidas que son correctas.
- **Cobertura (Recall)**: Proporción de ranuras relevantes que se transfieren exitosamente.
- **F1 Score**: Media armónica de [precisión y cobertura](/es/glossary/precision-and-recall/).

| Método            | Precisión | Cobertura | F1    |
|-------------------|-----------|-----------|-------|
| Línea base ingenua| 17.01     | 92.50     | 28.74 |
| Línea base reglas | 91.79     | 67.11     | 77.53 |
| Encoder-Decoder   | 73.31     | 96.17     | 83.20 |
| +Word Attention   | 75.76     | 94.65     | 84.16 |

*Fuente: [Chen et al., 2019, Tabla 2](https://aclanthology.org/W19-4111/)*

### Gestión de memoria y privacidad

#### Tipos de memoria

| Tipo de memoria | Alcance                  | Ejemplo de uso          |
|-----------------|--------------------------|-------------------------|
| Corto plazo     | Dentro de la sesión      | Flujo de reserva actual |
| Largo plazo     | Entre sesiones/usuarios  | Perfil de usuario       |
| Contextual      | Por tema o hilo          | Tarea de múltiples pasos|
| Episódica       | Episodios específicos    | Historial de soporte    |

*Ver también: [Tencent Cloud Techpedia](https://www.tencentcloud.com/techpedia/127640)*

#### Privacidad y escalabilidad

- **Retención de datos**: Políticas estrictas sobre qué información se almacena y por cuánto tiempo.
- **Consentimiento del usuario**: Mecanismos de opt-in/opt-out y [transparencia](/es/glossary/transparency/).
- **Almacenamiento seguro**: Cifrado y control de acceso a valores sensibles de ranura.
- **Escalabilidad**: Indexado y recuperación eficiente para soportar grandes cantidades de usuarios e historiales largos.

**Riesgos de privacidad y protección:**  
Los chatbots pueden almacenar inadvertidamente datos sensibles del usuario (por ejemplo, ubicación, identificadores personales) en memorias de ranura, generando inquietudes de privacidad. Buenas prácticas incluyen:

- Limitar el almacenamiento de información personal identificable (PII).
- Brindar a los usuarios opciones explícitas para controlar lo que se recuerda.
- Depurar regularmente memorias de ranura conforme a la política de privacidad.
- Usar almacenamiento cifrado y controles de acceso.

## Aplicaciones y ejemplos

### Asistentes multidominio

La transferencia de ranuras es indispensable para asistentes que soportan múltiples dominios (por ejemplo, clima, búsqueda local, reservas). Permite transiciones fluidas y resolución natural de referencias.

**Ejemplo de diálogo:**

| Turno | Dominio      | Entrada del usuario                        | Ranuras extraídas/transferidas         |
|-------|--------------|--------------------------------------------|----------------------------------------|
| U1    | Clima        | "¿Qué tiempo hace en Tokio?"               | WeatherLocation: Tokyo                 |
| V1    | Clima        | "Está lluvioso y 15°C."                    | Temperature: 15°C                      |
| U2    | Búsqueda local| "Encuentra un restaurante de sushi allí." | PlaceType: sushi<br>City: Tokyo (transferida) |
| V2    | Búsqueda local| "Sushi Go está a 2 km."                  | Entity: Sushi Go                       |
| U3    | Reservas     | "Reserva una mesa allí para mañana."       | Entity: Sushi Go (transferida)         |

### Fragmentos técnicos de diálogo

#### Transferencia monodominio

```
Usuario: ¿Qué tiempo hace en San Francisco?
Bot: Está soleado y 18°C.
Usuario: Reserva un hotel allí para esta noche.
```
*Transferencia: "San Francisco" se transfiere de clima a reserva de hotel.*

#### Mapeo de esquemas entre dominios

```
Usuario: Busca restaurantes italianos en París.
Bot: Aquí tienes algunas opciones.
Usuario: Reserva una mesa en el primero.
```
*Transferencia: "París" se mapea de "Location" en búsqueda a "City" en reservas.*

#### Transferencia a larga distancia

```
Usuario: Quiero volar a Berlín.
Bot: ¿Qué fechas estás considerando?
Usuario: El próximo fin de semana.
Bot: ¿Reservo también un hotel allí?
Usuario: Sí, por favor.
```
*"Berlín" se referencia a lo largo de varios turnos y dominios.*

## Retos y limitaciones

- **Propagación de errores:** Los errores en la extracción o transferencia de ranuras pueden acumularse y afectar etapas posteriores.
- **Alineamiento de esquemas:** El mapeo automático de ranuras entre dominios con esquemas dispares sigue siendo complejo, especialmente a gran escala.
- **Resolución de ambigüedades:** Referencias implícitas, pronombres y expresiones dependientes del contexto requieren modelado avanzado de co-referencia y contexto.
- **Privacidad de datos:** El almacenamiento y procesamiento de datos sensibles exige salvaguardas robustas, cifrado y cumplimiento (ej. RGPD).
- **Coste computacional:** Los modelos basados en transformers y mecanismos de atención aumentan los requerimientos computacionales y de memoria para ventanas de contexto amplias.

## Referencias y lecturas adicionales

- [Improving Long Distance Slot Carryover in Spoken Dialogue Systems – Amazon Science](https://www.amazon.science/publications/improving-long-distance-slot-carryover-in-spoken-dialogue-systems)
- [arXiv: Improving Long Distance Slot Carryover in Spoken Dialogue Systems (Chen et al., 2019)](https://arxiv.org/abs/1906.01149)
- [ACL Anthology: Improving Long Distance Slot Carryover in Spoken Dialogue Systems](https://aclanthology.org/W19-4111/)
- [Interspeech 2018: Contextual Slot Carryover for Disparate Schemas (Naik et al.)](https://www.isca-archive.org/interspeech_2018/naik18_interspeech.html)
- [Hugging Face: Dialogue State Tracking Datasets Collection](https://huggingface.co/collections/pietrolesci/dialogue-state-tracking-datasets)
- [Mozilla Foundation: How to Protect Your Privacy from ChatGPT and Other AI Chatbots](https://www.mozillafoundation.org/en/privacynotincluded/articles/how-to-protect-your-privacy-from-chatgpt-and-other-ai-chatbots/)

## Tabla resumen: Transferencia de ranuras vs. conceptos relacionados

| Concepto               | Propósito                                   | Técnicas típicas                                       |
|------------------------|---------------------------------------------|--------------------------------------------------------|
| Transferencia de ranuras| Retener y transferir ranuras entre turnos  | Basado en reglas, redes pointer, transformers, atención|
| Seguimiento del estado del diálogo| Rastrear el conjunto completo de ranuras/valores por turno | Modelos secuenciales, redes de memoria, seguimiento de marcos |
| Memoria contextual     | Mantener historial conversacional           | Memoria corto/largo plazo, ventanas de contexto, RAG   |
| Mapeo de esquemas      | Alinear ranuras entre dominios              | Basado en embeddings, impulsado por datos, mapeo manual|

**Nota:**  
Para ejemplos más técnicos y a nivel de código, consulte los siguientes recursos y sus referencias:  
- [Chen et al., 2019, arXiv PDF](https://arxiv.org/pdf/1906.01149)  
- [ISCA Archive: Naik et al. 2018](https://www.isca-archive.org/interspeech_2018/naik18_interspeech.html)  
- [[Hugging Face](/es/glossary/hugging-face/) DST Dataset Collection](https://huggingface.co/collections/pietrolesci/dialogue-state-tracking-datasets)