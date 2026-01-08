+++
title = "Tarjetas multimedia enriquecidas"
translationKey = "rich-media-cards"
description = "Las tarjetas multimedia enriquecidas son componentes interactivos de la interfaz en flujos de chat, que entregan contenido multimedia y elementos accionables como imágenes, videos y botones para conversaciones atractivas."
keywords = ["tarjetas multimedia enriquecidas", "chatbot", "IA conversacional", "plataformas de mensajería", "engagement de usuario"]
category = "Chatbot de IA & Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Rich-Media-Cards/"

+++
## Definición

Las tarjetas multimedia enriquecidas son componentes estructurados e interactivos de la interfaz de usuario que se integran en flujos de chat, permitiendo entregar contenido multimedia atractivo y elementos accionables directamente dentro de la conversación. A diferencia de los mensajes de texto plano, una tarjeta multimedia enriquecida puede agrupar imágenes, GIFs, videos, títulos, subtítulos y botones, ofreciendo a los usuarios una experiencia visualmente atractiva y práctica. Estas tarjetas actúan como mini páginas de destino en el chat, capaces de impulsar acciones, recopilar información y mejorar la usabilidad y la conversión.

**Referencias autorizadas:**- [Google RCS Business Messaging: Rich Cards](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards)  
- [Microsoft Bot Framework: Add Rich Card Attachments](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0)  
- [Sprinklr: Chatbot Analytics](https://www.sprinklr.com/blog/chatbot-analytics/)  
- [Tars: Rich Media for Chatbots](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)  
- [Kommunicate: Best Chatbot Practices](https://www.kommunicate.io/blog/best-chatbot-practices/)  
- [Quickchat: Chatbot Analytics Deep Dive](https://quickchat.ai/post/chatbot-analytics)  

## Anatomía de una tarjeta multimedia enriquecida

Las tarjetas multimedia enriquecidas se construyen a partir de un conjunto de componentes estándar, cada uno con una función visual y/o funcional. Estos incluyen:

- **Elemento multimedia:**Imágenes (JPEG, PNG, GIF), animaciones, videos (MP4, M4V, WebM, etc.) o incluso PDFs (según la plataforma). El medio sirve para captar atención, ilustrar productos o dar carácter.
  - [Ver formatos y alturas soportadas por Google RCS](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#media)
- **Miniatura:**Vista previa personalizada o predeterminada para archivos multimedia, especialmente para archivos grandes o PDFs. Las miniaturas deberían pesar menos de 100 KB para cargar óptimamente.
- **Título:**El encabezado o etiqueta principal, normalmente hasta 200 caracteres (según la plataforma). Debe ser conciso e informativo.
- **Subtítulo/Descripción:**Texto de apoyo, a menudo hasta 2.000 caracteres, brindando contexto adicional, beneficios o información de llamada a la acción (CTA).
- **Botones de acción:**Elementos clicables que disparan acciones inmediatas (navegación web, postbacks, llamadas telefónicas, descargas, etc.). Los límites y tipos de botones varían según la plataforma.
- **Respuestas sugeridas:**Respuestas predefinidas presentadas como chips o botones, guiando la conversación por caminos óptimos y compatibles con bots.
- **Elementos interactivos opcionales:**Carruseles (grupos desplazables de tarjetas), formularios (para captura de datos), [respuestas rápidas](/es/glossary/quick-replies/), selectores de listas y cargas útiles personalizadas.

**Ilustraciones y referencias:**- [Google: Componentes de una Rich Card](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#rich-card-components)
- [Microsoft: Tipos de tarjetas](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0#types-of-rich-cards)

## Cómo se usan las tarjetas multimedia enriquecidas

### 1. Engagement conversacional

Las tarjetas multimedia enriquecidas mejoran drásticamente la interacción con chatbots al hacer las conversaciones más accionables, expresivas y atractivas visualmente. Casos de uso comunes incluyen:

- **Recomendaciones de productos:**Mostrar imágenes de productos, precios y botones de “Comprar ahora”.
- **Generación de leads:**Integrar formularios para captar datos del usuario dentro del chat.
- **Soporte al cliente:**Presentar guías paso a paso, cada una con botones de “¿Esto ayudó?”.
- **Reservas/Agendamientos:**Mostrar horarios o servicios disponibles como tarjetas con botones de reserva instantánea.
- **Encuestas y feedback:**Solicitar calificaciones, comentarios o selecciones directamente a través de las tarjetas.
- **FAQs interactivas:**Temas de ayuda navegables con tarjetas expandibles/colapsables para explorar contenido de soporte.

**Mejor práctica:**Utiliza tarjetas multimedia enriquecidas para imitar el flujo conversacional natural, ofreciendo opciones de un solo toque que reducen fricción y aumentan tasas de finalización. [Tars: Cómo mejorar la tasa de finalización de tu chatbot usando rich media](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)

### 2. Mensajería multiplataforma

El soporte y las funciones de las tarjetas multimedia enriquecidas difieren entre plataformas de mensajería. Los entornos clave incluyen:

- **Widgets de chat web:**Soporte completo de tarjetas, [carrusel](/es/glossary/carousel/) y formularios; layouts personalizables (ej. Intercom, Drift, Kommunicate).
- **Mensajería social:**- **Facebook Messenger:**Plantillas de tarjetas, carruseles, respuestas rápidas, hasta 10 tarjetas por carrusel.
  - **WhatsApp:**Plantillas de listas y botones limitadas (sin carrusel), hasta 3 botones por mensaje.
  - **Apple Business Chat:**Tipos de tarjetas avanzados, Apple Pay, formularios, selectores de listas.
  - **Telegram, Viber, Slack:**Soporte variable para tarjetas, botones y multimedia.
- **Soluciones empresariales:**- **Microsoft Dynamics 365, Salesforce:**Adaptive Cards (basadas en JSON), carruseles, captura de datos personalizada, integración profunda.
  - **APIs:**Bots personalizados con cargas útiles programables y renderizado de UI.
## Implementación técnica y plataformas soportadas

### Estructura de tarjetas y cargas útiles

Las tarjetas multimedia enriquecidas normalmente se definen en formatos estructurados como JSON. Cada plataforma puede tener su propio esquema, pero la mayoría comparte elementos comunes:

**Ejemplo: Tarjeta de producto genérica (JSON)**```json
{
  "type": "card",
  "title": "Auriculares inalámbricos",
  "subtitle": "Cancelación de ruido, batería de 20h",
  "image_url": "https://example.com/img/headphones.png",
  "buttons": [
    {
      "type": "web_url",
      "title": "Comprar ahora",
      "url": "https://example.com/buy/headphones"
    },
    {
      "type": "postback",
      "title": "Más info",
      "payload": "INFO_HEADPHONES"
    }
  ]
}
```
- [Google: Estructura JSON para RCS Rich Cards](https://developers.google.com/business-communications/rcs-business-messaging/guides/build/messages/send)
- [Microsoft: Esquemas de tarjetas de Bot Framework](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0)

### Carrusel (conjunto de tarjetas desplazable)

Un carrusel presenta varias tarjetas en formato desplazable horizontalmente, ideal para descubrimiento de productos o selección de opciones.

**Ejemplo: Carrusel (JSON)**```json
{
  "type": "carousel",
  "cards": [
    {
      "title": "Producto 1",
      "image_url": "https://example.com/img/p1.png",
      "buttons": [ ... ]
    },
    {
      "title": "Producto 2",
      "image_url": "https://example.com/img/p2.png",
      "buttons": [ ... ]
    }
  ]
}
```

### Tipos de tarjetas soportadas (Microsoft Bot Framework)

- **HeroCard:**Imagen grande, texto y botones.
- **ThumbnailCard:**Imagen pequeña, texto y botones.
- **AnimationCard/VideoCard/AudioCard:**Reproducción de medios embebidos.
- **ReceiptCard:**Recibos estructurados con ítems, precios y totales.
- **SignInCard:**Flujos de autenticación OAuth o de terceros.
- **AdaptiveCard:**Tarjetas altamente personalizables con elementos UI, layouts y formularios. [Adaptive Cards Designer](https://adaptivecards.io/designer/)

**Referencia detallada:**- [Microsoft Bot Framework Card Types](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0#types-of-rich-cards)

### Restricciones específicas por plataforma

| Plataforma             | Soporte de tarjetas  | Máx tarjetas/carrusel | Límite de tamaño de imagen | Límite de botones | Características destacadas            |
|------------------------|---------------------|----------------------|---------------------------|-------------------|---------------------------------------|
| Widgets de chat web    | Completo (tarjetas, formularios) | Varía (hasta 10)   | ~1MB por imagen           | 3–5/botón         | Layouts personalizados, respuestas rápidas |
| WhatsApp               | Limitado (lista, botón) | 1–3/fila           | <1MB                      | 3                 | Tarjetas simples, sin carruseles      |
| Apple Business Chat    | Avanzado            | Varía                | ~1MB                      | 3–5               | Apple Pay, formularios, selectores de lista |
| Facebook Messenger     | Completo (tarjeta, carrusel) | 10/carrusel      | 1MB                       | 3                 | Plantillas, respuestas rápidas        |
| Microsoft Dynamics 365 | Completo (tarjetas, JSON) | 10/carrusel       | 1MB                       | 5                 | Adaptive cards, formularios, JSON personalizado |

**Notas técnicas:**- Comprime siempre imágenes y videos para mejorar la velocidad, especialmente en móviles.
- Respeta los límites de caracteres específicos de cada plataforma (títulos, botones, etc.).
- Prueba la interactividad y formato en diferentes dispositivos y canales.
- Usa analítica y seguimiento para clics en botones, vistas de tarjetas y acciones de usuario.
- [Google: Guía de subida de medios y miniaturas](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#thumbnail)

## Beneficios clave de las tarjetas multimedia enriquecidas

### 1. Mayor engagement

Las tarjetas multimedia enriquecidas superan constantemente a los mensajes solo de texto en términos de engagement. Los datos muestran:
- Las conversaciones con imágenes pueden generar **2–3 veces más engagement**([Conferbot](https://www.conferbot.com/features/rich-media), [Tars](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media))
- Los elementos visuales y botones captan la atención y fomentan la interacción.
- Sin fricción: los usuarios pueden actuar con un solo toque (comprar, reservar, responder).

### 2. Mejores tasas de conversión

- Los chatbots con elementos multimedia enriquecidos consiguen hasta **85% más tasa de conversión**que los bots solo de texto ([Tars](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)).
- Formularios interactivos, carruseles y CTAs optimizan el recorrido del usuario y reducen la deserción.

### 3. Mejor experiencia de marca

- Las tarjetas refuerzan la identidad de marca con imágenes, colores y tono personalizados.
- Son más memorables y agradables, elevando el recuerdo de marca.
- Humanizan el chatbot—añadiendo personalidad con GIFs, emojis o video.

### 4. Eficiencia operativa

- Disminuye la carga del soporte guiando a los usuarios a respuestas de autoservicio.
- Estandariza respuestas, garantizando consistencia y precisión.

### 5. Analítica avanzada y seguimiento

Las tarjetas multimedia enriquecidas son rastreables, permitiéndote medir cuáles tarjetas, botones y flujos generan engagement. Analíticas clave incluyen:
- Tasa de clics en botones
- Número de vistas de tarjetas
- Puntos de abandono y análisis de embudo
- Tasas de finalización de objetivos
## Casos de uso y ejemplos reales

### Generación de leads

**Escenario:**Un chatbot web muestra un carrusel de servicios, cada uno con botón de “Consultar”. El usuario envía sus datos de contacto directamente en el chat.  
**Beneficio:**Captura de datos sin fricción que incrementa el volumen y calidad de leads.

### Descubrimiento de productos en e-commerce

**Escenario:**Bot de Messenger envía un carrusel de más vendidos, cada tarjeta con imagen del producto, precio y botón “Comprar ahora”.  
**Beneficio:**Navegación y compra simplificadas, impulsando la conversión.

### Soporte al cliente

**Escenario:**Un bot presenta pasos de solución de problemas como tarjetas, cada una con botones de “¿Esto ayudó?”.  
**Beneficio:**Reduce carga de agentes y acelera la resolución.

### Reserva de citas

**Escenario:**El bot muestra horarios disponibles como tarjetas; el usuario toca para confirmar.  
**Beneficio:**Simplifica la agenda y reduce el abandono.

### Encuestas y feedback

**Escenario:**Tras una interacción, una tarjeta pide puntuación con estrellas y comentarios opcionales.  
**Beneficio:**Aumenta la tasa de respuesta y calidad del feedback.

### Inmobiliaria y listados

**Escenario:**Bot inmobiliario muestra casas disponibles como tarjetas, cada una con imágenes y botón “Agendar visita”.  
**Beneficio:**Involucra a compradores y permite acción instantánea.

### Entrega de contenido

**Escenario:**Bot de medios envía noticias como tarjetas con miniatura, titular y botón “Leer más”.  
**Beneficio:**Incrementa el consumo de contenido y el engagement.

**Recursos adicionales:**- [Sendbird: ¿Qué es rich media?](https://sendbird.com/learn/what-is-rich-media)  
- [Madgicx: Rich Media Ads](https://madgicx.com/blog/rich-media)

## Mejores prácticas para tarjetas multimedia enriquecidas

1. **Prioriza claridad y simplicidad**- Limita las tarjetas por carrusel (3–10, según plataforma).
   - Usa textos concisos, imágenes de calidad y acciones claras.
2. **Optimiza el rendimiento**- Mantén imágenes/videos debajo de 1MB; miniaturas entre 50–100KB.
   - Aloja el contenido en CDNs rápidos y prueba carga en conexiones lentas.
3. **Diseño mobile-first**- Asegura botones grandes y fáciles de tocar.
   - Evita layouts densos; haz el contenido legible y accionable.
4. **Botones orientados a la acción**- Usa CTAs claros y específicos (ej. “Reservar”, “Solicitar cotización”).
   - Limita a 3–5 acciones por tarjeta, según plataforma.
5. **Personalización**- Adapta el contenido según contexto, historial o preferencias del usuario.
6. **Accesibilidad**- Agrega texto alternativo descriptivo a imágenes.
   - Asegura que los botones sean legibles por lectores de pantalla.
7. **A/B Testing**- Experimenta con el orden de tarjetas, visuales y mensajes.
   - Itera usando la analítica de uso real.
8. **Analítica avanzada**- Rastrea impresiones, clics, abandonos y finalización de objetivos.
   - Usa dashboards y visualización de embudos para optimizar ([Guía de Quickchat AI](https://quickchat.ai/post/chatbot-analytics)).
9. **Consistencia de marca**- Usa colores, logotipos y tipografía aprobados por la marca.
   - Asegura que el mensaje coincida con el tono de la marca.

**Errores comunes a evitar:**- Sobrecargar tarjetas con texto o demasiados botones.
- Descuidar la optimización de imágenes—cargas lentas reducen engagement.
- Usar visuales genéricos o irrelevantes.
- Ignorar límites y restricciones específicas por plataforma.
## Analítica avanzada y medición

### Métricas clave para tarjetas multimedia enriquecidas

- **Usuarios totales:**Número de usuarios únicos que interactuaron con el bot.
- **Usuarios activos/comprometidos:**Quienes interactuaron más allá del mensaje de bienvenida.
- **Vistas de tarjetas:**Veces que una tarjeta fue mostrada.
- **Clics en botones/engagement en CTA:**Tasa de clics en cada botón de acción.
- **Tasa de abandono:**Puntos donde los usuarios dejan la conversación.
- **Tasa de finalización de objetivos:**Porcentaje de usuarios que completan una acción deseada (formulario, compra, etc.).
- **Tasa de autoservicio:**Problemas resueltos por el bot sin intervención humana.
- **Tasa de desvío:**Porcentaje de consultas gestionadas por el bot, reduciendo la carga humana.
- **CSAT/NPS:**Calificaciones de satisfacción, a menudo recogidas con tarjetas de encuesta multimedia.

### Cómo usar la analítica para optimizar resultados

- **Análisis de embudo:**Rastrear cómo los usuarios navegan por carruseles/tarjetas, identificando puntos de abandono.
- **Optimización de contenido:**Ajustar imágenes, títulos o CTAs según analítica a nivel de tarjeta.
- **A/B Testing:**Probar orden de tarjetas, botones o textos CTA para mejorar finalización.
- **Personalización:**Segmentar usuarios y entregar tarjetas personalizadas usando datos analíticos.

**Dashboards y herramientas:**- [Sprinklr: Chatbot Analytics Dashboard](https://www.sprinklr.com/blog/chatbot-analytics/)
- [Quickchat: Analítica de agentes IA](https://quickchat.ai/post/chatbot-analytics)

## Guías técnicas por plataforma

- [Google: Capacidades y restricciones de RCS Rich Card](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards)
- [Microsoft: Tipos de tarjetas y matriz de canales de Bot Framework](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0)
- [Adaptive Cards Designer](https://adaptivecards.io/designer/)
- [Plantillas de Messenger Platform](https://developers.facebook.com/docs/messenger-platform/send-messages/template/)
- [Plantillas de mensajes de WhatsApp Business](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates)

## Preguntas frecuentes (FAQs)

### ¿Cuál es la diferencia entre una tarjeta multimedia enriquecida y un mensaje estándar?
Los mensajes estándar son solo texto. Las tarjetas multimedia enriquecidas pueden incluir imágenes, videos, carruseles y botones, permitiendo experiencias interactivas y visualmente atractivas.

### ¿Necesito habilidades de diseño para crear tarjetas multimedia enriquecidas?
La mayoría de plataformas de chatbot ofrecen constructores visuales con creación de tarjetas mediante arrastrar y soltar (ej. Kommunicate, Tars, Microsoft Adaptive Cards Designer). Se requieren mínimas habilidades de diseño, aunque la claridad y la coherencia de marca son importantes.

### ¿El rich media ralentizará mi chatbot?
Imágenes y videos optimizados (preferiblemente menores a 1MB) evitan ralentizaciones. Comprime todos los medios y usa CDN para archivos grandes.

### ¿Puedo rastrear interacciones de usuario con tarjetas multimedia enriquecidas?
Sí. Casi todas las plataformas ofrecen analítica para clics en botones, vistas de tarjetas, abandonos y objetivos completados (ver arriba para detalles).

### ¿Se soportan las tarjetas multimedia enriquecidas en todas las apps de mensajería?
El soporte varía según la plataforma. Web chat, Messenger y Apple Business Chat ofrecen soporte robusto; WhatsApp y SMS son