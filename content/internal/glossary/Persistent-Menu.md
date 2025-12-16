+++
title = "Menú Persistente"
translationKey = "persistent-menu"
description = "Aprenda sobre los Menús Persistentes en chatbots: qué son, por qué usarlos, cómo implementarlos y mejores prácticas para mejorar la navegación y experiencia del usuario."
keywords = [
  "Menú Persistente",
  "Chatbot",
  "Facebook Messenger",
  "Menú de Navegación",
  "Elementos de Menú"
]
category = "General"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Persistent-Menu/"

+++
## ¿Qué es un Menú Persistente?

Un **Menú Persistente** es una interfaz de menú estática y siempre visible integrada en un chatbot, disponible para los usuarios durante toda su sesión. Ofrece acceso inmediato a acciones críticas del chatbot, independientemente del contexto del mensaje o el flujo de la conversación. El menú suele aparecer mediante un icono reconocible (a menudo un [menú hamburguesa](/es/glossary/hamburger-menu/)) y lista acciones esenciales como reiniciar, ayuda, darse de baja o accesos directos de navegación.

- **Características clave:**
  - Siempre accesible—nunca desaparece después de usar un botón.
  - Disponible en cualquier paso de la conversación o en el onboarding.
  - Presenta un conjunto claro y consistente de opciones para el usuario.
  - Ideal tanto para usuarios primerizos como recurrentes.
## ¿Por Qué Usar un Menú Persistente? (Beneficios Principales)

Un Menú Persistente bien configurado aporta valor claro al usuario y respalda los objetivos del negocio:

- **Navegación más rápida:** Los usuarios acceden al instante a funciones o información frecuentes—sin necesidad de recordar comandos o buscar en los hilos de conversación.
- **Reduce la Fricción:** Evita que los usuarios se pierdan o se frustren; ofrece una vía rápida de escape de flujos confusos.
- **Descubrimiento de Funciones:** Los usuarios nuevos y recurrentes ven las principales capacidades del bot de un vistazo.
- **Alineación con el Negocio:** Promueve acciones clave (por ejemplo, quizzes de productos, soporte, seguimiento de pedidos) que generan valor para el negocio.
- **Accesibilidad:** Usuarios con necesidades de accesibilidad se benefician de acciones estructuradas y siempre disponibles.
## ¿Cómo se Usa un Menú Persistente?

El Menú Persistente suele accederse haciendo clic o tocando un icono de menú (comúnmente el icono hamburguesa) en la ventana de chat. Su contenido está disponible en cualquier momento, sin importar la etapa de la conversación.

**Aspectos destacados de la experiencia de usuario:**
- Los usuarios pueden abrir el menú en el onboarding, a mitad de la conversación o al completar una acción.
- Acciones típicas: reiniciar bot, acceder a ayuda/FAQ, ir al menú principal, darse de baja, abrir URLs externas o iniciar quizzes.
## Canales Soportados y Limitaciones de Plataforma

Los Menús Persistentes son compatibles con las principales plataformas de mensajería y web, pero las funciones y los límites pueden variar:

| Plataforma              | Nivel de Soporte           | Notas/Limitaciones                                                                            |
|-------------------------|---------------------------|-----------------------------------------------------------------------------------------------|
| Facebook Messenger      | Completo                   | Máximo 3 elementos de nivel superior; soporta menús anidados, control de entrada del usuario.  |
| Instagram               | Soportado (vía API)        | Similar a Messenger; consulte la documentación específica de la plataforma para actualizaciones.|
| Widgets Webchat         | Completo (la mayoría)      | Apariencia de botones, control de entrada y anidamiento varían según el proveedor.             |
| WhatsApp, Telegram      | Limitado/Varía             | Revise la documentación de cada constructor de bots para soporte y limitaciones.               |

- **Límite de botones:** Messenger permite hasta 3 botones por nivel de menú.
- **Apariencia:** El icono y la ubicación del menú pueden variar según el canal.
- **Ámbito del menú:** Algunas plataformas solo permiten un menú por instancia de bot.
- **Deshabilitar entrada:** Suele aplicarse globalmente, no por flujo.
## Tipos de Elementos y Estructura del Menú

### Acciones de Botón

Un Menú Persistente puede incluir varios tipos de acciones:

- **Enviar mensaje:** Dispara un flujo específico del bot o envía un mensaje definido.
- **Abrir URL:** Abre una página web específica, frecuentemente en un navegador dentro de la app.
- **Reiniciar Bot:** Reinicia la conversación al inicio o paso de bienvenida.
- **Darse de baja:** Excluye al usuario de futuros mensajes o interacciones.
- **Tomar Quiz:** Inicia un quiz de producto o feedback.
- **Ayuda/FAQ:** Muestra soporte o respuestas a preguntas frecuentes.

### Menús Anidados

Algunas plataformas (como Messenger) permiten anidar menús, agrupando acciones relacionadas bajo una etiqueta. Ejemplo: “Cuenta” → “Perfil”, “Configuración”.

- **Limitación:** No todas las plataformas o constructores permiten menús (sub)anidados.

### Ejemplos de Elementos de Menú

