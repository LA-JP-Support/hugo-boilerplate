+++
title = "Utterance"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "utterance"
description = "Aprende qué es una utterance en IA conversacional, su rol en NLU/NLP, tipos, flujo de trabajo, desafíos y mejores prácticas para entrenar chatbots de manera efectiva."
keywords = ["utterance", "IA conversacional", "chatbot", "NLU", "NLP"]
category = "Chatbot de IA y Automatización"
type = "glosario"
draft = false
url = "/internal/glossary/Utterance/"

+++
## ¿Qué es una Utterance en IA Conversacional?

Una **utterance** es cualquier entrada, frase o declaración que un usuario comunica a un chatbot o [IA conversacional](/es/glossary/conversational-ai/) durante una conversación, ya sea escribiendo o hablando. Cada mensaje o comando—ya sea una oración, pregunta o fragmento—es una utterance. Por ejemplo:

- Usuario: “¿Cuál es mi saldo de cuenta?” *(utterance)*
- Usuario: “Cancela mi último pedido.” *(utterance)*
- Usuario: “¡Hola!” *(utterance)*

Las utterances son los bloques básicos que los sistemas de IA conversacional interpretan para comprender las necesidades del usuario y generar respuestas apropiadas. Son fundamentales para sistemas que dependen del **entendimiento del lenguaje natural (NLU)** y **procesamiento del lenguaje natural (NLP)**.

