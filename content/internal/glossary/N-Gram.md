+++
title = "N-Gram"
translationKey = "n-gram"
description = "Un N-grama es una secuencia contigua de n elementos (palabras, caracteres o símbolos) extraídos de texto o habla, fundamental en PLN para modelado de lenguaje y análisis de texto."
keywords = ["N-grama", "Procesamiento de Lenguaje Natural", "Modelado de Lenguaje", "Análisis de Texto", "Reconocimiento de Voz"]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/N-Gram/"

+++
## Definición y visión general

Un **N-grama**es una secuencia contigua de *n* elementos de una muestra dada de texto o habla. En el contexto del [Procesamiento de Lenguaje Natural (PLN)](https://es.wikipedia.org/wiki/Procesamiento_de_lenguaje_natural), los N-gramas suelen ser secuencias de palabras, caracteres o símbolos. El valor de *n* determina la longitud de cada fragmento:

- Para *n=1*, el modelo utiliza **unigramas**(palabras o tokens individuales).
- Para *n=2*, utiliza **bigramas**(secuencias de dos palabras).
- Para *n=3*, utiliza **trigramas**(secuencias de tres palabras).
- También se emplean N-gramas de orden superior (*n > 3*) en casos donde se necesita un contexto más amplio.

Los modelos de N-gramas son fundamentales en la lingüística computacional, proporcionando marcos estadísticos para comprender, generar y predecir lenguaje. Son la base de muchos sistemas clásicos de PLN, incluyendo correctores ortográficos, texto predictivo, traducción automática y reconocimiento de voz.

Un modelo de lenguaje basado en N-gramas asigna una probabilidad a secuencias de tokens, utilizando información estadística sobre la coocurrencia de elementos en un corpus grande. Esto permite que los sistemas sugieran automáticamente las siguientes palabras más probables, corrijan errores o generen texto similar al humano.

*Fuente: [Stanford Speech and Language Processing, N-gram Language Models (PDF)](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

## Contexto histórico y desarrollo

Los N-gramas tienen una rica historia tanto en lingüística como en teoría de la información. La formalización matemática de los N-gramas se remonta a Andrey Markov, cuyo trabajo sobre **cadenas de Markov**a principios del siglo XX sentó las bases del modelado de secuencias. El aporte de Markov fue que la probabilidad de un evento podía depender solo del evento(s) anterior en una cadena, y no de toda la historia (la "propiedad de Markov").

En las décadas de 1940 y 1950, Claude Shannon aplicó modelos de Markov al texto en inglés, introduciendo el concepto de modelos N-grama para el lenguaje. Los experimentos de Shannon demostraron que los modelos estadísticos podían generar texto sorprendentemente similar al humano, sentando las bases de la lingüística computacional.

Para las décadas de 1980 y 1990, con el auge de los corpus digitales y el incremento de la potencia computacional, los modelos de N-gramas se convirtieron en el enfoque estándar para tareas como reconocimiento de voz, reconocimiento óptico de caracteres (OCR) y sistemas tempranos de traducción automática. Su simplicidad, interpretabilidad y eficacia los convirtieron en referencia básica en muchos flujos de PLN.

Hoy en día, aunque arquitecturas neuronales avanzadas como los [Transformers](https://www.geeksforgeeks.org/machine-learning/getting-started-with-transformers/) han superado a los modelos de N-gramas en muchas tareas, los N-gramas siguen siendo esenciales para la ingeniería de características, comparaciones de referencia y aplicaciones donde la eficiencia y la [transparencia](/es/glossary/transparency/) son críticas.

*Lectura adicional: [Wikipedia: N-grama](https://es.wikipedia.org/wiki/N-grama)*

## Tipos de N-gramas

### Unigramas

- **Definición:**Secuencias de elementos individuales (usualmente palabras).
- **Ejemplo:**Texto: "[Procesamiento de lenguaje natural](/es/glossary/natural-language-processing--nlp-/) es divertido."  
  Unigramas: "Procesamiento", "de", "lenguaje", "natural", "es", "divertido"
- **Casos de uso:**Análisis básico de frecuencias de palabras, clasificación de texto, recuperación de información.

### Bigramas

- **Definición:**Secuencias de dos elementos consecutivos.
- **Ejemplo:**Texto: "Procesamiento de lenguaje natural es divertido."  
  Bigramas: "Procesamiento de", "de lenguaje", "lenguaje natural", "natural es", "es divertido"
- **Casos de uso:**Detección de frases, [análisis de sentimiento](/es/glossary/sentiment-analysis/) ("no bueno"), reconocimiento de voz.

### Trigramas

- **Definición:**Secuencias de tres elementos consecutivos.
- **Ejemplo:**Texto: "Procesamiento de lenguaje natural es divertido."  
  Trigramas: "Procesamiento de lenguaje", "de lenguaje natural", "lenguaje natural es", "natural es divertido"
- **Casos de uso:**Captura de contexto más amplio, autocompletado, corrección ortográfica.

### N-gramas de orden superior

- **Definición:**Secuencias de cuatro o más elementos consecutivos (ej: 4-gramas, 5-gramas).
- **Ejemplo:**Para "Procesamiento de lenguaje natural es divertido."  
  4-grama: "Procesamiento de lenguaje natural", "de lenguaje natural es", "lenguaje natural es divertido"
- **Casos de uso:**Modelado de lenguaje específico de dominio, detección de plagio.
- **Consideraciones:**A medida que *n* aumenta, el número de posibles N-gramas crece exponencialmente, lo que genera escasez de datos y sobrecarga computacional.

*Fuente: [GeeksforGeeks: N-gram in NLP](https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/)*

## Cómo funcionan los modelos N-grama

### Estimación de probabilidad

Los modelos N-grama estiman la probabilidad de una palabra o token en función de los *n-1* elementos anteriores. La **regla de la cadena de probabilidad**expresa la probabilidad conjunta de una secuencia como producto de probabilidades condicionales:

\[
P(w_1, w_2, \ldots, w_n) = P(w_1) \cdot P(w_2|w_1) \cdot P(w_3|w_1, w_2) \cdots P(w_n|w_1, \ldots, w_{n-1})
\]

Esta fórmula es computacionalmente costosa para secuencias largas. Los modelos N-grama simplifican esto mediante la **suposición de Markov**.

### Suposición de Markov

La **suposición de Markov**postula que la probabilidad de una palabra depende solo de las *n-1* palabras previas, y no de todo el contexto precedente. Esto es crucial para el cálculo práctico.

Para un bigrama (*n=2*):
\[
P(w_n | w_1, w_2, ..., w_{n-1}) \approx P(w_n | w_{n-1})
\]

Para un trigama (*n=3*):
\[
P(w_n | w_1, ..., w_{n-1}) \approx P(w_n | w_{n-2}, w_{n-1})
\]

Esta suposición reduce drásticamente el número de parámetros y hace viable el modelado del lenguaje con datos reales.

*Fuente: [Stanford Speech and Language Processing, N-gram Language Models (PDF)](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

### Estimación de Máxima Verosimilitud (MLE)

MLE se utiliza para estimar las probabilidades de los N-gramas a partir de los datos observados. La fórmula general para un modelo N-grama es:

\[
P(w_n | w_{n-N+1}, ..., w_{n-1}) = \frac{C(w_{n-N+1}, ..., w_n)}{C(w_{n-N+1}, ..., w_{n-1})}
\]

Donde:
- \(C(w_{n-N+1}, ..., w_n)\): Conteo del N-grama en el corpus.
- \(C(w_{n-N+1}, ..., w_{n-1})\): Conteo del prefijo (N-1)-grama.

Para bigramas, esto se convierte en:
\[
P(w_n | w_{n-1}) = \frac{C(w_{n-1}, w_n)}{C(w_{n-1})}
\]

**Ejemplo de cálculo:**Dado el corpus:
- "Yo soy Sam"
- "Sam yo soy"
- "Yo no me gustan los huevos verdes y jamón"

Para calcular \(P(soy | yo)\):
- Conteo de "yo soy": 2
- Conteo de "yo": 3
- \(P(soy | yo) = 2/3\)

*Consulta el cálculo completo y derivación matemática en [Stanford Speech and Language Processing, Capítulo 3](https://web.stanford.edu/~jurafsky/slp3/3.pdf).*

### Técnicas de suavizado (Smoothing)

#### Necesidad del suavizado

A medida que *n* aumenta, muchos N-gramas válidos pueden no aparecer en los datos de entrenamiento, resultando en estimaciones de probabilidad cero. Esto se denomina **escasez de datos**. Las técnicas de suavizado ajustan las probabilidades para tener en cuenta N-gramas no vistos, mejorando la generalización.

#### Suavizado de Laplace (aditivo)

El suavizado de Laplace simplemente añade una constante pequeña (usualmente 1) a todos los conteos de N-gramas:

\[
P_{Laplace}(w_n | w_{n-1}) = \frac{C(w_{n-1}, w_n) + 1}{C(w_{n-1}) + V}
\]

Donde:
- \(V\) es el tamaño del vocabulario.

Esto asegura que ningún N-grama tenga probabilidad cero.

#### Suavizados avanzados: Good-Turing, Kneser-Ney

- **Good-Turing Smoothing:**Ajusta las frecuencias de N-gramas según el número de N-gramas observados una vez, dos veces, etc.
- **Kneser-Ney Smoothing:**Estado del arte en modelado de lenguaje, considera tanto la frecuencia como la distribución de los contextos en los que aparece un N-grama.

*Explicación detallada: [Stanford PDF, Sección 3.4](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

### Perplejidad y entropía

- **Perplejidad**es una medida de qué tan bien un modelo probabilístico predice una muestra. Una perplejidad menor indica un mejor modelo de lenguaje.
  \[
  Perplexity(P) = 2^{H(P)}
  \]
  donde \(H(P)\) es la entropía de la distribución de probabilidad.
- **Entropía**mide la imprevisibilidad del texto.

*Más detalles: [Stanford PDF, Sección 3.5](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

### Ejemplo de implementación en Python

#### Extracción básica de N-gramas

```python
def generate_ngrams(texto, n):
    tokens = texto.split()
    ngrams = [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
    return ngrams

texto = "Geeks for Geeks Community"

unigramas = generate_ngrams(texto, 1)
bigramas = generate_ngrams(texto, 2)
trigramas = generate_ngrams(texto, 3)

print("Unigramas:", unigramas)
print("Bigramas:", bigramas)
print("Trigramas:", trigramas)
```

#### Salida
```
Unigramas: [('Geeks',), ('for',), ('Geeks',), ('Community',)]
Bigramas: [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
Trigramas: [('Geeks', 'for', 'Geeks'), ('for', 'Geeks', 'Community')]
```

#### Ejemplo de suavizado de Laplace

```python
from collections import Counter

def laplace_smoothing(ngrams, vocab_size):
    ngram_counts = Counter(ngrams)
    smoothed_ngrams = {ngram: (count + 1) / (len(ngrams) + vocab_size)
                       for ngram, count in ngram_counts.items()}
    return smoothed_ngrams

ngrams = [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
vocab_size = 5

smoothed_ngrams = laplace_smoothing(ngrams, vocab_size)
print("N-gramas suavizados:", smoothed_ngrams)
```

**Salida:**```
N-gramas suavizados: {('Geeks', 'for'): 0.25, ('for', 'Geeks'): 0.25, ('Geeks', 'Community'): 0.25}
```

#### Ejemplo con NLTK

```python
import nltk
words = nltk.word_tokenize("Voy a la tienda")
bigramas = list(nltk.ngrams(words, 2))
trigramas = list(nltk.ngrams(words, 3))
print("Bigramas:", bigramas)
print("Trigramas:", trigramas)
```

## Ingeniería de características con N-gramas

Las características de N-gramas se utilizan ampliamente en PLN para modelos de aprendizaje automático. Son la columna vertebral de clasificadores de texto clásicos, recuperación de información y más.

### Modelo Bag-of-N-grams

El enfoque **Bag-of-N-grams**representa un documento como un vector disperso, donde cada dimensión corresponde a un N-grama del vocabulario. El valor suele ser la frecuencia del N-grama en el documento.

#### Ejemplo: Python con SciPy

```python
import scipy.sparse as sp
import numpy as np

def extract_ngrams(texto, n):
    ngrams_list = []
    for i in range(len(texto) - n + 1):
        ngrams_list.append(tuple(texto[i:i + n]))
    return ngrams_list

def build_bag_of_ngrams(texto, n, vocabulary):
    ngrams_list = extract_ngrams(texto, n)
    ngrams_index = {ngram: i for i, ngram in enumerate(vocabulary)}
    col = [ngrams_index[ngram] for ngram in ngrams_list if ngram in ngrams_index]
    data = [1] * len(col)
    row = [0] * len(col)
    vector = sp.csr_matrix((data, (row, col)), shape=(1, len(vocabulary)))
    return vector
```

### Skip-grams y N-gramas de subpalabra

- **Skip-grams:**N-gramas no contiguos (ej: "Yo ... Sam" en "Yo soy Sam"), útiles para captar dependencias a largo plazo.
- **N-gramas de subpalabra:**N-gramas a nivel de caracteres o sílabas, esenciales para tratar lenguajes con morfología rica o datos ruidosos (ej: Twitter, OCR).

### Representación de secuencias

En lugar de un bag-of-N-grams, algunos modelos utilizan representaciones secuenciales (listas ordenadas de N-gramas) como entrada para modelos secuenciales como [Modelos Ocultos de Markov](https://www.geeksforgeeks.org/machine-learning/hidden-markov-model-in-machine-learning/), [RNNs](https://www.geeksforgeeks.org/understanding-rnn-recurrent-neural-network/) o [Transformers](https://www.geeksforgeeks.org/machine-learning/getting-started-with-transformers/).

*Fuente: [Guía completa de ingeniería de características con N-gramas en PLN](https://www.linkedin.com/pulse/comprehensive-guide-feature-engineering-n-grams-david-adamson-mbcs)*

## Aplicaciones de los N-gramas

Los N-gramas son fundamentales en numerosas tareas de PLN y automatización de IA:

- **Modelado de lenguaje:**Predicen la próxima palabra en una oración, impulsando el autocompletado, escritura predictiva y respuestas de chatbots.
- **Clasificación de texto:**Extracción de características para categorizar documentos (temas, sentimiento). Bigramas como "no bueno" mejoran los clasificadores de sentimiento.
- **Reconocimiento de voz:**Modelan secuencias de palabras para mejorar la precisión de transcripción.
- **Corrección ortográfica:**Sugiere correcciones basadas en secuencias de palabras probables (ej: "forma" vs. "forma").
- **Traducción automática:**Los sistemas estadísticos de traducción utilizan probabilidades de N-gramas para construir frases en el idioma destino.
- **Recuperación de información:**Los motores de búsqueda emplean N-gramas para indexar y clasificar documentos.
- **Detección de plagio:**Detectan secuencias superpuestas en documentos.
- **Autocompletado/escritura predictiva:**Sugieren las siguientes palabras a medida que el usuario escribe, usando secuencias frecuentes de N-gramas.

**Ejemplos concretos:**- En análisis de sentimiento, bigramas como "muy bueno" o "mala calidad" indican fuertemente sentimiento positivo o negativo.
- Las sugerencias de búsqueda de Google se basan en el análisis de trigramas frecuentes: al escribir "cómo", sugiere "cómo cocinar", "cómo programar", en base a la frecuencia de N-gramas.

*Fuente: [GeeksforGeeks: N-gram in NLP](https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/)*

## Temas avanzados

### Escasez de datos y dimensionalidad

Con valores altos de *n*, el número de posibles N-gramas aumenta exponencialmente. Por ejemplo, un vocabulario de 10,000 palabras produce:

- 10,000 unigramas
- 100,000,000 bigramas
- 1,000,000,000,000 trigramas

Esto provoca:
- **Escasez de datos:**Muchos N-gramas nunca aparecen en el corpus.
- **Alta dimensionalidad:**El almacenamiento y computo se vuelven un reto.

### Backoff e interpolación en N-gramas

**Backoff:**Si un N-grama de orden superior