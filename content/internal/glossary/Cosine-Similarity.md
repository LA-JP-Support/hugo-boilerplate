+++
title = "Cosine Similarity"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "cosine-similarity"
description = "Cosine similarity es una métrica que mide el coseno del ángulo entre dos vectores no nulos, evaluando su similitud en función de la orientación en lugar de la magnitud. Ampliamente utilizada en machine learning, PLN y sistemas de recomendación."
keywords = ["cosine similarity", "machine learning", "procesamiento de lenguaje natural", "sistemas de recomendación", "similitud de vectores"]
category = "Infraestructura e Implementación de IA"
type = "glossary"
draft = false
url = "/internal/glossary/Cosine-Similarity/"

+++
## ¿Qué es Cosine Similarity?

Cosine similarity es una métrica cuantitativa que calcula el coseno del ángulo entre dos vectores no nulos en un espacio de producto interno. Esta métrica se utiliza ampliamente en minería de datos, machine learning e inteligencia artificial para evaluar cuán similares son dos vectores, basándose exclusivamente en su orientación y no en su magnitud. Su principal ventaja radica en el enfoque en la dirección, lo que la hace ideal para representaciones de alta dimensión como embeddings de documentos o vectores de características (ver [IBM: What is Cosine Similarity](https://www.ibm.com/think/topics/cosine-similarity), [GeeksforGeeks: Cosine Similarity](https://www.geeksforgeeks.org/dbms/cosine-similarity/)).

**Fórmula:**  
\[
\text{Cosine Similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \times \|\mathbf{B}\|}
\]
- \(\mathbf{A} \cdot \mathbf{B}\): Producto punto de los vectores A y B  
- \(\|\mathbf{A}\|\), \(\|\mathbf{B}\|\): Norma euclidiana (magnitud) de cada vector  
- \(\theta\): Ángulo entre los vectores

**Interpretación:**
- Puntuación de **1**: Los vectores apuntan en la misma dirección (similitud perfecta).
- Puntuación de **0**: Los vectores son ortogonales (sin similitud).
- Puntuación de **-1**: Los vectores apuntan en direcciones opuestas (máxima disimilitud).

La mayoría de aplicaciones prácticas (minería de texto, embeddings) usan vectores no negativos, por lo que los valores de cosine similarity suelen estar en el rango de 0 a 1.

## Explicación Matemática

**Cálculo Paso a Paso:**

Dados dos vectores no nulos:
\[
\mathbf{A} = [a_1, a_2, \ldots, a_n]
\]
\[
\mathbf{B} = [b_1, b_2, \ldots, b_n]
\]

1. **Producto Punto:**  
   \[
   \mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} a_i b_i
   \]

2. **Magnitud (Norma Euclidiana):**  
   \[
   \|\mathbf{A}\| = \sqrt{\sum_{i=1}^{n} a_i^2}
   \]
   \[
   \|\mathbf{B}\| = \sqrt{\sum_{i=1}^{n} b_i^2}
   \]

3. **Cosine Similarity:**  
   \[
   \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \times \|\mathbf{B}\|}
   \]

**Ejemplo de cálculo:**  
Sea  
\(\mathbf{A} = [3, 2, 0, 5]\),  
\(\mathbf{B} = [1, 0, 0, 0]\).

- Producto punto: \(3*1 + 2*0 + 0*0 + 5*0 = 3\)
- Magnitud de A: \(\sqrt{3^2 + 2^2 + 0^2 + 5^2} = \sqrt{9 + 4 + 0 + 25} = \sqrt{38} \approx 6.16\)
- Magnitud de B: \(\sqrt{1^2 + 0^2 + 0^2 + 0^2} = 1\)
- Cosine Similarity: \(3 / (6.16 * 1) \approx 0.49\)

