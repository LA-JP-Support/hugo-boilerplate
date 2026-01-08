+++
title = "Docker"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "docker"
description = "Aprende sobre Docker, una plataforma de código abierto para empaquetar, enviar y ejecutar aplicaciones en contenedores ligeros y portátiles. Comprende su arquitectura, beneficios y casos de uso."
keywords = ["Docker", "contenedores", "contenedorización", "microservicios", "Kubernetes"]
category = "Infraestructura de IA y Despliegue"
type = "glossary"
draft = false
url = "/internal/glossary/Docker/"

+++
## ¿Qué es Docker?

Docker es una plataforma de código abierto que permite a desarrolladores y administradores de sistemas construir, empaquetar, enviar y ejecutar aplicaciones como contenedores. Los contenedores son unidades ligeras, autónomas y ejecutables que encapsulan todo lo necesario para ejecutar una aplicación: código, entorno de ejecución, herramientas del sistema, bibliotecas y configuraciones. Esta encapsulación asegura que el software se comporte de manera idéntica en diferentes entornos: desarrollo, pruebas, preproducción y producción.

La innovación de Docker radica en proporcionar una forma estandarizada de desarrollar, distribuir y desplegar aplicaciones, eliminando el famoso problema de “funciona en mi máquina”. Los contenedores Docker son portátiles, consistentes y pueden ejecutarse en cualquier infraestructura que soporte Docker, incluyendo laptops de desarrolladores, centros de datos locales y nubes públicas como AWS, Azure o Google Cloud.

