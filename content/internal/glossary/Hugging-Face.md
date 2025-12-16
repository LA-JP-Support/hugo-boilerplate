+++
title = "Hugging Face"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "hugging-face"
description = "Explora Hugging Face, la plataforma de IA de código abierto y comunidad global para democratizar el aprendizaje automático. Descubre modelos, conjuntos de datos y herramientas para PLN, visión por computadora y más."
keywords = ["modelos hugging face", "grandes modelos de lenguaje", "librería transformers", "model hub", "datasets huggingface"]
category = "Infraestructura y Despliegue de IA"
type = "glosario"
draft = false
url = "/internal/glossary/Hugging-Face/"

+++
## ¿Qué es Hugging Face?

Hugging Face es una plataforma de IA de código abierto y una comunidad global centrada en democratizar el aprendizaje automático y la inteligencia artificial. Ofrece un ecosistema integrado para compartir, descubrir y desplegar modelos de aprendizaje automático, conjuntos de datos y aplicaciones en áreas como [procesamiento del lenguaje natural (PLN)](/es/glossary/natural-language-processing--nlp-/), visión por computadora, audio e IA multimodal.

- **Misión:** Hacer que la IA sea accesible y transparente para todos.
- **Enfoque:** Bibliotecas de código abierto, colaboración en modelos y conjuntos de datos, y herramientas de despliegue sin fricciones.
- **Impacto:** Hugging Face apoya a millones de usuarios, cuenta con más de 2 millones de modelos, más de 500,000 conjuntos de datos y más de 1 millón de aplicaciones de demostración (“Spaces”). Sus recursos ayudan a investigadores, desarrolladores y empresas a construir y desplegar soluciones de IA de última generación, acelerando la innovación y el desarrollo responsable de IA.

Hugging Face funciona como un “GitHub para IA”, permitiendo que cualquiera colabore, contribuya o aproveche modelos y datos preentrenados para aplicaciones avanzadas de IA.

