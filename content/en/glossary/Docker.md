---
title: "Docker"
date: 2025-11-25
lastmod: 2025-12-05
translationKey: "docker"
description: "Learn about Docker, an open-source platform for packaging, shipping, and running applications in lightweight, portable containers. Understand its architecture, benefits, and use cases."
keywords: ["Docker", "containers", "containerization", "microservices", "Kubernetes"]
category: "AI Infrastructure & Deployment"
type: "glossary"
draft: false
---
## What is Docker?

Docker is an open-source platform that enables developers and system administrators to build, package, ship, and run applications as containers. Containers are lightweight, standalone, and executable units that encapsulate everything needed to run an application: code, runtime, system tools, libraries, and settings. This encapsulation ensures that software behaves identically across different environments—development, testing, staging, and production.

Docker’s innovation lies in providing a standardized way to develop, distribute, and deploy applications, eliminating the notorious “it works on my machine” problem. Docker containers are portable, consistent, and can run on any infrastructure that supports Docker, including developer laptops, on-premises data centers, and public clouds such as AWS, Azure, or Google Cloud.

**Further reading:**
- [Docker Official Overview](https://docs.docker.com/get-started/docker-overview/)
- [Docker Curriculum Introduction](https://docker-curriculum.com#what-is-docker-)

## Why Containerization Matters

Traditional deployments often encounter environmental inconsistencies. For instance, a web application might work on a developer’s machine, but fail in a production environment due to differences in software versions, configurations, or missing dependencies.

[Containerization](/en/glossary/containerization/) solves this by packaging everything an application needs into a single, isolated unit—a container. Docker leverages Linux kernel features, such as namespaces and cgroups, to provide process isolation, resource allocation, and security boundaries. This model allows:

- **Consistent environments:** The same container image runs identically everywhere.
- **Efficient resource use:** Containers share the host OS kernel, reducing overhead.
- **Rapid deployment and scaling:** Containers start in seconds and are easier to replicate or scale.
- **Simplified management:** Containers can be started, stopped, or replaced quickly, streamlining deployment and operational processes.
## How Docker Works

Docker relies on operating system–level virtualization to create isolated containers. Each container is an isolated process running on the host, sharing the host OS kernel but possessing its own filesystem, network stack, and process space.

**Operational workflow:**
1. **Build:** Use a Dockerfile—a text file defining the application environment, dependencies, and build steps—to create a Docker image.
2. **Ship:** Store and distribute the image via a container registry (such as Docker Hub or a private registry).
3. **Run:** Pull the image from the registry and start a container from it, anywhere Docker is supported.

**Example:**
- Building a web application image with a Dockerfile, pushing it to Docker Hub, and running it on a cloud VM.
## Docker Architecture

Docker’s architecture is based on a client-server model, with several key components working together:

### 1. Docker Daemon (`dockerd`)
- The Docker daemon is a background service managing Docker objects (images, containers, networks, volumes).
- Listens for Docker API requests and performs operations accordingly.
- Runs as a system process and requires root privileges or appropriate user group membership.
### 2. Docker Client (`docker`)
- The primary user interface for Docker.
- Command-line tool (`docker`) to issue commands like `docker build`, `docker run`, `docker ps`.
- Communicates with the Docker daemon via a REST API over a UNIX socket or network.

### 3. Docker Registries
- Storage and distribution systems for Docker images.
- **Docker Hub** is the default public registry, with millions of images available.
- Organizations can run private registries for internal use.

**See:**  
[Docker Registry Docs](https://docs.docker.com/registry/)

### 4. Docker Images
- Read-only templates with instructions for creating containers.
- Built in layers; each Dockerfile command (RUN, COPY, etc.) creates a new layer.
- Images can inherit from other images, enabling modular builds.

**Details:**  
[What is a Docker Image? (Official Docs)](https://docs.docker.com/get-started/overview/)

### 5. Docker Containers
- Runnable instances of images.
- Isolated from the host and other containers but can communicate via Docker networks.
- Ephemeral by default, but can use volumes for persistent data.

### 6. Docker Compose
- A tool for defining and managing multi-container applications using a YAML file (`docker-compose.yml`).
- Enables declarative configuration of services, networks, and volumes.
### 7. Docker Networks and Volumes
- **Networks:** Virtual networks for container communication and isolation (bridge, host, overlay, etc.).
- **Volumes:** Persistent storage for container data, surviving restarts and container destruction.

**Diagram:**  
[See Docker Architecture Diagram](https://docs.docker.com/get-started/overview/#the-docker-architecture)

## Key Technical Terms Defined

- **Container:** Isolated process encapsulating an application and its dependencies. Uses kernel features such as namespaces for isolation and cgroups for resource management. [What is a Container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- **Docker Image:** Read-only layered template for creating containers.
- **Dockerfile:** Script with instructions to build a Docker image.
- **Docker Daemon (`dockerd`):** Service managing Docker objects.
- **Docker Client (`docker`):** CLI or API to interact with the Docker daemon.
- **Registry:** Repository for storing and distributing images.
- **Docker Compose:** Tool for orchestrating multi-container applications.
- **Namespace:** Linux kernel feature for process isolation.
- **Volume:** Persistent storage mounted into containers.
- **Network:** Virtual network for container-to-container and container-to-host communication.

## Benefits of Docker

Docker containers deliver numerous advantages over traditional deployment models and virtual machines:

### 1. Portability
- Containers run the same way across different OSes and infrastructure.
- Move workloads seamlessly between local, on-premises, and cloud environments.

### 2. Speed
- Containers start in milliseconds or seconds (no OS boot).
- Quicker build, test, and deploy cycles.

### 3. Resource Utilization
- Containers share the host OS kernel, reducing overhead.
- High application density per host.

### 4. Isolation and Security
- Containers isolate processes, reducing risk of conflicts and improving security posture.
- Linux namespaces and cgroups enforce boundaries.

### 5. Scalability and Flexibility
- Scale applications by starting/stopping containers.
- Supports microservices and dynamic deployment.

### 6. Consistency and Reproducibility
- Identical environments from development to production.

### 7. Integration with CI/CD
- Automates build, test, and deploy steps in modern DevOps workflows.
## Docker vs. Virtual Machines (VMs)

| Feature                | Docker Containers                    | Virtual Machines (VMs)             |
|------------------------|--------------------------------------|------------------------------------|
| Isolation              | OS-level (namespaces, cgroups)       | Hardware-level (hypervisor)        |
| Resource Usage         | Lightweight, minimal overhead        | Each VM runs full guest OS         |
| Startup Time           | Seconds or less                      | Minutes                            |
| Portability            | Highly portable                      | Less portable (hypervisor-specific)|
| Scalability            | Easily scalable, low overhead        | Less scalable, higher overhead     |
| Density (per host)     | High                                 | Lower                              |

**Additional insights:**
- Containers can run on VMs, combining the benefits of both in cloud environments.
- Containers use the host's kernel, so they are less suitable for running different OSes than the host.

**Further reading:**  
[Containers vs. VMs (Docker Docs)](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms)

## Common Use Cases for Docker

### 1. Microservices Architectures
- Decompose monolithic applications into independently deployable services.
- Each microservice runs in its own container, enabling independent scaling and updates.

### 2. Continuous Integration / Continuous Deployment (CI/CD)
- Standardize build/test environments for automation pipelines.
- Minimize environment drift and deployment errors.

### 3. Cloud-Native Application Development
- Simplify multi-cloud or hybrid deployments.
- Enable rapid prototyping and release cycles.

### 4. Big Data and Analytics
- Package data processing jobs and analytics tools for reproducible runs.
- Scale compute resources dynamically.

### 5. Dev/Test Environments
- Provision disposable, consistent environments for developers and testers.
- Accelerate onboarding and troubleshooting.

### 6. Web Application Deployment
- Deploy web servers, APIs, and frontends as isolated containers.
- Enable rapid scaling and consistent performance.

### 7. Containers as a Service (CaaS)
- Provide managed container platforms for teams or customers.

**Real-world examples:**
- [Netflix](https://netflixtechblog.com/), [Uber](https://eng.uber.com/), and [Airbnb](https://medium.com/airbnb-engineering) leverage Docker for microservices and scalable infrastructure.
- Enterprises deploy machine learning models using containers for reproducibility and scalability.

## Getting Started with Docker

### 1. Install Docker

- Install Docker Desktop for Windows, macOS, or Linux.
- Official installation guide: [Get Docker](https://docs.docker.com/get-docker/)

### 2. Create a Dockerfile

A Dockerfile defines the build steps for your image.

**Example:**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### 3. Build the Image

Terminal command:
```bash
docker build -t my-python-app .
```

### 4. Run a Container

```bash
docker run -d -p 5000:5000 my-python-app
```
- `-d`: detached mode
- `-p`: maps host port to container port

### 5. Push/Pull Images

Push:
```bash
docker push username/my-python-app
```
Pull:
```bash
docker pull username/my-python-app
```

### 6. Use Docker Compose

**Example `docker-compose.yml`:**
```yaml
version: '3'
services:
  web:
    image: my-python-app
    ports:
      - "5000:5000"
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: example
```

Start all services:
```bash
docker-compose up
```

**Hands-on tutorial:**  
[Docker Curriculum: Webapps with Docker](https://docker-curriculum.com#webapps-with-docker)

## Best Practices

- **Minimal images:** Use official/minimal base images, remove unnecessary files.
- **Multi-stage builds:** Separate build and runtime dependencies to keep images lean.
- **Avoid root:** Use non-root users for better security.
- **Tag images:** Employ semantic versioning and clear tags.
- **Environment variables:** Use for configuration, not hardcoded [secrets](/en/glossary/environment-variables--secrets-/).
- **Monitor/log:** Centralize logs and monitor health.
- **Update images:** Regularly update images and dependencies to patch vulnerabilities.
- **Volumes:** Use for persistent data.

**Further reading:**  
[Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## Docker in AI Infrastructure & Deployment

- **Model Packaging:** Containers encapsulate machine learning models and their dependencies for reproducible deployment.
- **Resource Efficiency:** Run multiple data pipelines in isolated containers on the same hardware.
- **Scalable Serving:** Deploy AI inference services as scalable, independent containers.
- **CI/CD Integration:** Automate testing, validation, and deployment with containerized stages.

**Example:**  
A data scientist builds a Docker image with a trained model and API, then deploys it to Kubernetes for scalable inference.

**Case studies:**  
[Docker for Machine Learning](https://www.docker.com/blog/tag/machine-learning/)

## Advanced Topics

### Container Orchestration

- **Kubernetes** and **Docker Swarm:** Tools for managing deployment, scaling, and operation of containers across clusters.
- **Service discovery, load balancing, auto-scaling, self-healing** are handled by orchestrators.

**Learn more:**  
[Kubernetes Documentation](https://kubernetes.io/docs/)

### Security Considerations

- Use trusted images (official or verified publishers).
- Regularly scan images for vulnerabilities ([Docker Scout](https://docs.docker.com/scout/)).
- Principle of Least Privilege: restrict container permissions.
- Isolate sensitive workloads with dedicated hosts.

### Networking & Service Discovery

- **Bridge:** Default network for single-host containers.
- **Host:** Shares host’s network stack.
- **Overlay:** Enables multi-host communication (used by orchestrators).
## Frequently Used Docker Commands

- `docker run` — Start a new container
- `docker ps` — List running containers
- `docker images` — List images
- `docker build` — Build image from Dockerfile
- `docker pull` — Download image from registry
- `docker push` — Upload image to registry
- `docker exec` — Run command in running container
- `docker logs` — Fetch container logs
- `docker stop` — Stop running container
- `docker rm` — Remove container

**Complete CLI reference:**  
[Docker CLI Docs](https://docs.docker.com/engine/reference/commandline/cli/)

## Glossary: Key Docker Terms

| Term                  | Definition                                                                                   |
|-----------------------|---------------------------------------------------------------------------------------------|
| Container             | Isolated process running an application and its dependencies.                               |
| Image                 | Read-only template with instructions for container creation.                                |
| Dockerfile            | File defining build steps for a Docker image.                                               |
| Registry              | Service for storing and distributing images (e.g., Docker Hub).                             |
| Docker Daemon         | Background process managing Docker objects.                                                 |
| Docker Client         | CLI/API interface to Docker daemon.                                                         |
| Volume                | Persistent storage for containers.                                                          |
| Network               | Virtual networking for containers.                                                          |
| Compose               | Tool for defining/running multi-container applications.                                     |
| Orchestration         | Automation of deployment, scaling, and management of containers.                            |
| Namespace             | Linux kernel feature for resource/process isolation.                                        |
| cgroup                | Linux kernel feature for resource allocation/control.                                       |
| Overlay Network       | Virtual network enabling multi-host container communication.                                |
| Multi-stage Build     | Dockerfile technique to separate build/runtime dependencies.                                |
| Docker Swarm          | Native clustering/orchestration tool for Docker.                                            |

## Further Resources

- [Docker Official Documentation](https://docs.docker.com/get-started/docker-overview/)
- [Docker: What is a Container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Docker Curriculum (Beginner to Advanced)](https://docker-curriculum.com)
- [AWS: What is Docker?](https://aws.amazon.com/docker/)
- [Oracle: What is Docker?](https://www.oracle.com/cloud/cloud-native/container-registry/what-is-docker/)
- [GeeksforGeeks: Containerization using Docker](https://www.geeksforgeeks.org/blogs/containerization-using-docker/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Docker Hub](https://hub.docker.com)
- [Docker Networking](https://docs.docker.com/network/)

**Summary:**  
Docker standardizes application packaging into containers, enabling rapid, consistent, and portable deployment across diverse environments. Its lightweight design, resource efficiency, and rich ecosystem make it foundational in modern software development, cloud operations, and AI infrastructure. Mastery of Docker architecture, best practices, and integration with orchestration and CI/CD systems unlocks efficient, scalable, and reliable software delivery.

**Authoritative References:**
- [Docker Docs: What is a Container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Docker Curriculum](https://docker-curriculum.com)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Kubernetes Docs](https://kubernetes.io/docs/)
