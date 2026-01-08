+++
title = "Chroma"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "chroma"
description = "Explora Chroma, una base de datos vectorial de código abierto para aplicaciones nativas de IA. Aprende sobre sus conceptos clave, arquitectura, casos de uso como RAG y búsqueda semántica, y compárala con alternativas."
keywords = ["Chroma", "base de datos vectorial", "embeddings", "aplicaciones nativas de IA", "búsqueda semántica"]
category = "General"
type = "glossary"
draft = false
url = "/internal/glossary/Chroma/"

+++
## ¿Qué es Chroma?

**Chroma**es una base de datos vectorial (de embeddings) de código abierto diseñada para aplicaciones nativas de IA, especialmente aquellas que utilizan modelos de lenguaje grandes (LLMs) e IA multimodal. A diferencia de las bases de datos tradicionales, Chroma está especializada en almacenar, indexar y recuperar embeddings vectoriales de alta dimensión: representaciones numéricas de texto, imágenes y otros datos no estructurados.

La misión principal de Chroma es facilitar a desarrolladores y organizaciones la incorporación de búsqueda semántica, recomendaciones, RAG y capacidades nativas de IA en sus aplicaciones, con una configuración mínima y máxima flexibilidad. Ofrece:

- Soporte nativo para almacenar y buscar embeddings junto con documentos y metadatos
- Búsqueda rápida de vecinos más cercanos aproximados (ANN) mediante indexación [HNSW](/es/glossary/hnsw--hierarchical-navigable-small-world-/)
- Soporte multimodal (texto, imágenes y más)
- Consultas híbridas: búsqueda semántica + por palabras clave, además de filtrado por metadatos
- APIs amigables para desarrolladores (Python, JS) e integraciones nativas con frameworks como LangChain y LlamaIndex
- Licencia Apache 2.0 de código abierto
- Opciones tanto autogestionadas como en la nube administrada
## Conceptos clave

### Embeddings

Los **embeddings**son vectores densos que codifican el significado semántico de los datos. Por ejemplo, una oración, imagen o fragmento de audio puede transformarse en un vector de cientos o miles de números. Los puntos de datos similares en significado tendrán embeddings similares (es decir, estarán “cerca” en el espacio vectorial), aunque los datos originales sean muy diferentes.

Chroma soporta embeddings generados por modelos populares, incluyendo:
- Modelos de OpenAI para embeddings de texto (por ejemplo, `text-embedding-3-small`)
- Modelos de HuggingFace (por ejemplo, `all-MiniLM-L6-v2`)
- Cohere, OpenCLIP y embeddings personalizados

Esto es fundamental para la búsqueda semántica, recomendaciones y generación aumentada por recuperación.
### Colecciones

Una **colección**en Chroma es un agrupamiento lógico de documentos, embeddings y sus metadatos asociados. Cada colección tiene su propia configuración, incluyendo:
- Función/modelo de embedding
- Ubicación de almacenamiento (en memoria o persistente)
- Configuraciones personalizadas opcionales para rendimiento o filtrado

Esto permite que aplicaciones o proyectos de IA separados funcionen en paralelo, cada uno ajustado a sus necesidades específicas.
### Metadatos y búsqueda híbrida

Chroma permite asociar metadatos arbitrarios clave-valor con cada documento o vector. Esto habilita la **búsqueda híbrida**: filtrar resultados por metadatos (por ejemplo, autor, fecha, etiquetas) y ordenarlos por similitud vectorial.

Los operadores incluyen:
- Igualdad y desigualdad
- Consultas por rango (`$gt`, `$lt`)
- Pertenencia a conjunto (`$in`)
- Combinaciones lógicas (`$and`, `$or`)
## ¿Cómo funciona Chroma?

### Indexado vectorial y búsqueda por similitud

Chroma utiliza grafos **Hierarchical Navigable Small World (HNSW)**para una búsqueda rápida y aproximada de los vecinos más cercanos (ANN). HNSW es un algoritmo de última generación para búsqueda de similitud en vectores de alta dimensión, equilibrando exactitud (recall) y velocidad, y escalando a millones de vectores.

Propiedades clave:
- Tiempo de búsqueda sublineal para grandes volúmenes de datos
- Alta exactitud/recall (configurable)
- Soporte para inserciones dinámicas y eliminación eficiente
### Almacenamiento de documentos y metadatos

Cada entrada en Chroma incluye:
- El documento/contenido original (texto, URI de imagen, etc.)
- El embedding vectorial
- Metadatos asociados (clave-valor arbitrario en JSON)

Esto permite consultas híbridas y búsqueda semántica completa.

