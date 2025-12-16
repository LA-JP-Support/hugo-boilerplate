+++
title = "Human Approval Node"
translationKey = "human-approval-node"
description = "Un paso de flujo de trabajo que pausa la automatización para revisión y toma de decisiones humanas. También conocido como Human-in-the-Loop (HITL), garantiza la supervisión humana en flujos de trabajo automatizados o agenticos."
keywords = ["aprobación humana", "human-in-the-loop", "supervisión humana", "toma de decisiones", "flujos de aprobación"]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Human-Approval-Node/"

+++
## Definición

**Human Approval Node:**  
Un paso en el flujo de trabajo que pausa la automatización hasta que un usuario humano designado revisa la tarea y hace clic en 'Aprobar' o 'Rechazar' (o proporciona comentarios) a través de un panel, interfaz o canal de comunicación. Este paso—también conocido como un punto de control "[Human-in-the-Loop](/en/glossary/human-in-the-loop--hitl-/)" (HITL)—impone supervisión y toma de decisiones humanas en puntos predefinidos de flujos de trabajo automatizados o agenticos.  
## Concepto y Propósito

La automatización sobresale en tareas rutinarias y repetitivas, pero los puntos críticos de decisión—como aprobar transacciones de alto valor, manipular datos sensibles o ejecutar cambios de configuración—requieren juicio humano para seguridad, cumplimiento y auditabilidad. Los Human Approval Nodes existen para:

- Insertar una pausa controlada en los flujos de trabajo para revisión humana.
- Canalizar decisiones críticas a operadores humanos autorizados.
- Exigir consentimiento humano explícito antes de cualquier acción de alto impacto, ambigua o no reversible.
- Proporcionar una pista de auditoría inmutable y verificable de aprobaciones/rechazos para cumplimiento.

**¿Por qué es esencial HITL?**  
Los agentes de IA y la automatización pueden alucinar, malinterpretar o actuar fuera del alcance previsto. Los nodos de aprobación humana mitigan estos riesgos al requerir revisión explícita y contextual, y registrar todas las decisiones.  
## Características Clave

- **Pausa de Flujo de Trabajo:** La ejecución de la automatización se detiene en este paso hasta recibir decisión humana.
- **Asignación Basada en Roles:** Las tareas pueden ser asignadas a usuarios/roles específicos (ej. gerente, oficial de cumplimiento).
- **Rutas de Aprobación y Rechazo:** Soporta ramas de flujo de trabajo distintas según la entrada humana.
- **Actualizaciones en Tiempo Real:** Los cambios de estado se reflejan al instante en paneles o listas de tareas.
- **Notificaciones:** Alertas por correo, Slack o dentro de la app notifican a revisores sobre tareas pendientes.
- **Registro de Auditoría:** Todas las acciones y decisiones se registran de forma inmutable para [transparencia](/en/glossary/transparency/) y auditoría.
- **Tipos de Entrada Flexibles:** Soporta retroalimentación binaria (aprobar/rechazar) y abierta (comentarios, modificaciones).
- **Integración Fluida:** Compatible con los principales motores de flujo de trabajo (LangGraph, n8n, Permit.io, etc.).
- **Tiempos de Espera y Escalación:** Tiempos de espera configurables para respuesta con escalación alternativa.
- **Permisos Granulares:** Control de acceso detallado sobre quién puede ver, aprobar o rechazar tareas.
- **Historial Inmutable:** Los registros de aprobación son inviolables para cumplimiento e investigación.
## Cómo se Usan los Human Approval Nodes

### Ubicación en el Flujo

Inserte nodos de aprobación en puntos de decisión donde:

- Se requiere contexto o juicio humano (ej. salida ambigua de LLM, transacciones que exceden umbrales).
- La política o el cumplimiento exigen supervisión (SOC2, GDPR).
- Las acciones pueden causar cambios irreversibles (ej. eliminar cuentas, modificar infraestructura).

**Ejemplo:**  
_"Si el gasto supera el umbral predefinido, escalar a revisión humana para aprobación."_  
### Configuración e Implementación

