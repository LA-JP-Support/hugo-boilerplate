+++
title = "Script de Inserción"
translationKey = "embed-script"
description = "Aprenda sobre los scripts de inserción, fragmentos de JavaScript utilizados para integrar chatbots de IA y contenido dinámico en cualquier sitio web. Descubra usos, ejemplos, personalización y mejores prácticas."
keywords = [
  "script de inserción",
  "chatbot",
  "JavaScript",
  "integración de sitios web",
  "automatización con IA"
]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Embed-Script/"

+++
## ¿Qué es un Script de Inserción?

Un **script de inserción** es un fragmento compacto y autónomo de JavaScript que se inserta en el HTML de un sitio web para cargar y mostrar contenido dinámico de terceros—comúnmente chatbots o widgets de IA. Al agregarse al sitio, el script recupera el código y los recursos del chatbot desde los servidores del proveedor y muestra el widget en el navegador.

**Características clave:**
- **Plug-and-play:** Solo requiere copiar y pegar en el HTML—sin programación avanzada.
- **Dinámico:** Carga dependencias e interfaz desde el proveedor en tiempo real.
- **Aislado:** Se ejecuta en un contexto de navegador aislado, minimizando riesgos de interferencia con otros elementos del sitio.
- **Universal:** Funciona en prácticamente cualquier plataforma web que permita HTML o JavaScript personalizado.

**Contexto de Chatbot de IA y Automatización:**  
Los scripts de inserción permiten desplegar chatbots—impulsados por IA—para ventas, soporte, generación de leads y engagement, directamente en su sitio o aplicación web. Los visitantes interactúan con el chatbot en tiempo real, recibiendo respuestas automatizadas y personalizadas.

## Cómo se usan los Scripts de Inserción

### Integración Básica

La mayoría de los proveedores de chatbots ofrecen un script de inserción listo para usar vinculado a su cuenta o instancia. El flujo básico es:

