+++
title = "Spot Instances"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "spot-instances"
description = "Las Spot Instances son recursos de computación en la nube con descuento de AWS, Azure y GCP, ideales para cargas de trabajo tolerantes a fallos como procesamiento por lotes, analítica y entrenamiento de ML."
keywords = ["Spot Instances", "computación en la nube", "AWS", "Azure", "GCP"]
category = "Infraestructura y Despliegue de IA"
type = "glosario"
draft = false
url = "/internal/glossary/Spot-Instances/"

+++
## ¿Qué son las Spot Instances?

Las Spot Instances son un modelo de compra de computación en la nube donde los usuarios acceden a recursos sobrantes con descuentos que a menudo alcanzan **hasta un 90% menos**que el precio bajo demanda. Los principales proveedores incluyen:

- **Amazon Web Services (AWS) Spot Instances:**Los usuarios especifican un precio máximo y reciben instancias si el precio de mercado está por debajo de este umbral. [Documentación de AWS Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- **Microsoft Azure Spot Virtual Machines (VMs):**Los usuarios fijan un precio máximo; las VMs son desalojadas cuando el precio de mercado lo supera. [Guía de Azure Spot VMs](https://spot.io/resources/azure-pricing/the-complete-guide/what-are-azure-spot-virtual-machines/)
- **Google Cloud Spot VMs:**Ofrecen descuentos similares, con ahorros fijos y sustanciales, y el precio es estable hasta por un mes. [Google Cloud Spot VMs](https://cloud.google.com/compute/docs/instances/spot)

Las Spot Instances son más adecuadas para **aplicaciones flexibles y tolerantes a fallos**. Los proveedores pueden reclamar estas instancias con poco aviso, por lo que la resiliencia ante interrupciones es un requisito esencial.  

## ¿Cómo funcionan las Spot Instances?

### Mecanismo de precios

- **Dinámico, basado en oferta/demanda:**El precio spot para cada tipo de instancia y región fluctúa según tendencias a largo plazo en oferta y demanda, no por subastas en tiempo real. [AWS Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- **Precio máximo:**Los usuarios pueden establecer un precio máximo que están dispuestos a pagar. Mientras el precio spot esté por debajo, la instancia sigue funcionando.
- **Sin subasta en tiempo real (modelo moderno):**Los sistemas iniciales implicaban pujas en vivo, pero ahora la mayoría de proveedores usan un modelo de precio máximo fijo por simplicidad. Los usuarios ya no compiten en subastas en tiempo real. [Spot.io: Spot vs On-Demand](https://spot.io/resources/spot-instances/spot-instances-vs-on-demand-instances-pros-and-cons/)
- **Granularidad de facturación:**AWS, Azure y GCP facturan por segundo, tras un mínimo de 1 minuto. [Google Cloud Pricing](https://cloud.google.com/compute/pricing)

> **Ejemplo:**En AWS, una instancia On-Demand `m5.large` cuesta $0.096/hr, mientras que el precio Spot podría ser tan bajo como $0.019/hr (más del 80% de ahorro).  
> Consulta [AWS Spot Pricing](https://aws.amazon.com/ec2/spot/pricing/)

### Disponibilidad e interrupciones

- **Pool de capacidad:**Cada solicitud de Spot Instance proviene de un pool definido por tipo de instancia y zona de disponibilidad.
- **Política de interrupción:**Los proveedores pueden terminar o desalojar instancias con poco aviso—2 minutos en AWS, 30 segundos en Azure y GCP—cuando necesitan la capacidad o el precio spot supera tu oferta máxima.
- **Notificación de interrupción:**AWS envía una advertencia de 2 minutos, mientras que Azure y GCP dan aviso de 30 segundos.  
  - [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
  - [Azure Spot VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)
  - [GCP Spot VMs](https://cloud.google.com/compute/docs/instances/spot#preemption)
- **Rebalanceo:**AWS ofrece "recomendaciones de rebalanceo", avisando antes si una Spot Instance tiene alto riesgo de interrupción.  
  - [AWS Rebalance Recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)
  
> **Punto clave:**Las aplicaciones **deben**estar diseñadas para manejar interrupciones—sin estado, checkpointing y auto-recuperación son esenciales.

## Spot Instances vs. On-Demand vs. Reserved Instances

| Característica            | **Spot Instances**| **On-Demand Instances**| **Reserved Instances**|
|--------------------------|--------------------------------------------------------------|------------------------------------------------|---------------------------------------------|
| **Precio**| Variable, hasta un 90% menos que bajo demanda                | Fijo, precio más alto                          | Descuento (hasta 72%), fijo                 |
| **Disponibilidad**| Sólo si hay capacidad sobrante                               | Siempre disponible (si hay capacidad)          | Garantizada durante el periodo reservado     |
| **Interrupciones**| Pueden ser interrumpidas en cualquier momento (2 min o 30 seg de aviso) | El usuario decide cuándo terminar              | No se interrumpen durante el periodo         |
| **Compromiso**| Sin compromiso                                               | Sin compromiso                                 | 1 o 3 años (compromiso requerido)           |
| **Casos de uso**| Flexibles, tolerantes a fallos, no críticos                  | Todas las cargas, especialmente críticas       | Cargas previsibles y estables                |
| **SLA**| Sin SLA                                                      | SLA estándar                                   | SLA estándar                                |
| **Granularidad facturación**| Por segundo (tras el 1er minuto)                         | Por segundo                                    | Por segundo                                 |

- **Más información:**[Opciones de compra y facturación de AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)

## Comparativa entre proveedores cloud

| Característica              | **AWS Spot Instances**| **GCP Spot VMs**| **Azure Spot VMs**|
|-----------------------------|------------------------------------|-----------------------------------|------------------------------------|
| **Modelo de precios**| Variable, según oferta/demanda     | Descuento fijo (hasta 91% menos)  | Variable, según oferta/demanda     |
| **Límite de uso**| Sin límite fijo                    | Máx. 24 horas                     | Sin límite fijo                    |
| **Aviso de interrupción**| 2 minutos                          | 30 segundos                       | 30 segundos                        |
| **Facturación**| Por segundo (tras 1 min)           | Por segundo                       | Por segundo                        |
| **SLA**| Sin SLA                            | Sin SLA                           | Sin SLA                            |
| **Herramientas de integración**| Spot Fleet, ASG, Kubernetes   | MIG, GKE                          | VM Scale Sets, AKS                 |
| **Mejores casos de uso**| Batch, CI/CD, ML, HPC, apps sin estado | Batch, analítica, dev/test      | Batch, apps sin estado, CI/CD      |
| **Características únicas**| Spot block (interrupción a plazo fijo) | Descuentos por uso sostenido    | Personalización de política de desalojo |

- [Spot.io Provider Comparison](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/)

## Conceptos clave

### Pool de capacidad Spot

Grupo de máquinas virtuales no utilizadas del mismo tipo y zona de disponibilidad. Cada pool opera de forma independiente, y la capacidad/precio varía entre pools. [AWS Spot Pools](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

### Solicitud de Spot Instance

Una solicitud iniciada por el usuario para asignar una Spot Instance. Las solicitudes pueden ser:
- **Única vez:**Se aprovisiona una vez si hay capacidad.
- **Persistente:**Se reenvía automáticamente si se interrumpe (útil para trabajos que deben completarse).

### Recomendación de rebalanceo (AWS)

AWS emite una recomendación de rebalanceo antes del aviso estándar de interrupción si una Spot Instance tiene alto riesgo de ser terminada, permitiendo migrar o guardar el trabajo proactivamente. [AWS Instance Rebalance Recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)

## Casos de uso y ejemplos prácticos

Las Spot Instances sobresalen cuando **la interrupción es gestionable**y se buscan minimizar los costes. Los principales casos de uso incluyen:

### Casos ideales

- **Procesamiento por lotes:**Analítica de datos, transcodificación de vídeo, renderizado, ETL.
  - *Ejemplo:* Investigadores realizando simulaciones de Monte Carlo para datos climáticos, ahorrando más del 80% en computación.
- **Analítica de big data:**Clústeres Hadoop/Spark, análisis de logs/datos a escala.
  - *Ejemplo:* Empresas de medios procesando petabytes de logs cada noche en AWS EMR con Spot Instances.
- **Pipelines CI/CD:**Entornos de construcción y pruebas de corta vida.
  - *Ejemplo:* Proveedores SaaS usando Spot Instances como agentes Jenkins para CI rentable y paralelizado.
- **Entrenamiento de Machine Learning:**Deep learning, ajuste de hiperparámetros, entrenamiento con checkpoint en GPUs.
  - *Ejemplo:* Equipos entrenando redes neuronales en GPU Spot con guardado automático para recuperación ante interrupciones.
- **Contenedores y microservicios:**Servicios sin estado orquestados por Kubernetes o [Docker](/en/glossary/docker/) Swarm.
- **Entornos de desarrollo/pruebas:**Workloads no productivos donde la interrupción es aceptable.
- **High-Performance Computing (HPC):**Secuenciación genómica, modelado financiero, simulaciones científicas.

- [AWS Spot Use Cases](https://aws.amazon.com/ec2/spot/use-cases/)

### Casos no ideales

- **Aplicaciones críticas:**Donde la alta disponibilidad y el mínimo downtime son esenciales.
- **Apps con estado sin resiliencia:**Aplicaciones que no pueden guardar estado o recuperarse de una terminación repentina.

- [Spot.io: Suitable Use Cases](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Suitable-Use-Cases-for-Spot-Instances)

## Riesgos, desafíos y estrategias de mitigación

### Riesgos clave

- **Riesgo de interrupción:**Las instancias pueden ser terminadas o desalojadas con tan sólo 30 segundos de aviso.
- **Volatilidad de capacidad:**La capacidad Spot puede desaparecer de forma impredecible según región, tipo y demanda.
- **Fluctuaciones de precio:**El precio Spot puede subir, especialmente para tipos populares en periodos de alta demanda.
- **Sin SLA:**Los proveedores no garantizan disponibilidad o uptime para Spot Instances.

- [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
- [Spot.io: Risks & Strategies](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Strategies-to-Optimize-the-Use-of-Spot-Instances)

### Estrategias de mitigación

- **Automatización:**- Utilizar sistemas de orquestación (ej. Kubernetes, Auto Scaling de AWS) para reprogramar y reemplazar cargas interrumpidas.
  - Mezclar Spot con instancias bajo demanda y reservadas para resiliencia.
  - Emplear plataformas de automatización (ej. [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/), [Spot.io](https://spot.io/products/eco/)) que gestionan ciclos de vida y fallback.
- **Diseño de aplicaciones:**- Arquitectar servicios sin estado y utilizar almacenamiento externo.
  - Implementar checkpointing para reanudar trabajos tras interrupción.
  - Usar acoplamiento flexible para tolerar fallos de nodo.
- **Monitoreo proactivo:**- Vigilar tasas de interrupción por región/tipo con herramientas como [AWS Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/).
  - Actuar ante [recomendaciones de rebalanceo](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations) para migrar cargas antes.
- **Diversificación:**- Usar mezcla de tipos y regiones para evitar interrupciones masivas.
  - Fijar ofertas máximas sensatas para reducir riesgo de desalojo repentino.

- [Cast AI Spot Guide](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)

## Buenas prácticas para usar Spot Instances

1. **Comienza con cargas no críticas:**Valida tus estrategias de manejo de interrupciones.
2. **Diversifica:**Usa múltiples tipos de instancia y zonas de disponibilidad para mayor fiabilidad.
3. **Automatiza:**Emplea [AWS Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html), Auto Scaling Groups o autoscalers de Kubernetes.
4. **Monitorea tendencias:**Usa [AWS Spot Price History](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html) y [Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/).
5. **Fija precios máximos:**Limita tu oferta al precio bajo demanda o menos.
6. **Planifica la interrupción:**Diseña para recuperación rápida y cero pérdida de datos.
7. **Aprovecha herramientas externas:**Prueba [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/) o [CloudZero](https://www.cloudzero.com/blog/spot-instances/) para optimización y automatización.
8. **Usa etiquetas:**Rastrear uso y ahorros por equipo/proyecto.
9. **Revisa periódicamente:**Actualiza tu mezcla y estrategias según los informes de uso.

- [AWS Spot Best Practices](https://aws.amazon.com/blogs/compute/best-practices-to-optimize-your-amazon-ec2-spot-instances-usage/)
- [CloudZero Spot Guide](https://www.cloudzero.com/blog/spot-instances/)

## Facturación y detalles de precios

- **Precio spot:**Fijado por el proveedor, fluctúa con oferta y demanda del mercado.
- **Granularidad de facturación:**Por segundo tras el primer minuto (AWS, Azure, GCP).
- **Facturación por terminación:**Por lo general, si AWS interrumpe, no se cobra la última fracción de hora; si el usuario termina, paga los segundos usados. [Detalles de facturación de AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-for-interrupted-spot-instances.html)
- **Seguimiento de ahorros:**Usa los paneles de proveedor, [reportes de ahorro de AWS Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html), o herramientas externas (ej. [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/), [Infracost](https://www.infracost.io/glossary/spot-instances/)).
- **Sin solapamiento con Savings Plans:**El uso de Spot no cuenta para los compromisos de AWS Savings Plans.

- [AWS EC2 Spot Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- [GCP Spot Pricing](https://cloud.google.com/compute/pricing)
- [Azure Spot Pricing](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/spot/)

## Escenario de ejemplo

**Equipo de investigación ejecutando simulaciones**Un grupo de investigación universitaria necesita ejecutar miles de simulaciones de Monte Carlo para modelado climático. Usando Spot Instances orquestadas por Kubernetes, reducen los costes de computación en un 85% respecto al precio bajo demanda. Los checkpoints se guardan en almacenamiento persistente antes de la interrupción, por lo que los trabajos se reanudan sin pérdida.

- [AWS Spot HPC Use Case](https://aws.amazon.com/ec2/spot/use-cases/hpc/)
- [Milvus AI Quick Reference: Spot Instances](https://milvus.io/ai-quick-reference/what-are-spot-instances-in-cloud-computing)

## Preguntas frecuentes (FAQ)

**P: ¿Puedo usar Spot Instances para cargas en producción?**R: Sí, si tu aplicación es resiliente a interrupciones. Muchas organizaciones combinan Spot con instancias bajo demanda o reservadas para cargas críticas.  
- [AWS Spot FAQ](https://aws.amazon.com/ec2/spot/faqs/)

**P: ¿Cuánto puedo ahorrar con Spot Instances?**R: Típicamente entre 70–90% respecto a bajo demanda, según región, tipo y demanda.  
- [AWS Spot Savings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html)

**P: ¿Qué sucede cuando una Spot Instance se interrumpe?**R: Recibes un aviso corto de interrupción (2 minutos en AWS, 30 segundos en Azure/GCP). La instancia se termina, detiene o hiberna según la política del proveedor.  
- [AWS Spot Interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)

**P: ¿Cómo solicito una Spot Instance?**R: Usa la consola del proveedor, CLI o API. Especifica tipo de instancia, precio máximo y duración según lo necesario.  
- [AWS Spot Requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html)

**P: ¿Pueden usarse Spot Instances con Kubernetes?**R: Sí, orquestadores de contenedores como Kubernetes pueden reprogramar pods cuando una Spot Instance se interrumpe.  
- [Kubernetes with Spot Instances](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)

**P: ¿Existe algún SLA para Spot Instances?**R: No. Los proveedores no garantizan disponibilidad ni uptime para Spot Instances.

## Recursos de referencia y lecturas recomendadas

- [AWS Spot Instances Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- [AWS EC2 Spot Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- [CloudZero Spot Instances Guide](https://www.cloudzero.com/blog/spot-instances/)
- [Infracost Spot Instances Glossary](https://www.infracost.io/glossary/spot-instances/)
- [Cast AI Spot Instances Guide](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)
- [Milvus AI Quick Reference: Spot Instances](https://milvus.io/ai-quick-reference/what-are-spot-instances-in-cloud-computing)
- [Amazon EC2 Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html)
- [AWS Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/)
- [Spot.io Ultimate Guide](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/)
- [AWS Spot FAQ](https://aws.amazon.com/ec2/spot/faqs/)

## Términos relacionados

- [On-Demand Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html)
- [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest