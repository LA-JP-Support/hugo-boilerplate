+++
title = "Slot Filling"
translationKey = "slot-filling-the-definitive-glossary-for-conversational"
description = "Slot filling extrae parámetros específicos de las consultas de los usuarios para completar tareas en IA conversacional. Esencial para recopilar datos, permitir interacción natural y asegurar la finalización de tareas."
keywords = [
  "Slot Filling",
  "IA conversacional",
  "Chatbot",
  "Entidades",
  "Intenciones",
]
category = "Chatbot de IA y Automatización"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Slot-Filling/"

+++
## ¿Qué es Slot Filling?

Slot filling es una técnica central en los sistemas de diálogo orientados a tareas para la [IA conversacional](/en/glossary/conversational-ai/). Se centra en identificar y extraer los parámetros requeridos—llamados slots—de las consultas de los usuarios. Estos slots son necesarios para cumplir una acción concreta, como reservar un vuelo, pedir comida o agendar una cita.

Por ejemplo, en la consulta:

> “Reserva un vuelo de Nueva York a Londres el 20 de julio.”

El agente conversacional debe extraer:
- **Ciudad de salida:** Nueva York
- **Ciudad de destino:** Londres
- **Fecha:** 20 de julio

Slot filling es el mecanismo que permite a la IA analizar esta información, almacenarla y utilizarla de manera efectiva para responder o actuar en nombre del usuario. Si falta alguna información, el sistema solicita al usuario que la proporcione, asegurando un conjunto de datos completo para la tarea.

**Fuentes autorizadas:**  
- [Microsoft Copilot Studio: Uso de entidades y slot filling en agentes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling)  
- [Documentación Dydu: Slot filling](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling)  
- [Just AI Conversational Cloud: Slot filling](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling)  

## ¿Por qué es importante Slot Filling?

Slot filling es esencial para que los sistemas de IA puedan:
- Recopilar todos los datos necesarios para completar una solicitud del usuario (por ejemplo, reservas, pedidos, soporte).
- Permitir que los usuarios proporcionen información de forma natural, en cualquier orden y a lo largo de varias intervenciones.
- Reducir intercambios innecesarios extrayendo el máximo de información de las consultas iniciales y solicitando solo los datos que falten.
- Asegurar la integridad y precisión antes de ejecutar cualquier acción, lo que minimiza errores y malentendidos.

Slot filling es la columna vertebral de cualquier interfaz conversacional que requiera extraer datos estructurados de la entrada libre del usuario ([Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling), [Dydu](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling)).

## Conceptos clave: Slots, Entidades e Intenciones

- **Intención:** El objetivo o propósito del usuario (ej. "Reservar un hotel", "Pedir pizza").
- **Slot:** Un espacio reservado para un dato requerido u opcional necesario para cumplir la intención (ej. “fecha de check-in”, “tamaño de la pizza”).
- **Entidad:** El tipo o categoría de información que un slot espera (ej. ciudad, fecha, número, tipo de ítem).

**Relación:**  
Una intención define la acción, los slots son los parámetros requeridos para esa acción y las entidades describen el tipo de dato que espera cada slot ([Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling), [Just AI](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling)).

## Tipos de entidades usadas en Slot Filling

Las entidades permiten que los chatbots reconozcan y extraigan datos relevantes de la entrada del usuario. Principales categorías:

### 1. Entidades integradas/sistema
Predefinidas por la plataforma conversacional, gestionan tipos de datos comunes como:
- Fechas y horas
- Direcciones de email
- Números de teléfono
- Ciudades y ubicaciones
- Colores, números, moneda

[Entidades predefinidas de Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-about#entities)

### 2. Entidades personalizadas
Definidas por desarrolladores para necesidades específicas del dominio.
- **Entidades de lista cerrada:** Conjunto enumerado de valores aceptables (ej. ingredientes de pizza, SKUs de productos).
- **Expresiones regulares (RegEx):** Patrones para extraer datos estructurados (ej. números de tickets como “INC000123”).

Las entidades personalizadas amplían la capacidad del bot para manejar vocabulario y tipos de datos especializados. ([Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling#closed-list-entities), [Guía de entidades Just AI](https://help.cloud.just-ai.com/en/jaicp/platform_ux/nlu_core/entities))

**Consejo:**  
Use sinónimos y coincidencia difusa para ampliar el reconocimiento de entidades (ej. “NYC” como sinónimo de “New York City”).

## Proceso de Slot Filling: Paso a paso

**1. Definir slots requeridos:**  
Enumere toda la información necesaria para cumplir una intención específica.

**2. Asociar entidades con cada slot:**  
Especifique qué tipo de dato o patrón debe aceptar cada slot.

**3. Extraer valores de slots de la entrada del usuario:**  
Utilice NLU (Natural Language Understanding) para identificar y extraer valores para cada slot.

**4. Solicitar slots faltantes:**  
Si algún slot obligatorio no está completado, el bot hace preguntas para recopilar la información faltante.

**5. Gestionar diálogos multi-turno:**  
Permita que los usuarios completen slots a lo largo de varios mensajes y en cualquier orden.

**6. Confirmar los valores recopilados:**  
Opcionalmente, presente la información recopilada al usuario para su confirmación antes de actuar.

**7. Ejecutar la tarea:**  
Proceda con la acción (ej. reservar, pedir, soporte) cuando todos los slots obligatorios estén completados y confirmados.

**Ejemplo visual (de Dydu):**

- Usuario: "Quiero pedir una pizza."
- Bot: "¿Cuántas porciones desea?"
- Usuario: "8"
- Bot: "¿Qué tipo de pizza desea?"
- Usuario: "Pepperoni"
- Bot: "Desea una pizza de pepperoni de 8 porciones. ¿Es correcto?"
- Usuario: "Sí"
- Bot: "¡Pedido confirmado!"

([Documentación de slot filling de Dydu, con imágenes y flujo de diálogo completo](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling))

## Configuración de slots: Parámetros y opciones

Al definir slots, las opciones de configuración incluyen:

- **Nombre:** Identificador para el slot (ej. `departure_city`).
- **Entidad:** Tipo de dato esperado—integrada o personalizada.
- **Obligatorio:** ¿Es este slot imprescindible para la tarea? Si es así, el bot debe solicitarlo hasta completarlo o cancelar.
- **Es array:** ¿Debe el slot aceptar múltiples valores (ej. “Pide dos pizzas: una Margarita, una Pepperoni”)?
- **Preguntas aclaratorias:** Prompts para usar al solicitar valores de slots faltantes.
- **Valor por defecto:** Valor de respaldo si el slot es opcional y queda vacío.
- **Restablecer/Sobrescribir:** ¿Debe el valor del slot sobrescribirse si el usuario proporciona nueva información?
- **Máximo de reintentos / conteo de basura:** Número máximo de veces para solicitar información antes de abandonar el proceso.
- **Confirmación:** Opción para confirmar los valores de los slots con el usuario antes de continuar.

([Detalles de parámetros de slots en Just AI](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#slot-parameters), [Opciones de slots en Dydu](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#id-1-configuration-of-the-slots))

## Estrategias de implementación y detalles técnicos

### Flujo general

1. **Reconocimiento de intención:**  
   Utilice modelos NLU para detectar la intención e identificar qué slots aplican.

2. **Extracción de entidades:**  
   Aplique reconocimiento de entidades para extraer valores de slots de la entrada del usuario.

3. **Seguimiento de slots:**  
   Mantenga el estado de los slots completados/faltantes durante la conversación.

4. **Lógica de prompts:**  
   Implemente lógica para solicitar los slots obligatorios y gestionar reintentos o interrupciones.

5. **Acceso a scripts/código:**  
   Acceda a los slots completados en scripts de conversación o código backend.

6. **Finalización y confirmación:**  
   Cuando todos los slots obligatorios estén completos, confirme opcionalmente con el usuario antes de ejecutar la acción backend.

**Ejemplo: extracción de slots en código (pseudocódigo)**
```python
if not slots['city']:
    prompt("¿A qué ciudad viaja?")
elif not slots['date']:
    prompt("¿Para qué fecha desea viajar?")
else:
    confirm(f"Reservar un billete a {slots['city']} el {slots['date']}. ¿Es correcto?")
```

### Detalles específicos de la plataforma

- **Copilot Studio:**  
  - Use entidades predefinidas y personalizadas.
  - Active “Smart Matching” para coincidencia difusa y autocorrección.
  - Añada sinónimos en entidades de lista cerrada.
  - Utilice expresiones regulares para extracción de datos estructurados.

([Documentación de entidades y slots en Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling))

- **Just AI Conversational Cloud:**  
  - Configure slots obligatorios/opcionales, tipos array y lógica de reintentos/timeouts en `chatbot.yaml`.
  - Acceda a los slots vía `$parseTree` u otras variables relacionadas.

([Guía de Slot Filling en Just AI](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling))

- **Dydu:**  
  - Defina tipos de conocimiento tipo Slot y configure el proceso de slot filling de forma visual.
  - Use frases introductorias, de confirmación y finales para gestionar el flujo del usuario.

([Guía de configuración de Slot Filling en Dydu](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#id-1-configuration-of-the-slots))

## Ejemplos prácticos y fragmentos de diálogo

### Ejemplo 1: Pedido de pizza (Dydu)
- **Slots requeridos:** Número de porciones, Tipo de pizza

```
Usuario: "Quiero pedir una pizza."
Bot: "¿Cuántas porciones desea?"
Usuario: "8"
Bot: "¿Qué tipo de pizza desea?"
Usuario: "Pepperoni"
Bot: "Desea una pizza de pepperoni de 8 porciones. ¿Es correcto?"
Usuario: "Sí"
Bot: "¡Pedido confirmado!"
```
([Ejemplo de slot filling de Dydu](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#use-case-order-a-pizza))

### Ejemplo 2: Reservar billete de tren
- **Slots requeridos:** Ciudad de destino, Fecha

```
Usuario: "Necesito comprar un billete de tren a París."
Bot: "¿Para qué fecha desea viajar?"
Usuario: "El próximo lunes."
Bot: "Billete a París para el próximo lunes. ¿Procedo?"
```
([Ejemplo de billete de tren de Dydu](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#use-case-buy-a-train-ticket))

### Ejemplo 3: Consulta del clima (Just AI)
- **Slots:** Ciudad (obligatorio), Fecha (opcional)

```
Usuario: "¿Qué tiempo hace en Londres hoy?"
Bot: "El clima en Londres para hoy es soleado con 20°C."
```
Si falta la fecha:
```
Usuario: "¿Qué tiempo hace en París?"
Bot: "¿Para qué fecha necesita el pronóstico?"
```
([Ejemplo de slot filling de Just AI](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#slot-extraction))

## Buenas prácticas en Slot Filling

1. **Utilice entidades integradas cuando sea posible:**  
   Aproveche las entidades proporcionadas por la plataforma para manejar datos comunes de forma robusta.

2. **Agregue sinónimos a las entidades de lista cerrada:**  
   Expanda el reconocimiento con variaciones y términos relacionados.

3. **Active coincidencia inteligente o difusa:**  
   Permita errores ortográficos y términos similares para ampliar el reconocimiento de entidades.

4. **Sea creativo con expresiones regulares:**  
   Use RegEx para formatos de datos estructurados, especialmente para códigos e identificadores.

5. **Confirme valores críticos de slots:**  
   Siempre confirme con el usuario antes de ejecutar acciones importantes.

6. **Establezca límites máximos de reintentos/prompts:**  
   Evite bucles infinitos limitando las solicitudes de slots no completados.

7. **Diseñe para interrupciones:**  
   Permita que los usuarios abandonen los flujos de slot filling o cambien de tema de forma fluida.

8. **Gestione arrays y múltiples valores de slots:**  
   Soporte escenarios donde los usuarios proporcionan varios valores para el mismo slot.

([Buenas prácticas de Just AI](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#interruption-of-slot-filling), [Buenas prácticas de Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/slot-filling-best-practices))

## Errores comunes y cómo evitarlos

- **Falta de preguntas aclaratorias:**  
  Si no se especifica un prompt para un slot obligatorio, la intención puede no ser nunca reconocida.

- **Definiciones de entidades demasiado rígidas:**  
  Evite restringir las entidades a una lista estrecha; use sinónimos y coincidencia inteligente.

- **No gestionar interrupciones de slot filling:**  
  Siempre permita a los usuarios una forma de abandonar o reiniciar el proceso si se quedan atascados.

- **Ignorar pasos de confirmación:**  
  No confirmar los valores de los slots puede derivar en errores o frustración del usuario.

- **No soportar llenado multi-turno o fuera de orden:**  
  Los usuarios esperan poder dar información en cualquier orden y a lo largo de varios mensajes.

- **No manejar máximos de reintentos/timeouts:**  
  Establezca límites razonables para evitar que los usuarios queden atrapados en bucles de aclaración.

([Errores de Just AI](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#interruption-of-slot-filling), [Errores de Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/slot-filling-best-practices))

## Enfoques avanzados: BERT y más allá

### Uso de BERT para Slot Filling

BERT (Bidirectional Encoder Representations from Transformers) ha revolucionado el slot filling al aprovechar el entendimiento profundo y contextual del lenguaje:

- **Representaciones contextuales:** BERT captura el contexto de toda la entrada, ayudando a una detección precisa de los límites de slots.
- **Resolución de ambigüedad:** Gestiona frases ambiguas y abreviaturas en consultas de usuario.
- **Gestión de OOV:** La tokenización por subpalabras soporta la extracción incluso cuando los usuarios usan términos raros o mal escritos.
- **Fine-tuning:** Los modelos BERT preentrenados pueden ajustarse en datasets de slot filling para adaptación al dominio.

**Pasos de implementación:**
1. **Preparación de datos:** Crear datasets etiquetados (tokens + etiquetas de slots).
2. **Tokenización BERT:** Convertir texto en tokens/subpalabras.
3. **Arquitectura del modelo:** Usar BERT como encoder, con una capa de clasificación de slots.
4. **Ajuste fino:** Entrenar con datos etiquetados usando cross-entropy loss.
5. **Inferencia:** Predecir etiquetas de slots para cada token de la entrada del usuario.

**Ejemplo en Python ([Analytics Vidhya](https://www.analyticsvidhya.com/blog/2023/10/conversational-ai-with-bert/)):**
```python
from transformers import BertTokenizer, BertForTokenClassification

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForTokenClassification.from_pretrained('bert-base-uncased', num_labels=num_labels)

# Tokenizar y predecir slots
inputs = tokenizer("Reserva un vuelo de Nueva York a Londres", return_tensors='pt')
outputs = model(**inputs)
```

**Recursos:**  
- [Mejorando la IA conversacional con BERT: El poder del Slot Filling - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2023/10/conversational-ai-with-bert/)

## Casos de uso y aplicaciones en el mundo real

Slot filling impulsa una amplia gama de aplicaciones de IA conversacional:

- **Reservas de viajes:** Ciudades de salida/llegada, fechas, número de pasajeros, clase, etc.
- **Pedidos de e-commerce:** Tipos de producto, cantidades, tallas, colores, direcciones de entrega.
- **Soporte al cliente:** Números de ticket, IDs de cuenta, descripción de incidencias.
- **Reservas en restaurantes:** Nombre del restaurante, fecha, hora, número de comensales, solicitudes especiales.
- **Smart Home/Utilidades:** Nombres de dispositivos, acciones, horarios, configuraciones.
- **Chatbots de salud:** Síntomas, fechas de cita, nombres de médicos, información de seguros.

([Casos de uso en Dydu](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling), [Casos de uso en Just AI](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#slot-extraction))

## Puntos clave

- Slot filling es fundamental en la IA conversacional orientada a tareas, permitiendo que los bots recopilen todos los datos requeridos para cumplir intenciones.
- Se basa en la definición de intenciones, slots y entidades, con NLU robusta para la extracción.
- Diálogos multi-turno, flexibles y pasos de confirmación incrementan la usabilidad y precisión.
- Las buenas prácticas incluyen aprovechar entidades integradas, usar sinónimos y coincidencia difusa, y establecer límites de reintentos.
- Modelos de última generación como BERT permiten una extracción avanzada y de alta precisión.

## Preguntas frecuentes (FAQ)

**P1: ¿Cuál es la diferencia entre un slot y una entidad?**  
Un slot es un espacio reservado para un dato específico necesario para completar una tarea (ej. “fecha” al reservar un billete), mientras que una entidad es la categoría o tipo de dato (ej. “ciudad”, “número”, “fecha”) que puede completar ese slot.

**P2: ¿Cómo sabe un chatbot qué slots debe llenar?**  
Cada intención está asociada a un conjunto de slots requeridos y opcionales. El chatbot rastrea cuáles se han completado y pregunta por los faltantes, según la entrada del usuario y el estado del diálogo.

**P3: ¿Qué pasa si el usuario no proporciona todos los valores requeridos?**  
El chatbot solicitará con preguntas aclaratorias los slots obligatorios que falten, hasta un límite máximo de reintentos o hasta que el usuario abandone el proceso.

**P4: ¿Pueden los usuarios completar varios slots en un solo mensaje?**