1. **Obtener el Script de Inserción:**  
   - Inicie sesión en el panel de control (por ejemplo, [Chatbase](https://chatbase.co/), [ChatBot.com](https://www.chatbot.com/), [Pickaxe](https://pickaxe.co/)).
   - Navegue a la sección “Desplegar”, “Publicar” o “Integraciones”.
   - Copie el fragmento de JavaScript proporcionado ([ejemplo para Chatbase](https://chatbase.co/docs/developer-guides/javascript-embed#quick-start-guide)).

2. **Agregarlo a su sitio web:**  
   - Pegue el script en su HTML, ya sea en el `<head>` o justo antes de la etiqueta de cierre `</body>` para mejor rendimiento.
   - Guarde y vuelva a publicar o actualice su sitio.

**Ejemplo:**
```html
<!-- Ejemplo de Script de Inserción de Chatbase -->
<script src="https://www.chatbase.co/embed.min.js" agent-id="YOUR_AGENT_ID" async></script>
```
O para configuración avanzada:
```html
<script>
  window.chatbaseConfig = {
    agentId: 'YOUR_AGENT_ID',
    user: { name: 'Jane Doe', email: 'jane@example.com' }
  };
</script>
<script src="https://www.chatbase.co/embed.min.js" async></script>
```
**Resultado:**  
Aparece una burbuja de chat en su sitio web, ofreciendo interacción instantánea impulsada por IA a sus visitantes.

### Métodos Avanzados de Integración

Más allá de la inserción básica, los scripts permiten integraciones más profundas:

- **Verificación de Identidad:**  
  Pase datos del usuario (por ejemplo, nombre, email, ID de usuario) para saludos personalizados, respuestas contextuales y acciones seguras.  
  [Ver Verificación de Identidad de Chatbase](https://chatbase.co/docs/developer-guides/identity-verification)

- **Escuchadores de Eventos:**  
  Reaccione a acciones del usuario o del bot (por ejemplo, registre conversaciones, active analíticas, abra/cierre el widget programáticamente).  
  ```javascript
  window.chatbase.addEventListener("user-message", (event) => {
    console.log("El usuario dijo:", event.content);
    // Lógica personalizada
  });
  ```
  [Escuchadores de Eventos de Chatbase](https://chatbase.co/docs/developer-guides/javascript-embed#advanced-features)

- **Acciones Personalizadas:**  
  Dispare formularios, flujos de trabajo o llamadas a APIs desde la interfaz de chat.

- **Contenido Dinámico:**  
  Cambie saludos, apariencia del widget o contexto de la conversación según el contenido de la página o la sesión del usuario.

- **Control de Widget (API):**  
  Use APIs de JS para abrir, cerrar, ocultar o destruir el widget programáticamente (ver [API de Widget de ChatBot.com](https://www.chatbot.com/docs/chat-widget-api/)):
  ```javascript
  OpenWidget.call('maximize');    // Abrir chat
  OpenWidget.call('minimize');    // Minimizar chat
  OpenWidget.call('hide');        // Ocultar chat
  OpenWidget.call('destroy');     // Eliminar chat
  ```

### Uso Específico por Plataforma

**WordPress:**  
- Use plugins oficiales (por ejemplo, [ChatBot.com para WordPress](https://wordpress.org/plugins/chatbot/)).
- Ingrese su clave API o ID de agente en la configuración del plugin.
- No se requiere edición manual de scripts.

**Shopify, Wix, Squarespace:**  
- Use los marketplaces de apps o inserte el código de inserción en las secciones de tema/código personalizado.
- [Ejemplo de app para Shopify](https://apps.shopify.com/), [Guía de código personalizado para Wix](https://support.wix.com/en/article/embedding-custom-code-to-your-site).

**HTML/CMS Personalizado:**  
- Pegue directamente el código de inserción en archivos de plantilla o inyectores de código.

**Knack, Webflow, Constructores No-Code:**  
- Si el HTML está restringido, inyecte el script dinámicamente mediante JavaScript:
  ```javascript
  (function() {
      var script = document.createElement('script');
      script.src = 'https://cdn.customgpt.ai/js/chat.js';
      script.defer = true;
      script.onload = function() {
          CustomGPT.init({
              p_id: '#####',  // ID del proyecto
              p_key: '################' // Clave del proyecto
          });
      };
      document.head.appendChild(script);
  })();
  ```
  ([Ejemplo de la comunidad Knack](https://forums.knack.com/t/embed-chatbot/18777))

## Ejemplos de Scripts de Inserción

### Script Básico de Inserción de Chatbot

```html
<script src="https://cdn.example.com/chatbot.js" defer></script>
<script>
  window.ChatBot.init({
    apiKey: 'YOUR_API_KEY',
    position: 'bottom-right',
    language: 'en'
  });
</script>
```

### Script de Inserción con Verificación de Identidad

```html
<script src="https://cdn.chatbase.co/widget.js" defer></script>
<script>
  window.chatbaseConfig = {
    agentId: 'AGENT_ID',
    user: {
      name: 'Jane Doe',
      email: 'jane@example.com'
    }
  };
</script>
```
([Verificación de Identidad de Chatbase](https://chatbase.co/docs/developer-guides/identity-verification))

### Inyección Dinámica de Script (para plataformas con restricciones en HTML)

```javascript
(function() {
  var script = document.createElement('script');
  script.src = 'https://cdn.customgpt.ai/js/chat.js';
  script.defer = true;
  script.onload = function() {
    CustomGPT.init({
      p_id: '#####',  // Reemplace por su ID de proyecto
      p_key: '################'  // Reemplace por su clave de proyecto
    });
  };
  document.head.appendChild(script);
})();
```
([Ejemplo de la comunidad Knack](https://forums.knack.com/t/embed-chatbot/18777))

## Casos de Uso Comunes

| Caso de Uso              | Descripción                                                                                 | Plataformas de Ejemplo        |
|--------------------------|--------------------------------------------------------------------------------------------|-------------------------------|
| Soporte al Cliente       | Ofrezca respuestas automáticas e instantáneas a preguntas frecuentes y consultas de soporte.| Quidget, Chatbase, ChatBot.com|
| Generación de Leads      | Califique leads haciendo preguntas y recolectando datos de contacto mediante formularios.  | Drift, Intercom, Chatbase     |
| Asistencia en E-commerce | Guíe a los compradores, recomiende productos y ofrezca descuentos personalizados en tiempo real.| Shopify, WooCommerce          |
| Búsqueda en Base de Conocimientos | Permita a los usuarios buscar documentación o información de productos desde el widget.| ChatBot.com, Freshdesk        |
| Herramientas Internas    | Inserte chatbots para onboarding de empleados o mesa de ayuda TI en intranet o dashboards SaaS.| HTML personalizado, Webflow   |
| Soporte Multilingüe      | Atienda a clientes en varios idiomas configurando el idioma del chatbot.                   | Quidget, Chatbase             |
| Agendamiento de Citas    | Integre widgets de reservas o calendarios en el chat para agendar rápidamente.             | Calendly, Acuity vía chatbot  |
| Accesibilidad            | Garantice que todos los usuarios, incluidas personas con discapacidad, puedan interactuar con su chatbot.| Todas las plataformas modernas|

## Funcionalidades Clave y Opciones de Personalización

### Tabla Comparativa de Funcionalidades

| Funcionalidad                  | Script Básico de Inserción | Integración Avanzada | Plugin/App de Plataforma |
|-------------------------------|---------------------------|----------------------|-------------------------|
| Configuración Rápida (Copiar y Pegar) | ✔️                | ✔️                  | ✔️                 |
| Personalización de Apariencia  | ✔️                | ✔️                  | ✔️ (basada en UI)  |
| Control de Posición            | ✔️                | ✔️                  | ✔️                 |
| Saludos Personalizados         | ✔️                | ✔️                  | ✔️                 |
| Branding (Logo, Colores)       | ✔️                | ✔️                  | ✔️                 |
| Seguridad de Clave API         | Manual            | Mejorada            | Integrada           |
| Escuchadores de Eventos        | ❌                | ✔️                  | ❌                 |
| Verificación de Identidad      | ❌                | ✔️                  | Parcial             |
| Analíticas                     | Basadas en plataforma | Basadas en plataforma| Basadas en plataforma|
| Cumplimiento (GDPR, CCPA)      | Soporte de plataforma | Soporte de plataforma | Soporte de plataforma|
| Funcionalidades de Accesibilidad| Usualmente incluidas | Usualmente incluidas | Usualmente incluidas|

### Opciones de Personalización

- **Apariencia Visual:**
  - Cambie el color de la burbuja, fondo del widget y fuentes.
  - Suba un logo o avatar personalizado de la empresa.
  - White-label o elimine el branding del proveedor (en planes seleccionados).

- **Mensajes de Bienvenida:**
  - Configure mensajes de bienvenida estáticos o dinámicos.
  - Muestre enlaces, botones o llamados a la acción personalizados en la ventana inicial.

- **Posición del Widget:**
  - Ubique el widget en la esquina inferior izquierda, derecha o con coordenadas personalizadas.
  - Elija auto-lanzamiento o que el usuario deba hacer clic para abrir.

- **Comportamiento:**
  - Habilite/deshabilite entrada de texto libre.
  - Configure flujos conversacionales, “personalidad” del bot, respuestas alternativas y transferencia a agentes humanos.

- **Idioma y Localización:**
  - Establezca el idioma por defecto.
  - Active detección multilingüe o permita al usuario cambiar de idioma.
  - [Opciones de idioma de Chatbase](https://chatbase.co/docs/developer-guides/javascript-embed#user-experience)

- **Accesibilidad:**
  - Navegación por teclado, roles ARIA, soporte para lectores de pantalla, modo de alto contraste.

## Consideraciones de Seguridad y Cumplimiento

### Seguridad de Clave API

- **Nunca exponga claves API secretas o privilegiadas en scripts públicos.**
- Use solo claves públicas o restringidas para uso en el cliente.
- Para autenticación de usuario, utilice verificación de identidad segura (pase tokens o contexto de usuario desde su backend).
- Considere proxies del lado servidor para operaciones sensibles o privilegiadas.

**Lista de Verificación de Seguridad:**

| Tarea de Seguridad                               | Recomendación                                            |
|--------------------------------------------------|----------------------------------------------------------|
| Usar claves API públicas/restringidas            | ✔️                                                       |
| Evitar incrustar claves secretas/privadas en scripts | ✔️                                                   |
| Ofuscar o enviar datos sensibles vía backend      | ✔️                                                       |
| Usar HTTPS para todas las comunicaciones         | ✔️                                                       |
| Validar dominios permitidos en la configuración  | ✔️                                                       |

### Cumplimiento de Privacidad y Legal

- **GDPR / CCPA:**  
  Obtenga consentimiento antes de recolectar datos personales a través del chatbot.
- **Acceso y Eliminación de Datos:**  
  Permita a los usuarios solicitar, acceder o eliminar sus datos.
- **Encriptación:**  
  Garantice que todos los datos en tránsito y en reposo estén cifrados.
- **Auditoría y Logs:**  
  Mantenga registros de las interacciones del chatbot para cumplimiento.

La mayoría de los proveedores reconocidos incluyen funcionalidades y documentación de cumplimiento integrados.

### Accesibilidad

- Use widgets que soporten roles ARIA, compatibilidad con lectores de pantalla y navegación por teclado.
- Pruebe contraste de colores, tamaños de fuente e indicadores de enfoque.

## Solución de Problemas con Scripts de Inserción

| Problema                                 | Posible Causa                               | Solución                                               |
|------------------------------------------|---------------------------------------------|--------------------------------------------------------|
| El widget no aparece                     | Script mal ubicado, ID de agente incorrecto | Verifique ubicación, ID/API key y dominio permitido    |
| El widget carga lento                    | Script bloquea renderizado                  | Agregue `async` o `defer` al tag de script             |
| El chat no responde                      | Falta/clave API inválida, problemas de red  | Verifique clave API, revise consola de red             |
| Eventos personalizados no funcionan      | Listener antes de cargar el script          | Agregue listeners después de cargar el script          |
| El widget se sobrepone al contenido      | Conflictos de CSS                           | Ajuste posición o z-index en CSS personalizado         |
| El widget no es accesible en móviles     | Widget no optimizado para móviles           | Pruebe en dispositivos, ajuste configuración móvil     |

**Diagnóstico Paso a Paso:**
1. Abra la consola del navegador y revise errores de JavaScript.
2. Valide URLs de scripts, parámetros e IDs de agente.
3. Confirme que el dominio de su sitio está permitido en la configuración del chatbot.
4. Pruebe con extensiones de navegador deshabilitadas o en modo incógnito.
5. Revise la documentación oficial de solución de problemas:
   - [Solución de problemas en Chatbase](https://chatbase.co/docs/developer-guides/javascript-embed#troubleshooting)
   - [Guía de instalación de widget en ChatBot.com](https://www.chatbot.com/help/install-chatbot/widget-installation/)

## Mejores Prácticas para Scripts de Inserción

- **Utilice siempre el código oficial más reciente de su proveedor de chatbot.**
- **Cargue los scripts de forma asíncrona (`async` o `defer`) para no bloquear el renderizado del sitio.**
- **Pruebe el chatbot en los principales navegadores y dispositivos móviles.**
- **Minimice la cantidad de scripts de terceros para reducir riesgos de seguridad.**
- **Revise regularmente analíticas y feedback de usuarios para optimizar el rendimiento y UX del chatbot.**
- **Actualice el script si su proveedor lanza nuevas versiones.**

**Consejos de Accesibilidad:**
- Asegure la navegación por teclado y los estados de enfoque.
- Proporcione alternativas de texto para íconos y avatares.
- Siga las [directrices WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/).

**Consejos de Cumplimiento:**
- Muestre avisos de privacidad y consentimiento antes de recolectar información.
- Brinde a los usuarios opciones para darse de baja o solicitar sus datos.

## Preguntas Frecuentes (FAQ)

**P: ¿Qué es un script de inserción?**  
R: Es un fragmento de JavaScript que carga un chatbot o widget de IA en su sitio web al pegarlo en su HTML.

**P: ¿Dónde debo colocar el script de inserción?**  
R: Preferiblemente justo antes de la etiqueta de cierre `</body>` por rendimiento, o en el `<head>` para cargar el widget más rápido. Algunas plataformas especifican la ubicación exacta—consulte la documentación.

**P: ¿Puedo personalizar la apariencia y saludos del chatbot?**  
R: Sí. La mayoría de los proveedores le permiten configurar apariencia, saludos, branding y más desde el panel de control o la configuración del script.

**P: ¿Es seguro incluir mi clave API en el script de inserción?**  
R: Solo si la clave es pública o restringida para uso en cliente. Nunca exponga claves secretas o privilegiadas.

**P: ¿Cómo aseguro el cumplimiento con GDPR/CCPA?**  
R: Utilice funciones de cumplimiento integradas, muestre avisos de privacidad y permita a los usuarios gestionar sus datos.

**P: ¿Qué hago si no aparece el widget de chatbot?**  
R: Revise la ubicación del script, la clave API/ID de agente, la consola del navegador para errores y verifique la lista de dominios permitidos.

**P: