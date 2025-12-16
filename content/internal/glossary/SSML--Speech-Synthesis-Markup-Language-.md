+++
title = "SSML (Speech Synthesis Markup Language)"
translationKey = "ssml-speech-synthesis-markup-language"
description = "SSML es un lenguaje de marcado basado en XML para controlar la salida de voz sintética, incluyendo pronunciación, entonación, ritmo y emoción, utilizado por los principales proveedores de TTS."
keywords = ["SSML", "Lenguaje de Marcado de Síntesis de Voz", "Texto a Voz", "TTS", "W3C", "prosodia", "fonética", "interfaces de voz", "chatbot de IA"]
category = "Chatbot de IA y Automatización / Texto a Voz / Interfaces de Voz"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/SSML--Speech-Synthesis-Markup-Language-/"

+++
## ¿Qué es SSML?

El Lenguaje de Marcado de Síntesis de Voz (SSML) es un estándar de marcado basado en XML, desarrollado y mantenido por el [W3C](https://www.w3.org/TR/speech-synthesis11/). SSML permite a desarrolladores, diseñadores y lingüistas describir con precisión cómo debe reproducirse un texto en voz sintética (generada por máquina). Esto es esencial para aplicaciones que requieren una salida hablada natural, expresiva y adecuada al contexto.

**Características clave:**
- Control detallado sobre la pronunciación (usando alfabetos fonéticos como IPA/XSAMPA)
- Especificación directa de prosodia: tono, velocidad, volumen y énfasis
- Inserción de pausas naturales, estructuración de oraciones y párrafos
- Manejo explícito de contenido especial (fechas, horas, siglas, moneda, números de teléfono)
- Capacidad de alternar entre diferentes voces o idiomas en la misma secuencia
- Inclusión de archivos de audio externos
- Soporte de extensiones específicas de proveedor (por ejemplo, emociones y roles en Amazon Alexa, estilos de voz neuronal en Azure)

**Adopción en la industria:**  
SSML es el estándar de facto para todos los principales proveedores de TTS en la nube, incluyendo:
- [Amazon Alexa Skills Kit](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html)
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs/ssml)
- [Microsoft Azure Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup)
- [IBM Watson Text-to-Speech](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-ssml)
- [Speechify](https://docs.sws.speechify.com/docs/features/ssml)

## Propósito e importancia

### ¿Por qué usar SSML?

Los sistemas de texto a voz (TTS) convierten texto plano en audio hablado. Sin SSML, las salidas de TTS suelen ser robóticas, monótonas y propensas a errores de pronunciación o entonación poco natural. SSML resuelve estos problemas permitiendo al creador:

- **Controlar la prosodia:** Ajustar cómo se pronuncia el texto configurando atributos de tono, velocidad y volumen para lograr una voz más humana.
- **Mejorar la pronunciación:** Corregir pronunciaciones predeterminadas para términos técnicos, nombres de marca o palabras extranjeras usando alfabetos fonéticos o sustituciones.
- **Clarificar contenido especial:** Indicar la lectura explícita de fechas, horas, abreviaturas, números, correos y monedas.
- **Agregar expresividad:** Inyectar énfasis, estilo y matices emocionales mediante atributos o extensiones específicas de proveedor.
- **Mejorar la accesibilidad:** Hacer que la salida de voz sea más clara y comprensible para usuarios que dependen de tecnología asistiva.
- **Insertar pausas y audio:** Usar pausas para imitar el flujo conversacional natural o insertar sonidos/música para mejorar la experiencia del usuario.
- **Cambiar voces o idiomas:** Alternar sin problemas entre diferentes voces, acentos o idiomas en una misma salida.

**Problemas comunes que resuelve:**
- Voz plana y robótica
- Pronunciación incorrecta de palabras poco comunes o ambiguas
- Ritmo o agrupamiento de frases poco natural
- Incapacidad para transmitir emoción o estilo
- Dificultad para entender números, fechas o secuencias especiales

**Notas sobre las plataformas:**
- [Amazon Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html) soporta un subconjunto de SSML de W3C, con etiquetas propias para emoción y estilo.
- [Google Cloud](https://cloud.google.com/text-to-speech/docs/ssml) y [Microsoft Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup) implementan extensiones específicas de proveedor y tecnologías de voz neuronal.

## SSML: Estructura básica y uso

### El elemento raíz: `<speak>`

Todos los documentos SSML válidos comienzan con el elemento raíz `<speak>`, que define los límites del contenido de síntesis de voz. Esto es obligatorio en todos los motores TTS que soportan SSML.

```xml
<speak>
  Bienvenido a tu asistente de IA.
</speak>
```

- **Consejo:** Omitir la etiqueta `<speak>` resultará en errores o el motor TTS renderizará el texto como plano.

**Documentación de proveedores:**  
- [Sintaxis SSML de Google Cloud](https://cloud.google.com/text-to-speech/docs/ssml)
- [Sintaxis SSML de Amazon Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported)
- [Resumen de SSML en Microsoft Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup)

## Etiquetas y características principales de SSML

### Tabla resumen: Etiquetas comunes de SSML

| Etiqueta       | Propósito                                       | Atributos típicos                 | Soportado por                |
|----------------|-------------------------------------------------|-----------------------------------|------------------------------|
| `<speak>`      | Encierra el contenido SSML (raíz)               | N/A                               | Todos los proveedores        |
| `<break>`      | Inserta una pausa                               | `time`, `strength`                | Todos los proveedores        |
| `<prosody>`    | Modifica tono, velocidad, volumen                | `pitch`, `rate`, `volume`         | Todos los proveedores        |
| `<emphasis>`   | Añade énfasis al texto incluido                 | `level`                           | Todos los proveedores        |
| `<say-as>`     | Especifica interpretación de contenido especial | `interpret-as`, `format`, `detail`| Todos los proveedores        |
| `<phoneme>`    | Especifica pronunciación fonética               | `alphabet`, `ph`                  | Todos los proveedores        |
| `<sub>`        | Sustituye el texto incluido por un alias        | `alias`                           | Todos los proveedores        |
| `<audio>`      | Inserta un archivo de audio                     | `src`, `clipBegin`, etc.          | Todos, con limitaciones      |
| `<voice>`      | Cambia características/persona de la voz        | `name`, `language`, `gender`      | Todos los proveedores        |
| `<p>`, `<s>`   | Estructura de párrafos y oraciones              | N/A                               | Todos los proveedores        |
| `<lang>`       | Especifica idioma para el texto incluido        | `xml:lang`                        | Todos los proveedores        |

**Lista completa de etiquetas soportadas:**  
- [Etiquetas SSML soportadas por Amazon Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported)
- [Etiquetas SSML soportadas por Google Cloud](https://cloud.google.com/text-to-speech/docs/ssml#supported_ssml)
- [Etiquetas SSML soportadas por Microsoft Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-structure#ssml-supported-elements)

### Referencia etiqueta por etiqueta y detalles

#### `<speak>`: Elemento raíz

- **Propósito:** Obligatorio como raíz en todos los documentos SSML.
- **Ejemplo:**
    ```xml
    <speak>
      Este es un ejemplo simple de SSML.
    </speak>
    ```
- **Mejor práctica:** Siempre encierre el script SSML completo en etiquetas `<speak>`. Algunos SDKs de proveedor (por ejemplo, Alexa SDKs para Node.js/Java) pueden añadir esto de forma automática, pero el marcado explícito es más seguro para compatibilidad multiplataforma ([fuente](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported)).

#### `<break>`: Insertar pausas

- **Propósito:** Añade una pausa o controla el límite entre palabras o frases.
- **Atributos:**
    - `time`: Duración exacta de la pausa (por ejemplo, "500ms", "2s")
    - `strength`: Intensidad relativa de la pausa ("none", "x-weak", "weak", "medium", "strong", "x-strong")
- **Ejemplo:**
    ```xml
    <speak>
      Por favor espera.<break time="1s"/>Procesando tu solicitud.
    </speak>
    ```
- **Detalles de proveedor:**  
    - Google Cloud y Amazon Alexa soportan los atributos `time` y `strength`, pero los valores máximos/mínimos de pausa pueden variar ([docs Google](https://cloud.google.com/text-to-speech/docs/ssml#break-tag), [docs Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#break)).
    - Microsoft Azure soporta `<break>` para control de pausas ([docs Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-structure#break-element)).

#### `<prosody>`: Control de tono, velocidad, volumen

- **Propósito:** Cambia la expresividad del habla.
- **Atributos:**
    - `pitch`: "x-low", "low", "medium", "high", "x-high", o porcentaje (por ejemplo, "+20%")
    - `rate`: "x-slow", "slow", "medium", "fast", "x-fast", o porcentaje (por ejemplo, "-20%")
    - `volume`: "silent", "x-soft", "soft", "medium", "loud", "x-loud", decibelios (por ejemplo, "-6dB"), o porcentaje
- **Ejemplo:**
    ```xml
    <speak>
      <prosody pitch="high" rate="fast" volume="+20%">
        Esto se pronuncia más agudo, rápido y fuerte.
      </prosody>
    </speak>
    ```
- **Mejor práctica:** Evite valores extremos; los cambios sutiles producen una voz más natural ([buenas prácticas Google](https://cloud.google.com/text-to-speech/docs/ssml#prosody-tag), [buenas prácticas Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#prosody-element)).

#### `<emphasis>`: Resaltar palabras

- **Propósito:** Aumenta o reduce el énfasis en palabras/frases específicas.
- **Atributo:** `level` ("strong", "moderate", "reduced")
- **Ejemplo:**
    ```xml
    <speak>
      Debes <emphasis level="strong">completar</emphasis> la tarea.
    </speak>
    ```
- **Detalles:** Algunos motores TTS pueden interpretar el énfasis de manera diferente, y el uso excesivo puede sonar poco natural ([docs Alexa emphasis](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#emphasis)).

#### `<say-as>`: Interpretar tipo de contenido

- **Propósito:** Indica al TTS leer el texto como un tipo específico (por ejemplo, fecha, hora, moneda, teléfono, caracteres).
- **Atributos:**
    - `interpret-as`: Valores como "cardinal", "ordinal", "characters", "date", "time", "telephone", "currency", "fraction", "unit", "expletive".
    - `format`, `detail`: Para fechas/horas, define la estructura.
- **Ejemplos:**
    - Siglas como caracteres:
        ```xml
        <speak>
          <say-as interpret-as="characters">SSML</say-as>
        </speak>
        ```
    - Fecha:
        ```xml
        <speak>
          <say-as interpret-as="date" format="yyyymmdd" detail="2">20230610</say-as>
        </speak>
        ```
    - Moneda:
        ```xml
        <speak>
          <say-as interpret-as="currency" language="en-US">$19.99</say-as>
        </speak>
        ```
- **Documentación de atributos:**  
  - [Google say-as](https://cloud.google.com/text-to-speech/docs/ssml#say-as-tag)
  - [Amazon Alexa say-as](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#say-as)

#### `<phoneme>`: Pronunciación personalizada

- **Propósito:** Especifica la pronunciación exacta usando alfabetos fonéticos (IPA, XSAMPA, etc.).
- **Atributos:**
    - `alphabet`: Por ejemplo, "ipa", "x-sampa"
    - `ph`: Cadena fonética
- **Ejemplo:**
    ```xml
    <speak>
      <phoneme alphabet="ipa" ph="ˈniːʃ">niche</phoneme>
    </speak>
    ```
- **Mejor práctica:** Use [IPA](https://es.wikipedia.org/wiki/Alfabeto_Fon%C3%A9tico_Internacional) para claridad; valide con [herramientas del proveedor TTS](https://speech.microsoft.com/portal/voicegallery).
- **Docs:** [Google phoneme](https://cloud.google.com/text-to-speech/docs/ssml#phoneme-tag), [Alexa phoneme](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#phoneme)

#### `<sub>`: Sustituir texto

- **Propósito:** Lee el valor del alias en vez del texto incluido.
- **Atributo:** `alias`
- **Ejemplo:**
    ```xml
    <speak>
      Bienvenido al <sub alias="World Wide Web Consortium">W3C</sub>.
    </speak>
    ```
- **Casos de uso:** Nombres de marca, siglas, palabras extranjeras.
- **Docs:** [Google sub](https://cloud.google.com/text-to-speech/docs/ssml#sub-tag), [Alexa sub](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#sub)

#### `<audio>`: Insertar clips de audio

- **Propósito:** Inserta audio grabado en la salida de voz (por ejemplo, efectos, música).
- **Atributo:** `src` (URL HTTPS)
- **Ejemplo:**
    ```xml
    <speak>
      Por favor, escucha este sonido. <audio src="https://www.example.com/sound.mp3">No se puede reproducir el audio.</audio>
    </speak>
    ```
- **Limitaciones de proveedor:**  
  - [Google Cloud](https://cloud.google.com/text-to-speech/docs/ssml#audio-tag): Solo ciertos formatos soportados, pueden aplicar límites de tiempo.
  - [Amazon Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#audio): Máximo 240 segundos, requiere HTTPS, límites de tamaño.
  - [Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-structure#audio-element): Soportado con restricciones.

#### `<voice>`: Cambiar voz o personaje

- **Propósito:** Cambia a una voz, idioma o personaje diferente.
- **Atributos:** `name`, `language`, `gender`
- **Ejemplo:**
    ```xml
    <speak>
      <voice name="en-US-Wavenet-D">Hola, soy la voz predeterminada.</voice>
      <voice name="en-GB-Wavenet-B">Y yo soy una voz británica.</voice>
    </speak>
    ```
- **Extensiones de proveedor:**  
  - Azure soporta [estilos y roles de voz neuronal](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#style-attribute).
  - Alexa soporta [emoción y dominio](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#amazon-emotion).

#### `<p>` y `<s>`: Estructurar texto

- **Propósito:** Define párrafos (`<p>`) y oraciones (`<s>`) para mejorar el ritmo y agrupamiento.
- **Ejemplo:**
    ```xml
    <speak>
      <p>
        <s>Esta es la primera oración.</s>
        <s>Esta es la segunda oración.</s>
      </p>
    </speak>
    ```

#### `<lang>`: Especificar idioma

- **Propósito:** Especifica el idioma de un segmento de texto, permitiendo pronunciación y acento adecuados.
- **Atributo:** `xml:lang`
- **Ejemplo:**
    ```xml
    <speak>
      Aquí hay una palabra en francés: <lang xml:lang="fr-FR">bonjour</lang>.
    </speak>
    ```
- **Nota:** No todas las voces soportan todos los idiomas; revise el [soporte de idiomas del proveedor](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts).

### Extensiones específicas de proveedor

- **Amazon Alexa:**  
  - `<amazon:emotion>`: Añade emoción "excited" o "disappointed" ([docs](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#amazon-emotion)).
  - `<amazon:domain>`: Cambia el estilo de entrega (por ejemplo, "news", "music", "conversational").
- **Microsoft Azure:**  
  - `<mstts:express-as>`: Estilos/roles de voz neuronal ([docs](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#microsoft-extensions)).
- **Speechify:**  
  - `<speechify:style>`: Control de estilo propietario ([docs](https://docs.sws.speechify.com/docs/features/ssml)).

## Ejemplos prácticos de SSML

### Ejemplo 1: Salida TTS integral

```xml
<speak>
  Bienvenido a la demo.
  <break time="500ms"/>
  Tu cita es el
  <say-as interpret-as="date" format="yyyymmdd">20230610</say-as>.
  El monto a pagar es
  <say-as interpret-as="currency" language="en-US">$19.99</say-as>.
  Para asistencia, llama al <say-as interpret-as="telephone">18001234567</say-as>.
  <prosody rate="slow">Gracias por utilizar nuestro servicio.</prosody>
</speak>
```
**Salida esperada:**  
"Bienvenido a la demo. [pausa] Tu cita es el diez de junio de dos mil veintitrés..."