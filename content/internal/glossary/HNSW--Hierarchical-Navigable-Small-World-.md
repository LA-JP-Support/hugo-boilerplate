+++
title = "HNSW (Hierarchical Navigable Small World)"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "hnsw-hierarchical-navigable-small-world"
description = "HNSW (Hierarchical Navigable Small World) es un algoritmo basado en grafos para búsqueda aproximada de vecinos más cercanos (ANN) rápida y precisa en bases de datos vectoriales, ideal para datos de alta dimensión."
keywords = ["HNSW", "Approximate Nearest Neighbor", "Vector Search", "Vector Databases", "Graph Algorithm"]
category = "Infraestructura e Implementación de IA"
type = "glossary"
draft = false
url = "/internal/glossary/HNSW--Hierarchical-Navigable-Small-World-/"

+++
## ¿Qué es HNSW?

HNSW (Hierarchical Navigable Small World) es un algoritmo de grafos de proximidad para búsqueda *aproximada de vecinos más cercanos (ANN)* rápida, escalable y precisa en espacios vectoriales de alta dimensión. Es ampliamente utilizado en bases de datos vectoriales y aplicaciones impulsadas por IA para encontrar los ítems (vectores) más cercanos a una consulta sin realizar una búsqueda exhaustiva. HNSW supera a muchos algoritmos ANN anteriores en velocidad y recall, especialmente en escenarios a gran escala y en memoria.

- **Propósito:**Búsqueda ANN eficiente con alto recall en conjuntos de datos grandes y de alta dimensión.
- **Innovaciones clave:**Combina las ventajas de los grafos small-world (para navegación rápida) y jerarquía tipo skip-list (para búsqueda multiescala).
- **Aplicaciones típicas:**Búsqueda semántica de documentos, recuperación de imágenes/videos, motores de recomendación, recuperación de contexto LLM, detección de anomalías.
## Conceptos Fundamentales

### Búsqueda Vectorial y ANN

La *búsqueda vectorial* busca los vectores más cercanos (más similares) a una consulta. Cada punto de datos se representa como un vector de alta dimensión (como un BERT de 768 dimensiones o un embedding de OpenAI de 1536 dimensiones). La búsqueda por fuerza bruta escala linealmente con el tamaño del conjunto de datos (O(N)), lo que la hace impráctica para colecciones grandes.

Los **algoritmos de vecinos más cercanos aproximados (ANN)**como HNSW reducen el tiempo de búsqueda aceptando una mínima pérdida de recall (precisión) para obtener incrementos drásticos de velocidad, logrando complejidad sublineal. Esto es crítico para aplicaciones en tiempo real con millones o miles de millones de vectores.

