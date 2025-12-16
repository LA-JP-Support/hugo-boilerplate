+++
title = "NLU Confidence Threshold"
translationKey = "nlu-confidence-threshold"
description = "El umbral de confianza NLU es la puntuación mínima de confianza que un motor NLU requiere para activar una intención específica ante una expresión de usuario. Es central en la IA conversacional."
keywords = ["umbral de confianza NLU", "comprensión del lenguaje natural", "puntuaciones de confianza", "chatbot", "clasificación de intenciones"]
category = "Chatbot de IA & Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/NLU-Confidence-Threshold/"

+++
## Definición

**Umbral de confianza NLU:**  
El [umbral de confianza](/es/glossary/confidence-threshold/) de NLU (Natural Language Understanding) es la puntuación mínima de confianza que un motor NLU requiere para activar una intención específica ante una [expresión](/es/glossary/utterance/) de usuario. Si la puntuación de confianza de la intención principal está por debajo de este umbral, normalmente el NLU activa una lógica de recuperación—como pedir al usuario que reformule, confirmar la intención o derivar a un agente humano. El umbral es ajustable (usualmente 0.0–1.0) y es central para que los sistemas de [IA conversacional](/es/glossary/conversational-ai/) interpreten la entrada y gestionen la incertidumbre.

## 1. ¿Qué es una puntuación de confianza NLU?

Cuando un modelo NLU procesa una expresión de usuario, predice la intención más probable y asigna una puntuación de confianza a cada candidata. Esta puntuación es un escalar (típicamente 0–1) que refleja cuán seguro está el modelo de que la entrada coincide con una intención concreta.

**Ejemplo:**  
Un usuario escribe “Olvidé mi contraseña.” El modelo NLU podría evaluar:
- `ResetPassword` — 0.92
- `ChangeEmail` — 0.12
- `AccountLockout` — 0.08

La intención principal, `ResetPassword`, tiene una puntuación de confianza de 0.92.

**Punto Clave:**  
La puntuación de confianza expresa la certeza interna del modelo sobre su predicción. No es una probabilidad calibrada, sino un valor comparativo para elegir entre intenciones.
## 2. Distinción: Puntuación de Confianza vs. Probabilidad Estadística

**Puntuación de confianza:**  
- Es una métrica interna del motor NLU, no una probabilidad real.
- No está garantizado que esté calibrada ni que sume 1 entre todas las intenciones.
- Indica certeza relativa, no probabilidad absoluta.

**Confianza/Probabilidad estadística:**  
- En estadística, un intervalo de confianza (ej. 95%) define el rango para un resultado.
- La probabilidad estadística está matemáticamente calibrada; las puntuaciones de confianza NLU no.

**Precaución:**  
No interpretes una puntuación de confianza de 0.9 como un 90% de probabilidad de acierto. Trátala como “el modelo está mucho más seguro de esta intención que de las demás ahora mismo.”
## 3. Rol del umbral de confianza en los flujos de chatbots

El umbral de confianza actúa como puerta en la lógica de decisión de la IA conversacional. Determina qué ocurre si el modelo no está suficientemente seguro en su clasificación.

### Flujo típico

1. **El modelo NLU procesa la entrada:**  
   El modelo asigna puntuaciones a todas las intenciones candidatas.

2. **Comparar con el umbral:**  
   Si la puntuación de la intención principal ≥ umbral, se continúa con esa intención.  
   Si no, se activa la lógica de recuperación.

3. **Ejemplos de lógica de recuperación:**
   - Pedir al usuario que confirme la intención detectada.
   - Solicitar al usuario que reformule.
   - Derivar a un agente humano.
   - Activar una intención de recuperación (ej. `AMAZON.FallbackIntent` en Amazon Lex).

**Diagrama (descripción):**  
Entrada de usuario → Modelo NLU → [¿La confianza principal ≥ umbral?] → (Sí: Continuar con la intención) / (No: Recuperación/Confirmación)
## 4. Tipos de umbrales de confianza

