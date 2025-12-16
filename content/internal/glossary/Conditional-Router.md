+++
title = "Conditional Router"
translationKey = "conditional-router"
description = "Un Router Condicional evalúa los datos según reglas y los dirige a rutas específicas. Esencial para ramificación dinámica basada en reglas en flujos de automatización, chatbots de IA y software."
keywords = ["Router Condicional", "Automatización de flujos", "Ramificación basada en reglas", "Chatbots de IA", "Enrutamiento de datos"]
category = "General"
type = "glossary"
date = 2025-12-02
draft = false
url = "/internal/glossary/Conditional-Router/"

+++
## Definición

Un **Router Condicional** es un componente o nodo de flujo de trabajo que evalúa los datos entrantes según una o más reglas definidas por el usuario y dirige los datos a una ruta descendente específica según la condición que coincida. Su propósito es habilitar ramificación dinámica y basada en reglas en flujos de automatización, chatbots de IA, automatización de procesos empresariales y arquitecturas de software. Cada puerto de salida corresponde a un posible resultado de enrutamiento, determinado por reglas personalizables utilizando una variedad de operadores.

- **Fuente autorizada:** [AWS Glue Conditional Router](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html), [FlowHunt Conditional Router](https://www.flowhunt.io/components/ConditionalRouter/)

**Capacidades clave:**
- Recibe entrada (texto, objetos estructurados, metadatos, etc.)
- Aplica condiciones definidas por el usuario (ej.: `equals`, `contains`, `is_email`, `regex`)
- Activa exactamente una salida (ruta) por evaluación, excepto en algunos contextos ETL (ver [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html))
- Soporta flujos deterministas y gestionables en automatizaciones complejas


## Cómo funciona el Router Condicional

### Lógica central

El Router Condicional compara los datos entrantes con valores o expresiones lógicas especificadas utilizando un conjunto de operadores configurables. Cada condición está vinculada a una salida nombrada. El router verifica las condiciones en orden: la primera condición `true` determina la ruta de salida. Si ninguna condición coincide, el router activa una ruta predeterminada o de respaldo (si está configurada).

- **Enrutamiento de un solo camino:** Solo una salida se activa por evaluación (enrutamiento exclusivo), excepto en algunos marcos ETL (ver [AWS Glue: multiple groups](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)).
- **Reglas configurables:** Las condiciones se definen con operadores y pueden referenciar múltiples campos, incluidos datos anidados.
- **Extensible:** Permite composición lógica, condiciones anidadas y expresiones personalizadas.

### Secuencia de evaluación

1. **Recepción de entrada:** Recibe datos y metadatos o parámetros opcionales.
2. **Evaluación de condición:** Evalúa secuencialmente cada condición definida usando los operadores configurados.
3. **Decisión de enrutamiento:** La primera condición que resulte `true` determina la salida.
4. **Manejo predeterminado:** Si ninguna condición coincide, los datos se envían a una ruta predeterminada (si está definida).
5. **Procesamiento descendente:** Los datos se pasan al siguiente componente o acción.

- **Ejemplos del mundo real:** [Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder) permite a los usuarios crear flujos de trabajo de múltiples ramas basados en entradas de formularios o metadatos de mensajes sin código.


## Entradas

Los parámetros de entrada para Routers Condicionales pueden variar según la plataforma, pero normalmente incluyen:

| Nombre de entrada   | Tipo           | Descripción                                                        | Requerido | Avanzado |
|---------------------|----------------|--------------------------------------------------------------------|-----------|----------|
| Datos/Texto de entrada | Cadena/Objeto | Los datos principales a evaluar (ej.: entrada de usuario, respuesta de API) | Sí        | No       |
| Valor de coincidencia | Cadena/Objeto | El valor o expresión con el que comparar                           | No        | No       |
| Operador            | Cadena         | Operador de comparación (ver [Operadores disponibles](#available-operators)) | Sí        | Sí       |
| Sensible a mayúsculas | Booleano      | Habilita comparaciones sensibles a mayúsculas                      | No        | Sí       |
| Metadatos/Parámetros | Objeto         | Campos adicionales para enrutamiento (ej.: user_plan, región, modelo) | No    | Sí       |
| Objeto de mensaje   | Objeto         | Carga útil que se pasa por la ruta                                 | No        | No       |

- **Fuente:** [FlowHunt Inputs](https://www.flowhunt.io/components/ConditionalRouter/), [AWS Glue Documentation](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)
- Muchas plataformas (ej.: [Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter)) soportan enrutamiento basado en plantillas con variables dinámicas.


## Operadores disponibles

Los Routers Condicionales soportan una amplia variedad de operadores para enrutamiento flexible:

| Operador            | Descripción                                       | Ejemplo de uso                        |
|---------------------|---------------------------------------------------|---------------------------------------|
| `equals` / `$eq`    | El valor es igual al de coincidencia              | `"status" == "active"`                |
| `not equals`/ `$ne` | El valor no es igual al de coincidencia           | `"role" != "admin"`                   |
| `contains`          | El valor contiene la subcadena                    | `"hello@example.com" contains "@"`    |
| `starts with`       | El valor comienza con la subcadena                | `"prefix"` starts with "pre"          |
| `ends with`         | El valor termina con la subcadena                 | `"file.pdf"` ends with ".pdf"         |
| `is empty`          | El valor está vacío/nulo/indefinido               | `""`                                  |
| `is not empty`      | El valor no está vacío                            | `"not empty"`                         |
| `is_url`            | El valor coincide con el formato de URL           | `"https://..."`                       |
| `is_email`          | El valor coincide con el formato de correo        | `"name@domain.com"`                   |
| `is_number`         | El valor es numérico                              | `123`                                 |
| `$in`               | El valor está en el array/lista                   | `tier in ["pro", "enterprise"]`       |
| `$nin`              | El valor no está en el array/lista                | `status not in ["error"]`             |
| `$regex`            | El valor coincide con la expresión regular        | `input matches /pattern/`             |
| `$gt`, `$gte`       | Mayor que / mayor o igual (números)               | `score >= 0.8`                        |
| `$lt`, `$lte`       | Menor que / menor o igual (números)               | `temperature < 0.7`                   |

- **Operadores lógicos:** `$and` (todas las condiciones deben ser verdaderas), `$or` (cualquier condición verdadera)
- **Fuentes:** [FlowHunt Operator List](https://www.flowhunt.io/components/ConditionalRouter/), [Portkey Conditional Routing](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)


## Salidas

Cada nodo Router Condicional proporciona múltiples puertos de salida:

| Nombre de salida | Condición de disparo                   | Tipo de datos de salida |
|------------------|----------------------------------------|------------------------|
| Ruta Verdadera   | Cuando la condición es `true`          | Mensaje/Objeto         |
| Ruta Falsa       | Cuando la condición es `false`         | Mensaje/Objeto         |
| Rutas personalizadas | Salidas nombradas para cada condición | Mensaje/Objeto         |
| Ruta predeterminada | Cuando ninguna condición coincide     | Mensaje/Objeto         |

- **Puertos de salida nombrados:** Cada condición se vincula a una salida nombrada.
- **Salida predeterminada:** Maneja datos no coincidentes.
- **Reenvío de datos:** El mensaje/dato original (o transformado) se pasa por la salida activada.

- **Fuente:** [FlowHunt Outputs](https://www.flowhunt.io/components/ConditionalRouter/), [AWS Glue Routing](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)


## Configuración avanzada

### Operadores lógicos

Para definir lógica de múltiples condiciones para una sola ruta, utilice operadores lógicos:

**Ejemplo ([Portkey](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing))**
```json
{
  "query": {
    "$and": [
      { "metadata.user_type": { "$eq": "pro" } },
      { "params.model": { "$eq": "gpt-4" } }
    ]
  },
  "then": "pro_gpt4_target"
}
```

- Soporta `$and`, `$or` e incluso bloques lógicos anidados.

### Sensibilidad a mayúsculas

Configure si las comparaciones de cadenas deben ser sensibles a mayúsculas:

- `case_sensitive: true` para coincidencia exacta
- `case_sensitive: false` para ignorar mayúsculas

### Manejo de plantillas inseguras

Algunas plataformas (ej.: [Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter)) permiten renderizado inseguro de plantillas para escenarios avanzados, como pasar objetos complejos por las salidas. Úselo con precaución, ya que habilitarlo puede introducir riesgos de seguridad como ejecución remota de código.


## Ejemplos prácticos

### Ejemplo 1: Coincidencia simple de texto ([FlowHunt](https://www.flowhunt.io/components/ConditionalRouter/))
Enrutar el mensaje del usuario a soporte si contiene la palabra clave "help", de lo contrario, enrutar al bot.

```json
{
  "input_text": "I need help with my order",
  "match_text": "help",
  "operator": "contains",
  "case_sensitive": false
}
```

### Ejemplo 2: Selección de modelo basada en parámetros ([Portkey](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing))
Enrutar solicitudes a diferentes modelos según el parámetro `model`.

```json
{
  "strategy": {
    "mode": "conditional",
    "conditions": [
      {
        "query": { "params.model": { "$eq": "fastest" } },
        "then": "fast-model"
      },
      {
        "query": { "params.model": { "$eq": "smartest" } },
        "then": "smart-model"
      }
    ],
    "default": "balanced-model"
  }
}
```

### Ejemplo 3: Validación de datos ([Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter))
Enrutar según la longitud de la entrada:

```python
routes = [
  {
    "condition": "{{ query|length > 10 }}",
    "output": ["{{ query }}", "{{ query|length }}"],
    "output_name": ["ok_query", "length"],
    "output_type": [str, int],
  },
  {
    "condition": "{{ query|length <= 10 }}",
    "output": ["query too short: {{ query }}", "{{ query|length }}"],
    "output_name": ["too_short_query", "length"],
    "output_type": [str, int],
  },
]
```

### Ejemplo 4: Enrutamiento combinado por metadatos y parámetros ([Portkey](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing#combined-routing-with-multiple-conditions))
Enrutar usuarios empresariales con solicitudes de alta creatividad a un modelo premium.

```json
{
  "strategy": {
    "mode": "conditional",
    "conditions": [
      {
        "query": {
          "$and": [
            { "metadata.user_tier": { "$eq": "enterprise" } },
            { "params.temperature": { "$gte": 0.7 } }
          ]
        },
        "then": "creative-premium-target"
      }
    ],
    "default": "standard-target"
  }
}
```

### Ejemplo de flujo de trabajo real

- **Slack:** [Automatización de un flujo de solicitudes de soporte](https://slack.com/blog/news/conditional-branching-workflow-builder) donde las entradas de un formulario dirigen la solicitud a diferentes equipos o activan aprobaciones multinivel—sin código.


## Usos típicos

### 1. Lógica de ramificación

- Dirigir a los usuarios a diferentes diálogos o rutas de proceso según intención, contenido o atributos.
- Orquestar flujos de automatización que se bifurcan según el evento o los datos del mensaje.

### 2. Validación y filtrado

- Aplicar validación de entrada (ej.: campos obligatorios, formatos correctos)
- Detectar y filtrar spam o contenido inapropiado

### 3. Personalización y segmentación de usuarios

- Enrutar usuarios premium vs. gratuitos a diferentes flujos ([FlowHunt](https://www.flowhunt.io/components/ConditionalRouter/))
- Implementar pruebas A/B asignando usuarios a ramas experimentales

### 4. Selección de modelo y banderas de características

- Seleccionar modelos de IA dinámicamente según el segmento de usuario o las propiedades de la solicitud ([Portkey](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing))
- Habilitar/deshabilitar características mediante flags de configuración

### 5. Control de acceso y cumplimiento

- Garantizar el enrutamiento de datos según la región para cumplimiento normativo
- Aplicar restricciones de acceso basadas en roles usando metadatos


## Mejores prácticas

- **Orden de condiciones:** Coloque las condiciones específicas antes que las genéricas para evitar coincidencias prematuras. ([FlowHunt](https://www.flowhunt.io/components/ConditionalRouter/), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html))
- **Valores predeterminados de seguridad:** Configure siempre una salida predeterminada para datos no coincidentes.
- **Pruebas:** Valide la lógica con datos de prueba para asegurar el enrutamiento correcto; use registros y analítica para monitorear decisiones de enrutamiento.
- **Documentación:** Comente o documente condiciones complejas para mantenibilidad.
- **Seguridad:** Evite la evaluación insegura de plantillas a menos que sea esencial y las entradas sean confiables. ([Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter))
- **Rendimiento:** Evite anidamientos excesivos o condiciones extremadamente complejas para mantener un enrutamiento rápido y manejable.
- **Accesibilidad sin código:** Use plataformas con interfaces gráficas o sin código para una accesibilidad más amplia (ver [Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)).


## Solución de problemas y Preguntas frecuentes

**P: ¿Qué ocurre si coinciden múltiples condiciones?**  
R: Solo se selecciona la primera condición coincidente (en orden); las coincidencias posteriores se ignoran ([FlowHunt](https://www.flowhunt.io/components/ConditionalRouter/), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)). En algunas herramientas ETL, los datos pueden enrutarse a múltiples salidas.

**P: ¿Cómo enrutó según múltiples campos?**  
R: Use operadores lógicos (`$and`, `$or`) para combinar condiciones sobre varios campos ([Portkey](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing)).

**P: ¿Qué pasa si falta un campo referenciado?**  
R: La condición normalmente se evalúa como `false` y el router continúa a la siguiente condición o predeterminada.

**P: ¿Puedo usar regex o coincidencia avanzada?**  
R: Sí, muchos routers soportan `$regex` o operadores basados en patrones.

**P: ¿Es adecuado para personas no técnicas?**  
R: Muchas plataformas ofrecen configuración sin código (ver [Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)).

**P: ¿Puedo realizar enrutamiento paralelo?**  
R: La mayoría de routers son exclusivos (una sola ruta por evaluación). Para acciones paralelas, use componentes especializados de múltiples rutas o ramificación.


## Documentación relacionada

- [FlowHunt Conditional Router](https://www.flowhunt.io/components/ConditionalRouter/)
- [AWS Glue: Conditional Router](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)
- [Haystack ConditionalRouter](https://docs.haystack.deepset.ai/docs/conditionalrouter)
- [Portkey AI Conditional Routing](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing)
- [Fluix Conditional Routing](https://fluix.io/help/conditional-logic-tutorial)
- [Slack Conditional Branching](https://slack.com/blog/news/conditional-branching-workflow-builder)
- [Frontline AI Conditional Routing](https://help.getfrontline.ai/en/articles/10174140-understanding-conditional-routing-in-ai-agent-flows)
- [Rapidomize Conditional Routing](https://rapidomize.com/docs/services/router/)



## Recursos en profundidad y lecturas adicionales

- [AWS Glue Conditional Router](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)
- [FlowHunt Conditional Router](https://www.flowhunt.io/components/ConditionalRouter/)
- [Haystack ConditionalRouter](https://docs.haystack.deepset.ai/docs/conditionalrouter)
- [Portkey AI Gateway Routing](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing)
- [Fluix Conditional Routing Tutorial](https://fluix.io/help/conditional-logic-tutorial)
- [Slack Workflow Builder: Conditional Branching](https://slack.com/blog/news/conditional-branching-workflow-builder)


Para ejemplos de implementación, configuración avanzada y solución de problemas, consulte los enlaces de documentación oficial arriba. Estos cubren detalles específicos de plataforma para herramientas de IA, automatización y procesos empresariales.


**Citas:**
- [Slack Blog: Conditional Branching](https://slack.com/blog/news/conditional-branching-workflow-builder)
- [AWS Glue Conditional Router](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)
- [FlowHunt Conditional Router](https://www.flowhunt.io/components/ConditionalRouter/)
- [Fluix Conditional Routing](https://fluix.io/help/conditional-logic-tutorial)
- [Portkey AI Routing](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing)
- [Haystack Conditional Router](https://docs.haystack.deepset.ai/docs/conditionalrouter)

Para una introducción interactiva y visual, consulte la [demo de Workflow Builder de Slack](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder) y la [demo en vivo de FlowHunt](https://www.flowhunt.io/demo/).


**Video tutoriales:**  
- [Conditional Routing in Slack Workflow Builder (YouTube)](https://www.youtube.com/watch?v=3O4c7iYhD5Y)  
- [How to Use Conditional Router in FlowHunt (YouTube)](https://www.youtube.com/watch?v=rgqX7Qj3QAo)  
- [AWS Glue Conditional Router Tutorial (YouTube)](https://www.youtube.com/watch?v=90p4Vq8F9pQ)


Esta página de glosario sintetiza conocimiento técnico profundo, orientación práctica y mejores prácticas para Routers Condicionales en contextos de IA y automatización de flujos de trabajo. Para mayor exploración, consulte la documentación y los tutoriales en video enlazados.