**Lecturas adicionales:**- [Descripción general oficial de Docker](https://docs.docker.com/get-started/docker-overview/)
- [Introducción al currículo Docker](https://docker-curriculum.com#what-is-docker-)

## Por qué es importante la contenedorización

Los despliegues tradicionales suelen enfrentar inconsistencias ambientales. Por ejemplo, una aplicación web puede funcionar en la máquina de un desarrollador pero fallar en producción debido a diferencias en versiones de software, configuraciones o dependencias faltantes.

[La contenedorización](/en/glossary/containerization/) resuelve esto al empaquetar todo lo que una aplicación necesita en una sola unidad aislada: un contenedor. Docker aprovecha funcionalidades del kernel de Linux, como namespaces y cgroups, para proporcionar aislamiento de procesos, asignación de recursos y límites de seguridad. Este modelo permite:

- **Entornos consistentes:**La misma imagen de contenedor se ejecuta de forma idéntica en todas partes.
- **Uso eficiente de recursos:**Los contenedores comparten el kernel del sistema anfitrión, reduciendo la sobrecarga.
- **Despliegue y escalado rápido:**Los contenedores se inician en segundos y son más fáciles de replicar o escalar.
- **Gestión simplificada:**Los contenedores pueden iniciarse, detenerse o reemplazarse rápidamente, agilizando los procesos de despliegue y operación.
## Cómo funciona Docker

Docker se basa en la virtualización a nivel de sistema operativo para crear contenedores aislados. Cada contenedor es un proceso aislado que se ejecuta en el anfitrión, compartiendo el kernel pero con su propio sistema de archivos, pila de red y espacio de procesos.

**Flujo operativo:**1. **Construir:**Usa un Dockerfile—un archivo de texto que define el entorno, dependencias y pasos de construcción—para crear una imagen Docker.
2. **Enviar:**Almacena y distribuye la imagen mediante un registro de contenedores (como Docker Hub o un registro privado).
3. **Ejecutar:**Descarga la imagen del registro e inicia un contenedor a partir de ella, en cualquier lugar donde Docker esté soportado.

**Ejemplo:**- Construir una imagen de aplicación web con un Dockerfile, subirla a Docker Hub y ejecutarla en una VM en la nube.
## Arquitectura de Docker

La arquitectura de Docker se basa en un modelo cliente-servidor, con varios componentes clave que trabajan en conjunto:

### 1. Docker Daemon (`dockerd`)
- El demonio Docker es un servicio en segundo plano que gestiona objetos Docker (imágenes, contenedores, redes, volúmenes).
- Escucha solicitudes de la API de Docker y ejecuta operaciones según corresponda.
- Se ejecuta como un proceso del sistema y requiere privilegios de root o pertenencia a un grupo de usuarios adecuado.
### 2. Cliente Docker (`docker`)
- La interfaz principal de usuario para Docker.
- Herramienta de línea de comandos (`docker`) para emitir comandos como `docker build`, `docker run`, `docker ps`.
- Se comunica con el demonio Docker mediante una API REST sobre un socket UNIX o red.

### 3. Registros Docker
- Sistemas de almacenamiento y distribución de imágenes Docker.
- **Docker Hub**es el registro público predeterminado, con millones de imágenes disponibles.
- Las organizaciones pueden operar registros privados para uso interno.

**Ver:**[Documentación de Docker Registry](https://docs.docker.com/registry/)

### 4. Imágenes Docker
- Plantillas de solo lectura con instrucciones para crear contenedores.
- Construidas por capas; cada comando del Dockerfile (RUN, COPY, etc.) crea una nueva capa.
- Las imágenes pueden heredar de otras imágenes, permitiendo construcciones modulares.

**Detalles:**[¿Qué es una imagen Docker? (Documentación oficial)](https://docs.docker.com/get-started/overview/)

### 5. Contenedores Docker
- Instancias ejecutables de imágenes.
- Aislados del anfitrión y de otros contenedores, pero pueden comunicarse mediante redes Docker.
- Efímeros por defecto, pero pueden usar volúmenes para datos persistentes.

### 6. Docker Compose
- Herramienta para definir y gestionar aplicaciones multi-contenedor usando un archivo YAML (`docker-compose.yml`).
- Permite configuración declarativa de servicios, redes y volúmenes.
### 7. Redes y volúmenes Docker
- **Redes:**Redes virtuales para la comunicación e aislamiento de contenedores (bridge, host, overlay, etc.).
- **Volúmenes:**Almacenamiento persistente para datos de contenedores, sobreviviendo reinicios y destrucción del contenedor.

**Diagrama:**[Ver diagrama de arquitectura Docker](https://docs.docker.com/get-started/overview/#the-docker-architecture)

## Términos técnicos clave definidos

- **Contenedor:**Proceso aislado que encapsula una aplicación y sus dependencias. Usa características del kernel como namespaces para aislamiento y cgroups para gestión de recursos. [¿Qué es un contenedor?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- **Imagen Docker:**Plantilla en capas y de solo lectura para crear contenedores.
- **Dockerfile:**Script con instrucciones para construir una imagen Docker.
- **Docker Daemon (`dockerd`):**Servicio que gestiona objetos Docker.
- **Cliente Docker (`docker`):**CLI o API para interactuar con el demonio Docker.
- **Registro:**Repositorio para almacenar y distribuir imágenes.
- **Docker Compose:**Herramienta para orquestar aplicaciones multi-contenedor.
- **Namespace:**Funcionalidad del kernel Linux para aislamiento de procesos.
- **Volumen:**Almacenamiento persistente montado en contenedores.
- **Red:**Red virtual para comunicación entre contenedores y con el host.

## Beneficios de Docker

Los contenedores Docker ofrecen numerosas ventajas sobre los modelos de despliegue tradicionales y las máquinas virtuales:

### 1. Portabilidad
- Los contenedores se ejecutan igual en distintos sistemas operativos e infraestructuras.
- Mueve cargas de trabajo sin problemas entre entornos locales, on-premise y en la nube.

### 2. Velocidad
- Los contenedores se inician en milisegundos o segundos (sin arranque de SO).
- Ciclos de construcción, prueba y despliegue más rápidos.

### 3. Utilización de recursos
- Los contenedores comparten el kernel del anfitrión, reduciendo la sobrecarga.
- Alta densidad de aplicaciones por anfitrión.

### 4. Aislamiento y seguridad
- Los contenedores aíslan procesos, reduciendo riesgos de conflictos y mejorando la seguridad.
- Namespaces y cgroups de Linux aplican límites y separación.

### 5. Escalabilidad y flexibilidad
- Escala aplicaciones iniciando/deteniendo contenedores.
- Soporte para microservicios y despliegues dinámicos.

### 6. Consistencia y reproducibilidad
- Entornos idénticos desde desarrollo hasta producción.

### 7. Integración con CI/CD
- Automatiza etapas de construcción, prueba y despliegue en flujos DevOps modernos.
## Docker vs. Máquinas Virtuales (VMs)

| Característica          | Contenedores Docker                  | Máquinas Virtuales (VMs)           |
|------------------------|--------------------------------------|------------------------------------|
| Aislamiento            | A nivel de SO (namespaces, cgroups)  | A nivel de hardware (hipervisor)   |
| Uso de recursos        | Ligeros, mínima sobrecarga           | Cada VM ejecuta SO propio completo |
| Tiempo de arranque     | Segundos o menos                     | Minutos                            |
| Portabilidad           | Altamente portátiles                 | Menos portátiles (depende del hipervisor)|
| Escalabilidad          | Fácilmente escalables, baja sobrecarga| Menos escalables, mayor sobrecarga |
| Densidad (por host)    | Alta                                 | Baja                               |

**Notas adicionales:**- Los contenedores pueden ejecutarse en VMs, combinando beneficios de ambos en entornos cloud.
- Los contenedores usan el kernel del anfitrión, por lo que no son adecuados para ejecutar SOs diferentes al del anfitrión.

**Lecturas adicionales:**[Contenedores vs. VMs (Documentación Docker)](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms)

## Casos de uso comunes para Docker

### 1. Arquitecturas de microservicios
- Descompone aplicaciones monolíticas en servicios desplegables de forma independiente.
- Cada microservicio se ejecuta en su propio contenedor, permitiendo escalado y actualizaciones independientes.

### 2. Integración y despliegue continuos (CI/CD)
- Estandariza los entornos de construcción/pruebas para pipelines de automatización.
- Minimiza diferencias de entorno y errores de despliegue.

### 3. Desarrollo de aplicaciones cloud-native
- Simplifica despliegues multi-nube o híbridos.
- Facilita la creación rápida de prototipos y ciclos de lanzamiento.

### 4. Big Data y analítica
- Empaqueta trabajos de procesamiento de datos y herramientas analíticas para ejecuciones reproducibles.
- Escala recursos de cómputo dinámicamente.

### 5. Entornos de desarrollo/pruebas
- Provisión de entornos desechables y consistentes para desarrolladores y testers.
- Acelera la incorporación y resolución de problemas.

### 6. Despliegue de aplicaciones web
- Despliega servidores web, APIs y frontends como contenedores aislados.
- Permite escalado rápido y desempeño consistente.

### 7. Contenedores como servicio (CaaS)
- Plataformas gestionadas de contenedores para equipos o clientes.

**Ejemplos reales:**- [Netflix](https://netflixtechblog.com/), [Uber](https://eng.uber.com/) y [Airbnb](https://medium.com/airbnb-engineering) usan Docker para microservicios e infraestructura escalable.
- Empresas despliegan modelos de machine learning usando contenedores para reproducibilidad y escalabilidad.

## Primeros pasos con Docker

### 1. Instalar Docker

- Instala Docker Desktop para Windows, macOS o Linux.
- Guía oficial de instalación: [Obtener Docker](https://docs.docker.com/get-docker/)

### 2. Crear un Dockerfile

Un Dockerfile define los pasos de construcción para tu imagen.

**Ejemplo:**```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### 3. Construir la imagen

Comando en terminal:
```bash
docker build -t mi-app-python .
```

### 4. Ejecutar un contenedor

```bash
docker run -d -p 5000:5000 mi-app-python
```
- `-d`: modo detached
- `-p`: mapea puerto del host al contenedor

### 5. Subir/Descargar imágenes

Subir:
```bash
docker push usuario/mi-app-python
```
Descargar:
```bash
docker pull usuario/mi-app-python
```

### 6. Usar Docker Compose

**Ejemplo `docker-compose.yml`:**```yaml
version: '3'
services:
  web:
    image: mi-app-python
    ports:
      - "5000:5000"
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: ejemplo
```

Iniciar todos los servicios:
```bash
docker-compose up
```

**Tutorial práctico:**[Currículo Docker: Aplicaciones web con Docker](https://docker-curriculum.com#webapps-with-docker)

## Buenas prácticas

- **Imágenes mínimas:**Usa imágenes base oficiales/mínimas, elimina archivos innecesarios.
- **Construcciones multi-etapa:**Separa dependencias de compilación y de ejecución para mantener imágenes livianas.
- **Evita root:**Usa usuarios sin privilegios para mayor seguridad.
- **Etiqueta imágenes:**Emplea versionado semántico y etiquetas claras.
- **Variables de entorno:**Úsalas para configuración, no para [secretos](/en/glossary/environment-variables--secrets-/) codificados.
- **Monitorea/registra:**Centraliza logs y monitoriza salud.
- **Actualiza imágenes:**Actualiza imágenes y dependencias con regularidad para corregir vulnerabilidades.
- **Volúmenes:**Úsalos para datos persistentes.

**Lecturas adicionales:**[Buenas prácticas Docker](https://docs.docker.com/develop/dev-best-practices/)

## Docker en Infraestructura de IA y Despliegue

- **Empaquetado de modelos:**Los contenedores encapsulan modelos de machine learning y sus dependencias para un despliegue reproducible.
- **Eficiencia de recursos:**Ejecuta múltiples pipelines de datos en contenedores aislados en el mismo hardware.
- **Servicio escalable:**Despliega servicios de inferencia de IA como contenedores escalables e independientes.
- **Integración CI/CD:**Automatiza pruebas, validación y despliegue con etapas contenedorizadas.

**Ejemplo:**Un científico de datos construye una imagen Docker con un modelo entrenado y una API, luego la despliega en Kubernetes para inferencia escalable.

**Casos de estudio:**[Docker para Machine Learning](https://www.docker.com/blog/tag/machine-learning/)

## Temas avanzados

### Orquestación de contenedores

- **Kubernetes**y **Docker Swarm:**Herramientas para gestionar el despliegue, escalado y operación de contenedores en clústeres.
- **Descubrimiento de servicios, balanceo de carga, auto-escalado, auto-recuperación**son gestionados por los orquestadores.

**Más información:**[Documentación de Kubernetes](https://kubernetes.io/docs/)

### Consideraciones de seguridad

- Usa imágenes de confianza (oficiales o de editores verificados).
- Escanea imágenes regularmente buscando vulnerabilidades ([Docker Scout](https://docs.docker.com/scout/)).
- Principio de mínimo privilegio: restringe permisos de contenedores.
- Aísla cargas sensibles en hosts dedicados.

### Redes y descubrimiento de servicios

- **Bridge:**Red predeterminada para contenedores en un solo host.
- **Host:**Comparte la pila de red del anfitrión.
- **Overlay:**Permite comunicación multi-host (usado por orquestadores).
## Comandos Docker más usados

- `docker run` — Iniciar un nuevo contenedor
- `docker ps` — Listar contenedores en ejecución
- `docker images` — Listar imágenes
- `docker build` — Construir imagen desde Dockerfile
- `docker pull` — Descargar imagen desde registro
- `docker push` — Subir imagen a registro
- `docker exec` — Ejecutar comando en contenedor en ejecución
- `docker logs` — Obtener logs del contenedor
- `docker stop` — Detener contenedor en ejecución
- `docker rm` — Eliminar contenedor

**Referencia completa CLI:**[Documentación CLI Docker](https://docs.docker.com/engine/reference/commandline/cli/)


## Más recursos

- [Documentación oficial de Docker](https://docs.docker.com/get-started/docker-overview/)
- [Docker: ¿Qué es un contenedor?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Currículo Docker (Principiante a Avanzado)](https://docker-curriculum.com)
- [AWS: ¿Qué es Docker?](https://aws.amazon.com/docker/)
- [Oracle: ¿Qué es Docker?](https://www.oracle.com/cloud/cloud-native/container-registry/what-is-docker/)
- [GeeksforGeeks: Contenerización usando Docker](https://www.geeksforgeeks.org/blogs/containerization-using-docker/)
- [Documentación Docker Compose](https://docs.docker.com/compose/)
- [Documentación Kubernetes](https://kubernetes.io/docs/)
- [Referencia CLI Docker](https://docs.docker.com/engine/reference/commandline/cli/)
- [Buenas prácticas Docker](https://docs.docker.com/develop/dev-best-practices/)
- [Docker Hub](https://hub.docker.com)
- [Redes Docker](https://docs.docker.com/network/)

**Resumen:**Docker estandariza el empaquetado de aplicaciones en contenedores, permitiendo un despliegue rápido, consistente y portátil en entornos diversos. Su diseño ligero, eficiencia de recursos y rico ecosistema lo hacen fundamental en el desarrollo moderno, operaciones cloud e infraestructura de IA. Dominar la arquitectura Docker, las buenas prácticas y la integración con orquestación y sistemas CI/CD desbloquea una entrega de software eficiente, escalable y confiable.

**Referencias autorizadas:**- [Documentación Docker: ¿Qué es un contenedor?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Docker Curriculum](https://docker-curriculum.com)
- [Buenas prácticas Docker](https://docs.docker.com/develop/dev-best-practices/)
- [Documentación Kubernetes](https://kubernetes.io/docs/)