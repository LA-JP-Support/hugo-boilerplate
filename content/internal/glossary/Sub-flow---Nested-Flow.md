+++
title = "Sub-flujo / Flujo Anidado"
translationKey = "sub-flow-nested-flow"
description = "Aprenda sobre sub-flujos (flujos anidados) en automatización. Incruste flujos de trabajo dentro de otros para simplificar lógica compleja, mejorar la reutilización y facilitar el mantenimiento."
keywords = ["sub-flujo", "flujo anidado", "automatización de flujos de trabajo", "reutilización", "flujo modular"]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Sub-flow---Nested-Flow/"

+++
## ¿Qué son los Sub-flujos / Flujos Anidados?

Un **sub-flujo**(o **flujo anidado**) es un flujo de trabajo autónomo que se invoca como un paso dentro de un flujo de trabajo principal o padre. Este patrón modular permite descomponer lógica empresarial compleja, habilitando la reutilización consistente y el mantenimiento simplificado. Los sub-flujos son análogos a funciones de software: encapsulan lógica específica reutilizable en múltiples contextos.

- **Ejemplo:**En la incorporación de empleados, sub-flujos separados gestionan la configuración de TI, el cumplimiento de RRHH, la provisión de equipos y la creación de cuentas. Cada sub-flujo se desarrolla una vez y se invoca donde sea necesario.
## ¿Por qué usar Sub-flujos / Flujos Anidados?

### Beneficios Clave

- **Modularidad:**Los flujos complejos se dividen en unidades manejables y lógicas.  
- **Reutilización:**La lógica común (validaciones, notificaciones, transformación de datos) se construye una vez y se reutiliza en todas partes.  
- **Mantenibilidad:**Los cambios en un sub-flujo actualizan instantáneamente todos los flujos padres, reduciendo riesgos y costos.  
- **Escalabilidad:**Las automatizaciones grandes son más fáciles de ampliar y adaptar componiendo piezas pequeñas y bien definidas.  
- **Consistencia:**Los procesos idénticos se ejecutan de forma uniforme en todos los flujos.  
- **Seguridad Mejorada:**El acceso a lógica sensible se aísla y protege mediante permisos.  
- **Mejor Gestión de Errores:**La gestión de errores centralizada se aplica a los sub-flujos para recuperación confiable y registro unificado.
## ¿Cómo Funcionan los Sub-flujos / Flujos Anidados?

### Proceso Paso a Paso

1. **Diseñar el Sub-flujo:**Identifique lógica repetitiva (ejemplo: validación de datos, notificaciones) y constrúyala como un flujo autónomo con entradas/salidas definidas.

2. **Integrar con el Flujo Padre:**Invoque el sub-flujo en el paso deseado, pasando los datos necesarios como entradas.

3. **Ejecución:**El flujo padre dispara el sub-flujo, que se ejecuta como una sola operación. La ejecución puede ser síncrona (el padre espera) o asíncrona (el padre continúa).

4. **Gestión de Estado y Resultados:**Los resultados del sub-flujo se devuelven y quedan disponibles para el procesamiento posterior. El estado se gestiona dentro del sub-flujo pero puede acceder al contexto del padre si es necesario.

5. **Reutilización Entre Flujos:**El mismo sub-flujo puede ser llamado desde varios flujos padres, apoyando la estandarización y el desarrollo ágil.