- [Sitio Oficial de Hugging Face](https://huggingface.co/)


### Modelo
Un artefacto de aprendizaje automático entrenado para realizar una tarea específica, como clasificación de texto, reconocimiento de imágenes o conversión de voz a texto. Los modelos de Hugging Face pueden estar preentrenados (entrenados con datos públicos) o afinados (adaptados a un conjunto de datos o tarea específica).

### Model Hub
Un repositorio centralizado en Hugging Face para almacenar, compartir y descubrir modelos de aprendizaje automático. El Model Hub soporta [fichas de modelo](/es/glossary/model-cards/) (documentación), control de versiones, demostraciones en vivo e integración con las principales librerías de ML.

- [Documentación de Model Hub](https://huggingface.co/docs/hub/en/models-the-hub)

### Conjunto de datos
Una colección estructurada de muestras de datos (texto, imágenes, audio, etc.) para entrenar, evaluar o comparar modelos de aprendizaje automático.

### Datasets Hub
Un repositorio de conjuntos de datos seleccionados, que proporciona fichas de datos (documentación), control de versiones, metadatos y acceso programático mediante la librería Datasets.

- [Documentación de Datasets Hub](https://huggingface.co/docs/hub/en/datasets-overview)

### Transformers
Una arquitectura de red neuronal basada en mecanismos de auto-atención, presentada en el artículo "Attention is All You Need" (Vaswani et al., 2017). Ampliamente utilizada en PLN y, cada vez más, en visión, audio y tareas multimodales.

### Librería Transformers
Una librería de Python desarrollada por Hugging Face, que proporciona acceso sencillo a modelos basados en transformers (BERT, GPT, T5, etc.), utilidades para tokenización, entrenamiento e inferencia.

- [Documentación de Transformers](https://huggingface.co/docs/transformers/en/index)

### Tokenizador
Una utilidad que convierte la entrada sin procesar (por ejemplo, texto) en tokens (subunidades léxicas) para el procesamiento del modelo, y decodifica las salidas del modelo a formato legible para humanos.

### Afinado (Fine-Tuning)
El proceso de adaptar un modelo preentrenado a un conjunto de datos o tarea específica, normalmente con entrenamiento adicional.

### Proveedor de Inferencia
Infraestructura en la nube o servicio gestionado integrado con Hugging Face para servir modelos de forma escalable y sin servidor.

- [Documentación de Proveedores de Inferencia](https://huggingface.co/docs/hub/en/models-inference)

### Space
Una aplicación web alojada en Hugging Face, utilizada normalmente para demostraciones interactivas, prototipos y aplicaciones impulsadas por ML. Los Spaces soportan Gradio, Streamlit y frameworks personalizados.

- [Visión general de Spaces](https://huggingface.co/docs/hub/en/spaces-overview)

### Ficha de Modelo
Un archivo de documentación estandarizado que describe el uso previsto de un modelo, los datos de entrenamiento, limitaciones, consideraciones éticas y licenciamiento.

- [Fichas de Modelo](https://huggingface.co/docs/hub/en/model-cards)

### Ficha de Conjunto de Datos
Similar a una ficha de modelo, pero para conjuntos de datos. Describe el origen, estructura, uso previsto y consideraciones éticas del conjunto de datos.

- [Fichas de Conjuntos de Datos](https://huggingface.co/docs/hub/en/datasets-cards)

### LLM (Gran Modelo de Lenguaje)
Un modelo basado en transformers con cientos de millones a miles de millones de parámetros, capaz de generación avanzada de texto, comprensión, traducción y razonamiento.

### ZeroGPU
Una funcionalidad que permite acceso a GPU para Spaces sin que los usuarios tengan que configurar o pagar instancias dedicadas.

### Historial de commits / Versionado
Seguimiento de cambios en modelos, conjuntos de datos y repositorios de código a lo largo del tiempo, soportando la reproducibilidad y la colaboración.

### Modelos/Conjuntos de Datos Restringidos (Gated)
Recursos que requieren aprobación explícita de acceso por parte del autor, a menudo por razones de cumplimiento o licenciamiento.

## Componentes Principales de la Plataforma

### Model Hub

El Model Hub es la plataforma central de Hugging Face para compartir, descubrir y utilizar modelos de aprendizaje automático. Está diseñado para que modelos de alta calidad sean accesibles para todos, acelerando la investigación, el desarrollo y el despliegue en producción.

**Funciones clave:**
- Buscar y filtrar modelos por tarea (por ejemplo, generación de texto, clasificación), arquitectura (por ejemplo, BERT, GPT), conjunto de datos o idioma.
- Fichas de modelo: Documentación completa sobre uso previsto, datos de entrenamiento, limitaciones, sesgos y licenciamiento.
- Versionado: Cada actualización del modelo queda registrada, permitiendo reproducibilidad, retrocesos y colaboración.
- Integración con las principales librerías de machine learning como Transformers, PyTorch, TensorFlow, Flax y JAX.
- Widgets de modelos en el navegador para inferencia interactiva y demostraciones en vivo.
- Estadísticas de descargas, etiquetas y metadatos para obtener información del ecosistema.

**Beneficios:**
- Reducir la necesidad de entrenar desde cero aprovechando modelos preentrenados.
- Acelerar la creación de prototipos y el despliegue en producción.
- Fomentar una IA responsable y ética mediante documentación transparente.

**Ejemplos populares de modelos:**
- BERT, RoBERTa, GPT-2, GPT-3, GPT-4 (PLN)
- Stable Diffusion, DeepSeek, Z-Image-Turbo (Visión/Multimodal)
- Whisper (Voz)
- LLMs de dominio específico (legal, biomédico, código)

**Explorar el Model Hub:**  
- [https://huggingface.co/models](https://huggingface.co/models)

**Subida y Compartición de Modelos:**  
- [Guía para Subir Modelos](https://huggingface.co/docs/hub/en/models-uploading)
- [Checklist para Liberación de Modelos](https://huggingface.co/docs/hub/en/model-release-checklist)

**Descarga y Uso de Modelos:**  
- [Guía para Descargar Modelos](https://huggingface.co/docs/hub/en/models-downloading)
- Ejemplo:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
```

**Widgets para Modelos:**  
Incorpora demostraciones de modelos en páginas web o utiliza widgets en Spaces para pruebas instantáneas.

- [Documentación de Widgets de Modelos](https://huggingface.co/docs/hub/en/models-widgets)

### Datasets Hub

El Datasets Hub es un repositorio de conjuntos de datos seleccionados para investigación y producción en aprendizaje automático, diseñado para accesibilidad, reproducibilidad y cumplimiento normativo.

**Funciones clave:**
- Más de 500,000 conjuntos de datos en PLN, visión por computadora, audio y dominios multimodales.
- Fichas de conjunto de datos: Documentación sobre esquema, origen, uso previsto, licencia y limitaciones.
- Control de versiones y metadatos para rastrear cambios y garantizar reproducibilidad.
- Conjuntos de datos públicos y privados para satisfacer requisitos de privacidad y regulación.
- Data Studio: Exploración interactiva y basada en navegador de los conjuntos de datos.
- Procesamiento y transmisión de datos en tiempo real para ML a gran escala.

**Integración:**
- Librería Datasets de Hugging Face para acceso programático y procesamiento eficiente.
- Soporte para múltiples formatos de datos (CSV, JSON, Parquet, imagen, audio, video).

**Conjuntos de datos populares:**
- Common Crawl, OpenWebText (entrenamiento LLM a escala web)
- SQuAD, MNLI, GLUE (benchmarks de PLN)
- nvidia/PhysicalAI-Autonomous-Vehicles (visión)
- openai/gdpval (evaluación PLN)

**Explorar el Datasets Hub:**  
- [https://huggingface.co/datasets](https://huggingface.co/datasets)

**Documentación de Datasets:**  
- [Documentación de la Librería Datasets](https://huggingface.co/docs/datasets/index)
- [Guía para Añadir Datasets](https://huggingface.co/docs/hub/en/datasets-adding)
- [Fichas de Conjuntos de Datos](https://huggingface.co/docs/hub/en/datasets-cards)

**Ejemplo de uso:**
```python
from datasets import load_dataset
dataset = load_dataset("squad")
print(dataset["train"][0])
```

### Spaces

Spaces es la plataforma de Hugging Face para alojar, compartir y demostrar aplicaciones de aprendizaje automático y apps web interactivas. Spaces permite a individuos y equipos mostrar modelos y experimentos sin preocuparse por el backend o la infraestructura.

**Características:**
- Alojar apps interactivas creadas con Gradio, Streamlit, HTML/JS estático o [Docker](/es/glossary/docker/).
- Integración directa con modelos y conjuntos de datos del Hub.
- [Aceleración por GPU](/es/glossary/gpu-acceleration/) mediante ZeroGPU para demostraciones que requieren computación intensiva.
- Opciones de almacenamiento persistente para apps que requieren retención de datos.
- Modo de desarrollo de Spaces para desarrollo y depuración en vivo.
- Participación de la comunidad mediante likes, etiquetas y compartición.

**Beneficios:**
- Mostrar investigaciones, demostraciones y prototipos a una audiencia global.
- Recoger feedback y fomentar la colaboración.
- Crear un portafolio profesional o compartir recursos de aprendizaje.

**Ejemplos populares de Spaces:**
- [Tongyi-MAI/Z-Image-Turbo (Generación de Imágenes)](https://huggingface.co/spaces/Tongyi-MAI/Z-Image-Turbo)
- [Dream-wan2-2-faster-Pro (Generación de Video)](https://huggingface.co/spaces/dream2589632147/Dream-wan2-2-faster-Pro)

**Explorar Spaces:**  
- [https://huggingface.co/spaces](https://huggingface.co/spaces)

**Documentación de Spaces:**  
- [Visión general de Spaces](https://huggingface.co/docs/hub/en/spaces-overview)
- [Modo de Desarrollo de Spaces](https://huggingface.co/docs/hub/en/spaces-dev-mode)
- [Mejoras de GPU en Spaces](https://huggingface.co/docs/hub/en/spaces-gpus)
- [Almacenamiento en Spaces](https://huggingface.co/docs/hub/en/spaces-storage)

### Proveedores de Inferencia y Endpoints

Los proveedores de inferencia permiten el despliegue escalable y sin servidor de modelos de Hugging Face en infraestructuras en la nube gestionadas. Esto abstrae la complejidad del hardware, escalado y confiabilidad del sistema.

**Cómo funciona:**
- Selecciona un modelo del Hub.
- Elige un proveedor de inferencia (por ejemplo, SambaNova, Replicate, Together AI).
- Despliega y sirve el modelo mediante endpoints de API REST, con autoescalado y monitorización.
- Precios por uso o cuotas gratuitas con suscripción Pro.

**Beneficios:**
- Probar o desplegar modelos rápidamente sin gestionar infraestructura.
- Integrar inferencia ML en sistemas web/móvil/backend.
- Optimizar para coste, velocidad, cumplimiento y localización geográfica.

**Ejemplo de código:**
```python
from huggingface_hub import InferenceClient

client = InferenceClient()
result = client.text_generation("Escribe un poema sobre la IA de código abierto.")
print(result.generated_text)
```

- [Documentación de Proveedores de Inferencia](https://huggingface.co/docs/hub/en/models-inference)
- [Explorar Modelos de Inferencia](https://huggingface.co/inference/models)

### Transformers y Librerías Relacionadas

La librería Transformers es el paquete insignia de código abierto en Python de Hugging Face para trabajar con modelos transformers en diferentes dominios.

**Funciones clave:**
- Cargar, afinar y desplegar cientos de arquitecturas de modelos.
- Compatibilidad con PyTorch, TensorFlow y JAX/Flax.
- Utilidades para tokenización, entrenamiento distribuido, evaluación y cuantización.
- Soporte multimodal (texto, visión, audio).
- Integración con el Hub de Hugging Face para descarga/subida de modelos.
- Tutoriales extensos y referencia de API.

**Otras librerías destacadas:**
- **Datasets:** Carga y procesamiento de datos rápida y eficiente en memoria.
- **Tokenizers:** Tokenización de texto rápida y personalizable.
- **Diffusers:** Implementa modelos de difusión de última generación para IA generativa.
- **Safetensors:** Almacenamiento seguro y de alto rendimiento para pesos de modelos.
- **PEFT:** Afinado eficiente en parámetros para grandes modelos de lenguaje.
- **Gradio:** Crea y comparte interfaces de usuario impulsadas por ML en minutos.
- **TRL:** Entrenamiento de algoritmos de refuerzo para modelos de lenguaje.

- [Documentación de Transformers](https://huggingface.co/docs/transformers)
- [Documentación de Datasets](https://huggingface.co/docs/datasets)
- [Documentación de Diffusers](https://huggingface.co/docs/diffusers)
- [Documentación de Tokenizers](https://huggingface.co/docs/tokenizers)
- [Documentación de Gradio](https://gradio.app/docs/)
- [Documentación de PEFT](https://huggingface.co/docs/peft)
- [Documentación de Safetensors](https://huggingface.co/docs/safetensors)
- [Documentación de TRL](https://huggingface.co/docs/trl)

## Código Abierto y Comunidad

El ecosistema de Hugging Face se basa en principios de código abierto y colaboración comunitaria.

**Colaboración:**
- Publica y comparte modelos, conjuntos de datos y Spaces.
- Pull requests, control de versiones y debates para desarrollo colaborativo.
- Más de 50,000 organizaciones, incluyendo Meta, Google, Amazon, Microsoft y AI2, usan Hugging Face para compartir y desplegar modelos.

**Transparencia:**
- Uso intensivo de fichas de modelos y conjuntos de datos para documentación.
- Seguimiento de versiones, licenciamiento y debates abiertos para un uso responsable.

**Contribuciones:**
- Cualquier persona puede aportar modelos, datasets, mejoras o tutoriales.
- Foros de la comunidad, Discord y eventos (por ejemplo, semana de la comunidad JAX/Flax, talleres) fomentan el intercambio de conocimiento y mentoría.

**Participa:**
- [Regístrate](https://huggingface.co/join)
- [Guía Comunitaria](https://huggingface.co/code-of-conduct)
- [Guía de Contenidos](https://huggingface.co/content-guidelines)
- [Foros de la Comunidad](https://discuss.huggingface.co/)

## Cómo se Usa Hugging Face

### Ejemplos de Flujos de Trabajo

#### 1. Desplegar un Modelo Preentrenado para Generación de Texto

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
result = generator("Hugging Face es", max_length=30)
print(result[0]['generated_text'])
```
- [Pipeline de Generación de Texto](https://huggingface.co/docs/transformers/en/main_classes/pipelines#transformers.TextGenerationPipeline)

#### 2. Afinar un Modelo para Análisis de Sentimiento

```python
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
dataset = load_dataset("imdb")

def tokenize(batch):
    return tokenizer(batch["text"], padding="max_length", truncation=True)

tokenized_dataset = dataset.map(tokenize, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=8,
    num_train_epochs=3,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
)
trainer.train()
```
- [API de Trainer](https://huggingface.co/docs/transformers/en/main_classes/trainer)

#### 3. Compartir un Modelo con la Comunidad

- Crea un nuevo repositorio en el Hub.
- Sube tu modelo y añade una Ficha de Modelo.
- Configura la visibilidad (pública/privada).
- Colabora mediante pull requests, debates y control de versiones.

- [Guía para Compartir Modelos](https://huggingface.co/docs/hub/en/models-uploading)

#### 4. Construir una App Demo en Spaces

- Desarrolla una app Gradio o Streamlit usando tu modelo.
- Sube el código y los requisitos a un Space.
- Comparte tu aplicación mediante una URL pública.

- [Documentación de Spaces](https://huggingface.co/docs/hub/en/spaces-overview)

### Fragmentos de Código

**Descargar un modelo:**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
```

**Acceder a un conjunto de datos:**
```python
from datasets import load_dataset
dataset = load_dataset("squad")
print(dataset["train"][0])
```

**Ejemplo de inferencia vía API REST:**
```python
import requests
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_TOKEN"}
payload = {"inputs": "Hugging Face es