**Pasos:**

1. **Definir Propósito:** Use nombres descriptivos para los nodos (ej. "Aprobación Legal", "Revisión de Publicación").
2. **Establecer Lógica de Asignación:** Asigne a usuarios o roles específicos según tipo de tarea/criticidad.
3. **Configurar Permisos:** Especifique qué usuarios/roles pueden ver/actuar en cada nodo de aprobación.
4. **Diseñar Ramas:**  
    - Aprobar → continuar flujo  
    - Rechazar → activar flujo alternativo (notificar, revertir, escalar)
5. **Notificaciones:** Habilite alertas por correo, Slack o app para nuevas tareas de aprobación.
6. **Pista de Auditoría:** Asegure que todas las decisiones y comentarios se registren para cumplimiento.

### Flujo de Interacción

**Secuencia típica:**

1. La automatización llega al nodo de aprobación y se pausa.
2. Se genera la tarea y se asigna al revisor designado.
3. El revisor recibe notificación y abre el panel de aprobación.
4. El revisor examina el contexto, instrucciones y acción propuesta.
5. El revisor selecciona "Aprobar" o "Rechazar" (con comentarios opcionales).
6. El flujo de trabajo continúa según la rama correspondiente a la decisión.

**Diagrama:**

```
[Paso Automatizado] → [Human Approval Node] → [Aprobar] → [Siguiente Paso]
                                            ↓
                                        [Rechazar] → [Flujo Alterno]
```
## Casos de Uso y Ejemplos Reales

### Ejemplo 1: Flujo de Aprobación de Gastos (LangGraph)

**Escenario:**  
Procesamiento automatizado de gastos con escalación a revisión humana si se excede el umbral.

**Flujo:**

1. El empleado envía el gasto.
2. El agente de IA revisa:
    - Si el monto ≤ $50 → auto-aprueba.
    - Si el monto > $50 → pausa en Human Approval Node.
3. El revisor humano aprueba o rechaza.
4. El flujo continúa según corresponda.