**Ejemplos de Plataformas:**- **Microsoft Power Automate for Desktop:**Los sub-flujos automatizan acciones en Excel, web o Windows y se invocan dentro de flujos principales.  
  [Tutorial](https://learn.microsoft.com/en-us/training/modules/create-subflows-web-automation-online-workshop/)

- **ServiceNow Workflow Studio:**Los sub-flujos, acciones y plantillas se construyen como lógica reutilizable e invocable en cualquier flujo.  
  [Documentación de Workflow Studio](https://docs.servicenow.com/csh?version=latest&topicname=workflow-studio)

- **AWS Step Functions:**Las máquinas de estado padres orquestan flujos de trabajo hijos (anidados), soportando jerarquías complejas y separación de dominios.  
  [Documentación de AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html)

## Flujo Padre vs. Sub-flujo: Términos Clave

- **Flujo Padre:**La automatización principal que controla el proceso e invoca sub-flujos como pasos.
- **Sub-flujo / Flujo Anidado:**Un flujo de trabajo contenido y reutilizable que se ejecuta dentro del flujo padre.
- **Componente Reutilizable:**Cualquier flujo modular o sub-flujo diseñado para uso repetido.
- **Transiciones de Estado:**Movimiento entre estados del flujo, incluyendo la llamada a sub-flujos y el procesamiento de sus resultados.
- **Gestión de Errores:**Mecanismos para manejar fallos en sub-flujos, propagando incidencias al flujo padre para recuperación.

## Importancia y Propuesta de Valor

- **Reducción de Redundancia:**Elimina duplicidad de código; la lógica se actualiza centralmente.
- **Actualizaciones Centralizadas:**Un solo cambio actualiza todos los flujos dependientes.
- **Simplificación de la Lógica Compleja:**Los flujos grandes son más fáciles de entender y depurar.
- **Impulso a la Colaboración de Equipos:**Los equipos gestionan sub-flujos distintos, habilitando expertise y mantenimiento distribuido.
- **Habilita Patrones Avanzados:**- **Ejecución Paralela:**Invoque múltiples sub-flujos simultáneamente.  
  - **Lógica Condicional:**Llame sub-flujos en función de condiciones de ejecución.  
  - **Bucles:**Ejecute sub-flujos repetidamente hasta cumplir una condición.  
  - **Suspensión/Reanudación:**Pause y reanude flujos en los límites de sub-flujos.

**Valor Real en AWS Step Functions:**Desacoplar flujos en sub-flujos redujo costos mensuales y mejoró el aislamiento de errores, la depuración y los indicadores operativos ([comparación completa de AWS](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/)).

## Casos de Uso Comunes

1. **Recursos Humanos (RRHH):**- **Onboarding:**Sub-flujos para configuración TI, documentación de RRHH, cumplimiento.
   - **Reclutamiento:**Filtrado, programación de entrevistas, creación de ofertas.

2. **Finanzas:**- **Procesamiento de Pagos:**Sub-flujos para verificación de crédito, detección de fraude, registro de transacciones.
   - **Gestión de Facturas:**Validación, rutas de aprobación, reembolso.

3. **Atención al Cliente:**- **Ingreso de Tickets:**Sub-flujo para validación de datos y comprobación de cuentas.
   - **Escalamiento:**Sub-flujos para diferentes rutas de escalamiento.

4. **Marketing:**- **Automatización de Campañas:**Sub-flujos para segmentación, personalización y envío de emails.

5. **Cumplimiento y Auditoría:**- **Preparación de Auditoría:**Recopilación documental, auto-verificaciones, seguimiento de finalización.
   - **Gestión de Incidentes:**Notificaciones, investigaciones, reportes.

6. **Operaciones:**- **Gestión de Inventario:**Actualización de existencias, disparadores de reabastecimiento, validación de proveedores.

**Ejemplo:**Un sub-flujo de “verificación de crédito” se reutiliza tanto en la solicitud de préstamos como en el onboarding de clientes nuevos, asegurando lógica de cumplimiento y validación consistente.

## Patrones Técnicos y Funcionalidades

### Implementaciones en Plataformas

- **Microsoft Power Automate:**Los sub-flujos automatizan acciones web/escritorio, devolviendo resultados y gestionando errores de forma centralizada.  
  [Guía](https://learn.microsoft.com/en-us/training/modules/create-subflows-web-automation-online-workshop/)

- **ServiceNow Workflow Studio:**Constructor unificado para flujos, sub-flujos y acciones personalizadas. Soporta depuración, versionado y flujos conversacionales potenciados por LLM.  
  [Notas de lanzamiento](https://www.servicenow.com/docs/bundle/zurich-release-notes/page/release-notes/now-platform-app-engine/flow-designer-rn.html)

- **AWS Step Functions:**- **Patrón Padre-Hijo:**Los flujos padres orquestan sub-flujos (hijos), cada uno enfocado en un dominio u operación.  
  - **Separación de Dominios:**Flujos separados para pagos, inventario, envíos, etc.  
  - **Utilidades Compartidas:**Sub-flujos reutilizables para notificaciones, registro, validación.  
  - **Flujos de Errores:**Sub-flujos centralizados para gestión de errores y mantenibilidad.

**Ejemplo de Código AWS (Tipo TypeScript):**```typescript
const nestedWorkflow = new LegacyWorkflow({ name: "nested-workflow" })
  .step(stepA)
  .then(stepB)
  .commit();

const parentWorkflow = new LegacyWorkflow({ name: "parent-workflow" })
  .step(nestedWorkflow)
  .then(stepC)
  .commit();
```
- [Más ejemplos y guías de AWS](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/)

### Características Clave de Plataforma

- Invocación y paso de resultados
- Ejecución paralela de sub-flujos
- Ramas condicionales
- Suspensión/reanudación para flujos de larga duración
- Monitorización de estado y propagación de errores

## Enfoques de Flujos Monolíticos vs. Modulares (Anidados)

| Aspecto              | Flujo Monolítico                      | Flujo Modular/Anidado                     |
|----------------------|---------------------------------------|-------------------------------------------|
| **Mantenibilidad**| Difícil de actualizar; acoplado       | Fácil de actualizar; desacoplado          |
| **Reutilización**| Baja (lógica redundante)              | Alta (lógica común centralizada)          |
| **Gestión de Errores**| Difícil de aislar y rastrear errores | Centralizada, más fácil de manejar        |
| **Escalabilidad**| Limitada por la complejidad           | Escalable componiendo sub-flujos          |
| **Depuración**| Compleja, por explosión de estados    | Más simple, con dominios de error aislados|
| **Versionado**| Requiere re-desplegar todo el flujo   | Actualice sub-flujos individualmente      |
## Buenas Prácticas para Sub-flujos / Flujos Anidados

1. **Diseñe para la Modularidad:**Encapsule pasos relacionados; evite sub-flujos “Dios”.
2. **Convenciones de Nomenclatura:**Use nombres descriptivos para claridad y trazabilidad.
3. **Contratos de Entrada/Salida:**Defina claramente los datos esperados; use esquemas o tipos.
4. **Gestión de Errores:**Centralice la lógica de errores; propague errores al flujo padre.
5. **Gestión de Estado:**Permita que los sub-flujos gestionen su propio estado; acceda al contexto padre solo si es necesario.
6. **Control de Acceso:**Restrinja permisos para sub-flujos sensibles.
7. **Pruebas y Versionado:**Pruebe de forma independiente y en contexto; versionar sub-flujos para evitar cambios disruptivos.
8. **Documentación:**Documente interfaces, lógica y uso para mantenibilidad.

**Lecturas recomendadas:**- [ServiceNow: Guía y Buenas Prácticas](https://sn.works/CoE/StartFlow#h_320418873381665150474199)  
- [Mejores Prácticas AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/best-practices.html)

## Preguntas Frecuentes sobre Sub-flujos / Flujos Anidados

**P: ¿En qué se diferencian los flujos anidados de los flujos multi-paso?**R: Los flujos multi-paso son lineales; los flujos anidados invocan flujos reutilizables como componentes.

**P: ¿Pueden los sub-flujos ejecutarse en paralelo?**R: Sí, la mayoría de plataformas soportan ejecución concurrente de sub-flujos.

**P: ¿Cómo se gestionan los errores?**R: Los errores se propagan hacia arriba; los flujos padres pueden reintentar, abortar o escalar.

**P: ¿Acceden los sub-flujos a los datos del padre?**R: Reciben entradas definidas; el acceso más amplio depende de la configuración de seguridad de la plataforma.

**P: ¿Cómo actualizo un sub-flujo usado en varios flujos?**R: Actualice la definición del sub-flujo; todos los flujos padres utilizarán la nueva versión inmediatamente.

**P: ¿Qué ocurre si un sub-flujo se suspende o pausa?**R: Los flujos padres pueden esperar y reanudar según sea necesario—soporta procesos [human-in-the-loop](/en/glossary/human-in-the-loop--hitl-/).

**P: ¿Pueden los sub-flujos anidarse a varios niveles?**R: Sí, permitiendo jerarquías complejas.

## Solución de Problemas y Consejos

- **El sub-flujo falla inesperadamente:**Verifique los datos de entrada y parámetros; revise la gestión de errores.
- **Sub-flujos paralelos ralentizan el rendimiento:**Monitoree uso de recursos; agrupe o limite según sea necesario.
- **Mapeo de resultados poco claro:**Documente explícitamente las salidas y utilice esquemas.
- **Problemas de versionado:**Implemente control de versiones; gestione cuidadosamente los cambios disruptivos.

## Recursos Autoritativos y Lecturas Adicionales

- [Activepieces Glosario – Flujos Anidados](https://resources.activepieces.com/glossary/nested-flows)  
- [Way We Do Blog – Introducción a Subprocesos](https://www.waywedo.com/blog/introducing-sub-processes/)  
- [Mastra Docs – Flujos de Trabajo Anidados (Legacy)](https://mastra.ai/docs/workflows-legacy/nested-workflows)  
- [AWS Compute Blog – Modularización de Workflows Step Functions](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/)  
- [Microsoft Power Automate: Taller de Sub-flujos](https://learn.microsoft.com/en-us/training/modules/create-subflows-web-automation-online-workshop/)  
- [Documentación ServiceNow Flow Designer](https://docs.servicenow.com/csh?version=latest&topicname=flow-designer)  

## Tutoriales y Videos en Profundidad por Plataforma

- **Microsoft Power Automate for Desktop:**[Crear sub-flujos y automatización web (tutorial oficial)](https://learn.microsoft.com/en-us/training/modules/create-subflows-web-automation-online-workshop/)

- **ServiceNow: Sub-flujos en IA Conversacional**[YouTube – Ejecutar un Sub-flujo desde una conversación Now Assist](https://www.youtube.com/watch?v=jbRhPq6jREY)

## Diagramas Técnicos y Notas de Versión

- [ServiceNow Zurich Release: Sub-flujos y Acciones](https://www.servicenow.com/docs/bundle/zurich-release-notes/page/release-notes/now-platform-app-engine/flow-designer-rn.html)
- [AWS Step Functions: Diagramas de Máquinas de Estado Padre-Hijo](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/)

*Para profundizar en guías específicas de plataforma y patrones arquitectónicos avanzados, consulte los recursos anteriores. Implementar sub-flujos es fundamental para una automatización de workflows escalable, mantenible y resiliente tanto en entornos empresariales como en pymes.*