+++
title = "Suggestion Chips"
translationKey = "suggestion-chips"
description = "Las suggestion chips son elementos interactivos con forma de pastilla en chatbots e interfaces conversacionales, que ofrecen opciones rápidas y contextuales de respuesta y desaparecen tras seleccionarse."
keywords = ["suggestion chips", "chatbots", "conversational UI", "quick replies", "Dialogflow"]
category = "Chatbot de IA y Automatización"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Suggestion-Chips/"

+++
## ¿Qué son las Suggestion Chips?

**Las suggestion chips**son elementos seleccionables, visualmente diferenciados y con forma de pastilla que presentan a los usuarios opciones de respuesta rápidas y predefinidas en chatbots e interfaces conversacionales. Estas chips aparecen debajo o cerca de la pregunta del bot y representan las respuestas más probables o apropiadas según el contexto. Al tocarlas o hacer clic, el valor de la chip se envía como respuesta del usuario y las chips desaparecen para mantener la interfaz despejada.

**Propósito:**- Acelerar la entrada ofreciendo respuestas de un solo toque.
- Guiar a los usuarios hacia entradas válidas, reduciendo ambigüedades y errores.
- Aumentar la tasa de finalización de conversaciones evitando callejones sin salida.

**Ejemplo:**> Bot: “¿Qué tamaño de pizza deseas?”  
> Suggestion Chips: [Pequeña] [Mediana] [Grande]

## Características clave de las Suggestion Chips

- **Efímeras:**Las chips suelen ser visibles solo para una pregunta y desaparecen tras la selección o la entrada del usuario, ayudando a mantener la conversación limpia y enfocada.

- **Predefinidas:**El conjunto de opciones lo genera la lógica del chatbot, adaptado al contexto actual de la conversación.

- **No persistentes:**Las chips no son botones permanentes de navegación o acción: existen solo para el turno de diálogo relevante.