**Fragmento de Código (Python / LangGraph):**
```python
def review_expense(state):
    if state["expense_amount"] <= 50:
        return Command(update={"approval_status": ["Auto Approved"]}, goto="end_node")
    return {"approval_status": ["Needs Human Review"]}

def human_approval_node(state):
    user_feedback = interrupt({"approval_status": state["approval_status"], "message": "Approve, Reject, or provide comments."})
    if user_feedback.lower() in ["approve", "approved"]:
        return Command(update={"approval_status": state["approval_status"] + ["Final Approved"]}, goto="end_node")
    elif user_feedback.lower() in ["reject", "rejected"]:
        return Command(update={"approval_status": state["approval_status"] + ["Final Rejected"]}, goto="end_node")
```
- [Guía completa en DEV Community](https://dev.to/sreeni5018/langgraph-uncoveredai-agent-and-human-in-the-loop-enhancing-decision-making-with-intelligent-3dbc)

### Ejemplo 2: Automatización de Respuestas de Email con HITL (n8n Workflow)

**Escenario:**  
Respuestas de correo generadas por IA siempre son revisadas por humanos antes de enviarse.

**Flujo:**

1. Email entrante activa el flujo.
2. IA resume y redacta respuesta.
3. Human Approval Node envía borrador a un revisor.
4. El revisor aprueba o rechaza la respuesta.
5. Sólo se envían respuestas aprobadas.

**Cadena de nodos n8n:**  
Activador Email → Resumen → Borrador IA → Human Approval Node (Aprobar Email) → Enviar Email

- [Tutorial No-Code en YouTube](https://www.youtube.com/watch?v=n6llypVyGx8)
- [Plantilla de flujo](https://n8n.io/workflows/2907-a-very-simple-human-in-the-loop-email-response-system-using-ai-and-imap/)

### Ejemplo 3: Solicitudes de Control de Acceso de Agentes (Permit.io / LangChain MCP)

**Escenario:**  
Un agente LLM intenta modificar roles de usuario o acceder a recursos sensibles.

**Flujo:**

1. El agente propone acción privilegiada.
2. El agente pausa el flujo (llama a `interrupt()`), envía solicitud de acceso.
3. El revisor humano recibe la solicitud en el panel.
4. El revisor aprueba/rechaza; solo acciones aprobadas se ejecutan.

**Patrón:**  
Los agentes LLM nunca ejecutan operaciones privilegiadas sin aprobación humana explícita.

- [Permit.io: Documentación Human-in-the-Loop](https://docs.permit.io/)
- [Mejores Prácticas, Frameworks, Casos y Demo](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo)

## Patrones de Diseño y Buenas Prácticas

### Interrumpir y Reanudar

- **Usado en:** LangGraph, flujos agenticos.
- **Patrón:** Use `interrupt()` para pausar el flujo y esperar entrada humana, luego continuar.
- **Consejo:** Acciones críticas siempre pasan por un punto de control de interrupción para revisión explícita.
### Flujos de Aprobación

- **Usado en:** Permit.io, n8n, cadenas de aprobación empresariales.
- **Patrón:** Asigne derechos de aprobación a roles específicos. Solo usuarios autorizados pueden aprobar acciones sensibles.
- **Consejo:** Configure control de acceso basado en roles para evitar aprobaciones no autorizadas.

### Escalación Alternativa

- **Patrón:** Si la confianza es baja o la respuesta se retrasa, escale a un humano por panel, Slack o correo.
- **Consejo:** Use escalación para equilibrar eficiencia automatizada con supervisión humana en casos complejos.

### Buenas Prácticas Generales

- Inserte nodos de aprobación en puntos de decisión lógicos para supervisión y cumplimiento.
- Mantenga las solicitudes de aprobación claras y contextuales—resuma la acción y el motivo de la revisión.
- Configure controles de acceso granulares para roles y usuarios.
- Registre todas las intervenciones humanas para trazabilidad y auditoría.
- Planifique los tiempos de respuesta humana; maneje demoras/tiempos de espera adecuadamente.
- Use reglas impulsadas por políticas, no lógica rígida, para criterios de aprobación.
- Proporcione contexto completo en tareas de aprobación para decisiones rápidas e informadas.
- Pruebe los flujos extremo a extremo, incluyendo aprobación, notificación, revisión y registro.
## Configuración e Integración

### Control de Acceso Basado en Roles

- Asigne permisos según roles de usuario (admin, revisor, gerente).
- Solo usuarios con roles apropiados pueden ver/actuar en nodos de aprobación específicos.
- Separe acceso a tareas de la gestión general del flujo.

**Ejemplo:**

1. Abra Configuración de Gestión de Tareas.
2. Seleccione roles (ej. “Revisor de Contenido”) para derechos de aprobación.
3. Guarde y aplique los cambios.
### Notificación y Gestión de Tareas

- Habilite notificaciones por correo/Slack para nuevas tareas de aprobación.
- Incluya enlaces directos a paneles de tareas y vistas previas de acción.
- Use interfaces centralizadas para seguimiento de solicitudes de aprobación.

### Fragmentos Técnicos de Integración

**Ejemplo de Interrupción en LangGraph:**
```python
from langgraph.types import interrupt

def human_approval_node(state):
    user_feedback = interrupt({
        "approval_status": state["approval_status"],
        "message": "Approve, Reject, or provide comments."
    })
    # Reanudar flujo según la entrada
```

**Estructura n8n:**  
Coloque el nodo “Aprobar Email” tras el paso de borrador IA. Rutee las ramas de aprobado y rechazado según corresponda.

## Resolución de Problemas y Errores Comunes

- **Los usuarios no ven tareas asignadas:** Verifique permisos de roles y configuración de acceso.
- **No se reciben notificaciones de tareas:** Revise spam, valide correos y configuración de alertas.
- **No se pueden asignar tareas a ciertos usuarios/roles:** Confirme permisos y configuración de roles.
- **Demoras en aprobaciones:** Añada reglas de escalación o recordatorios.

> **Consejo:** Use escalación y recordatorios para garantizar revisiones humanas oportunas.


## Referencias y Lecturas Adicionales

- [Permit.io: Human-in-the-Loop for AI Agents: Best Practices, Frameworks, Use Cases, and Demo](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo)
- [Delegación de permisos de IA a usuarios humanos](https://www.permit.io/blog/delegating-ai-permissions-to-human-users-with-permitios-access-request-mcp)
- [Identidad de IA & IAM](https://www.permit.io/tags/ai-identity)
- [LangGraph Uncovered – Blog de ejemplo](https://dev.to/sreeni5018/langgraph-uncoveredai-agent-and-human-in-the-loop-enhancing-decision-making-with-intelligent-3dbc)
- [Referencia de interrupt() en LangGraph](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)
- [Ejemplo de flujo HITL en n8n](https://n8n.io/workflows/2907-a-very-simple-human-in-the-loop-email-response-system-using-ai-and-imap/)
- [YouTube: Añadir supervisión humana en n8n](https://www.youtube.com/watch?v=n6llypVyGx8)
- [Comunidad n8n: Revisión humana en flujos](https://community.n8n.io/t/ideas-for-implementing-human-review-in-workflow/81096)
- [Gestión de permisos de IA – Permit.io](https://www.permit.io/blog/managing-ai-permissions)

## Ver También

- [Flujos Agenticos](https://wpaiworkflowautomation.com/ai-workflow-automation-demos/)
- [Control de Acceso y Gestión de Roles](https://docs.permit.io/)
- [Patrones de flujo de aprobación](https://n8n.io/workflows/)

**Ejemplos de Frases de Implementación:**

- “El Human Approval Node pausa la automatización hasta que un usuario designado aprueba o rechaza la tarea.”
- “Use la función `interrupt()` para insertar un punto de control humano en tiempo real en su flujo de trabajo.”
- “Configure qué roles tienen acceso para aprobar tareas en la Configuración de Gestión de Tareas.”
- “Inserte Human Approval Nodes en puntos de decisión lógicos para supervisión y cumplimiento.”
- “Todas las acciones que requieren intervención humana se registran para auditoría.”
- “Mejor práctica: Mantenga las solicitudes de aprobación claras y contextuales—resuma la acción y por qué se requiere aprobación humana.”
- “Resolución de problemas: Si los usuarios no ven tareas asignadas, verifique sus roles y permisos de acceso.”

## Tabla Resumen

| Característica                | Descripción                                                                                 |
|-------------------------------|--------------------------------------------------------------------------------------------|
| Pausa de Flujo de Trabajo     | La automatización se detiene en el nodo y continúa tras la entrada humana                  |
| Asignación Basada en Roles    | Asigne tareas a usuarios o roles según la política                                         |
| Rutas de Aprobación/Rechazo   | Ramas separadas para resultados aprobados/rechazados                                       |
| Notificaciones                | Alertas por correo o app para nuevas tareas                                                |
| Registro de Auditoría         | Todas las acciones y decisiones se registran para revisión                                 |
| Actualizaciones en Tiempo Real| El estado de la tarea se actualiza instantáneamente en paneles                             |
| Tipos de Entrada Flexibles    | Soporta tanto retroalimentación binaria como abierta                                       |
| Integración                   | Compatible con los principales frameworks (LangGraph, n8n, Permit.io, etc.)                |

Para soporte avanzado o guía de implementación, consulte la documentación oficial o contacte los canales de soporte de su plataforma.

**Fuentes y Lecturas Adicionales:**

- [Permit.io: Human-in-the-Loop for AI Agents: Best Practices, Frameworks, Use Cases, and Demo](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo)
- [Delegando permisos de IA a usuarios humanos con Access Request MCP de Permit.io](https://www.permit.io/blog/delegating-ai-permissions-to-human-users-with-permitios-access-request-mcp)
- [Referencia de interrupt() en LangGraph](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)
- [Tutorial de flujo HITL en n8n (YouTube)](https://www.youtube.com/watch?v=n6llypVyGx8)
- [Ejemplo de flujo HITL en n8n](