**Para saber más:**- [Zilliz: Vector Similarity Search](https://zilliz.com/learn/vector-similarity-search)
- [Pinecone: What is Similarity Search?](https://www.pinecone.io/learn/what-is-similarity-search/)

### Grafos Small World Navegables (NSW)

*Los grafos small-world* son redes donde la mayoría de los nodos pueden alcanzarse desde cualquier otro con pocos saltos, gracias a enlaces locales y de largo alcance. En los grafos NSW, cada nodo se conecta con sus vecinos más cercanos y algunos lejanos, lo que permite enrutamiento codicioso: en cada paso, moverse al vecino más próximo a la consulta.

- Los grafos NSW tienen complejidad de búsqueda logarítmica o polilogarítmica [Zilliz](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW).
- El proceso de *búsqueda codiciosa* sigue el camino más corto disponible hacia la consulta.

**Para saber más:**- [Navigable Small World Graphs (Wikipedia)](https://en.wikipedia.org/wiki/Small-world_network)

### Skip Lists y Jerarquía

*Las skip lists* son listas enlazadas por capas donde las capas superiores permiten saltos más largos, acelerando la búsqueda (ver [Skip List, Wikipedia](https://en.wikipedia.org/wiki/Skip_list)). HNSW introduce una jerarquía similar:

- A cada vector se le asigna aleatoriamente el número de capas en las que aparece, siguiendo una distribución geométrica.
- Las capas superiores son dispersas y permiten recorrido rápido; las inferiores son densas y aseguran búsqueda precisa.

Esta estructura jerárquica permite una navegación eficiente de grueso a fino.

**Para saber más:**- [Probability Skip List (Pinecone)](https://www.pinecone.io/learn/series/faiss/hnsw/#Probability-Skip-List)

## ¿Cómo funciona HNSW?

### Capas y Estructura del Grafo

HNSW crea un grafo de proximidad dirigido con múltiples capas:

- **Capa superior:**Contiene menos nodos, cada uno con conexiones de largo alcance.
- **Capas intermedias:**Gradualmente más densas, con conexiones de menor alcance.
- **Capa inferior (Capa 0):**Contiene todos los vectores con conexiones de corto alcance (vecinos más cercanos).

A cada nodo se le asigna la capa más alta mediante una distribución geométrica (probabilidad p, a menudo 1/ln(N)), asegurando que el número de nodos por capa disminuya exponencialmente con la altura ([arXiv](https://arxiv.org/abs/1603.09320)). Esta estructura permite una complejidad de búsqueda logarítmica en la práctica.

**Visualización:**- [Pinecone HNSW Structure Diagram](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fe63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png&w=3840&q=75)

### Proceso de Búsqueda

1. **Comenzar en la capa superior:**En un nodo de entrada designado.
2. **Recorrido codicioso:**En cada nivel, moverse repetidamente al vecino más cercano al vector de consulta.
3. **Mínimo local:**Cuando ningún vecino es más cercano, descender a la siguiente capa y repetir.
4. **Lista de candidatos:**En la capa inferior, mantener una cola de prioridad (tamaño controlado por el parámetro `efSearch`) con nodos candidatos.
5. **Resultado:**Devolver los k vectores más cercanos tras finalizar la búsqueda.

Este proceso garantiza búsquedas rápidas y precisas aprovechando enlaces de largo alcance para navegación global y enlaces de corto alcance para refinamiento local.
### Construcción del Grafo (Inserción)

1. **Asignación aleatoria de capas:**Cada nuevo vector recibe aleatoriamente una capa más alta usando una distribución geométrica.
2. **Recorrido de arriba hacia abajo:**Comenzando en la parte superior, realizar búsqueda codiciosa en cada capa para encontrar el punto de entrada más cercano.
3. **Conexión:**En cada capa, conectar el nuevo nodo con sus M vecinos más cercanos (M es un parámetro ajustable).
4. **Repetir:**Descender por las capas asignadas, conectando en cada una, hasta llegar a la capa 0.

**Punto clave:**Este proceso incremental y probabilístico permite construir el índice de forma dinámica y eficiente.
### Parámetros Clave y Compensaciones

- **M (máx. vecinos):**Controla el número de vecinos por nodo. Un M mayor aumenta el recall y el uso de memoria.
- **efConstruction:**Número de candidatos considerados durante la construcción. Valores altos generan índices de mayor calidad, a costa de mayor tiempo de construcción.
- **efSearch:**Número de candidatos considerados durante la búsqueda. Valores altos incrementan el recall, a costa de mayor [latencia](/es/glossary/latency/).

**Compensaciones:**- Aumentar M o ef* mejora el recall pero incrementa el uso de memoria y/o la latencia.
- Disminuirlos reduce el uso de RAM y acelera las consultas pero puede disminuir el recall.

**Complejidad matemática:**- **Memoria:**O(M*N) enlaces para N vectores.
- **Tiempo de construcción:**O(N log N) con efConstruction alto.
- **Búsqueda:**O(log N) saltos esperados en grafos bien ajustados.
## Comparación con Otros Algoritmos ANN

| Algoritmo        | Estructura      | Ventajas             | Desventajas                 | Mejores casos de uso          |
|------------------|-----------------|----------------------|-----------------------------|-------------------------------|
| **HNSW**| Grafo + Jerarquía | Recall alto, dinámico, SOTA | Alta memoria, complejidad    | La mayoría de DBs vectoriales, cargas IA |
| **KD-Tree**| Árbol           | Simple, baja dimensión| Degrada en alta dimensión    | Conjuntos pequeños/baja dimensión |
| **IVF**| Clústeres planos| Escalable en disco, simple | Recall bajo, índice estático | Billones, menor recall        |
| **LSH**| Hash buckets    | Rápido, eficiente en RAM | Recall bajo, aleatorio       | Alta dimensión, escenarios de hashing |

**Benchmarks y estudios:**- [arXiv: “Down with the Hierarchy: The 'H' in HNSW Stands for 'Hubs'” (2024)](https://arxiv.org/html/2412.01940v1): Estudia el impacto real de la estructura jerárquica; encuentra que los "hubs" (nodos muy conectados) en el grafo juegan un papel crítico en la velocidad de navegación y el recall, a veces más que la jerarquía misma.
- [Redis: HNSW vs. IVF/LSH](https://redis.io/blog/how-hnsw-algorithms-can-improve-search/): Explica por qué HNSW suele ser el estándar en bases de datos en memoria, mientras que IVF y LSH son mejores para escenarios en disco o streaming.

## Implementación y Uso

### Uso de HNSW en Librerías Populares

#### Python + Faiss

```python
import faiss
import numpy as np

d = 128        # dimensión del vector
M = 32         # número de vecinos
ef_construction = 200
ef_search = 50

index = faiss.IndexHNSWFlat(d, M)
index.hnsw.efConstruction = ef_construction

# Agregar vectores
index.add(xb)  # xb = np.ndarray de forma (num_vectors, d)

# Buscar
index.hnsw.efSearch = ef_search
D, I = index.search(xq, k)  # xq = vectores consulta, k = top k
```
- [Documentación HNSW de Faiss](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes#hnsw)

#### PostgreSQL + pgvector

```sql
CREATE INDEX document_embedding_idx ON document_embedding USING hnsw(embedding vector_cosine_ops);
```
- [Documentación HNSW de pgvector](https://github.com/pgvector/pgvector#hnsw)

#### Redis

```bash
FT.CREATE docs_idx ON HASH PREFIX 1 docs: SCHEMA doc_embedding VECTOR HNSW 512 TYPE FLOAT32 DISTANCE_METRIC COSINE M 16 EF_CONSTRUCTION 32
```
- [Documentación HNSW de Redis](https://redis.io/docs/latest/develop/interact/search-and-query/advanced-concepts/vectors/#hnsw-index)

#### Milvus

- [Documentación HNSW de Milvus](https://milvus.io/docs/hnsw.md#HNSW)
- [Guía HNSW de Zilliz](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW)

### Ajuste de Parámetros: Guía Práctica

Comience con los valores por defecto: M=16–32, efConstruction=100–200, efSearch=40–100.

- Para mayor recall: Aumente efSearch y/o M.
- Para consultas más rápidas/menos memoria: Disminuya M o efSearch.
- Siempre mida recall y latencia en datos representativos antes de finalizar.

**Notas de ingeniería:**- Use construcción paralela si está soportada (ej. Faiss, Redis).
- Para cargas dinámicas, monitorice periódicamente la conectividad para evitar “islas”.
- Para actualizaciones frecuentes, use inserciones/borrados incrementales.
## Aplicaciones y Casos de Uso

- **Búsqueda semántica de texto:**Recuperación de documentos, FAQs o fragmentos de código relevantes por similitud vectorial (embedding search).
- **Recuperación de imágenes/video:**Encontrar activos visualmente similares en grandes catálogos.
- **Recomendación de productos o contenido:**Sugerir ítems, artículos o canciones similares usando similitud de embeddings.
- **Detección de anomalías:**Detectar outliers en series temporales, grafos o logs según distancia a centros de clúster.
- **Recuperación de contexto LLM:**Habilitar pipelines RAG (Retrieval Augmented Generation) para chatbots y asistentes.

**Ejemplo (búsqueda semántica):**Una consulta de cliente “reset my password” se embebe y se compara en milisegundos contra millones de documentos de soporte usando HNSW.

**Ejemplo (búsqueda de imágenes):**Dada una foto, recuperar las imágenes visualmente más similares de un dataset de 10 millones de productos.
## Fortalezas y Desafíos

### Fortalezas

- **Alto rendimiento:**Recall y velocidad de última generación para ANN.
- **Dinámico:**Soporta inserciones/borrados incrementales eficientes sin reconstrucción completa.
- **Flexible:**M, efConstruction y efSearch permiten ajuste específico por aplicación.
- **Ampliamente soportado:**Integrado en Faiss, [Milvus](/es/glossary/milvus/), [Pinecone](/es/glossary/pinecone/), Vespa, Redis, pgvector, [Weaviate](/es/glossary/weaviate/).

### Desafíos

- **Uso intensivo de memoria:**La estructura de grafo (O(M*N) enlaces) puede consumir mucha RAM, especialmente con M grande o alta cardinalidad.
- **Escalabilidad más allá de la RAM:**Indexado solo en memoria; para conjuntos que superan la RAM, se requieren índices híbridos (disco+RAM) o basados en disco (como DiskANN, Vamana) ([Zilliz: DiskANN](https://zilliz.com/learn/DiskANN-and-the-Vamana-Algorithm)).
- **Sensibilidad a parámetros:**Configuraciones inadecuadas pueden degradar el recall o la velocidad; requiere ajuste cuidadoso.
- **Complejidad:**Depuración, monitoreo y [sharding](/es/glossary/sharding/) distribuido pueden ser más difíciles que con métodos basados en árboles o hash.

**Estrategias de mitigación:**- Aplicar reducción de dimensionalidad (ej. PCA) o cuantización para problemas grandes y de alta dimensión.
- Para conjuntos masivos, usar algoritmos híbridos HNSW+IVF o streaming/basados en disco.
- Monitorear conectividad y recall para evitar nodos aislados.
## Temas Avanzados

### Filtrado y Búsqueda Híbrida

- **Pre-filtrado:**Aplicar filtros de metadatos o booleanos antes o durante la búsqueda HNSW.
- **Post-filtrado:**Filtrar resultados después del ANN; puede requerir mayor efSearch como compensación.
- **Índices híbridos:**Combinar HNSW con IVF o métodos basados en disco para casos RAM-limitada o streaming.

### Reducción de Dimensionalidad

- Técnicas como PCA, UMAP o proyección aleatoria pueden reducir el tamaño del vector, mejorando memoria y velocidad con mínima pérdida de recall.
- La cuantización de vectores puede reducir aún más el uso de RAM en despliegues a ultra gran escala.

### Entornos Distribuidos/Shardeados

- HNSW es shardeable; cada shard mantiene una partición de los datos y un índice HNSW local.
- El HNSW distribuido es más complejo, ya que la búsqueda cross-shard requiere difundir consultas o enrutar mediante un índice global.
- Algunos DBs vectoriales (Milvus, Redis Cluster, Pinecone) soportan gestión de clúster y HNSW distribuido de forma nativa.
- [Redis: HNSW Sharding](https://redis.io/blog/how-hnsw-algorithms-can-improve-search/)
## Más Lectura y Referencias

- [Artículo original de HNSW (arXiv)](https://arxiv.org/abs/1603.09320)
- [Pinecone: Hierarchical Navigable Small Worlds (HNSW)](https://www.pinecone.io/learn/series/faiss/hnsw/)
- [Zilliz: HNSW Technical Deep Dive](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW)
- [Redis: How HNSW Algorithms Can Improve Search](https://redis