- **Distinción visual:**Pastillas o burbujas, normalmente diseñadas según las [guías de Material Design](https://m3.material.io/components/chips/guidelines), con separación y relleno claros respecto al flujo principal del chat.

- **Selección de un toque:**Los usuarios pueden responder al instante, reduciendo esfuerzo de escritura y errores.

- **Adaptativas:**Las chips pueden generarse según el contexto, mostrando solo opciones relevantes o válidas según el estado de la conversación o el perfil del usuario.

## Suggestion Chips vs. Otros Elementos de UI

### Suggestion Chips vs. Botones

| Característica         | Suggestion Chips                        | Botones                            |
|-----------------------|-----------------------------------------|------------------------------------|
| Apariencia            | Pastilla/burbuja, efímera               | Rectangular, puede ser persistente |
| Desaparecen tras tocar| Sí                                      | No siempre, a menudo persistentes  |
| Caso de uso           | Opciones ligeras y sensibles al contexto| Navegación, acciones, persistentes |
| Ubicación             | Bajo la pregunta/zona de entrada        | Dentro de tarjetas, mensajes, pies |
| Ejemplo de plataforma | Dialogflow, Messenger ([Quick Replies](/en/glossary/quick-replies/)) | Messenger, Telegram, widgets web   |

**Punto clave:**Las suggestion chips son para decisiones rápidas, contextuales y puntuales; los botones son para acciones continuas o navegación.

### Suggestion Chips vs. Quick Replies

- **Terminología:**"Quick replies" es el término para este patrón en [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies/) y [Telegram](https://core.telegram.org/bots/api#replykeyboardmarkup). Google las llama "suggestion chips" en Dialogflow y Assistant.

- **Comportamiento:**Tanto las chips como los quick replies desaparecen tras usarse, son limitados en número y se orientan a entradas rápidas.

- **Nota técnica:**Algunas plataformas permiten que los quick replies envíen cargas estructuradas o recojan datos del usuario.

**Ver:**[Activechat: Chatbot buttons vs quick replies](https://activechat.ai/news/chatbot-buttons-vs-quick-replies/)

### Suggestion Chips vs. Menús Persistentes

- **Menús:**Siempre visibles, proporcionan navegación/acciones globales (ej: "Ayuda", "Configuración", "Reiniciar").

- **Suggestion Chips:**Efímeras, ligadas a la última pregunta.

### Suggestion Chips vs. Smart Chips

- **Smart Chips:**En [Google Docs](https://support.google.com/docs/answer/10710316?hl=en), son elementos integrados en documentos para enlaces, personas o archivos—no relacionados con UI conversacional.

## Implementación Técnica

### Flujo General

1. **Pregunta del bot:**El chatbot envía un mensaje que requiere entrada.
2. **Mostrar chips:**El cliente muestra las suggestion chips bajo la pregunta.
3. **Acción del usuario:**El usuario toca una chip; el valor se envía al backend.
4. **Respuesta del bot:**El bot procesa la entrada y responde; las chips desaparecen.

### Guía por Plataforma

#### Dialogflow

- **Soporte nativo:**Las suggestion chips están soportadas en integraciones Dialogflow CX y ES para [Google Assistant](https://developers.google.com/assistant/df-asdk/rich-responses), web chat y canales compatibles.

- **Límites técnicos:**- Hasta 8 suggestion chips por pregunta.
  - Solo disponibles en dispositivos con `actions.capability.SCREEN_OUTPUT`.
  - Se requiere al menos una respuesta simple antes de las chips.
  - No se permiten chips en una `FinalResponse`.

- **Chips dinámicas:**Utilice webhooks para generar chips contextuales en los payloads de respuesta.

- **Diseño:**Combine chips con tarjetas o respuestas; no repita la misma información en ambos.
#### Facebook Messenger

- **Quick Replies:**- Hasta 13 quick replies por mensaje ([docs](https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies/)).
  - Cada reply puede tener texto, una imagen opcional y un payload.
  - Desaparecen tras seleccionarse o entrada libre.

- **Botones persistentes:**Para navegación o acciones estáticas, no para entradas efímeras.
#### Telegram

- **ReplyKeyboardMarkup:**- Proporciona teclados personalizados para respuestas de un toque ([docs](https://core.telegram.org/bots/api#replykeyboardmarkup)).
  - Los teclados pueden configurarse como "one-time", haciendo que desaparezcan tras una respuesta.
  - Los botones pueden organizarse en filas y el teclado ocultarse tras usarse.

- **Inline Keyboard:**Usados para botones de acción persistentes.
### Código de ejemplo: Dialogflow Webhook (Node.js)

```javascript
// Ejemplo de fulfillment para suggestion chips en webhook de Dialogflow
const {WebhookClient, Suggestion} = require('dialogflow-fulfillment');

function sendSuggestionChips(agent) {
  agent.add("¿Qué tamaño de pizza deseas?");
  agent.add(new Suggestion('Pequeña'));
  agent.add(new Suggestion('Mediana'));
  agent.add(new Suggestion('Grande'));
}
```
- La clase `Suggestion` está disponible en la librería [dialogflow-fulfillment](https://github.com/dialogflow/dialogflow-fulfillment-nodejs).
- Las chips pueden generarse dinámicamente según la entrada o contexto del usuario.

## Buenas Prácticas para Suggestion Chips

- **Limite la cantidad:**Presente entre tres y cinco opciones como máximo. Demasiadas alternativas saturan y afectan la experiencia del usuario.

- **Sea contextual:**Muestre solo opciones relevantes según el estado del usuario o contexto conversacional.

- **Mantenga etiquetas cortas:**Use textos concisos (menos de 20 caracteres) para evitar saltos de línea o problemas de diseño.

- **Desambiguación:**Utilice chips para clarificar entradas ambiguas o confirmar entidades detectadas.

- **Accesibilidad:**Asegúrese de que las chips tengan buen contraste de color, sean amigables con lectores de pantalla y tengan etiquetas claras. Siga la [guía de accesibilidad de Material Design](https://m3.material.io/components/chips/guidelines).

- **Gestione entradas libres:**Valide y procese la entrada del usuario incluso si ignora las chips y escribe una respuesta.

- **Cumpla límites de la plataforma:**Respete los límites de cantidad y longitud de las chips según cada plataforma.

## Errores Comunes y Cómo Evitarlos

- **Demasiadas chips:**Evite mostrar listas largas. Limítese a 3–5 opciones.

- **Chips desconectadas:**Cada chip debe activar un manejador o intención válida; nunca deje chips sin función.

- **Chips persistentes:**Asegúrese de que las chips desaparezcan tras seleccionarse para evitar confusiones.

- **Entrada no validada:**Siempre gestione los casos en que los usuarios escriben su respuesta en vez de seleccionar una chip.

- **Etiquetas vagas:**Use textos claros y específicos al contexto (“Sí”, “No”, “Mediana”) en vez de frases ambiguas.

- **Ignorar límites de la plataforma:**Cada plataforma tiene límites de cantidad y caracteres para chips/quick replies (ej: 8 en Dialogflow, 13 en Messenger).

## Casos de Uso y Escenarios Prácticos

1. **Slot Filling en flujos de pedido** *Pregunta:* “Elige tamaño de bebida.”  
   *Chips:* [Pequeña] [Mediana] [Grande]  
   *Resultado:* El usuario toca una chip para completar el campo sin escribir.

2. **Desambiguación tras entrada inválida** *Pregunta:* “Lo siento, selecciona tipo de vehículo:”  
   *Chips:* [Auto] [Camión]

3. **Encuestas rápidas o feedback** *Pregunta:* “¿Esto fue útil?”  
   *Chips:* [Sí] [No]

4. **Ramas de conversación** *Pregunta:* “¿Qué te gustaría hacer?”  
   *Chips:* [Explorar] [Estado de pedido] [Soporte]

5. **Recopilación de datos sensibles** *Pregunta:* “Comparte tu información de contacto.”  
   *Chips:* [Usar mi email] [Usar mi número de teléfono]  
   *Nota:* Las chips pueden rellenarse con datos del usuario si la plataforma lo permite.

## Preguntas Frecuentes: Suggestion Chips

**P: ¿Cuáles son los principales beneficios de las suggestion chips?**R: Entrada más rápida, estructurada y resistente a errores, lo que mejora la tasa de éxito de conversaciones.

**P: ¿En qué se diferencian las suggestion chips de los botones?**R: Las chips son efímeras y van ligadas a la pregunta; los botones suelen ser persistentes y se usan para navegación o acciones estáticas.

**P: ¿Los usuarios pueden ignorar las chips y escribir su respuesta?**R: Sí. Siempre valide tanto la selección de chips como la entrada de texto libre.

**P: ¿Qué hago si mi plataforma no soporta chips nativamente?**R: Use quick replies u otros elementos similares, o diseñe botones personalizados con forma de pastilla que imiten el comportamiento de las chips.

**P: ¿Qué hay de la accesibilidad?**R: Asegure buen contraste de color, fuentes legibles y etiquetas ARIA según las [guías de accesibilidad de Material Design](https://m3.material.io/components/chips/guidelines).

## Más recursos y referencias

- [Documentación de respuestas enriquecidas de Dialogflow (Google Assistant)](https://developers.google.com/assistant/df-asdk/rich-responses)
- [Facebook Messenger Quick Replies](https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies/)
- [Telegram Bot API: ReplyKeyboardMarkup](https://core.telegram.org/bots/api#replykeyboardmarkup)
- [Material Design 3: Chips](https://m3.material.io/components/chips/guidelines)
- [Dialogflow Fulfillment Library (Node.js)](https://github.com/dialogflow/dialogflow-fulfillment-nodejs)
- [Activechat: Chatbot buttons vs quick replies](https://activechat.ai/news/chatbot-buttons-vs-quick-replies/)
- [Stack Overflow: Slot filling chatbot, suggestion chips in prompts](https://stackoverflow.com/questions/48091538/slot-filling-chatbot-suggestion-chips-in-prompts)
- [YouTube: Dialogflow chatbot for websites | Botcopy's Bot prompt suggestion chips](https://www.youtube.com/watch?v=SZBMD435mV0)


## Tabla Resumen

| Característica            | Suggestion Chips     | Botones                | Quick Replies          | [Menú Persistente](/en/glossary/persistent-menu/)     |
|--------------------------|---------------------|------------------------|-----------------------|----------------------|
| Apariencia               | Pastilla, efímera   | Rectangular, persistente | Pastilla/burbuja, efímera | Lista, siempre visible |
| Desaparecen al seleccionar| Sí                  | A menudo no            | Sí                    | No                   |
| Caso de uso              | Entrada rápida y guiada | Navegación, acciones   | Entrada rápida         | Acciones globales    |
| Máx. opciones (FB)       | 13 (recomendado 3-5)| 3 por tarjeta          | 13 (óptimo 3-5)        | -                    |

**Conclusión clave:**Utilice suggestion chips (quick replies) para entradas rápidas y contextuales. Limite la cantidad para mayor claridad, mantenga las etiquetas concisas y gestione siempre la entrada libre.

**Términos relacionados:**- [Natural Language Understanding (NLU)](https://es.wikipedia.org/wiki/Comprensi%C3%B3n_del_lenguaje_natural)
- [Slot Filling](https://cloud.google.com/dialogflow/es/docs/slots)
- [Política de privacidad](https://activechat.ai/privacy-policy/)
- [Términos de servicio](https://activechat.ai/terms-of-service/)

**Ver también:**- [Insertar smart chips en Google Docs](https://support.google.com/docs/answer/10710316?hl=en) *(para colaboración en documentos, no chatbots)*

**Última actualización:**2024-06

**Fuentes y referencias:**- [Documentación de respuestas enriquecidas de Dialogflow](https://developers.google.com/assistant/df-asdk/rich-responses)
- [Material Design 3: Chips](https://m3.material.io/components/chips/guidelines)
- [Facebook Messenger Quick Replies](https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies/)
- [Telegram Bot API: ReplyKeyboardMarkup](https://core.telegram.org/bots/api#replykeyboardmarkup)
- [Activechat: Chatbot buttons vs quick replies](https://activechat.ai/news/chatbot-buttons-vs-quick-replies/)
- [Stack Overflow: Slot filling chatbot, suggestion chips in prompts](https://stackoverflow.com/questions/48091538/slot-filling-chatbot-suggestion-chips-in-prompts)
- [Dialogflow Fulfillment Library (Node.js)](https://github.com/dialogflow/dialogflow-fulfillment-nodejs)
- [YouTube: Dialogflow chatbot for websites | Botcopy's Bot prompt suggestion chips](https://www.youtube.com/watch?v=SZBMD435mV0)