| Etiqueta de Botón   | Acción                         | Descripción                                      |
|---------------------|-------------------------------|--------------------------------------------------|
| 🏠 Menú Principal   | Ir al flujo de menú principal  | Devuelve al usuario a la navegación principal    |
| 🔁 Reiniciar        | Reiniciar conversación         | Permite al usuario empezar de nuevo              |
| ❌ Darse de baja    | Acción de opt-out              | Finaliza futuros mensajes al usuario             |
| 📝 Tomar Quiz       | Lanzar recomendación/quiz      | Recoge info, brinda sugerencias personalizadas   |
| ❓ Ayuda            | Mostrar FAQ/opciones de contacto| Ofrece soporte instantáneo                       |
| 📦 Estado de pedido | Consultar pedido               | Para bots de comercio electrónico                |
| 💬 Contactar Soporte| Abrir flujo/email de soporte   | Agente humano u obtener ayuda adicional          |

*Puede mezclar distintos tipos de acciones en un mismo menú.*
## Paso a Paso: Cómo Añadir un Menú Persistente

El proceso depende del constructor/plataforma de su chatbot. Aquí una guía general, seguida de instrucciones específicas para plataformas populares.

### Pasos Generales

1. **Inicie sesión en el panel de su plataforma de bots**
2. **Abra Configuración del Bot o Constructor de Flujos**
   - Busque la sección “Menú Persistente”, “Menú” o “Navegación”.
3. **Cree/Edite el Menú Persistente**
   - Normalmente mediante un botón de “Crear” o “Editar”.
4. **Agregue Elementos de Menú**
   - Para cada espacio: elija tipo de acción, etiqueta y destino (flujo, URL, etc).
5. **Organice el Orden**
   - Arrastre y suelte para reordenar; acciones más importantes primero.
6. **Opciones Avanzadas**
   - Localice el menú, habilite/deshabilite entrada de usuario, agregue submenús si se permite.
7. **Guarde y Publique**
   - Haga clic en “Guardar”, “Publicar” o active el menú.
### Instrucciones Específicas por Plataforma

#### **Facebook Messenger (vía Chatfuel)**

