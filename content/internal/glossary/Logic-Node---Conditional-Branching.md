+++
title = "Logic Node / Conditional Branching"
translationKey = "logic-node-conditional-branching"
description = "Un Logic Node (ramificación condicional) evalúa condiciones en flujos de trabajo de chatbots y automatización, dirigiendo los caminos dinámicamente según la entrada del usuario o el contexto."
keywords = ["Logic Node", "Ramificación Condicional", "Chatbot", "Automatización", "Flujo de trabajo"]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Logic-Node---Conditional-Branching/"

+++
## ¿Qué es un Logic Node?

Un **Logic Node**es un bloque de decisión modular en flujos de trabajo de chatbots y automatización que evalúa condiciones (como elecciones del usuario, variables o estados) y ramifica el flujo en consecuencia. El logic node es el “punto de decisión” (ramificación condicional) donde el flujo de trabajo se desvía según reglas personalizadas.

**También conocido como:**- Nodo de ramificación condicional
- Rama If/Then
- Acción dividida ([TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/))
- Nodo de condición ([Noca AI](https://support.noca.ai/logic-nodes/))
- Nodo switch
- Nodo branch
## ¿Por qué usar ramificación condicional?

Los logic nodes permiten que los flujos de trabajo:

- **Respondan dinámicamente**a la entrada del usuario o al contexto
- **Dirijan a los usuarios**a acciones específicas según sus elecciones o datos
- **Implementen reglas de negocio**(verificaciones de elegibilidad, escalaciones, aprobaciones)
- **Personalicen experiencias**(basadas en etiquetas, propiedades de usuario o historial)
- **Reduzcan la intervención manual**al automatizar procesos complejos

**Ejemplo:**Si un cliente selecciona “Reportar un problema”, el bot solicita detalles; si elige “Consultar estado del pedido”, obtiene la información del pedido.

**Más:**- [BotStacks: Uso de condiciones y ramificación lógica](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic)

## Características principales de los Logic Nodes

1. **Evaluación condicional:**Defina una o más condiciones usando variables, entradas de usuario o estados del sistema.

2. **Control de ramificación/flujo:**Dirija a diferentes nodos/acciones según qué condición sea verdadera.

3. **Acceso a variables de contexto:**Lea/escriba variables en el contexto de la conversación o flujo de trabajo.

4. **Lógica anidada:**Soporte para condiciones multinivel o anidadas (ej.: “Si A, entonces chequear B; si no, hacer C”).

5. **Representación visual:**La mayoría de las plataformas proveen un editor visual para conectar y configurar logic nodes.

6. **Configuración sin código/con poco código:**Configurable vía interfaz gráfica, aunque lógica avanzada puede ser soportada por código o pseudocódigo.
## Tipos de Logic Nodes y ramificación

Las plataformas pueden ofrecer:

- **Ramas If/Then:**Ramificación binaria (verdadero/falso).
- **Nodos switch/case:**Ramificación multi-camino para valores discretos.
- **Acciones divididas:**Ramificación basada en la entrada de usuario, variables o aleatorización ([TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)).
- **Nodos de condición:**Evaluadores de verdadero/falso de propósito general.
- **Loop, break, continue:**Para lógica iterativa ([Noca AI](https://support.noca.ai/logic-nodes/)).
- **Ramificación aleatoria:**Para pruebas A/B o flujos aleatorios.
- **Ramificación multinivel:**Lógica anidada o de múltiples capas ([Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)).

## Cómo agregar y configurar un Logic Node

### Ejemplo en Kore.ai

Los logic nodes en Kore.ai solo pueden agregarse como parte de un nodo Bot Action.

**Pasos:**1. Abra la tarea de diálogo donde desea agregar la ramificación.
2. Agregue/expanda un nodo **Bot Action**([Documentación de Bot Action Node](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/bot-action-node/)).
3. Inserte un **Logic Node**.  
   - La pestaña **Component Properties**se muestra por defecto.
   - ![Agregando un logic node en Kore.ai](https://kore-wordpress.s3.us-east-2.amazonaws.com/developer.kore.ai/wp-content/uploads/20220921084031/add-logic-node-1024x456.gif)
4. Configure:
   - **Nombre**y **Display Name**en **Component Properties**.
   - Asigne espacios de nombres de variables según sea necesario.
   - Use **Manage Context Variables**para definir/actualizar variables (ej.: `_context.BotUserSession.<variable_name>_`).
   - En **Instance Properties**, establezca etiquetas o metadatos específicos del diálogo.
   - En **Connection Properties**, defina condiciones para controlar qué nodo se ejecuta a continuación, según valores de entidades, objetos de contexto o intenciones.
5. Guarde y conecte las ramas visualmente.
### Guía agnóstica de plataforma

La mayoría de las plataformas siguen un patrón similar:

1. Abra su constructor de bots/automatización (ej.: [Yellow.ai](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes), [HubSpot](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows), [Slack](https://slack.com/blog/news/conditional-branching-workflow-builder), [TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)).
2. Navegue al flujo o recorrido relevante.
3. Agregue un nodo de lógica/condición/división:
   - Busque **Logic**, **If/Then**, **Condition**o **Split Action**en el panel de nodos.
   - Arrástrelo y suéltelo en su lienzo.
4. Defina la(s) condición(es):
   - Especifique la propiedad o variable a evaluar.
   - Establezca operadores de comparación (igual, contiene, >, etc.).
   - Ingrese los valores a comparar.
5. Conecte las ramas a los siguientes pasos.
6. Pruebe el flujo usando herramientas de vista previa/pruebas.
## Configuración y propiedades del Logic Node

### Component Properties

- **Nombre:**Identificador interno.
- **Display Name:**Etiqueta visible para el usuario.
- **Espacios de nombres de variables:**Alcance de las variables (aislamiento a nivel de tarea o nodo).
- **Manage Context Variables:**Establecer/actualizar variables en el contexto de la conversación.

*Los cambios en Component Properties afectan todas las instancias de un logic node.*

### Instance Properties

- **Etiquetas:**Metadatos o etiquetas personalizadas para seguimiento/segmentación.
- **Configuraciones específicas del diálogo:**Ajustes vinculados al flujo/diálogo actual.

*Instance Properties solo afectan la instancia actual del nodo.*

### Connection Properties

- **Conexiones condicionales:**Definen qué nodo se ejecuta a continuación según condiciones.
- **Ruta de respaldo:**Rama por defecto si no se cumplen condiciones.
- **Intenciones/valores de entidades:**Use intenciones/valores de entidades detectados para ramificar.

*Algunas plataformas restringen las conexiones de logic nodes a ciertos alcances (ej.: dentro de nodos Bot Action en Kore.ai).*
## Sentencias condicionales y sintaxis

Las sentencias condicionales determinan cómo se evalúan las ramas. Estas pueden configurarse por interfaz gráfica o como expresiones.

**Operadores comunes:**- igual (==)
- distinto (!=)
- contiene
- mayor que (>)
- menor que (<)
- in (pertenencia a lista)
- and, or, not (operadores lógicos)

**Ejemplo de pseudocódigo:**```pseudo
if (user_response == "yes") {
    go_to("ConfirmOrder");
} else if (user_response == "no") {
    go_to("CancelOrder");
} else {
    go_to("ClarifyIntent");
}
```

**Ejemplo en interfaz de plataforma:**- En [HubSpot](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows), use la pestaña **If/then branches**para agregar reglas según respuesta del usuario, propiedad o disponibilidad de agentes.
- En [Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder), seleccione criterios como valores de desplegables, respuestas a formularios o datos de canal.

## Escenarios prácticos de uso

**1. Manejo de respuestas del usuario**Dirija a los usuarios según respuestas “Sí/No”, selecciones de opciones o texto libre.

**2. Enrutamiento de solicitudes de soporte**Dirija tickets de soporte al equipo correcto (ej.: técnico, facturación, equipamiento).

**3. Aprobaciones de múltiples pasos**Implemente aprobaciones por niveles (ej.: gerente, luego director).

**4. Personalización**Muestre respuestas según etiquetas de usuario o propiedades CRM.

**5. Validación de datos**Verifique números de teléfono, emails o campos requeridos antes de avanzar.

**6. Pruebas A/B**Ramifique aleatoriamente usuarios para experimentación o lanzamiento de funciones.

**7. Manejo de errores**Dirija a rutas de respaldo o aclaración en caso de entradas inválidas/faltantes.
## Ejemplos: ramificación condicional en el mundo real

### Ejemplo 1: Decisión Sí/No
**Escenario:**El bot pregunta, “¿Desea recibir notificaciones?”
- Si la respuesta del usuario es “sí” → Ir al nodo **Habilitar notificaciones**.
- Si no → Ir al nodo **Deshabilitar notificaciones**.

### Ejemplo 2: Enrutamiento de solicitudes de soporte ([Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder))
**Escenario:**Un usuario envía una solicitud de soporte con tipo de problema.
- Si `issue_type == "technical"` → Dirigir a `#tech-support`
- Si `issue_type == "billing"` → Dirigir a `#billing-support`
- Si `issue_type == "equipment"` → Dirigir a `#equipment-support`

### Ejemplo 3: Ramificación por respuesta rápida ([HubSpot Bot](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows))
**Escenario:**El bot pregunta, “¿En qué podemos ayudarte?”  
[Respuestas rápidas](/en/glossary/quick-replies/): “Estado del pedido”, “Soporte técnico”, “Otro”
- Si **Estado del pedido**→ Ir a consulta de pedidos
- Si **Soporte técnico**→ Ir a soporte
- Si **Otro**→ Consulta general

### Ejemplo 4: Aprobación multinivel ([Slack](https://slack.com/blog/news/conditional-branching-workflow-builder))
- Si `manager_approval == "approved"`:
  - Dirigir a director de finanzas.
  - Si `finance_approval == "approved"`: Notificar a compras.
  - Si no: Notificar rechazo.
- Si no: Notificar rechazo.

### Ejemplo 5: Split Action para validación de datos ([TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/))
- Si la entrada es un número de teléfono válido → Continuar.
- Si no → Enviar error y solicitar reingreso.

## Mejores prácticas y consejos

- Defina todas las ramas, incluyendo respaldo (“else”).
- Use nombres de nodos descriptivos para mayor claridad.
- Agrupe lógica relacionada para mayor modularidad.
- Pruebe cada rama usando herramientas de vista previa/pruebas.
- Use variables/etiquetas para analítica y personalización.
- Evite lógica excesivamente anidada; divida lógica compleja en flujos más pequeños.
- Documente reglas de negocio usando comentarios o descripciones.
## Limitaciones y casos particulares

- **Restricciones de alcance:**- En Kore.ai, los logic nodes se ubican dentro de nodos Bot Action.
- **Configuraciones globales vs. de instancia:**- Component Properties son globales, Instance Properties son locales.
- **Límites de nodos:**- Algunas plataformas tienen límites de nodos por flujo (ej.: Yellow.ai: 150 nodos).
- **Dependencias de eliminación:**- Las ramas activas deben eliminarse antes de borrar el nodo padre (HubSpot).
- **Consideraciones de tipo de dato:**- Los tipos de datos en las condiciones (cadena vs. número) deben ser compatibles.
- **Ramificación aleatoria/A/B:**- Puede producir resultados impredecibles sin semilla o seguimiento.
## Conceptos relacionados y lecturas adicionales

- [Bot Action Node (Kore.ai)](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/bot-action-node/)
- [Tipos de nodos en Yellow.ai](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes)
- [TextIt Flows](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)
- [Guía de Slack Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)
- [Noca AI Logic Nodes](https://support.noca.ai/logic-nodes/)
- [HubSpot Chatflows](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)


## Enlaces de origen y lecturas adicionales

- [BotStacks: Uso de condiciones y ramificación lógica](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic/)
- [Kore.ai: Trabajando con el Logic Node](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-logic-node/)
- [Yellow.ai: Logic Nodes](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes)
- [HubSpot: If/Then Branches](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)
- [Slack: Conditional Branching Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)
- [TextIt: Introducción a Flows](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)
- [Kore.ai: Gestión de Namespace](https://developer.kore.ai/docs/bots/bot-settings/bot-management/managing-namespace/)
- [Kore.ai: Etiquetas Meta Personalizadas](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/custom-meta-tags/)
- [Slack: Guía de Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)
- [Noca AI: Logic Nodes](https://support.noca.ai/logic-nodes/)

**Para más detalles, consulte siempre la documentación oficial y guías de desarrollo de su plataforma.**