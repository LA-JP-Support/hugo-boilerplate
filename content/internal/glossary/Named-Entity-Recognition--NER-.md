+++
title = "Named Entity Recognition (NER)"
translationKey = "named-entity-recognition-ner"
description = "El Reconocimiento de Entidades Nombradas (NER) identifica y clasifica entidades del mundo real (personas, organizaciones, ubicaciones, etc.) en texto, transformando datos sin procesar en información estructurada."
keywords = ["Reconocimiento de Entidades Nombradas", "NER", "Procesamiento de Lenguaje Natural", "PLN", "Extracción de Entidades"]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Named-Entity-Recognition--NER-/"

+++
## ¿Qué es el Reconocimiento de Entidades Nombradas (NER)?

[El Reconocimiento de Entidades Nombradas (NER)](https://en.wikipedia.org/wiki/Named-entity_recognition) es una tarea central en el [Procesamiento de Lenguaje Natural (PLN)](https://www.ibm.com/think/topics/natural-language-processing), centrada en identificar y clasificar automáticamente entidades del mundo real en texto no estructurado. Las entidades incluyen nombres de personas, organizaciones, ubicaciones, fechas, cantidades, valores monetarios y más. NER transforma texto sin procesar en datos estructurados y legibles por máquina, localizando subcadenas relevantes (menciones de entidades) y asignándolas a categorías predefinidas.

En términos prácticos, los modelos NER procesan datos textuales para extraer y anotar información clave, habilitando aplicaciones como búsqueda, respuesta a preguntas, recomendación de contenido y automatización documental.

**Ejemplo:** 
*"Apple está considerando comprar una startup del Reino Unido por $1 mil millones."*  
Salida de NER:  
- "Apple" → Organización (ORG)
- "U.K." → Entidad geopolítica (GPE)
- "$1 billion" → Dinero (MONEY)

Para un ejemplo visual y más explicación, consulte la [guía de NER de Encord](https://encord.com/blog/named-entity-recognition/).

## ¿Por qué es importante NER?

La mayoría del contenido digital es no estructurado—correos electrónicos, artículos, chats de clientes, publicaciones en redes sociales, historiales médicos, documentos legales y más. NER permite a las máquinas extraer significado factual de estos datos, apoyando una amplia gama de aplicaciones:

- **Búsqueda:**Mejora la relevancia de los resultados indexando entidades nombradas.
- **Recomendación:**Sugiere contenido basado en personas, lugares o productos reconocidos.
- **Automatización:**Extrae datos estructurados de facturas, contratos y formularios.
- **Cumplimiento:**Identifica y oculta información personal identificable (PII).
- **Grafos de conocimiento:**Estructura información para análisis y IA.

**Ejemplo de manejo de ambigüedad:**Los modelos NER analizan el contexto para resolver nombres ambiguos:
- *"Lincoln"* puede referirse a "Abraham Lincoln" (Persona), "Lincoln Motor Company" (Organización) o "Lincoln, Nebraska" (Ubicación).

Para más casos de uso, vea el [resumen de NER de AltexSoft](https://www.altexsoft.com/blog/named-entity-recognition/).

## Conceptos clave y terminología

### Entidad Nombrada (NE)
Un objeto único del mundo real denotado por un nombre propio o una referencia fija.  
**Ejemplos:**“Michelle Obama” (Persona), “Londres” (Ubicación), “Google” (Organización), “$500” (Dinero).

### Tipo de Entidad / Etiqueta / Tag
La categoría asignada a un tramo de entidad, como PER (Persona), ORG (Organización), LOC (Ubicación), DATE, MONEY, etc.

### Detección de Límites de Entidad
El proceso de detectar los índices de inicio y fin de las menciones de entidad en el texto, crucial para nombres de varias palabras y entidades complejas.
- Ejemplo: Extraer correctamente “The George Washington University Hospital” como una sola entidad.

### Esquemas de Etiquetado
Los modelos NER suelen usar esquemas de etiquetado para marcar los límites de las entidades:
- **BIO**(Begin, Inside, Outside): B-ORG, I-ORG, O
- **IOBES**(Inside, Outside, Begin, End, Single): B-ORG, I-ORG, E-ORG, S-ORG, O

**Ejemplos y visuales de etiquetado:**[Encord: Esquemas de etiquetado para NER](https://encord.com/blog/named-entity-recognition/)

### Etiquetado de Partes de la Oración (POS)
Asigna a las palabras su función gramatical (sustantivo, verbo, adjetivo, etc.), a menudo usado como característica para modelos NER.

### Chunking
Agrupa palabras en unidades significativas (por ejemplo, frases nominales), facilitando la identificación de los límites de entidades.

### Embeddings de Palabras
Transforma palabras en vectores numéricos densos (mediante modelos como Word2Vec, GloVe o modelos contextuales como BERT) que capturan relaciones semánticas y sintácticas para aprendizaje automático.

### Diccionarios de Entidades (Gazetteers/Léxicos)
Diccionarios de nombres de entidades conocidas usados para enfoques NER basados en reglas o híbridos.

### Corpus
Gran colección anotada de textos usada para entrenar y evaluar sistemas NER.

## ¿Cómo funciona NER? Flujo de trabajo detallado

El proceso NER comprende varias etapas secuenciales:

### 1. Entrada de texto y preprocesamiento
- **Tokenización:**Divide el texto en palabras, signos de puntuación y símbolos (tokens).
- **Segmentación de oraciones:**Identifica los límites de las oraciones.
- **Normalización:**Minúsculas, stemming o lematización para reducir formas de palabras.

### 2. Extracción de características
Los modelos NER extraen características para informar sobre los límites y la clasificación de las entidades:
- **Morfológicas:**Formas de palabras, prefijos, sufijos, uso de mayúsculas.
- **Sintácticas:**Etiquetas POS, estructura de frases.
- **Semánticas:**Significado contextual, palabras vecinas.
- **Externas:**Coincidencias en diccionarios, patrones de expresiones regulares.

### 3. Detección de límites de entidad
Localiza tramos candidatos que pueden representar entidades, usando señales contextuales y sintácticas.

### 4. Clasificación de entidades
Asigna a cada candidato detectado la etiqueta más probable (por ejemplo, Persona, Ubicación, Organización), usando reglas manuales, modelos estadísticos o aprendizaje profundo.

### 5. Post-procesamiento
- **Entidades solapadas/anidadas:**Resolver cuando las entidades se superponen o anidan (por ejemplo, “University of California, Berkeley”).
- **Resolución de ambigüedades:**Aprovechar el contexto para desambiguar nombres polisémicos.
- **Consistencia:**Garantizar etiquetado consistente dentro y entre documentos.

### 6. Generación de salida
Devuelve resultados estructurados, típicamente como texto anotado, JSON o XML.

**Ejemplo de JSON:**```json
[
  { "text": "Steve Jobs", "type": "PERSON", "startOffset": 0, "endOffset": 10 },
  { "text": "Apple", "type": "ORG", "startOffset": 22, "endOffset": 27 }
]
```

**Lecturas adicionales:**- [Guía NER de Encord](https://encord.com/blog/named-entity-recognition/)
- [IBM: ¿Qué es el Reconocimiento de Entidades Nombradas?](https://www.ibm.com/think/topics/named-entity-recognition)

## Tipos de etiquetas y esquemas de etiquetado en NER

### Etiquetas de entidad comunes

| Etiqueta      | Descripción                                        | Ejemplo                          |
|--------------|----------------------------------------------------|----------------------------------|
| PER          | Persona (individuos, personajes ficticios)          | “Marie Curie”, “Sherlock Holmes” |
| ORG          | Organización (empresas, agencias, grupos)           | “Google”, “Naciones Unidas”      |
| LOC          | Ubicación (montañas, ríos, ciudades, etc.)          | “Monte Everest”, “Nilo”          |
| GPE          | Entidad geopolítica (países, ciudades, estados)     | “Tokio”, “Estados Unidos”        |
| DATE         | Fechas o periodos de calendario                     | “1 de enero de 2022”, “siglo XIX”|
| TIME         | Tiempos o duraciones específicas                    | “5 PM”, “dos horas”              |
| MONEY        | Valores monetarios                                  | “$100”, “€50 millones”           |
| PERCENT      | Porcentajes                                         | “50%”, “la mitad”                |
| FAC          | Instalaciones (edificios, aeropuertos, carreteras)  | “Aeropuerto JFK”, “Puente Golden Gate” |
| PRODUCT      | Productos, vehículos, software                      | “iPhone”, “Boeing 747”           |
| EVENT        | Eventos nombrados (guerras, deportes, desastres)    | “Olimpiadas”, “Huracán Katrina”  |
| WORK_OF_ART  | Libros, películas, pinturas                         | “Mona Lisa”, “Star Wars”         |
| LANGUAGE     | Idiomas                                             | “Inglés”, “Mandarín”             |
| LAW          | Documentos legales, tratados                        | “Tratado de Versalles”           |
| NORP         | Nacionalidades, grupos religiosos o políticos       | “Americano”, “Demócrata”         |

**Para visuales y más detalle:**[Encord: Tabla de etiquetas NER](https://encord.com/blog/named-entity-recognition/)

### Esquemas de Etiquetado

- **BIO (Begin, Inside, Outside):**- B-ORG: Comienzo de una organización
  - I-ORG: Dentro de una organización
  - O: Fuera de cualquier entidad

- **IOBES/IOB2:**Expande BIO con E (Fin) y S (Única) para un control más fino de los límites.

- **Etiquetado anidado/solapado:**Algunos sistemas NER avanzados soportan reconocimiento de entidades anidadas, crucial para textos biomédicos y legales.

**Visuales y ejemplos:**[Encord: Esquemas de etiquetado](https://encord.com/blog/named-entity-recognition/)

## Métodos y enfoques

### 1. Basado en reglas (Patrones/Léxicos)
- Usa diccionarios (gazetteers), expresiones regulares y reglas lingüísticas.
- Rápido e interpretable, pero frágil—requiere actualización manual para nuevas entidades o dominios.
- Efectivo para formatos fijos (números de teléfono, fechas, PII conocidas).
### 2. Aprendizaje automático tradicional
- Aprende de conjuntos de datos anotados utilizando características diseñadas (formas de palabras, POS, contexto).
- Algoritmos populares: Conditional Random Fields (CRF), Hidden Markov Models (HMM), Support Vector Machines (SVM), Árboles de Decisión.
- Puede generalizar a ejemplos no vistos pero requiere datos etiquetados y diseño de características.
- **Más información:**[Stanford NLP CRFClassifier](https://nlp.stanford.edu/software/CRF-NER.html)

### 3. Enfoques de aprendizaje profundo

#### a. Redes Neuronales Recurrentes (RNN, LSTM)
- Aprenden dependencias secuenciales; populares antes de los transformers.
- LSTMs bidireccionales capturan contexto a izquierda y derecha.

#### b. Modelos basados en Transformers (BERT, RoBERTa, GPT, etc.)
- Usan self-attention para modelar dependencias contextuales complejas.
- Pre-entrenados en grandes corpus, afinados con datos NER etiquetados.
- Manejan ambigüedad, contexto, dependencias de largo alcance, subpalabras y entidades anidadas.
- **BERT para NER:**- Sensible al contexto, bidireccional, soporta aprendizaje por transferencia.
  - Soporta etiquetado IOB para entidades de varias palabras.
  - Supera modelos previos en benchmarks estándar.
  - [Cómo hacer NER con BERT: Machine Learning Mastery](https://machinelearningmastery.com/how-to-do-named-entity-recognition-ner-with-a-bert-model/)
  - [Avances recientes en NER: Encuesta arXiv](https://arxiv.org/html/2401.10825v3)
- **Ejemplo de código:**```python
  from transformers import pipeline
  ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy="simple")
  text = "Apple CEO Tim Cook announced new iPhone models in California yesterday."
  entities = ner_pipeline(text)
  for entity in entities:
      print(entity)
  ```

#### c. Modelos de Lenguaje Grandes (LLMs)
- LLMs de propósito general como GPT-4, PaLM y Claude pueden realizar NER vía prompting zero-shot o few-shot.
- Requieren menos datos etiquetados, pero pueden carecer de control fino o especificidad de dominio.

#### d. Adaptación de dominio & Aprendizaje por transferencia
- Afinar modelos pre-entrenados en corpus personalizados (ej. médico, legal) produce NER específico de dominio.

#### e. NER basado en aprendizaje por refuerzo y grafos
- El aprendizaje por refuerzo puede optimizar pipelines NER.
- Enfoques basados en grafos modelan relaciones entre entidades para mayor precisión.
- [Avances recientes: Encuesta NER arXiv](https://arxiv.org/html/2401.10825v3)

## Retos en NER

NER sigue siendo un problema difícil en PLN debido a:

- **Ambigüedad y polisemia:**Palabras con múltiples tipos de entidad (“Amazon”: empresa o río).
- **Detección de límites:**Nombres multi-palabra y entidades anidadas (“Martin Luther King Jr.”, “University of California, Berkeley”).
- **Adaptación de dominio:**Entidades nuevas o raras en dominios especializados (biomedicina, derecho).
- **Lenguaje evolutivo:**Nuevos términos, marcas, jerga o siglas.
- **NER multilingüe:**Manejo de code-switching, diferentes alfabetos o tipos de entidad específicos de idioma.
- **Datos etiquetados escasos:**Anotar grandes corpus es costoso y lento.
- **Entidades anidadas/solapadas:**Entidades dentro de entidades (especialmente en texto biomédico o legal).
- **Ruido e informalidad:**Redes sociales, OCR y transcripciones introducen errores y lenguaje informal.

**Para más desafíos, consulte:**[Encord: Retos en NER](https://encord.com/blog/named-entity-recognition/)  
[arXiv: Avances recientes en NER](https://arxiv.org/html/2401.10825v3)

## Casos de uso y aplicaciones de NER

### 1. Búsqueda y recuperación de información
NER etiqueta artículos y contenido, mejorando la relevancia al distinguir entidades como “Apple” (empresa vs fruta).

### 2. Motores de recomendación
Servicios de streaming recomiendan contenido según entidades extraídas (actores, géneros).

### 3. Automatización documental y RPA
Extrae nombres, fechas y montos de facturas, contratos y formularios para procesamiento automático.

### 4. Construcción de grafos de conocimiento
Crea grafos estructurados de entidades y relaciones a partir de documentos no estructurados, potenciando análisis e IA.

### 5. Cumplimiento y privacidad
Identifica y oculta PII en documentos sensibles para GDPR, HIPAA y otros cumplimientos regulatorios.

  **Ejemplo de redacción:**“Steve Jobs fundó Apple en Cupertino.”  
  → “[PERSON] fundó [ORG] en [LOCATION].”

### 6. Mejora de análisis de sentimiento
Asocia sentimiento con entidades específicas (ej. “desayuno buffet” negativo, “habitación” positivo en reseñas de hoteles).

### 7. Automatización de soporte al cliente
Encamina tickets extrayendo nombres de productos, títulos de cursos o temas de queja.

### 8. NER específico de dominio
Biomedicina (genes, proteínas, enfermedades), legal (casos, estatutos), financiero (tickers, instrumentos), y más.

**Casos de estudio y ejemplos:**- [Aplicaciones NER de AltexSoft](https://www.altexsoft.com/blog/named-entity-recognition/)
- [GeeksforGeeks: Aplicaciones NER](https://www.geeksforgeeks.org/nlp/named-entity-recognition/)

## Implementación práctica: ejemplo paso a paso con spaCy

### Paso 1: Instalar librerías requeridas
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### Paso 2: Cargar el modelo spaCy
```python
import spacy
nlp = spacy.load("en_core_web_sm")
```

### Paso 3: Procesar texto y extraer entidades
```python
content = "Steve Jobs y Steve Wozniak fundaron Apple el 1 de abril de 1976 en Cupertino, California."
doc = nlp(content)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

**Salida de ejemplo:**```
Steve Jobs 0 10 PERSON
Steve Wozniak 15 29 PERSON
Apple 39 44 ORG
April 1, 1976 48 61 DATE
Cupertino 65 74 GPE
California 76 86 GPE
```

### Paso 4: Visualizar entidades
```python
from spacy import displacy
displacy.render(doc, style="ent")
```
![Visualización NER con spaCy](https://www.altexsoft.com/static/blog-post/2024/3/afb1c9bf-f08e-4ad7-a4ec-ad9745dda06d.jpg)

### Paso 5: Convertir entidades a datos estructurados
```python
import pandas as pd
entities = [(ent.text, ent.label_) for ent in doc.ents]
df = pd.DataFrame(entities, columns=['Entity', 'Type'])
print(df)
```

**Resultado:**| Entity           | Type   |
|------------------|--------|
| Steve Jobs       | PERSON |
| Steve Wozniak    | PERSON |
| Apple            | ORG    |
| April 1, 1976    | DATE   |
| Cupertino        | GPE    |
| California       | GPE    |

**Para más tutoriales y ejemplos de código:**- [Documentación de entidades nombradas spaCy](https://spacy.io/usage/linguistic-features#named-entities)
- [MachineLearningMastery: Cómo hacer NER con BERT](https://machinelearningmastery.com/how-to-do-named-entity-recognition-ner-with-a-bert-model/)

## Principales herramientas, librerías y APIs para NER

| Herramienta/Librería                  | Destacados / Mejor para                                      | Idioma(s)      | Referencia |
|-------------------------------        |-------------------------------------------------------------|----------------|-----------|
| [spaCy](https://spacy.io/)            | Rápida, lista para producción, personalizable, modelos preentrenados | Python         | [Docs spaCy](https://spacy.io/usage/linguistic-features#named-entities) |
| [NLTK](https://www.nltk.org/)         | Educativa, NER básica, análisis lingüístico                  | Python         | [Docs NLTK](https://www.nltk.org/) |
| [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) | Estándar académico, RegexNER para reglas, soporte multilenguaje | Java, Python   | [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) |
| [Tonic Textual](https://www.tonic.ai/products/textual) | NER empresarial, redacción, síntesis, modelos personalizados | API, Python SDK| [Tonic Textual](https://www.tonic.ai/products/textual) |
| [DeepPavlov](https://deeppavlov.ai/)  | Aprendizaje profundo, modelos preentrenados, adaptación de dominio | Python         | [DeepPavlov](https://deeppavlov.ai/) |
| [Google Cloud NLP](https://cloud.google.com/natural-language)