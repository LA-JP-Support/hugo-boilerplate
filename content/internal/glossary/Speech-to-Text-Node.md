+++
title = "Speech-to-Text Node"
translationKey = "speech-to-text-node"
description = "Un nodo de Conversión de Voz a Texto es un componente modular en plataformas de automatización y flujos de trabajo de IA que transcribe lenguaje hablado en texto legible por máquina utilizando ASR."
keywords = ["Nodo de Voz a Texto", "Reconocimiento Automático del Habla", "Flujos de trabajo de IA", "Audio a Texto", "Transcripción"]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Speech-to-Text-Node/"

+++
## Descripción general

Un **nodo de Conversión de Voz a Texto** constituye la base de la [IA conversacional](/es/glossary/conversational-ai/), las cadenas de automatización y los sistemas de flujo de trabajo al convertir el lenguaje hablado en archivos de audio (grabaciones de voz, llamadas o bandas sonoras de videos) en texto estructurado y preciso. Esta transcripción puede luego analizarse, resumirse, traducirse o usarse para activar procesos automáticos adicionales.

**Flujo típico:**
1. Recibe entrada de audio (como archivo subido, URL o variable en el flujo de trabajo).
2. Procesa el audio usando un modelo ASR como [OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text), [Google Speech-to-Text](https://cloud.google.com/speech-to-text), [Azure Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text) o proveedores externos como [Rev AI](https://www.rev.ai/).
3. Entrega una transcripción (opcionalmente con marcas de tiempo a nivel de palabra, etiquetas de hablante o traducciones).

**Función en la automatización:**
- Permite que los chatbots procesen consultas por voz.
- Transcribe reuniones, entrevistas o clases para gestión del conocimiento.
- Automatiza la indexación de contenido y extracción de datos de interacciones de voz o multimedia.
## Capacidades clave

- **Reconocimiento Automático del Habla (ASR):** Convierte audio en texto usando modelos avanzados ([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/), [LiveKit](https://docs.livekit.io/agents/models/stt/), [Rev AI](https://www.rev.ai/)).
- **Soporte multilingüe:** Transcribe voz en múltiples idiomas y dialectos ([Idiomas soportados por Google](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages), [OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text#supported-languages)).
- **Traducción:** Traduce voz que no está en español a español u otros idiomas soportados (según proveedor).
- **Instrucciones de prompt personalizadas:** Acepta instrucciones sobre estilo de transcripción, etiquetas de hablante, terminología o manejo de errores.
- **Entrada de audio flexible:** Acepta archivos subidos, URLs o variables de pasos previos del flujo.
- **Manejo de archivos grandes:** Procesa archivos hasta el límite definido por el proveedor (usualmente 25 MB), con soporte para segmentación de archivos mayores.
- **Marcas de tiempo y diarización de hablantes:** Incluye opcionalmente marcas de tiempo a nivel de palabra/locución y etiquetas de hablante (ver [LiveKit Plugins](https://docs.livekit.io/agents/models/stt/#plugins)).
- **Filtrado de lenguaje inapropiado:** Elimina o enmascara contenido ofensivo según configuración o valores predeterminados del modelo.
- **Vocabulario personalizado y adaptación de modelos:** Mejora el reconocimiento de términos específicos del dominio (ver [Adaptación Google](https://cloud.google.com/speech-to-text/docs/adaptation)).
- **Salida estructurada (JSON):** Devuelve datos en esquemas aptos para procesamiento posterior.

## Cómo funciona

1. **Entrada de audio:**  
   - El nodo recibe un archivo de audio o URL (por ejemplo, de una carga de usuario, almacenamiento en la nube o paso previo del flujo).
   - Los formatos soportados incluyen típicamente MP3, WAV, MP4, M4A, WebM, MPGA y MPEG ([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/), [Rev AI](https://www.rev.ai/)).

2. **Selección de modelo y preprocesamiento:**
   - Elegir el modelo/proveedor ASR (por ejemplo, Whisper, Google, Azure, AssemblyAI, Deepgram).
   - Configurar idioma, traducción y características adicionales (marcas de tiempo, IDs de hablante, prompts personalizados).

3. **Proceso de transcripción:**
   - El motor ASR seleccionado procesa el audio y genera una transcripción en texto.
   - Opcionalmente: traducción, filtrado de lenguaje inapropiado, formato, diarización.

4. **Manejo de salida:**
   - El nodo entrega la transcripción (texto plano o JSON estructurado).
   - La salida es consumida por pasos siguientes—resumen, análisis o retroalimentación al usuario.

**Ejemplo de diagrama:**  
![Flujo de trabajo del nodo de Voz a Texto](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/images/how-audio-to-text-works.png)  
([Fuente: Documentación de Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/))

**Para LiveKit:**  
- [LiveKit Inference](https://docs.livekit.io/agents/models/stt/#inference) ofrece modelos AssemblyAI, Cartesia Ink Whisper y Deepgram Nova con opciones para diferentes idiomas y especialidades.

## Formatos de audio soportados y límites de archivos

- **Formatos de audio:**  
  - M4A, MP3, WebM, MP4, MPGA, WAV, MPEG ([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/), [Google](https://cloud.google.com/speech-to-text/docs/encoding), [Rev AI](https://www.rev.ai/)).

- **Límites de tamaño de archivo:**  
  - Máximo típico: **25 MB** por archivo (varía según proveedor).
  - Archivos más grandes deben dividirse en segmentos ≤25 MB, idealmente en límites de frase para preservar contexto y precisión ([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)).

> **Nota:** Algunas plataformas solo aceptan URLs como entrada por seguridad y escalabilidad.

## Guía de configuración paso a paso

### Ejemplo: Configuración de un nodo de Voz a Texto (Kore.ai)

**Requisitos previos:**
- Acceso a la plataforma de automatización (por ejemplo, [Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/), [LiveKit](https://docs.livekit.io/agents/models/stt/), [Google Cloud](https://cloud.google.com/speech-to-text), [Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text)).
- Clave API o credenciales de integración (si es necesario).
- Archivos de audio alojados en URLs accesibles o provistos mediante carga.

#### 1. Añadir el nodo a tu flujo de trabajo
- Abre tu constructor de automatización (por ejemplo, diseñador de flujo de bots de Kore.ai).
- Ubica y arrastra el nodo **Voz a Texto** (o **Audio a Texto**) a tu flujo.

#### 2. Configurar propiedades del nodo
- **Nombre del nodo:** Asigna un nombre único y descriptivo (ejemplo: “TranscripcionReunion”).
- **Entrada de archivo de audio:** Referencia la variable que contiene la URL del archivo de audio, por ejemplo, `{{context.steps.Start.MeetingAudioUrl}}`.
- **Selección de modelo:** Elige el modelo/proveedor ASR (por ejemplo, OpenAI Whisper, AssemblyAI, Deepgram).
- **Activación de características:** Habilita traducción, marcas de tiempo, diarización de hablantes o filtrado de lenguaje inapropiado según requieras.

#### 3. Definir instrucciones de prompt personalizadas
- Define instrucciones de transcripción (por ejemplo, estilo, etiquetas de hablante, manejo de errores).
- Ejemplo:  
  ```
  Proporcione una transcripción limpia, omitiendo muletillas, con etiquetas de hablante claras y términos técnicos correctos.
  ```

#### 4. (Opcional) Definir esquema JSON para la salida
- Especifica un esquema de respuesta para salida estructurada.
- Ejemplo:
  ```json
  {
    "type": "object",
    "properties": {
      "transcript": {"type": "string"},
      "timestamps": {"type": "array", "items": {"type": "object", "properties": {
        "word": {"type": "string"},
        "start": {"type": "number"},
        "end": {"type": "number"}
      }}}
    }
  }
  ```

#### 5. Conectar rutas de éxito y error
- **En caso de éxito:** Dirige hacia resumen, traducción u otros nodos posteriores.
- **En caso de error:** Dirige hacia manejo de errores o un nodo alternativo.

#### 6. Probar y validar
- Ejecuta el flujo con entradas de prueba.
- Revisa que la salida sea completa y correcta.
- Ajusta la configuración según sea necesario.

**Guía completa:** [Documentación Kore.ai Audio to Text Node](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)

## Parámetros de configuración y funciones avanzadas

| Parámetro         | Descripción                                                          | Ejemplo / Opciones                  |
|-------------------|---------------------------------------------------------------------|-------------------------------------|
| Entrada de audio  | URL o referencia al archivo de audio subido                         | `https://host/path/audio.mp3`       |
| Modelo            | Motor/modelo ASR a utilizar                                         | `OpenAI Whisper-1`, `Chirp 3`, `AssemblyAI Universal-Streaming` |
| Código de idioma  | Idioma para la transcripción (código BCP-47)                        | `es-ES`, `en-US`, `fr-FR`           |
| Traducción        | Habilitar traducción a español (si es soportado)                    | `true` / `false`                    |
| Marcas de tiempo  | Incluir marcas de tiempo a nivel de palabra/locución                | `true` / `false`                    |
| Etiquetas de hablante | Diarización, etiquetar hablantes en audio multi-participante    | `true` / `false`                    |
| Filtro de lenguaje inapropiado | Eliminar o enmascarar palabras ofensivas               | `true` / `false`                    |
| Prompt            | Instrucciones personalizadas para estilo de transcripción            | Ver arriba                          |
| Esquema JSON      | Salida estructurada para procesamiento posterior                     | Ver arriba                          |
| Vocabulario personalizado | Lista de palabras específicas del dominio para sesgar reconocimiento | `["AcmeCorp", "API Gateway"]`      |
| Variable de entrada | Variable de contexto con URL/referencia al archivo de audio         | `{{context.steps.Start.AudioURL}}`  |

> **LiveKit:** [Parámetros avanzados y STT personalizado](https://docs.livekit.io/agents/models/stt/#additional-parameters)

## Formatos de respuesta y manejo de salida

**Tipos de salida:**
- **Texto plano:** Transcripción por defecto.
- **JSON estructurado:** Incluye transcripción, marcas de tiempo, etiquetas de hablante y (opcionalmente) puntajes de confianza.

**Ejemplo de salida:**
```json
{
  "transcript": "Hola, gracias por llamar a AcmeCorp. ¿Cómo puedo ayudarte hoy?",
  "timestamps": [
    { "word": "Hola", "start": 0.0, "end": 0.5 },
    { "word": "gracias", "start": 0.6, "end": 0.8 }
  ],
  "speakers": [
    { "segment": "Cliente", "start": 0.0, "end": 3.0 }
  ]
}
```

- **Rev AI:** Ofrece insights como [análisis de sentimiento](/es/glossary/sentiment-analysis/), extracción de temas, resumen y alineación forzada ([Características de Rev AI](https://www.rev.ai/)).

## Casos de uso comunes

- **Transcripción de reuniones y clases:**  
  Transcribe reuniones, entrevistas o clases en texto consultable e indexable.
- **Automatización de soporte al cliente:**  
  Transcribe interacciones de voz para chatbots, CRM y sistemas de ayuda.
- **Generación de subtítulos y captions:**  
  Genera subtítulos para contenido de video, con alineación de marcas de tiempo.
- **Procesamiento de comandos de voz:**  
  Convierte comandos hablados en texto accionable para apps con voz.
- **Traducción basada en audio:**  
  Transcribe y traduce audio multilingüe para localización y accesibilidad.
- **Documentación médica:**  
  Convierte dictados y consultas médicas en registros clínicos.
- **Análisis de centros de llamadas:**  
  Transcribe llamadas grabadas para aseguramiento de calidad, cumplimiento o analítica.
- **Investigación de mercado:**  
  Transcribe grabaciones de grupos focales o entrevistas para análisis posterior.

- [Casos de uso de Rev AI](https://www.rev.ai/)

## Consejos de integración y mejores prácticas

- **Variables de contexto:** Usa variables para referenciar URLs o datos de audio de forma dinámica.
- **Ingeniería de prompts:** Ajusta instrucciones para etiquetas de hablante, terminología o formato según precisión deseada.
- **Procesamiento por lotes:** Para grandes volúmenes, utiliza modos batch o asincrónicos ([Transcripción por lotes de Google](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription)).
- **Preprocesamiento de audio:** Asegura audio claro, bajo ruido y formato compatible.
- **Segmentación de archivos:** Divide grabaciones largas en pausas lógicas.
- **Adaptación de modelo:** Proporciona listas de vocabulario personalizado para mejor rendimiento en dominios especializados ([Adaptación Google](https://cloud.google.com/speech-to-text/docs/adaptation)).
- **Cumplimiento y privacidad:** Activa filtrado de lenguaje inapropiado y selecciona opciones apropiadas de residencia de datos.

## Manejo de errores y monitoreo de rendimiento

- **Tipos de error:**
  - Formato de archivo no soportado o tamaño excedido.
  - URLs de audio inválidas/inaccesibles.
  - Errores de selección/configuración de modelo.
  - Incompatibilidades en el esquema de salida.

- **Manejo de errores:**
  - Valida la entrada antes de procesar.
  - Implementa lógica de reintentos o flujos alternativos.
  - Registra errores y monitorea mediante dashboards analíticos.

- **Métricas de rendimiento:**
  - Minutos de audio procesados (para seguimiento de costos/uso).
  - Uso de tokens (para sistemas ASR con LLM).
  - Tiempos de respuesta y rendimiento.

- [Dashboard de analítica de modelos Kore.ai](https://docs.kore.ai/agent-platform/settings/monitoring/analytics/model-analytics-dashboard/)  
- [Monitoreo de Google Speech-to-Text](https://cloud.google.com/monitoring)

## Comparación de proveedores

| Proveedor            | Características clave                                                                  | Idiomas          | Notas / Enlaces |
|----------------------|----------------------------------------------------------------------------------------|------------------|-----------------|
| **OpenAI Whisper**   | Multilingüe, traducción al español, ASR robusto, filtrado de lenguaje inapropiado      | 50+              | [Docs Whisper](https://platform.openai.com/docs/guides/speech-to-text) |
| **Google Speech-to-Text** | 125+ idiomas, streaming y batch, diarización, adaptación, filtrado                | 125+             | [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text) |
| **Azure Speech**     | Tiempo real/batch, modelos personalizados, adaptación sectorial, CLI & SDK             | 100+             | [Azure Speech Overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text) |
| **Rev AI**           | Asíncrono y streaming, transcripción humana y automática, insights, bajo WER           | 58+              | [Rev AI](https://www.rev.ai/) |
| **LiveKit**          | Modelos conectables (AssemblyAI, Cartesia, Deepgram), selección automática de modelo    | Según modelo     | [LiveKit STT](https://docs.livekit.io/agents/models/stt/) |
| **VectorShift**      | Flujos basados en nodos, entrada variable/subida, integración LLM                      | Según proveedor  | [VectorShift Docs](https://docs.vectorshift.ai/platform/pipelines/multi-modal/speech-to-text) |

## Ejemplos ilustrativos

### Ejemplo 1: Nodo de transcripción de reuniones (Kore.ai)

**Prompt:**  
"Usar discurso directo y resaltar vocabulario relacionado con problemas o desafíos."

**Entrada:**
```json
{
  "audioFile": "https://example.com/meeting-2024-06-10.mp3"
}
```

**Salida:**
```
Hablante 1: Estamos teniendo problemas recurrentes con nuestra puerta de enlace API.
Hablante 2: El principal desafío es integrar autenticación externa.
```
([Ejemplo Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/))

### Ejemplo 2: Google Speech-to-Text API (Node.js)

**Ejemplo de código:**
```javascript
const speech = require('@google-cloud/speech');
const client = new speech.SpeechClient();

async function transcribe() {
  const audio = { uri: 'gs://cloud-samples-data/speech/brooklyn_bridge.raw' };
  const config = { encoding: 'LINEAR16', sampleRateHertz: 16000, languageCode: 'es-ES' };
  const request = { audio, config };
  const [response] = await client.recognize(request);
  const transcription = response.results.map(r => r.alternatives[0].transcript).join('\n');
  console.log(`Transcripción: ${transcription}`);
}

transcribe();
```
[Guía completa Google Codelab](https://codelabs.developers.google.com/codelabs/cloud-speech-text-node)

### Ejemplo 3: Uso de modelo STT LiveKit (Python)

```python
from livekit.agents import AgentSession

session = AgentSession(
    stt="assemblyai/universal-streaming:es",
    # ... llm, tts, etc.
)
```
[Documentación de uso LiveKit](https://docs.livekit.io/agents/models/stt/#usage)

## Notas técnicas y casos límite

- **Límites de tokens:** Algunos modelos ASR tienen límites de tokens de entrada (por ejemplo, Whisper: 224 tokens).
- **Casos de audio límite:**  
  - Para archivos cercanos al límite de tamaño, segmentar en límites lógicos.
  - Mantener la integridad de las frases al dividir.
- **Filtrado de lenguaje inapropiado y contenido:**  
  - La eliminación es predeterminada en algunos modelos; configurable en otros.
- **Diarización de hablantes:**  
  - No es soportada universalmente—verificar con el proveedor