Chroma puede almacenar datos:
- En memoria (más rápido, no persistente)
- En disco (SQLite para metadatos, archivos binarios para vectores)
- En Chroma Cloud (totalmente administrado)
### APIs y librerías cliente

Chroma proporciona una API minimalista e intuitiva con cuatro operaciones principales:
- **Add:**Inserta documentos (opcionalmente con embeddings y metadatos)
- **Update:**Modifica entradas almacenadas
- **Delete:**Elimina entradas
- **Query:**Recupera documentos similares mediante búsqueda vectorial, con filtros de metadatos opcionales

Existen librerías cliente para:
- **Python:**[chromadb](https://pypi.org/project/chromadb/)
- **JavaScript/TypeScript:**[Chroma Node.js Client](https://github.com/chroma-core/chroma/tree/main/clients/js)

Chroma se integra de forma nativa con frameworks como:
- **LangChain**([guía de integración](https://docs.langchain.com/oss/python/integrations/providers/chroma))
- **LlamaIndex**## Arquitectura y Despliegue

### Código abierto (autogestionado)

Chroma puede ejecutarse localmente o en tu propia infraestructura en tres modos:
- **En memoria:**Rápido, efímero, ideal para prototipos o pruebas
- **Persistente:**Almacena datos en disco (SQLite + archivos binarios de vectores), adecuado para local/producción pequeña
- **Cliente-servidor:**Ejecuta como un servidor independiente, conecta mediante API HTTP (soporta multiusuario, multiproceso)

**Ejemplo de inicio de servidor:**```shell
chroma run --path ./db --port 8000
```
**Cliente Python:**```python
import chromadb
client = chromadb.HttpClient(host="localhost", port=8000)
```
### Chroma Cloud (sin servidor)

**Chroma Cloud**es una implementación totalmente administrada y sin servidor. Se encarga de:
- Escalado elástico
- Respaldo automático y [alta disponibilidad](/es/glossary/high-availability--ha-/)
- Mantenimiento y monitoreo

**Ejemplo de conexión:**```python
import chromadb
client = chromadb.HttpClient(
    host="api.trychroma.com",
    headers={"Authorization": f"Bearer {CHROMA_API_KEY}"}
)
```
## Configuración e Integración

### Instalación

**Python:**```bash
pip install chromadb
```
Para integración con LangChain:
```bash
pip install langchain-chroma
```
### Ejemplo básico de uso

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("documents")

collection.add(
    documents=[
        "La inteligencia artificial está transformando el diagnóstico en salud",
        "Modelos de aprendizaje automático predicen resultados de pacientes con mayor precisión",
        "Redes neuronales analizan imágenes médicas más rápido que los radiólogos"
    ],
    ids=["doc1", "doc2", "doc3"]
)

results = collection.query(
    query_texts=["Aplicaciones de IA en medicina"],
    n_results=2
)

print(results)
```
Este código crea una colección, inserta documentos y ejecuta una consulta de búsqueda semántica.
### Configuración de función de embedding

Las colecciones en Chroma pueden utilizar diferentes modelos de embedding. Para usar embeddings de OpenAI:
```python
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

openai_ef = OpenAIEmbeddingFunction(
    api_key="your-api-key",
    model_name="text-embedding-3-small"
)

collection = client.create_collection(
    name="openai_embeddings",
    embedding_function=openai_ef
)
```
### Integración con LangChain

LangChain ofrece un wrapper nativo para Chroma, soportando flujos de trabajo avanzados como RAG, chatbots y memoria.

**Ejemplo:**```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db", # opcional
)
```
## Características principales

- **Código abierto Apache 2.0**: Sin dependencia, extensible, orientado a la comunidad ([GitHub Stars 24k+](https://github.com/chroma-core/chroma))
- **Búsqueda ANN rápida**: Indexación HNSW para tiempos de búsqueda sublineales
- **Almacenamiento de documentos y metadatos**: Cada embedding se relaciona con un documento y metadatos definidos por el usuario
- **Búsqueda híbrida**: Combina búsqueda semántica (vectorial) y por palabras clave
- **Soporte multimodal**: Almacena/busca texto, imágenes y más
- **Operaciones en lote**: Inserción y consulta masiva para eficiencia
- **API sencilla**: Añadir, actualizar, eliminar, buscar
- **Integración**: Nativa con LangChain, LlamaIndex, OpenAI, HuggingFace, Cohere, OpenCLIP y más
- **Despliegue flexible**: En memoria, persistente, cliente-servidor y nube administrada
- **Comunidad activa**: Discord, GitHub, documentación
## Casos de uso clave

### Búsqueda semántica

Chroma potencia la búsqueda semántica comparando embeddings, no solo palabras clave.
- **E-commerce**: Buscar “zapatos cómodos de verano” devuelve resultados relevantes, aunque se use otro vocabulario.
- **Gestión del conocimiento**: Búsqueda en wikis internas, tickets de soporte, bases de código.
- **Salud**: Encuentra casos, investigaciones o imágenes diagnósticas similares.
### Sistemas de recomendación

Encuentra elementos/usuarios similares mediante similitud de embeddings:
- Recomendaciones personalizadas de productos/noticias/artículos
- Matching entre elementos o usuarios

### Generación aumentada por recuperación (RAG)

**RAG**permite que los LLMs accedan en tiempo real a bases de conocimiento externas, mejorando la precisión y reduciendo alucinaciones.
- Chatbots citan documentos específicos
- Asistentes responden con conocimiento actualizado de la empresa
### Búsqueda de imágenes, audio y multimodal

Embebe imágenes, texto y más en un espacio vectorial compartido.
- Búsqueda visual (encontrar imágenes similares)
- Cross-modal (buscar imágenes con texto y viceversa)
- Organizar datasets multimedia

### Chatbots y aplicaciones de IA

Chroma actúa como memoria semántica persistente para LLMs y chatbots.
- Recupera historial de conversaciones o fragmentos de conocimiento relevantes
- Potencia respuestas contextuales

### Ciencia de datos y análisis

- Análisis exploratorio de datos de alta dimensión
- Detección de anomalías en logs financieros/de seguridad
- Construcción de grafos de conocimiento, mapas semánticos
## Optimización de rendimiento

Chroma está diseñado para velocidad y eficiencia del desarrollador, pero algunos consejos de optimización incluyen:

- **Operaciones en lote**: Inserta/consulta en bloques para reducir overhead
- **Dimensionalidad de embeddings**: Vectores de menor dimensión usan menos memoria, búsqueda más rápida (puede afectar precisión)
- **Compactación de índices**: Compacta el índice HNSW tras eliminaciones/actualizaciones frecuentes
- **Prefiltrado por metadatos**: Filtra por metadatos antes de la similitud para reducir el cómputo

**Ejemplo:**```python
collection.add(
    documents=large_document_list,
    ids=id_list,
    metadatas=metadata_list
)
```
## Comparaciones y alternativas

### Chroma vs. Pinecone, Faiss, Weaviate, Qdrant, Milvus y otros

**Panorama del ecosistema:**- **Chroma**: OSS, configuración simple, búsqueda híbrida, ideal para prototipos/velocidad de desarrollo
- **Pinecone**: Administrado, distribuido, nivel empresarial, soporte multi-índice, alta escala
- **Faiss**: OSS, enfoque en investigación/ML, C++/Python, no es una base de datos (sin almacenamiento de doc/metadatos)
- **Weaviate**: OSS, distribuido, búsqueda híbrida, esquema, multi-tenant
- **Qdrant**: OSS, distribuido, filtrado, REST/gRPC, alto rendimiento
- **Milvus**: OSS, cloud-native, soporte GPU, muy alta escala
### Tabla comparativa

| Característica          | **Chroma**| **Pinecone**| **Faiss**| **Weaviate**| **Qdrant**| **Milvus**|
|------------------------|------------------|-----------------|-------------------|------------------|--------------|--------------|
| Código abierto         | ✅               | ❌              | ✅                | ✅ (open-core)   | ✅           | ✅           |
| Facilidad de setup     | Muy simple       | Administrado, fácil | Complejo       | Moderado         | Moderado     | Moderado     |
| Lenguajes soportados   | Python, JS       | Python, JS, Go  | Python, C++       | Python, JS, Go   | Python, REST | Python, REST |
| Indexación vectorial   | HNSW             | Múltiples       | Múltiples         | HNSW, otros      | HNSW         | IVF, HNSW    |
| Almacenamiento docs    | Incorporado      | No              | No                | Incorporado      | Incorporado  | Incorporado  |
| Filtrado por metadatos | Sí               | Sí              | Limitado          | Sí               | Sí           | Sí           |
| Búsqueda híbrida       | Sí               | No              | No                | Sí               | No           | No           |
| Cloud/serverless       | Chroma Cloud     | Sí              | No                | Sí               | Sí           | Sí           |
| RBAC/[multi-tenant](/es/glossary/multi-tenancy/) | No               | Sí             | No                | Sí              | Sí          | Sí          |
| Escalabilidad          | Nodo único       | Distribuido     | Local, dist.      | Distribuido      | Distribuido  | Distribuido  |
| Comunidad/soporte      | Activa, OSS      | Comercial       | Gran OSS          | Comercial + OSS  | OSS activo   | OSS activo   |
| Mejor para             | Velocidad de desarrollo, prototipos | Gran escala | Investigación, ML personalizado |