**Referencia Autoritativa:**  
- [SiteSpeakAI: ¿Qué es una Utterance?](https://sitespeak.ai/ai-chatbot-terms/utterance)
- [Emplifi: Documentación de Utterances de IA](https://docs.emplifi.io/platform/latest/home/ai-utterances)
- [LinkedIn: Utterance, Intent & Entity en IA Conversacional](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)

## Profundizando: Ejemplos Prácticos de Utterances

Las utterances pueden variar en complejidad, longitud e intención. Van desde saludos breves hasta comandos específicos o preguntas abiertas. Algunos ejemplos comunes:

| Ejemplo de Utterance                      | Posible Intención            |
|-------------------------------------------|------------------------------|
| "¿Cómo está el clima hoy?"                | Consulta de clima            |
| "Reserva un vuelo a París para la próxima semana."| ReservarVuelo            |
| "¡Ayuda!"                                | Solicitar asistencia         |
| "Muéstrame restaurantes italianos cerca." | Búsqueda de restaurante      |
| "Quiero cambiar mi contraseña."           | Gestión de cuenta            |
| "¿Puedes contarme un chiste?"             | Solicitud de entretenimiento |
| "Hola"                                   | Saludo                       |

### Casos de Uso en el Mundo Real

- **Chatbots Bancarios:**  
  - “¿Cómo consulto mi saldo?”
  - “Transfiere $100 a ahorros.”

- **Bots de E-commerce:**  
  - “Rastrea mi pedido.”
  - “Quiero devolver estos zapatos.”

- **Soporte al Cliente:**  
  - “No puedo iniciar sesión en mi cuenta.”
  - “Restablecer mi contraseña.”

Cada entrada de usuario es una utterance que el chatbot debe comprender para satisfacer la solicitud. Capturar una amplia gama de utterances es vital para entrenar IA conversacional de manera efectiva. ([SiteSpeakAI](https://sitespeak.ai/ai-chatbot-terms/utterance))

## Tipos y Categorías de Utterances

Entender la diversidad de utterances es central para un diseño robusto de chatbots y un [reconocimiento de intención](/es/glossary/intent-recognition/) efectivo.

### 1. Utterances Estructuradas vs. No Estructuradas

- **Estructuradas:** Formato claro y predecible.
  - Ejemplo: “Estado del pedido: #12345”
- **No estructuradas:** Fraseo libre y natural.
  - Ejemplo: “¿Me puedes decir dónde está mi último pedido?”

### 2. Utterances Contextuales vs. No Contextuales

- **Contextuales:** Dependen de la conversación previa o datos del usuario.
  - Ejemplo: “¿Cuándo llegará?” (después de hablar de un pedido)
- **No contextuales:** Independientes, se entienden por sí solas.
  - Ejemplo: “¿Cuál es su horario de atención?”

### 3. Utterances Positivas vs. Negativas

- **Positivas:** Satisfacción o acuerdo.
  - “¡Gracias, fue útil!”
- **Negativas:** Insatisfacción o queja.
  - “Esto no funciona para mí.”

### 4. Categorías Orientadas a la Intención

- **Comandos directos:** “Cancela mi cita.”
- **Peticiones corteses:** “¿Podrías cancelar mi cita, por favor?”
- **Preguntas:** “¿Cómo cancelo mi cita?”
- **Declaraciones de intención:** “Quiero cancelar mi cita.”
- **Hipotéticas:** “¿Y si cancelo mi cita?”
- **Parciales/Fragmentadas:** “Cancelar cita”
- **Emoción o retroalimentación:** “Esto es muy lento.” / “¡Gran servicio!”

### 5. Variación Lingüística

- **Formal vs. Informal:** “Me gustaría…” vs. “Quiero…”
- **Jerga, abreviaturas, errores:** “¿Tas ahí?” “Ayuda plz” “No puedo entrar”

#### Tabla de Categorías

| Categoría                | Ejemplo(s)                                 | Caso de Uso                       |
|--------------------------|--------------------------------------------|------------------------------------|
| Comando Directo          | “Eliminar cuenta”                          | Solicitudes de acción              |
| Petición Cortés          | “¿Podrías eliminar mi perfil?”             | Usuarios educados                  |
| Pregunta                 | “¿Cómo restablezco mi contraseña?”         | Búsqueda de orientación            |
| Declaración de Intención | “Quiero cambiar mi dirección de correo”    | Objetivo explícito del usuario     |
| Parcial/Fragmentada      | “Restablecer contraseña”                   | Entrada abreviada                  |
| Hipotética               | “¿Qué pasa si elimino mi cuenta?”          | Analizar consecuencias             |
| Retroalimentación (Positiva) | “¡Gracias por tu ayuda!”               | Expresar gratitud                  |
| Retroalimentación (Negativa) | “Esto no funciona”                     | Expresar frustración               |
| Saludo/Despedida         | “¡Hola!” / “Adiós”                         | Flujo de la conversación           |

## Utterances en el Flujo de Trabajo de un Chatbot

El flujo de procesamiento de utterances en un chatbot involucra varios pasos:

1. **El usuario envía una utterance:** El usuario escribe o pronuncia un mensaje.
2. **Procesamiento de Lenguaje Natural (NLP):** El chatbot analiza la utterance usando:
   - **Tokenización:** Divide la utterance en palabras o tokens.
   - **Stemming/Lematización:** Reduce palabras a su forma base.
   - **Etiquetado gramatical:** Identifica roles gramaticales.
   - **Reconocimiento de Entidades Nombradas (NER):** Extrae detalles clave (como fechas, lugares).
   - **Análisis de Sentimiento:** Evalúa el tono emocional.
3. **Clasificación de Intención:** Determina qué desea lograr el usuario.
   - Ejemplo: “Quiero reservar un vuelo a Tokio.” → Intención: ReservarVuelo
4. **Extracción de Entidades:** Obtiene detalles específicos de la utterance.
   - Ejemplo: Destino = Tokio
5. **Generación de Respuesta:** Usa la intención, entidades y contexto identificados para generar una respuesta.

### Relación: Utterance, Intención y Entidad

| Término    | Descripción                                                        | Ejemplo                                 |
|------------|--------------------------------------------------------------------|-----------------------------------------|
| Utterance  | Lo que dice el usuario                                             | “Encuéntrame vuelos a París el próximo fin de semana” |
| Intención  | El objetivo o propósito detrás de la utterance                     | ReservarVuelo                           |
| Entidad    | Detalles clave dentro de la utterance                              | Destino: París, Fecha: próximo fin de semana |
## Desafíos en el Manejo de Utterances

### 1. Ambigüedad Lingüística

- **Homónimos y homófonos:**  
  - “Reservar una mesa” (acción) vs. “Leer un libro” (objeto)
- **Intención implícita:**  
  - “Hace mucho frío aquí” (implícito: subir la calefacción)

### 2. Jerga, Abreviaturas y Lenguaje Informal

- “Quiero consultar saldo”
- “Ayuda plz”

### 3. Errores Ortográficos y Tipográficos

- “No puedo ingresar”
- “Tarnsferir fondos”

### 4. Utterances Multilingües y de Cambio de Código

- “Quiero order pizza” (mezcla de español e inglés)

### 5. Dependencia de Contexto

- “¿Cuánto cuesta el envío?” (después de hablar de un artículo)

### 6. Intenciones Superpuestas

- Utterances similares pueden corresponder a varias intenciones, causando confusión.

### 7. Variación de Entidades

- “NYC”, “Nueva York”, “La Gran Manzana” (mismo destino)
## Mejores Prácticas para Diseñar y Recopilar Utterances

### 1. Recopilar Utterances Diversas y Representativas

Usa datos reales de usuarios, registros de chat, lluvias de ideas y aprendizaje activo de conversaciones reales. Incluye variaciones en fraseo, estructura y formalidad.

### 2. Evitar Superposición entre Intenciones

Asegura que las utterances para diferentes intenciones sean distintas para evitar clasificación errónea. Revisa regularmente para redundancia o ambigüedad.

### 3. Usar Lenguaje Natural del Usuario

Prioriza cómo los usuarios realmente hablan o escriben, incluyendo jerga, errores y expresiones informales.

### 4. Balancear la Cantidad de Utterances por Intención

Evita sesgos manteniendo un número similar de utterances para cada intención.

### 5. Incluir Variaciones Contextuales y No Contextuales

Entrena tanto para consultas independientes como para aquellas que dependen de la conversación previa.

### 6. Actualizar y Refinar Regularmente la Biblioteca de Utterances

Revisa datos en vivo, añade nuevas utterances y elimina las que no funcionan. Usa herramientas de IA (p.ej., Emplifi, Microsoft LUIS, IBM Watson) para expandir y validar utterances.

### 7. Cubrir Casos Especiales

Incluye saludos, despedidas, solicitudes de ayuda, quejas y retroalimentación. Considera utterances fragmentadas o con errores.

### 8. Probar y Validar

Simula conversaciones reales e itera según la retroalimentación de usuarios y registros del chatbot.

### 9. Manejar Variaciones Multilingües y Regionales

Incluye utterances en todos los idiomas y dialectos soportados para audiencias globales.

### 10. Evitar Información Confidencial o Sensible

Asegura que los datos de utterances no contengan información personal o confidencial.

#### Lista de Verificación de Mejores Prácticas

| Práctica                                 | Descripción                                  |
|-------------------------------------------|----------------------------------------------|
| Variar estructura y longitud              | Utterances cortas, medias y largas           |
| Usar sinónimos y diferentes formulaciones | “Reservar” / “Agendar” / “Programar”         |
| Evitar superposición de intenciones       | Utterances distintas para cada intención      |
| Usar datos reales de usuarios             | Lenguaje auténtico y errores tipográficos     |
| Actualizar regularmente                   | Incorporar retroalimentación en vivo         |
| Balancear utterances por intención        | Prevenir sesgos                              |
| Cubrir casos especiales                   | Saludos, despedidas, manejo de errores        |
## Tipos de Utterances, Desafíos y Soluciones

| Categoría            | Ejemplo                            | Desafío Abordado               | Solución/Mejor Práctica                     |
|----------------------|------------------------------------|-------------------------------|---------------------------------------------|
| Estructurada         | “Estado del pedido: #12345”        | Adherencia al formato          | Incluir formas estructuradas/no estructuradas |
| No estructurada      | “¿Dónde está mi pizza?”            | Variación en el fraseo         | Recopilar utterances reales e informales      |
| Fragmentada          | “Cancelar cuenta”                  | Entrada parcial                | Entrenar con frases incompletas               |
| Errores ortográficos | “No puedo ingresar”                | Errores tipográficos           | Usar corrección ortográfica o entrenar con errores |
| Multilingüe          | “Bonjour, je veux un café”         | Diversidad lingüística         | Conjuntos multilingües de utterances          |
| Contextual           | “¿Cuánto tardará?”                 | Dependencia de contexto        | Motores NLU sensibles al contexto             |
| Retroalimentación negativa | “No funciona”                | Sentimiento, escalamiento      | [Análisis de sentimiento](/es/glossary/sentiment-analysis/), disparadores de escalamiento |
## Preguntas Frecuentes (FAQ) sobre Utterances

**P: ¿Por qué se necesitan múltiples utterances para entrenar un chatbot?**  
R: Los usuarios expresan la misma intención de muchas maneras. Entrenar con utterances diversas permite a los chatbots reconocer una amplia variedad de formulaciones, mejorando la precisión y la experiencia del usuario. ([SiteSpeakAI FAQ](https://sitespeak.ai/ai-chatbot-terms/utterance))

**P: ¿Cómo recopilo utterances para un nuevo chatbot?**  
R: Usa registros de chat históricos, encuestas a usuarios, lluvias de ideas y aprendizaje activo de conversaciones reales.

**P: ¿Cuántas utterances por intención se recomiendan?**  
R: La guía de la industria (p.ej., Microsoft LUIS, Emplifi) sugiere 10–20 utterances bien elegidas por intención. Demasiadas pueden causar confusión; muy pocas limitan la precisión. ([Guía de Utterances de Emplifi](https://docs.emplifi.io/platform/latest/home/ai-utterances))

**P: ¿Debo incluir errores y jerga?**  
R: Sí. Incluye errores comunes, abreviaturas y jerga para mejorar la robustez.

**P: ¿Puede una utterance contener múltiples intenciones?**  
R: Algunos mensajes de usuario pueden expresar más de una intención. Diseña tu chatbot para priorizar, aclarar o manejar utterances multi-intención.

**P: ¿Con qué frecuencia debo actualizar la biblioteca de utterances?**  
R: De forma continua. Revisa regularmente las interacciones en vivo, añade nuevas utterances y elimina ejemplos obsoletos.

**P: ¿Las utterances son solo entradas de usuario?**  
R: Principalmente sí, pero algunos sistemas también modelan utterances del bot/sistema para [gestión avanzada del diálogo](/es/glossary/dialogue-management/).

## Más Lecturas y Recursos

- [Microsoft LUIS: Utterances](https://learn.microsoft.com/en-us/azure/ai-services/luis/concepts/utterances)
- [IBM Cloud: ¿Qué es IA Conversacional? (Búsqueda en YouTube)](https://www.youtube.com/results?search_query=ibm+cloud+conversational+ai)
- [SiteSpeakAI: ¿Qué es una Utterance?](https://sitespeak.ai/ai-chatbot-terms/utterance)
- [Emplifi: Documentación de Utterances de IA](https://docs.emplifi.io/platform/latest/home/ai-utterances)
- [LinkedIn: ¿Qué es Utterance, Intención y Entidad?](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)
- [CogniTech: Intenciones, Entidades, Sinónimos](https://www.cognitech.systems/blog/artificial-intelligence/entry/intents-entities-synonyms-retrieval-natural-language-understanding)
- [BotPenguin: Utterance—Tipos y Desafíos](https://botpenguin.com/glossary/utterance)

## Puntos Clave

- Una **utterance** es cualquier entrada de usuario (texto o voz) proporcionada a un chatbot o IA conversacional.
- Las utterances impulsan el proceso de entendimiento de intención y extracción de entidades para respuestas significativas.
- Capturar utterances diversas, naturales y representativas es fundamental para construir IA conversacional efectiva.
- Revisa y actualiza regularmente la biblioteca de utterances, evita superposición de intenciones y refleja el lenguaje real de los usuarios.
- Manejar variaciones—como jerga, errores, contexto y entradas multilingües—mejora la robustez del chatbot y la satisfacción del usuario.

## Recursos en Video

Para aprendizaje visual y demostraciones, explora:
- [YouTube: IBM Cloud Conversational AI](https://www.youtube.com/results?search_query=ibm+cloud+conversational+ai)
- [Microsoft Azure AI: NLP y Chatbots](https://www.youtube.com/results?search_query=microsoft+azure+ai+chatbot)

*Categoría: Chatbot de IA y Automatización*