Los sistemas NLU pueden implementar varios umbrales para diferentes comportamientos:

- **Umbral de confirmación:**  
  Si la confianza de la intención principal está por debajo de este (pero por encima del de rechazo), el bot pide confirmación, ej. “¿Querías restablecer tu contraseña?”

- **Umbral de rechazo:**  
  Si la confianza está por debajo de este valor, el bot activa la lógica de recuperación, ej. “No entendí eso. ¿Podrías reformular?”

- **Umbral de ambigüedad (opcional):**  
  Si las dos intenciones principales tienen puntuaciones cercanas, el bot puede pedir al usuario que elija.

**Tabla de ejemplo:**

| Tipo de Umbral | Rango de Confianza | Acción del Bot           |
|----------------|--------------------|-------------------------|
| Rechazo        | < 0.2              | Recuperación/Rechazo    |
| Confirmación   | 0.2 – 0.4          | Pedir confirmación      |
| Aceptación     | > 0.4              | Continuar con la intención|
## 5. Cómo se usan los umbrales de confianza

**Uso operacional:**
- **Filtrado de intenciones:**  
  Las intenciones por debajo del umbral no se consideran válidas.
- **Derivación a recuperación:**  
  Si ninguna intención supera el umbral, se activa la intención de recuperación/por defecto.
- **Control de experiencia de usuario:**  
  Los umbrales equilibran rigor (evitar errores) y conveniencia (minimizar avisos innecesarios).

**Ejemplo (Amazon Lex):**  
Si todas las puntuaciones de intenciones están por debajo del umbral, Lex activa `AMAZON.FallbackIntent` y solicita al usuario mayor claridad ([docs](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)).

## 6. Selección y ajuste de umbrales de confianza

### Proceso paso a paso

1. **Reunir datos de prueba anotados:**  
   Usa un conjunto de expresiones reales de usuarios con intenciones conocidas.

2. **Ejecutar predicciones del modelo:**  
   Para cada expresión, obtén las puntuaciones de confianza de intenciones del modelo.

3. **Evaluar en múltiples umbrales:**  
   Para umbrales (ej. 0.0–1.0 en incrementos de 0.05), registra:
   - Aceptaciones correctas (verdaderos positivos)
   - Aceptaciones incorrectas (falsos positivos)
   - Rechazos correctos (verdaderos negativos)
   - Rechazos incorrectos (falsos negativos)

4. **Trazar curva ROC:**  
   La curva ROC (Receiver Operating Characteristic) grafica la tasa de verdaderos positivos frente a la de [falsos positivos](/es/glossary/false-positive/) para diferentes umbrales.

5. **Calcular F1 Score:**  
   F1 combina [precisión y recall](/es/glossary/precision-and-recall/) en una métrica, especialmente útil para conjuntos desbalanceados.

6. **Seleccionar umbral(es):**  
   Elige umbral(es) que equilibren:
   - Fricción de usuario (demasiadas confirmaciones)
   - Precisión (minimizar errores de clasificación)
   - Riesgo de negocio (coste de errores frente a interrupciones)

**Consejo:**  
La criticidad de los errores puede justificar umbrales más altos o bajos. En dominios regulados o de alto riesgo, prioriza umbrales altos y confirmaciones.
## 7. Evaluación técnica: métricas y herramientas

**Métricas:**
- **Precisión:**  
  Proporción de intenciones aceptadas correctas.
- **Recall:**  
  Proporción de intenciones correctas aceptadas.
- **F1 Score:**  
  Media armónica de precisión y recall.

**Visualización:**
- **Curva ROC:**  
  Para clasificación binaria de intenciones.
- **Gráficas personalizadas:**  
  Para sistemas multiclase, grafica aceptaciones y rechazos correctos/incorrectos por umbral.