(Referencia: [GeeksforGeeks Example](https://www.geeksforgeeks.org/dbms/cosine-similarity/))

**Cosine Dissimilarity:**  
A menudo, la disimilitud se calcula como \(1 - \text{Cosine Similarity}\). Para el ejemplo anterior, \(D_C(\mathbf{A}, \mathbf{B}) = 1 - 0.49 = 0.51\).

## Intuición Visual

Imagina dos flechas que parten del mismo origen en un espacio multidimensional:

- **0° (Coseno = 1):** Las flechas se superponen, indicando dirección idéntica.
- **90° (Coseno = 0):** Las flechas están en ángulo recto, sin relación.
- **180° (Coseno = -1):** Las flechas apuntan en direcciones opuestas, indicando total disimilitud.

Consulta el [diagrama de GeeksforGeeks](https://media.geeksforgeeks.org/wp-content/uploads/20200911171455/UntitledDiagram2.png) para una visualización.

**Explicación en video de StatQuest:**  
[YouTube: Cosine Similarity, Clearly Explained!!! (StatQuest)](https://www.youtube.com/watch?v=e9U0QAFbfLI)

## Implementación Práctica

**Librerías Populares:**
- **NumPy:** Eficiente para operaciones vectorizadas ([NumPy linalg documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html))
- **scikit-learn:** [`sklearn.metrics.pairwise.cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) para matrices de similitud por pares.
- **TensorFlow:** [CosineSimilarity loss integrado](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity)
- **PyTorch:** [`torch.nn.CosineSimilarity`](https://pytorch.org/docs/stable/generated/torch.nn.CosineSimilarity.html)
- **Bases de Datos Vectoriales:** Extensiones como [pgvector para PostgreSQL](https://github.com/pgvector/pgvector)

**Ejemplo en Python (NumPy):**
```python
import numpy as np

def cosine_similarity(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

A = [1, 2, 3]
B = [4, 5, 6]
similarity = cosine_similarity(A, B)
print("Cosine similarity:", similarity)  # Output: 0.9746318461970762
```
Para más información, ver [GeeksforGeeks: Python Measure Similarity Between Two Sentences](https://www.geeksforgeeks.org/machine-learning/python-measure-similarity-between-two-sentences-using-cosine-similarity/).

## Aplicaciones y Casos de Uso

**1. Similitud de Documentos y Motores de Búsqueda**  
Los documentos y consultas se transforman en vectores de alta dimensión usando TF-IDF o embeddings neuronales. Cosine similarity mide la relevancia del contenido comparando la orientación de los vectores.  
- [IBM: NLP and Cosine Similarity](https://www.ibm.com/think/topics/natural-language-processing)

**2. Sistemas de Recomendación**  
Las preferencias de usuarios y elementos se codifican como vectores. Las recomendaciones se generan encontrando los elementos o usuarios con mayor cosine similarity.  
- [IBM: Recommendation Engines](https://www.ibm.com/think/topics/recommendation-engine#:~:text=A%20recommendation%20engine%2C%20also%20called,items%20based%20on%20those%20patterns.)

**3. Procesamiento de Lenguaje Natural (PLN) y Embeddings**  
Cosine similarity es fundamental para comparar embeddings de palabras, frases o documentos. Esto cuantifica la similitud semántica, permitiendo búsqueda semántica, detección de paráfrasis y agrupamiento.  
- [IBM: Embedding Techniques](https://www.ibm.com/think/topics/embedding)

**4. Visión por Computadora y Estimación de Postura**  
Vectores de puntos clave que representan la pose corporal o características de imágenes se comparan usando cosine similarity para evaluar la similitud de configuración.  
- [IBM: Image Recognition](https://www.ibm.com/think/topics/image-recognition#:~:text=Image%20recognition%20is%20an%20application,in%20digital%20images%20or%20video.)

**5. Detección de Fraudes y Detección de Anomalías**  
Vectores de transacciones multidimensionales se comparan para identificar patrones anómalos usando cosine similarity.  
- [IBM: Fraud Detection](https://www.ibm.com/think/topics/fraud-detection)

## Ventajas y Desventajas

**Ventajas**
- **Insensible a la Magnitud:** Solo importa la dirección; vectores de distintas longitudes pueden ser altamente similares ([GeeksforGeeks](https://www.geeksforgeeks.org/dbms/cosine-similarity/)).
- **Robustez en Alta Dimensión:** Funciona bien en datos dispersos de alta dimensión (p.ej., análisis de texto, embeddings).
- **Eficiencia Computacional:** El cálculo es sencillo y está optimizado en las principales librerías de machine learning.
- **Normalización Incorporada:** No es necesario normalizar explícitamente los vectores de entrada.

**Limitaciones**
- **Ignora la Magnitud:** No distingue entre un vector pequeño y uno grande en la misma dirección.
- **No Definido para Vectores Cero:** Cosine similarity no está definida si alguno de los vectores es el vector cero.
- **Simetría:** \(\text{CosineSimilarity}(A, B) = \text{CosineSimilarity}(B, A)\); no considera la direccionalidad de la comparación.
- **Sensibilidad a la Dispersión:** Puede funcionar mal con datos extremadamente dispersos donde hay poco solapamiento de elementos no nulos.

## Comparativa con Otras Métricas de Similitud

| Métrica            | Enfoque      | Sensible a la Magnitud | Mejor Para                  | Referencia                                    |
|--------------------|--------------|------------------------|-----------------------------|-----------------------------------------------|
| Cosine Similarity  | Dirección    | No                     | Texto, embeddings           | [IBM](https://www.ibm.com/think/topics/cosine-similarity) |
| Euclidean Distance | Posición     | Sí                     | Datos numéricos, físicos    | [GeeksforGeeks](https://www.geeksforgeeks.org/maths/euclidean-distance/) |
| Jaccard Similarity | Solapamiento/Conjuntos | No              | Conjuntos, atributos binarios | [Wikipedia: Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index) |

- **Euclidean Distance:** Mide la distancia en línea recta; se ve afectada por dirección y magnitud. Útil cuando importan las diferencias absolutas ([scikit-learn Euclidean Distance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)).
- **Jaccard Similarity:** Mide el solapamiento entre conjuntos; ideal para características categóricas o binarias (p.ej., etiquetas compartidas).
- **Producto Punto:** Incluye magnitud; puede ser engañoso si las escalas difieren.

## Buenas Prácticas y Consejos Prácticos

1. **Normaliza los Datos:** Elimina vectores cero y asegúrate de que todos los vectores sean no nulos para evitar resultados indefinidos.
2. **Gestión de Datos Dispersos:** Utiliza librerías optimizadas para matrices dispersas al trabajar con datos de alta dimensión y dispersión (p.ej., [scikit-learn sparse matrices](https://scikit-learn.org/stable/modules/scipy_sparse.html)).
3. **Combina Métricas:** Para un análisis de similitud más rico, combina cosine similarity con otras métricas como características del modelo.
4. **Preprocesamiento Consistente:** Asegúrate de que todos los vectores se generen a partir del mismo proceso/modelo y tengan la misma dimensionalidad.
5. **Interpreta con Cuidado:** Una alta cosine similarity no siempre implica equivalencia semántica; el contexto y conocimiento del dominio son esenciales.
6. **Aprovecha Librerías Robusta:** Usa funciones integradas de [NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html), [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html), [TensorFlow](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity) o [pgvector](https://github.com/pgvector/pgvector).

## Referencias y Lecturas Recomendadas

- [Cosine Similarity – GeeksforGeeks](https://www.geeksforgeeks.org/dbms/cosine-similarity/)
- [IBM: What is Cosine Similarity](https://www.ibm.com/think/topics/cosine-similarity)
- [Wikipedia: Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
- [Built In: Understanding Cosine Similarity and Its Applications](https://builtin.com/machine-learning/cosine-similarity)
- [Tiger Data: A Guide to Cosine Similarity](https://www.tigerdata.com/learn/understanding-cosine-similarity)
- [YouTube: Cosine Similarity, StatQuest](https://www.youtube.com/watch?v=e9U0QAFbfLI)
- [scikit-learn: Cosine Similarity Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
- [NumPy: Linear Algebra (linalg)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)
- [TensorFlow: CosineSimilarity Loss](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity)
- [pgvector: PostgreSQL Vector Search Extension](https://github.com/pgvector/pgvector)

## Ver También

- [Euclidean Distance](https://www.geeksforgeeks.org/maths/euclidean-distance/)
- [Jaccard Similarity](https://en.wikipedia.org/wiki/Jaccard_index)
- [TF-IDF Vectorization](https://www.ibm.com/think/topics/bag-of-words)
- [Word Embeddings](https://www.ibm.com/think/topics/embedding)
- [Principal Component Analysis](https://www.ibm.com/think/topics/principal-component-analysis#:~:text=Principal%20component%20analysis%2C%20or%20PCA,of%20variables%2C%20called%20principal%20components.)

### Para más detalles técnicos, ejemplos de código y demostraciones matemáticas, visita la documentación y los recursos educativos enlazados arriba.