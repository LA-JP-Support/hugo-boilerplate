+++
title = "Máquina de Estados"
translationKey = "state-machine"
description = "Explora las máquinas de estados, un modelo computacional para las transiciones de sistemas. Aprende conceptos clave, tipos, usos en chatbots de IA y automatización, implementación, ventajas y desafíos."
keywords = [
  "máquina de estados",
  "chatbot IA",
  "automatización",
  "máquina de estados finita",
  "statecharts"
]
category = "General"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/State-Machine/"

+++
## ¿Qué es una Máquina de Estados?

Una máquina de estados es un modelo computacional formal que describe cómo un sistema transiciona entre un conjunto finito de estados en respuesta a eventos externos o entradas. Cada estado representa una situación distinta durante la operación del sistema, y las transiciones definen cómo el sistema pasa de un estado a otro según disparadores específicos.

En el desarrollo de chatbots y automatización, las máquinas de estados rastrean y controlan explícitamente el flujo de conversación, los pasos del flujo de trabajo o las etapas de un proceso. Definen toda la estructura de posibles estados (como ‘esperando entrada del usuario’, ‘procesando solicitud’ o ‘en espera de pago’), los disparadores que provocan transiciones y las reglas que las gobiernan.
## Conceptos Clave

### Estados

Un estado es una instantánea del sistema en un momento dado. En chatbots, los estados pueden incluir `SALUDO`, `PEDIR_INFORMACIÓN`, `PROCESANDO`, `OFRECER_SOLUCIÓN` o `DESPEDIDA`. El sistema siempre se encuentra exactamente en un estado en cada momento.

**Ejemplo:**- Estados de procesamiento de pedido: `Pendiente`, `Enviado`, `Entregado`, `Devuelto`
- Estados de chatbot: `SALUDO`, `PEDIR_PROBLEMA`, `PROCESAR_PROBLEMA`, `OFRECER_SOLUCIÓN`, `DESPEDIDA`
- Estados de reproductor de música: `Pausado`, `Reproduciendo`, `Detenido`

### Eventos

Los eventos son disparadores—entradas, acciones u ocurrencias—que provocan transiciones de estado. Los eventos pueden ser mensajes de usuario, acciones del sistema, temporizadores o señales externas.

**Ejemplo:**- `usuario dice hola`
- `artículo enviado`
- `botón de reproducir presionado`
- `ocurrió tiempo de espera`

### Transiciones

Una transición define el movimiento de un estado a otro, provocado por un evento. Las transiciones son direccionales y suelen estar etiquetadas con el evento que las desencadena.

**Ejemplo:**- De `Pendiente` (estado), ante `artículo enviado` (evento), a `Enviado` (estado):

  `Pendiente` + `artículo enviado` → `Enviado`

**Diagrama:**Las máquinas de estados suelen visualizarse como círculos (estados) conectados por flechas (transiciones), con cada flecha etiquetada con el evento que causa la transición.

## Tipos de Máquinas de Estados

### Máquinas de Estados Finitas (FSM)

Una Máquina de Estados Finita es el tipo estándar, con un número limitado y conocido de estados. Para cada estado y evento, existe una transición definida, lo que garantiza un comportamiento predecible y determinista.
### Máquinas de Estados Jerárquicas

Las máquinas de estados jerárquicas (también llamadas statecharts) permiten la anidación de estados. Un estado padre puede encapsular múltiples estados hijos, reduciendo la complejidad en sistemas grandes.

**Ejemplo:**Un estado padre `Reserva` puede incluir `ReservaVuelo`, `ReservaHotel` y `ReservaAuto` como subestados.
### Deterministas vs. No Deterministas

- **Determinista:**Cada combinación de estado y entrada conduce exactamente a un único siguiente estado posible.
- **No determinista:**Pueden existir múltiples transiciones posibles para un estado y entrada dados; se utiliza más comúnmente en modelos teóricos o reconocimiento de patrones.

## Cómo se Usan las Máquinas de Estados

### Chatbots de IA y Flujos Conversacionales

Las máquinas de estados gestionan la “memoria” y el flujo de las conversaciones de los chatbots. Cada estado conversacional refleja una etapa única (por ejemplo, saludo, recolección de detalles del problema, procesamiento, oferta de solución). Los eventos—típicamente entradas del usuario—disparan las transiciones.

**Ejemplo:**Un chatbot de soporte podría transicionar de `SALUDO` a `PEDIR_PROBLEMA` al recibir un saludo del usuario.
### Automatización y Gestión de Flujos de Trabajo

Las máquinas de estados se utilizan ampliamente en automatización de procesos y gestión de flujos de trabajo, representando pasos como `Pendiente`, `Aprobado`, `Enviado`, etc. Eventos como “aprobado” o “artículo enviado” avanzan el flujo de trabajo provocando transiciones.
### Otros Dominios