1. Vaya al [Panel de Chatfuel](https://dashboard.chatfuel.com).
2. Abra la pestaña de Flujos; cree o seleccione su flujo.
3. Haga doble clic en el lienzo, seleccione “Entry Points → Persistent Menu”.
4. Agregue hasta 3 botones (ejemplo: “Reiniciar Bot”, “Ayuda”, “Darse de baja”).
5. Arrastre para reordenar y active el menú con el interruptor.
6. Para localización, haga clic en “Localization” para añadir traducciones.

![Ejemplo de Menú Persistente en Chatfuel](https://storage.googleapis.com/chatfuel-cms-staging/pic/original_persistent_menu_0_8a23ef77c3/original_persistent_menu_0_8a23ef77c3.webp)

- [Chatfuel: Documentación de Menú Persistente](https://chatfuel.com/blog/persistent-menu)

#### **ChatbotBuilder.ai**

1. Vaya a Configuración → Canales → Facebook Messenger/Instagram → Menú Persistente.
2. Haga clic en “Editar” para abrir el asistente.
3. Agregue elementos de menú según lo requiera.
4. Para deshabilitar la entrada del usuario, desmarque “Permitir Entrada de Teclado”.
5. Guarde y publique.

- [ChatbotBuilder.ai: Menú Persistente](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)

#### **Certainly**

1. Abra [Configuración del Bot](https://support.certainly.io/knowledge/Individualize-your-chatbot-in-Bot-Settings).
2. Seleccione la pestaña Menú Persistente.
3. Agregue elementos (Abrir URL, Enviar mensaje, Anidar).
4. Guarde los cambios.

- [Certainly Knowledge Base: Agregar un Menú Persistente](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

#### **Webchat Widgets (Ejemplo BotSailor)**

1. Inicie sesión en el panel de BotSailor.
2. Vaya a su gestor de chatbot web.
3. Haga clic en “Menú Persistente”.
4. Haga clic en “Crear”, configure el menú en el popup.
5. Puede deshabilitar completamente la entrada del usuario si lo desea.
6. Guarde y pruebe su widget de chat web.

- [Tutorial de YouTube: Menú Persistente en Chatbot Web](https://www.youtube.com/watch?v=4kAlBEgCvwM)

## Personalización del Menú Persistente

### Localización (Múltiples Idiomas)

- Agregue traducciones mediante un botón de “Localización” o “Agregar Idioma”.
- Seleccione el idioma de destino e ingrese las etiquetas traducidas de los botones.
- Solo el texto de los botones del menú se localiza, no los flujos completos de conversación.

**Mejor Práctica:**  
Solo localice si su bot soporta esos idiomas durante todo el recorrido del usuario.

### Deshabilitar Entrada del Usuario

- Desactive la entrada libre de texto para restringir a los usuarios solo a menú/[respuestas rápidas](/es/glossary/quick-replies/).
- Útil para flujos estrictos (por ejemplo, quizzes, formularios) pero tenga en cuenta: esto suele deshabilitar la entrada globalmente.
- Para recolectar respuestas abiertas (emails, direcciones), deje habilitada la entrada del usuario.

### Apariencia y Orden del Menú

- El menú suele estar abajo a la derecha (Messenger), pero varía según plataforma.
- El orden importa: coloque las acciones más críticas arriba.
- Use etiquetas descriptivas y cortas (el límite común es 30 caracteres).
- Los emojis pueden ayudar a reconocer, pero mantenga un uso profesional.
- Los botones pueden abrir URLs o iniciar flujos del bot.

## Mejores Prácticas para Menús Persistentes

- **Manténgalo simple:** Limite a 2–3 acciones principales; evite menús sobrecargados.
- **Priorice funciones críticas:** “Reiniciar”, “Ayuda”, “Darse de baja” deben ser fácilmente accesibles.
- **Etiquetas claras:** Use términos como “Reiniciar Bot” en vez de vagos como “De nuevo”.
- **Combine tipos de acción:** Mezcle enlaces, flujos y submenús según sea necesario.
- **Pruebe exhaustivamente:** Verifique en todos los canales y dispositivos.
- **Mantenga la accesibilidad:** Use fuentes legibles y buen contraste.
- **Actualice regularmente:** Ajuste el menú según analíticas y feedback de usuarios.
## Casos de Uso Comunes y Ejemplos

### Menú de Chatbot de E-commerce

| Botón         | Acción                    |
|---------------|--------------------------|
| 🛒 Comprar    | Abrir flujo de compras    |
| 🚚 Seguir Pedido| Mostrar estado del pedido|
| ❓ Ayuda      | FAQ o flujo de soporte    |

### Quiz de Recomendación de Producto

| Botón           | Acción                        |
|-----------------|------------------------------|
| 📝 Tomar Quiz   | Iniciar flujo de quiz         |
| 🔁 Reiniciar Bot| Reiniciar conversación        |
| ❌ Darse de baja| Opt-out de mensajes del bot   |

### Bot de Reservas de Restaurante

| Botón          | Acción                    |
|----------------|--------------------------|
| 📅 Reservar    | Iniciar flujo de reservas|
| 📖 Menú        | Abrir URL del menú       |
| 🏠 Menú Principal| Volver al flujo inicial |

## Resolución de Problemas y Consideraciones

- **Menú no aparece:** Confirme que el menú esté habilitado y publicado; verifique soporte del canal.
- **Entrada del usuario deshabilitada por error:** Recuerde que deshabilitar suele aplicarse a todo el bot.
- **Problemas de localización:** Asegure que la configuración de idioma sea correcta; solo se localiza el texto de los botones.
- **Demasiados botones:** Respete los límites de la plataforma (por ejemplo, Messenger = 3 por nivel); use anidamiento si está disponible.
- **Pruebas:** Testee en todos los canales y dispositivos objetivo para visibilidad y funcionamiento.
## Recursos Adicionales y Siguientes Pasos

- [Blog de Chatfuel: Menú Persistente](https://chatfuel.com/blog/persistent-menu)
- [Documentación de ChatbotBuilder.ai](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)
- [Certainly Knowledge Base: Agregar un Menú Persistente](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)
- [Messenger Platform API: persistent_menu](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu/)
- [YouTube: Menú Persistente en Chatbot Web](https://www.youtube.com/watch?v=4kAlBEgCvwM)
- [YouTube: Usar Menú Persistente en Chatfuel](https://www.youtube.com/watch?v=DWovaAjFOOk)

## ¡Pruébelo Usted Mismo!

**Agregue un Menú Persistente a su chatbot:**
- Inicie sesión en su constructor de chatbot.
- Siga las instrucciones de configuración para su plataforma.
- Pruebe e itere según el feedback de los usuarios.

**¿Necesita ayuda?**  
Explore la documentación y los tutoriales en video enlazados arriba, o contacte al equipo de soporte de su plataforma.

## Palabras Clave Relacionadas

añadir menú persistente, botón menú persistente, menú persistente añadir, crear menú persistente, menú de navegación, deshabilitar entrada de usuario, quiz de recomendación, facebook messenger, reiniciar bot, chat bot, elementos de menú, agregar botones, menú usuarios, menú principal

**Guía Completa y Profunda**  
Este glosario consolida documentación de plataformas, mejores prácticas y detalles de implementación. Para detalles técnicos oficiales del API, consulte la [referencia de API persistent_menu de Meta](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu/).  

Para tutoriales visuales y paso a paso, vea:  
- [Cómo Configurar Menú Persistente en Chatbot Web (YouTube)](https://www.youtube.com/watch?v=4kAlBEgCvwM)  
- [Cómo Usar el Menú Persistente en Chatfuel (YouTube)](https://www.youtube.com/watch?v=DWovaAjFOOk)

Para lecturas adicionales sobre personalización y uso avanzado, visite:  
- [Documentación de ChatbotBuilder.ai](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)  
- [Certainly Knowledge Base](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

**Mejore su chatbot ahora aprovechando estos recursos y construyendo un Menú Persistente que se ajuste a las necesidades de sus usuarios y a los objetivos de su negocio.**