**Ejemplo de gráfico (descripción):**  
Gráficas de líneas mostrando:
- Aceptación correcta (verdadero positivo)
- Aceptación incorrecta (falso positivo)
- Rechazo correcto (verdadero negativo)
- Rechazo incorrecto ([falso negativo](/es/glossary/false-negative/))
## 8. Variaciones entre motores NLU

Distintos motores NLU tienen enfoques únicos para puntuaciones y umbrales de confianza:

- **Amazon Lex:**  
  Devuelve puntuaciones por intención. Permite fijar un umbral personalizado por idioma. Se activa recuperación si todas las puntuaciones están por debajo del umbral. [Documentación Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)

- **Genesys:**  
  El umbral por defecto es 0.4 (40%). Si la intención principal está por debajo, se usa la intención de recuperación/Ninguna.
  [Buenas prácticas Genesys](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)

- **ServiceNow:**  
  Los umbrales de confianza determinan qué intención se activa. Actualizaciones del modelo pueden cambiar la distribución de puntuaciones, requiriendo revisión de umbrales.
  [Q&A Comunidad ServiceNow](https://www.servicenow.com/community/developer-forum/how-is-the-nlu-confidence-threshold-calculated/m-p/2142617#M799543)

- **Voiceflow:**  
  Recomienda balancear dataset y probar umbrales en casos reales.
  [Principios de diseño NLU Voiceflow](https://www.voiceflow.com/pathways/5-principles-for-good-natural-language-understanding-nlu-design)

**Precaución:**  
Los umbrales no son portables entre motores. El scoring de cada NLU es único y puede evolucionar.

## 9. Monitoreo y ajuste continuo

**Por qué es necesario el ajuste continuo:**
- **Actualizaciones de modelo:**  
  Retraining o mejoras del NLU pueden desplazar las puntuaciones.
- **Drift del dataset:**  
  El lenguaje y patrones de usuario cambian, afectando la efectividad del umbral.
- **Cambios del motor:**  
  Mejoras del proveedor pueden modificar los umbrales óptimos.

**Mejores prácticas:**
- Re-evaluar periódicamente los umbrales con datos anotados recientes.
- Monitorear métricas (precisión, recall, F1) en producción.
- Ajustar umbrales ante cambios de desempeño o feedback de negocio.
- Probar umbrales tras cambios en el motor NLU, aunque datos/modelo no cambien.
## 10. Ejemplos prácticos y casos de uso

### Ejemplo 1: Chatbot bancario con intenciones solapadas

- **Escenario:**  
  “Consultar saldo” y “Gestionar tarjeta de crédito” comparten expresiones como “¿Cuál es el saldo de mi tarjeta de crédito?”
- **Problema:**  
  El solapamiento de expresiones reduce las puntuaciones de confianza.
- **Solución:**  
  Refinar las expresiones para minimizar solapamiento y ajustar umbrales tras reentrenar.

### Ejemplo 2: Agente virtual en contact center

- **Escenario:**  
  El NLU devuelve varias intenciones con puntuaciones cercanas para “error.”
- **Observación:**  
  “BuscarEnBaseDeConocimientos” y “DarFeedbackAgenteVirtual” devuelven 85%; “GenerarIncidencia” devuelve 70%.
- **Análisis:**  
  El mecanismo de puntuación puede favorecer ciertos patrones. Ajustar umbral y mejorar datos de entrenamiento.

### Ejemplo 3: Recuperación en Amazon Lex

- **Escenario:**  
  Usuario: “Necesito ayuda con mi factura.”
- **Salida NLU:**  
  - “AyudaFacturación” — 0.61
  - “AyudaCuenta” — 0.58
- **Umbral:**  
  Establecido en 0.65.
- **Resultado:**  
  Ambas por debajo del umbral; Lex activa `AMAZON.FallbackIntent`.
## 11. Errores comunes y mejores prácticas

### Errores

- **Umbrales demasiado altos:**  
  Demasiados avisos de recuperación/confirmación, mala experiencia de usuario.
- **Umbrales demasiado bajos:**  
  Acepta intenciones incorrectas, conversaciones desviadas.
- **Asumir portabilidad de umbral:**  
  Umbrales de un motor/dataset no generalizan.
- **Ignorar desbalance del dataset:**  
  Entrenamiento sesgado lleva a puntuaciones sesgadas.
- **No monitorear en producción:**  
  La precisión puede derivarse sin ser detectada.

### Mejores prácticas

- Usar datos representativos y anotados para la evaluación.
- Ajustar umbrales de confirmación y rechazo por separado.
- Visualizar el desempeño según umbrales.
- Balancear los datos de entrenamiento de intenciones.
- Reentrenar y re-evaluar regularmente tras cambios.
- Documentar la justificación para los umbrales elegidos.

**Consejo:**  
En dominios de alto riesgo (ej. salud, finanzas), establece umbrales conservadores y prioriza la confirmación.
## 12. Glosario de términos relacionados

- **Comprensión del Lenguaje Natural (NLU):**  
  IA para extraer intención/entidades de una entrada.
- **Intención:**  
  El objetivo/tarea que busca el usuario (ej. “ResetPassword”).
- **Expresión:**  
  Frase de entrada del usuario.
- **Puntuación de confianza:**  
  Estimación del NLU sobre coincidencia de intención.
- **Recuperación:**  
  Respuesta cuando ninguna intención coincide con suficiente confianza.
- **Curva ROC:**  
  Gráfica de verdaderos positivos vs. falsos positivos según umbral.
- **F1 Score:**  
  Media armónica de precisión y recall.
- **Falso positivo:**  
  El modelo acepta una intención incorrecta.
- **Falso negativo:**  
  El modelo rechaza una intención correcta.
- **Solapamiento de intenciones:**  
  Expresiones similares en distintas intenciones, reduciendo la confianza.

## 13. Referencias y lecturas recomendadas

- [Amazon Lex: Uso de puntuaciones de confianza en intenciones](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)
- [Genesys: Buenas prácticas para construir y probar tu NLU](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)
- [Genesys: Configuración de umbrales de confianza de bots](https://www.genesys.com/blog/post/set-bot-confidence-thresholds)
- [Voiceflow: 5 principios para el diseño NLU](https://www.voiceflow.com/pathways/5-principles-for-good-natural-language-understanding-nlu-design)
- [Q&A Community ServiceNow sobre NLU Confidence Threshold](https://www.servicenow.com/community/developer-forum/how-is-the-nlu-confidence-threshold-calculated/m-p/2142617#M799543)

**Palabras clave relacionadas:**  
comprensión del lenguaje natural nlu, umbrales de confianza, confianza nlu, aprendizaje automático, puntuaciones de confianza, intenciones expresiones, confianza de intención, configuración de confianza, umbral de puntuación de confianza, contact center, falsos positivos, intervalo de confianza, configuración de umbral, afectar confianza, mayor confianza, intenciones entidades, agente virtual, intención usuario, base de conocimientos, ejemplo de intención

Para guías de implementación, detalles de plataforma y mejores prácticas actualizadas, consulta las referencias anteriores y la documentación de tu proveedor NLU.

**Esta página cita y amplía:**

- [Documentación Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)
- [Centro de recursos Genesys](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)
- [Blog de Genesys](https://www.genesys.com/blog/post/set-bot-confidence-thresholds)
- [Diseño NLU Voiceflow](https://www.voiceflow.com/pathways/5-principles-for-good-natural-language-understanding-nlu-design)
- [Q&A Community ServiceNow](https://www.servicenow.com/community/developer-forum/how-is-the-nlu-confidence-threshold-calculated/m-p/2142617#M799543)

Si necesitas más detalle, ejemplos de código o guías prácticas de configuración para un motor NLU específico, consulta la documentación y artículos comunitarios enlazados arriba.