- **IA en Juegos:**Modela comportamientos de NPC (inactivo, patrulla, perseguir, atacar).
- **Robótica:**Controla secuencias (mover, recoger, colocar, recargar).
- **Automatización de Procesos Empresariales:**Gestiona aprobaciones, escalados y enrutamiento de tareas.

## Ejemplos Prácticos

### Ejemplo 1: Procesamiento de Pedidos

**Estados:**`Pendiente` → `Enviado` → `Entregado` → `Devuelto`

**Transiciones:**- `Pendiente` + `artículo enviado` → `Enviado`
- `Enviado` + `artículo entregado` → `Entregado`
- `Entregado` + `artículo devuelto` → `Devuelto`

**Diagrama:**[Ejemplo de Estados de Pedido](https://stately.ai/blog/2023-10-02-what-is-a-state-machine/order-states-light.png)

### Ejemplo 2: Conversación de Chatbot

**Estados:**`SALUDO` → `PEDIR_PROBLEMA` → `PROCESAR_PROBLEMA` → `OFRECER_SOLUCIÓN` → `SEGUIMIENTO` → `DESPEDIDA`

**Implementación de muestra en Python:**```python
class ChatbotFSM:
    def __init__(self):
        self.state = 'SALUDO'
    def transition(self, user_input):
        if self.state == 'SALUDO':
            print("¡Hola! ¿En qué puedo ayudarte?")
            self.state = 'PEDIR_PROBLEMA'
        elif self.state == 'PEDIR_PROBLEMA':
            print(f"Mencionaste: {user_input}. Déjame procesarlo.")
            self.state = 'PROCESAR_PROBLEMA'
        elif self.state == 'PROCESAR_PROBLEMA':
            print("Esto es lo que encontré: [Solución]")
            self.state = 'DESPEDIDA'
        elif self.state == 'DESPEDIDA':
            print("¡Adiós!")
```
(Fuente: [Tencent Cloud](https://www.tencentcloud.com/techpedia/127736))

### Ejemplo 3: Reproductor de Música

- Inicia en `Pausado`
- Al presionar "reproducir", transiciona a `Reproduciendo`
- Al presionar "pausa", regresa a `Pausado`
- "Saltar" funciona desde cualquier estado

### Ejemplo 4: Flujo de Reserva de Viaje

**Estados:**`Inactivo`, `Reservando Vuelo`, `Reservando Hotel`, `Reservando Auto`, `Confirmación`, `Error`

Eventos como “vuelo reservado”, “error al reservar hotel” o “tiempo de espera” disparan transiciones. Los estados jerárquicos pueden emplearse para manejo de errores.

## Guía de Implementación

### Diseño Modular

- **Separación de Responsabilidades:**Implementa cada estado como una función o clase separada para facilitar el mantenimiento.
- **Mapeo de Manejadores de Estado:**Usa diccionarios u objetos para mapear estados a funciones manejadoras.

### Persistencia de Estado y Contexto

- **Gestión de Sesiones:**Almacena el estado actual y el contexto (como entradas del usuario, historial de conversación) usando almacenamiento en memoria o una base de datos.

**Ejemplo:**```python
user_sessions = {user_id: {'state': 'PROCESAR_PROBLEMA', 'issue': 'problema de inicio de sesión'}}
```
(Fuente: [Tencent Cloud](https://www.tencentcloud.com/techpedia/127736))

### Herramientas y Librerías

- **[XState](https://stately.ai/docs/xstate):**Librería JavaScript/TypeScript para máquinas de estados y statecharts.
- **[Stately Editor](https://state.new):**Editor visual para diseñar y exportar máquinas de estados.
- **[Mermaid](https://mermaid-js.github.io/mermaid/):**Herramienta de diagramación para statecharts.
- **Librerías específicas de lenguaje**para Python, Java, etc.

### Fragmento de Código de Ejemplo

**Esqueleto FSM en Python:**```python
class StateMachine:
    def __init__(self, initial_state):
        self.state = initial_state
        self.transitions = {
            'Pendiente': {'artículo enviado': 'Enviado'},
            'Enviado': {'artículo entregado': 'Entregado'},
            'Entregado': {'artículo devuelto': 'Devuelto'},
        }
    def on_event(self, event):
        if event in self.transitions[self.state]:
            self.state = self.transitions[self.state][event]
        else:
            print("Transición inválida")
```

**Ejemplo XState:**```javascript
import { createMachine } from 'xstate';
const orderMachine = createMachine({
  initial: 'pendiente',
  states: {
    pendiente: { on: { ENVIAR: 'enviado' } },
    enviado: { on: { ENTREGAR: 'entregado' } },
    entregado: { on: { DEVOLVER: 'devuelto' } },
    devuelto: {}
  }
});
```
(Fuente: [Documentación XState](https://stately.ai/docs/xstate))

## Ventajas de las Máquinas de Estados

- **Claridad:**Los diagramas de estados visualizan la lógica y mejoran la comunicación.
- **Consistencia:**La definición explícita de estados y transiciones previene comportamientos inesperados.
- **Modularidad:**La lógica de cada estado está aislada, facilitando el mantenimiento y la escalabilidad.
- **Pruebas Exhaustivas:**Todos los caminos pueden enumerarse y probarse.
- **Contexto Explícito:**Mantiene de forma confiable el estado de la conversación o flujo de trabajo.
- **Previsibilidad:**Las transiciones deterministas aseguran resultados definidos.

## Desafíos y Limitaciones

- **Complejidad:**Un gran número de estados y transiciones puede causar explosión de estados, dificultando el manejo de diagramas.
- **Escalabilidad:**Sistemas abiertos o muy dinámicos pueden requerir máquinas de estados jerárquicas o composicionales.
- **Flexibilidad:**Los modelos estrictos de estados pueden ser rígidos; flujos creativos o no lineales pueden ser más difíciles de captar.
- **Integración:**Combinar con bases de datos, APIs o servicios externos agrega complejidad.
- **Limitaciones de Contexto:**En bots impulsados por LLM, el tamaño de la ventana de contexto puede limitar el recuerdo de estados; la gestión explícita del contexto es esencial.

**Estrategias de Mitigación:**- Utiliza manejadores de estado modulares y máquinas de estados jerárquicas.
- Persiste el contexto en almacenamiento externo.
- Refactoriza regularmente los diagramas de estados para mantener la complejidad manejable.

## Conceptos Avanzados

### Máquinas de Estados Jerárquicas y Anidadas

- Las máquinas de estados jerárquicas (statecharts) permiten que los estados tengan subestados anidados, encapsulando flujos complejos y reduciendo redundancias.
- Los statecharts agregan características como estados paralelos, historial y acciones de entrada/salida.
### Integración con Aprendizaje Automático

- **Modelos Híbridos:**Combina máquinas de estados con modelos de ML para transiciones adaptativas (por ejemplo, ML clasifica la intención del usuario; la máquina de estados gestiona el flujo de la conversación).
- **Aprendizaje por Refuerzo:**Los agentes pueden aprender transiciones óptimas a partir de la experiencia.
- **Lógica de Transición Dinámica:**Los modelos de ML pueden predecir el siguiente estado en función de contexto rico.
### Generación Dinámica de Persona

- En chatbots complejos, las máquinas de estados pueden cambiar la personalidad o rol del bot según el contexto (por ejemplo, de agente general a especialista).


## Referencias y Lecturas Adicionales

- [Understanding State Machines (freeCodeCamp)](https://www.freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66/)
- [What is a State Machine? (Stately Blog)](https://stately.ai/blog/2023-10-05-what-is-a-state-machine)
- [Guiding AI Conversations](https://promptengineering.org/guiding-ai-conversations-through-dynamic-state-transitions/)
- [Documentación XState](https://stately.ai/docs/xstate)
- [Stately Editor – Probar Online](https://state.new)
- [Tencent Cloud: Conversational FSM](https://www.tencentcloud.com/techpedia/127736)
- [Stately YouTube Video Introduction](https://www.youtube.com/watch?v=EzYIerEutgk)
- [Building a Chatbot with State Machines (Medium)](https://rogerjunior.medium.com/how-to-build-a-chatbot-from-scratch-with-javascript-using-state-machines-95597c436517)

## Más Recursos

- [Stately Visual Editor](https://state.new) – Diseña y exporta máquinas de estados de forma visual.
- [XState VS Code Extension](https://marketplace.visualstudio.com/items?itemName=statelyai.stately-vscode)
- [State Machine Based Human-Bot Conversation Model (NCBI)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7266438/)

*Para explorar de forma práctica, prueba el [editor online de Stately](https://state.new) o [mira esta introducción en video](https://www.youtube.com/watch?v=EzYIerEutgk).*
Este glosario es un documento vivo. Para las mejores prácticas y ejemplos de código más actualizados, consulta siempre la documentación oficial de [XState](https://stately.ai/docs/xstate) y [Stately](https://stately.ai/).

**Las fuentes se incluyen a lo largo del texto; el contenido técnico clave y los ejemplos de código provienen de [Tencent Cloud](https://www.tencentcloud.com/techpedia/127736) y [Stately/XState](https://stately.ai/docs/xstate).**