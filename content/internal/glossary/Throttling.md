+++
title = "Limitación (Limitación de API)"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "throttling-api-throttling"
description = "La limitación, también llamada limitación de API, es la restricción deliberada de solicitudes a una API o servicio dentro de un período de tiempo específico. Previene la sobrecarga, garantiza acceso equitativo, limita el abuso y mantiene el rendimiento."
keywords = ["limitación de API", "limitación de tasa", "token bucket", "puerta de enlace de API", "protección del sistema"]
category = "Infraestructura de IA y Despliegue"
type = "glosario"
draft = false
url = "/internal/glossary/Throttling/"

+++
## Resumen Conciso / Definición

**Limitación**, también conocida como *limitación de API*, es la restricción deliberada del número de solicitudes que un usuario, cliente o aplicación puede realizar a una API o servicio dentro de un período de tiempo específico. La limitación es crucial para prevenir la sobrecarga del backend, asegurar un acceso equitativo, limitar el abuso y mantener un rendimiento consistente del servicio gestionando y suavizando el flujo de tráfico entrante.

- [Documentación de Limitación de API Gateway de AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
- [Gravitee: Mejores Prácticas de Limitación de API](https://www.gravitee.io/blog/api-throttling-best-practices)
- [Knit.dev: 10 Mejores Prácticas para Limitación y Limitación de API](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)

## Por Qué Es Importante la Limitación / Casos de Uso

**La limitación cumple varios propósitos críticos:**- **Protección del Sistema:**Protege los servicios backend de picos de tráfico, uso indebido accidental o ataques deliberados que puedan degradar el rendimiento o causar caídas. Por ejemplo, AWS aplica limitación dura y suave en varios niveles del sistema para evitar la sobrecarga de la infraestructura ([fuente](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)).
- **Uso Justo:**Garantiza que ningún usuario o cliente pueda monopolizar los recursos de la API, asegurando acceso justo para todos los consumidores ([Gravitee](https://www.gravitee.io/blog/api-throttling-best-practices)).
- **Seguridad:**Restringe la capacidad de actores maliciosos para lanzar ataques de denegación de servicio (DoS/DDoS) al limitar la tasa a la que se aceptan las solicitudes ([Knit.dev](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)).
- **Estabilidad del Rendimiento:**Mantiene tiempos de respuesta de API predecibles y estables incluso bajo cargas variables o repentinas.
- **Monetización y Medición:**Permite precios diferenciados y niveles de servicio, con cuotas de uso para planes gratuitos y de pago.
- **Gestión de Recursos:**Evita el agotamiento de recursos backend (como bases de datos, cachés o GPUs) suavizando la demanda y limitando cargas simultáneas.

**Ejemplos en el mundo real:**- **APIs Sociales:**Twitter restringe el uso de la API por usuario por ventana de 15 minutos para desalentar el spam y proteger la estabilidad de la plataforma ([Documentación de la API de Twitter](https://developer.twitter.com/en/docs/twitter-api/rate-limits)).
- **Motores de Reservas:**Agencias de viajes en línea limitan llamadas a sistemas de reservas de aerolíneas (por ejemplo, Sabre, Amadeus) para evitar interrupciones de servicio aguas arriba.
- **Almacenamiento en la Nube:**AWS S3 aplica cuotas de solicitudes para preservar un rendimiento consistente para todos los inquilinos ([Límites de AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html)).
- **APIs de IA:**APIs de reconocimiento de imágenes o modelos de lenguaje aplican limitación por usuario o por app para controlar costos de GPU y mantener la [latencia de inferencia](/es/glossary/inference-latency/) ([Gravitee](https://www.gravitee.io/blog/api-throttling-best-practices)).

## Cómo Funciona la Limitación

**Los mecanismos de limitación incluyen:**1. **Límites de Tasa:**Establecen el número máximo de solicitudes permitidas por usuario, cliente o clave de API en un tiempo definido (por ejemplo, 1,000 solicitudes/hora).
2. **Límites de Ráfaga:**Permiten picos cortos por encima del ritmo sostenido, hasta un umbral (por ejemplo, 100 solicitudes en un segundo, promedio limitado a 10/seg).
3. **Códigos de Error:**Superar los límites genera una respuesta HTTP `429 Too Many Requests` ([RFC 6585](https://datatracker.ietf.org/doc/html/rfc6585#section-4)).
4. **Guía de Reintento:**Las APIs devuelven un encabezado `Retry-After`, indicando al cliente cuándo reintentar.
5. **Niveles de Aplicación:**La limitación puede ser por usuario, por clave de API, por app, por región o global, y suele aplicarse en la puerta de enlace de API o el backend.

**Flujo de limitación:**1. El cliente envía solicitud a la API.
2. El sistema revisa el conteo y el tiempo de las solicitudes contra los umbrales configurados (usando cubos de tokens, contadores o colas).
3. Si está dentro de los límites: la solicitud se procesa; si no: se retorna error `429` y encabezados como `Retry-After`, `X-RateLimit-Remaining`.
4. El cliente puede implementar estrategias de backoff—retrasar, reintentar o agrupar solicitudes.

**Ejemplo de Respuesta:**```http
HTTP/1.1 429 Too Many Requests
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1712345678
Retry-After: 60
Content-Type: application/json

{
  "error": "Límite de tasa excedido. Por favor espere 60 segundos antes de reintentar."
}
```

- [AWS: Cómo Funciona la Limitación](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

## Tipos y Algoritmos

### 1. Algoritmo de Cubo de Tokens

**Mecanismo:**Un cubo acumula tokens a una tasa fija. Cada solicitud consume un token. Solo se procesan solicitudes si hay tokens disponibles, permitiendo ráfagas cortas pero imponiendo una tasa promedio sostenida en el tiempo.

- **Ventajas:**Permite ráfagas, ajuste flexible, implementación sencilla.
- **Desventajas:**Cubos mal configurados pueden causar picos.
- **Analogía:**Cubeta de agua llenándose con gotas (tokens); solicitudes sacan gotas; si está vacía, debe esperar recarga.

- [Explicación del Cubo de Tokens de AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

**Pseudo-código:**```python
def allow_request():
    now = current_time()
    bucket.tokens += (now - bucket.last_check) * bucket.refill_rate
    bucket.tokens = min(bucket.tokens, bucket.capacity)
    bucket.last_check = now
    if bucket.tokens >= 1:
        bucket.tokens -= 1
        return True
    else:
        return False
```

**Ejemplo:**API bursátil: 100 solicitudes en ráfaga, recarga a 10/seg.

### 2. Algoritmo de Cubo con Fuga

**Mecanismo:**Las solicitudes entran a una cola de tamaño fijo (el "cubo"). Las solicitudes se procesan a una tasa constante. Si el cubo está lleno, las nuevas solicitudes se descartan o retrasan.

- **Ventajas:**Suaviza ráfagas, garantiza salida constante.
- **Desventajas:**Puede introducir [latencia](/es/glossary/latency/) o descartar tráfico ráfaga.
- **Analogía:**Cubo con un agujero—entra agua a cualquier ritmo, sale constantemente.

**Ejemplo:**API de emails pone en cola hasta 100 emails por minuto, envía a tasa constante.

### 3. Algoritmo de Ventana Fija

**Mecanismo:**Cuenta solicitudes dentro de un intervalo fijo (por ejemplo, minuto/hora). El contador se reinicia en el límite de la ventana.

- **Ventajas:**Sencillo de implementar.
- **Desventajas:**Vulnerable a picos en los bordes de ventana.

**Ejemplo:**Twitter permite 300 solicitudes por usuario cada ventana de 15 minutos.

### 4. Algoritmo de Ventana Deslizante

**Mecanismo:**Rastrea solicitudes en una ventana móvil (por ejemplo, últimos 60 segundos) para control más fino, suavizando ráfagas.

- **Ventajas:**Evita ráfagas en los bordes de ventana.
- **Desventajas:**Requiere rastrear timestamps, más complejo.

**Ejemplo:**API SaaS permite 100 solicitudes por 60 segundos deslizantes.

### 5. Limitación de Solicitudes Concurrentes

**Mecanismo:**Limita el número de solicitudes simultáneas (en vuelo) por cliente.

- **Ventajas:**Evita agotamiento de recursos por cargas paralelas.
- **Desventajas:**No limita el total de solicitudes en el tiempo.

**Ejemplo:**API de procesamiento de imágenes permite 5 solicitudes concurrentes por cliente.

### 6. Limitación Dura vs. Suave

- **Limitación Dura:**Aplicación estricta; solicitudes excesivas se rechazan (por ejemplo, niveles gratuitos, infraestructura crítica).
- **Limitación Suave:**Permite excesos temporales o pone en cola según la capacidad backend.

### 7. Limitación a Nivel Usuario vs. Sistema

- **Nivel Usuario:**Límites por usuario/cliente/clave de API para equidad.
- **Nivel Sistema:**Límites globales para la salud de la infraestructura.

- [Gravitee: Técnicas de Limitación de API](https://www.gravitee.io/blog/api-throttling-best-practices)

## Mejores Prácticas de Implementación

**Guías prácticas para una limitación robusta:**1. **Límites Granulares:**- Establecer en varios niveles (usuario, clave de API, endpoint, región).
   - Usar múltiples ventanas de tiempo (por segundo/minuto/hora/día).
   - [AWS: Por cliente, por método, por etapa](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html#apigateway-method-level-throttling-in-usage-plan).

2. **Contadores Distribuidos:**- Usar almacenes centralizados como Redis para contadores en sistemas distribuidos ([Knit.dev](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)).

3. **Mensajes de Error Claros:**- Siempre devolver HTTP `429`, con encabezados para límite, cuota restante, tiempo de reinicio (`Retry-After`).
   - Ejemplo de encabezados: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After`.

4. **Estrategias de Reintento:**- Recomendar backoff exponencial con jitter para evitar el problema de "manada trueno".

5. **Integración con Gateway de API:**- Usar plataformas como AWS API Gateway, Kong, Gravitee para gestión centralizada de políticas y analítica ([Gravitee](https://www.gravitee.io/platform/api-gateway)).

6. **Monitorear y Ajustar:**- Monitorear continuamente el uso, tasas de error y la salud del sistema; ajustar umbrales según sea necesario ([Knit.dev](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)).

7. **Transparencia:**- Documentar claramente las políticas de limitación y comunicar actualizaciones; proporcionar paneles de uso cuando sea posible.

**Ejemplo de Cubo de Tokens (Python):**```python
class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_checked = time.time()
    
    def allow_request(self):
        now = time.time()
        elapsed = now - self.last_checked
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_checked = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False
```
- [Knit.dev: Mejores Prácticas](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)

## Errores Comunes y Fallos

**Errores frecuentes:**- **Configuración Incorrecta de Límites:**- Muy bajo: Bloquea usuarios legítimos, afecta la experiencia.
  - Muy alto: No protege el backend, arriesgando caídas ([Guía de AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)).

- **Monitoreo Insuficiente:**- Sin analítica en tiempo real, el abuso o degradación puede pasar inadvertido.

- **Gestión de Errores Poco Clara:**- Respuestas `429` vagas o ausentes confunden a los consumidores de la API.

- **Falta de Documentación:**- No comunicar políticas de limitación genera frustración y fallos impredecibles.

- **Sin Guía de Reintento:**- Falta `Retry-After`, lo que produce tráfico innecesario y mal comportamiento del cliente.

- **Ignorar Sistemas Distribuidos:**- Contadores locales en entornos multinodo resultan en aplicación imprecisa ([Knit.dev](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)).

**Remedios:**- Pruebas de carga para calibrar umbrales.
- Usar contadores centralizados y atómicos.
- Incluir siempre info de límites en las respuestas.
- Documentar y comunicar límites y errores.
- Revisar y ajustar regularmente según uso real.

## Preguntas Frecuentes y Lecturas Adicionales

**Preguntas Frecuentes:**

**P1:**¿Qué sucede si se exceden los límites de limitación?  
**R:**La API retorna un error HTTP `429 Too Many Requests`, normalmente con encabezados indicando el periodo de espera. Los clientes deben esperar el enfriamiento o usar el valor de `Retry-After` antes de reintentar.  
- [RFC 6585, Sección 4](https://datatracker.ietf.org/doc/html/rfc6585#section-4)

**P2:**¿Cómo pueden los clientes evitar alcanzar los límites de limitación?  
**R:**Optimizar los patrones de solicitud (agrupando, usando caché), atender los encabezados de límite y realizar reintentos con backoff exponencial y jitter.  
- [Knit.dev: Estrategias de Reintento](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)

**P3:**¿Diferencia entre limitación y limitación de tasa?  
**R:**La limitación de tasa es la política que define los topes; la limitación es la aplicación—rechazar o demorar solicitudes para mantener la salud.

**P4:**¿Puede la limitación ser dinámica?  
**R:**Sí, la limitación dinámica adapta los límites según la carga en tiempo real o la hora del día, pero es más compleja de implementar.

**P5:**¿Cómo deben estructurarse las respuestas de error?  
**R:**Retornar HTTP `429`, con encabezados relevantes (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After`) y un mensaje claro en el cuerpo.

**Lecturas y Recursos Adicionales:**- [Limite solicitudes a sus APIs REST para mejor rendimiento en API Gateway – AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
- [Mejores Prácticas y Técnicas de Limitación de API – Blog Gravitee](https://www.gravitee.io/blog/api-throttling-best-practices)
- [¿Qué es Rate Limiting / API Throttling? – Explicativo en YouTube](https://www.youtube.com/watch?v=9CIjoWPwAhU)
- [¿Qué es la Limitación de API? – Glosario TIBCO](https://www.tibco.com/glossary/what-is-api-throttling)
- [Limitación de API – Glosario GetStream](https://getstream.io/glossary/api-throttling/)
- [Knit.dev: 10 Mejores Prácticas para Limitación y Limitación de API](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)

## Tabla Resumen: Algoritmos de Limitación

| Algoritmo           | ¿Permite ráfagas? | Límite estricto | Complejidad | Ejemplo de uso                |
|---------------------|:-----------------:|:---------------:|:-----------:|------------------------------|
| Cubo de tokens      | Sí                | No              | Media       | APIs de trading, servicios cloud |
| Cubo con fuga       | No                | Sí              | Media       | Envío de emails, web crawlers    |
| Ventana fija        | Sí (en borde)     | Sí              | Baja        | API de Twitter, APIs del clima   |
| Ventana deslizante  | Parcialmente      | Sí              | Alta        | APIs SaaS, microservicios        |
| Límite concurrente  | N/A               | Sí              | Baja        | Conexiones a BD, cargas GPU      |

## Escenario de Ejemplo: Limitación en Infraestructura de IA

Una empresa opera una API pública de reconocimiento de imágenes por IA:

- **Cubo de tokens**: 50 solicitudes permitidas en ráfaga, recarga a 5 solicitudes/seg.
- **Límite concurrente**: Solo 10 solicitudes en vuelo por cliente para evitar sobrecarga de GPU.
- **Limitación a nivel sistema**: Tope global para proteger todo el clúster de GPU.
- **Gestión de errores**: Al exceder límites se genera respuesta `429` con encabezado `Retry-After`; todo uso es registrado para análisis.

## Puntos Clave

- **La limitación**protege APIs, garantiza equidad y mantiene la confiabilidad en IA y otros servicios.
- Implemente gestión de errores robusta, comunicación transparente y monitoreo continuo.
- Elija el algoritmo y límites adecuados por caso de uso; los gateways de API ayudan a centralizar y escalar la aplicación.

**Para guías más detalladas y ejemplos de código, consulte la [Guía de Limitación de API Gateway de AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) y las [Mejores Prácticas de Limitación de API de Gravitee](https://www.gravitee.io/blog/api-throttling-best-practices).**Este glosario se basa en documentación y guías de mejores prácticas de la industria de AWS, Gravitee, Knit.dev y más. Para una introducción en video, vea: [¿Qué es Rate Limiting / API Throttling? (YouTube)](https://www.youtube.com/watch?v=9CIjoWPwAhU)