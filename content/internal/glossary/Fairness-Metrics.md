+++
title = "Fairness Metrics"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "fairness-metrics"
description = "Las métricas de equidad son herramientas matemáticas y estadísticas utilizadas para cuantificar, evaluar y monitorear el sesgo en sistemas de IA/ML, garantizando un trato equitativo entre grupos."
keywords = ["métricas de equidad", "sesgo en IA", "sesgo algorítmico", "IA responsable", "equidad en aprendizaje automático"]
category = "Ética de IA y Mecanismos de Seguridad"
type = "glossary"
draft = false
url = "/internal/glossary/Fairness-Metrics/"

+++
## **¿Qué son las métricas de equidad?**

Las métricas de equidad son herramientas matemáticas y estadísticas diseñadas para cuantificar, evaluar y monitorear el sesgo en sistemas de inteligencia artificial (IA) y aprendizaje automático (ML). Estas métricas proporcionan formas estructuradas de evaluar si un modelo de IA trata a individuos o grupos de manera equitativa, o si perjudica injustamente a alguien en función de atributos sensibles como raza, género, edad o estatus socioeconómico.

Las métricas de equidad son centrales para el desarrollo responsable de la IA. Permiten a las organizaciones identificar, medir y mitigar el sesgo algorítmico—clave para construir IA confiable, garantizar el cumplimiento normativo y fomentar la aceptación social.

## **¿Por qué se usan las métricas de equidad?**

Los modelos de IA influyen cada vez más en decisiones de contratación, salud, seguridad, finanzas y educación. Sin salvaguardas, estos modelos pueden:

- Perpetuar o amplificar sesgos existentes en los datos de entrenamiento.
- Perjudicar injustamente a ciertos individuos o grupos (por ejemplo, tasas de aprobación de préstamos más bajas para minorías).
- Generar riesgos reputacionales, éticos y legales.

**Las métricas de equidad se utilizan para:**

- Cuantificar y monitorear resultados dispares entre grupos demográficos.
- Identificar y abordar el sesgo algorítmico durante el desarrollo y despliegue del modelo.
- Guiar acciones correctivas como ajustar datos, refinar algoritmos o modificar umbrales de decisión.
- Demostrar [transparencia](/en/glossary/transparency/) y responsabilidad ante partes interesadas, reguladores y el público.
- Garantizar el cumplimiento normativo, incluyendo:
  - [EU AI Act](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)
  - [Ley de Informe Justo de Crédito](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act)
  - [Ley de Igualdad de Oportunidades de Crédito](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/equal-credit-opportunity-act/)
  - [Ley de Responsabilidad Algorítmica (EE.UU.)](https://www.congress.gov/bill/117th-congress/house-bill/6580/text)
  - [GDPR](https://gdpr.eu/)

## **¿Cómo se utilizan las métricas de equidad en la práctica?**

**Flujo de trabajo para el uso de métricas de equidad:**

1. **Recolección y preparación de datos**
   - Recopilar datos demográficos y de atributos sensibles (por ejemplo, género, raza, edad).
   - Garantizar datos representativos para todos los grupos relevantes.
2. **Entrenamiento y evaluación del modelo**
   - Entrenar modelos en conjuntos de datos etiquetados.
   - Evaluar los resultados del modelo entre grupos usando métricas de equidad.
3. **Evaluación del sesgo**
   - Aplicar una o varias métricas de equidad para medir disparidades en los resultados.
   - Analizar subgrupos específicos para identificar dónde ocurre la injusticia.

4. **Mitigación e iteración**
   - Utilizar información de las métricas de equidad para modificar datos, algoritmos o umbrales.
   - Reevaluar e iterar hasta alcanzar niveles aceptables de equidad.
5. **Monitoreo e informes**
   - Monitorear continuamente las métricas de equidad tras el despliegue.
   - Documentar hallazgos y esfuerzos de mitigación para auditorías y cumplimiento.
**Integración con el ciclo de vida del modelo:**

- **Pre-procesamiento:** Abordar el sesgo en los datos antes del entrenamiento (por ejemplo, reponderación, aumento de datos).
- **En procesamiento:** Aplicar restricciones de equidad o regularización durante el entrenamiento del modelo.
- **Post-procesamiento:** Ajustar predicciones o umbrales tras el entrenamiento para obtener resultados más equitativos.

## **Principales tipos de métricas de equidad**

### **1. Paridad Demográfica (Paridad Estadística / Equidad de Grupo)**

- **Definición:** Garantiza que individuos de diferentes grupos demográficos tengan la misma probabilidad de recibir un resultado positivo (por ejemplo, oferta de trabajo, aprobación de préstamo).
- **Fórmula matemática:**  
  P(Resultado = 1 | Grupo A) = P(Resultado = 1 | Grupo B)
- **Casos de uso:**
  - Algoritmos de contratación: Garantizar tasas de selección iguales para hombres y mujeres.
  - Aprobación de préstamos: Tasas de aprobación iguales entre etnias.
- **Limitaciones:**
  - No considera diferencias de calificación entre grupos.
  - La aplicación estricta puede llevar a "discriminación inversa" o menor utilidad.
### **2. Igualdad de Oportunidades**

- **Definición:** Individuos calificados de diferentes grupos tienen la misma probabilidad de recibir un resultado positivo.
- **Fórmula:**  
  P(Resultado = 1 | Calificado = 1, Grupo A) = P(Resultado = 1 | Calificado = 1, Grupo B)
- **Casos de uso:**
  - Admisiones universitarias: Estudiantes igualmente calificados de todos los orígenes tienen tasas de admisión iguales.
  - Promociones internas: Igual oportunidad de promoción para empleados igualmente calificados.
- **Limitaciones:**
  - Depende de una medición precisa y no sesgada de la "calificación".
### **3. Igualdad de Oportunidades en Resultados (Igualdad de Oportunidades)**

- **Definición:** Las tasas de verdaderos positivos y [falsos positivos](/en/glossary/false-positive/) son iguales entre grupos.
- **Fórmula:**  
  - TPR: P(Resultado = 1 | Real = 1, Grupo A) = P(Resultado = 1 | Real = 1, Grupo B)
  - FPR: P(Resultado = 1 | Real = 0, Grupo A) = P(Resultado = 1 | Real = 0, Grupo B)
- **Casos de uso:**
  - Evaluaciones de riesgo en justicia penal: Igual tasa de predicciones correctas e incorrectas para todas las razas.
  - Diagnóstico médico: Tasas de error diagnóstico iguales entre géneros.
- **Limitaciones:**
  - Difícil de lograr; puede entrar en conflicto con otras métricas o con la precisión del modelo.
### **4. Paridad Predictiva (Igualdad Predictiva / Paridad en Valor Predictivo)**

- **Definición:** La precisión (valor predictivo positivo) es igual entre grupos.
- **Fórmula:**  
  P(Real = 1 | Resultado = 1, Grupo A) = P(Real = 1 | Resultado = 1, Grupo B)
- **Casos de uso:**
  - Predicción de impago de préstamos: Igual probabilidad de que los solicitantes aprobados paguen en todos los grupos demográficos.
  - Recomendaciones de tratamientos médicos: Igual precisión al predecir el éxito del tratamiento para todos los grupos de pacientes.
- **Limitaciones:**
  - Puede entrar en conflicto con igualdad de oportunidades o igualdad de resultados.
### **5. Igualdad de Tratamiento**

- **Definición:** La proporción de falsos positivos a falsos negativos es igual entre grupos.
- **Fórmula:**  
  P(Resultado = 1 | Real = 0, Grupo A) / P(Resultado = 0 | Real = 1, Grupo A) =  
  P(Resultado = 1 | Real = 0, Grupo B) / P(Resultado = 0 | Real = 1, Grupo B)
- **Casos de uso:**
  - Policía predictiva: Equilibrar tasas de arrestos falsos y crímenes no detectados.
  - Detección de fraude: Igualar falsas alarmas y fraudes no detectados por segmentos de clientes.
- **Limitaciones:**
  - Complejo de interpretar e implementar.
### **6. Equidad Individual**

- **Definición:** Individuos similares deberían recibir resultados similares del sistema de IA.
- **Medición:** Requiere una métrica de similitud específica de la tarea y análisis de la consistencia del modelo para casos de entrada similares.
- **Casos de uso:**
  - Aprobación de préstamos: Individuos con perfiles financieros similares reciben decisiones similares.
  - Triaje médico: Pacientes comparables reciben recomendaciones consistentes.
- **Limitaciones:**
  - Definir "similitud" es subjetivo y depende del contexto.
### **7. Equidad Contrafactual**

- **Definición:** La predicción de un modelo permanece igual si se cambia un atributo sensible (por ejemplo, raza, género), manteniendo todo lo demás constante.
- **Medición:** Comparar resultados previstos para entradas reales vs. contrafactuales (alteradas).
- **Casos de uso:**
  - Solicitud de préstamo: ¿Cambiaría la decisión si el género del solicitante fuera diferente y todo lo demás igual?
  - Selección de personal: Garantizar que las decisiones no se vean afectadas por atributos protegidos.
- **Limitaciones:**
  - Requiere modelado causal y generación de datos contrafactuales.
## **Ejemplos y casos de uso en el mundo real**

### **Algoritmos de contratación**
- **Problema:** La herramienta de selección de currículums favorece candidatos de un género o etnia específica.
- **Métrica aplicada:** Paridad demográfica, igualdad de oportunidades.
- **Mitigación:** Ajustar datos de entrenamiento, aplicar restricciones de equidad, monitorear tasas de selección.
### **Sistemas de reconocimiento facial**
- **Problema:** Mayores tasas de error para grupos subrepresentados (por ejemplo, personas de color).
- **Métrica aplicada:** Igualdad de resultados.
- **Mitigación:** Diversificar datos de entrenamiento, reentrenar el modelo, auditar disparidades de desempeño.
### **Aprobación de préstamos**
- **Problema:** Tasas de aprobación más bajas para solicitantes minoritarios debido a sesgo histórico.
- **Métrica aplicada:** Paridad predictiva, equidad contrafactual.
- **Mitigación:** Aplicar técnicas de desescalado de sesgo, ajustar umbrales, garantizar cumplimiento normativo.
### **Diagnóstico médico**
- **Problema:** Herramientas de diagnóstico menos precisas para ciertos grupos demográficos.
- **Métrica aplicada:** Igualdad de resultados, igualdad de tratamiento.
- **Mitigación:** Aumentar datos de entrenamiento, monitorear métricas de equidad, involucrar a expertos del dominio.
## **Bibliotecas y herramientas open source de métricas de equidad**

- **[Fairlearn](https://fairlearn.org/):** Librería Python para evaluar y mejorar la equidad de modelos. Incluye métricas, algoritmos de mitigación y visualizaciones.
- **[AIF360 (AI Fairness 360)](https://aif360.res.ibm.com/):** Kit de herramientas de IBM con un amplio conjunto de métricas de equidad y técnicas de [mitigación de sesgo](/en/glossary/bias-mitigation/).
- **[Fairness Indicators](https://www.tensorflow.org/tfx/guide/fairness_indicators):** Herramienta de Google para evaluar y visualizar métricas de equidad, especialmente para modelos TensorFlow.
- **[FairComp](https://www.faircomp.io/):** Biblioteca para comparar intervenciones de equidad y analizar diferentes métricas.
- **[FairML](https://github.com/adebayoj/fairml):** Herramienta para auditar la equidad de modelos e identificar fuentes de sesgo.
- **[Aequitas](https://github.com/dssg/aequitas):** Herramienta de auditoría para analizar el impacto de modelos en grupos demográficos.
- **[Themis](https://github.com/LASER-UMASS/Themis) & [Themis-ML](https://github.com/cosmicBboy/themis-ml):** Bibliotecas enfocadas en equidad individual.

## **Mejores prácticas para el uso de métricas de equidad**

1. **Utilizar múltiples métricas:**  
   Combinar varias métricas para una visión integral de la equidad.
2. **Considerar el contexto:**  
   Adaptar la selección e interpretación de métricas al impacto en la vida real.

3. **Involucrar a las partes interesadas:**  
   Incluir a los grupos afectados, expertos y responsables de decisiones.

4. **Auditorías regulares:**  
   Monitorear continuamente las métricas de equidad tras el despliegue.

5. **Documentar e informar:**  
   Mantener la transparencia registrando análisis de equidad, decisiones y pasos de remediación.

6. **Equilibrar equidad y precisión:**  
   Mejorar la equidad puede reducir la precisión; utilizar optimización multiobjetivo y tomar decisiones informadas.

## **Errores comunes y cómo evitarlos**

- **Depender de una sola métrica:**  
  Rara vez una métrica proporciona una visión completa.
- **Ignorar el contexto social:**  
  Interpretar las métricas dentro del marco social y ético relevante.
- **Evaluación estática:**  
  Reevaluar regularmente a medida que los datos, modelos y poblaciones cambian.
- **Confundir correlación con causalidad:**  
  Las disparidades pueden reflejar desigualdades reales, no solo sesgo del modelo.
- **Descuidar la transparencia:**  
  No documentar puede generar problemas de cumplimiento y pérdida de confianza.

## **Cumplimiento, regulación y estándares de la industria**

**Marcos legales y regulatorios:**

- **[EU AI Act](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence):** Establece requisitos de transparencia, responsabilidad y equidad; exige evaluaciones de riesgo y documentación.
- **[Ley de Informe Justo de Crédito (FCRA)](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act):** Regula el uso de datos de crédito, prohíbe la discriminación en decisiones automatizadas.
- **[Ley de Igualdad de Oportunidades de Crédito (ECOA)](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/equal-credit-opportunity-act/):** Prohíbe la discriminación en decisiones crediticias.
- **[GDPR](https://gdpr.eu/):** Exige transparencia y "derecho a explicación" para decisiones automatizadas en la UE.
- **[Ley de Responsabilidad Algorítmica (EE.UU.)](https://www.congress.gov/bill/117th-congress/house-bill/6580/text):** (Propuesta) Requiere evaluación y reporte de sesgos algorítmicos.

**Guías de la industria:**

- **Comités de ética y responsables de IA:** Supervisión organizacional sobre equidad y sesgo.
- **Estándares de documentación:** Fichas de modelo y hojas de datos registran chequeos de equidad y riesgos.
## **Glosario: términos clave**

- **Sesgo (IA):** Error sistemático en los resultados de IA causado por datos prejuiciados, algoritmos defectuosos o entrenamiento sesgado.
- **Atributo sensible:** Característica demográfica (raza, género, edad) que puede llevar a discriminación si se usa en la toma de decisiones.
- **Impacto dispar:** Las predicciones de un modelo perjudican desproporcionadamente a un grupo protegido, aunque no se usen explícitamente atributos sensibles.
- **Transparencia:** Grado en que las decisiones y procesos de la IA pueden ser entendidos, auditados y explicados.
- **Responsabilidad:** Obligación de justificar y responder por los resultados del sistema de IA, especialmente en relación a la equidad.

## **Lecturas y recursos adicionales**

- [Shelf.io: Fairness Metrics in AI](https://shelf.io/blog/fairness-metrics-in-ai/)
- [Forbes: AI & Fairness Metrics](https://councils.forbes.com/blog/ai-and-fairness-metrics)
- [Google ML Fairness Guide](https://developers.google.com/machine-learning/crash-course/fairness/evaluating-for-bias)
- [AI Evaluation Metrics – Bias & Fairness](https://www.francescatabor.com/articles/2025/7/10/ai-evaluation-metrics-bias-amp-fairness)
- [Documentación de Fairlearn](https://fairlearn.org/)
- [Documentación de AIF360](https://aif360.res.ibm.com/)
- [Resumen del EU AI Act](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)

**Videos:**
- [YouTube: ML Fairness (Google Crash Course)](https://www.youtube.com/watch?v=59bMh59JQDo)
- [YouTube: IA Responsable—Equidad y Sesgo](https://www.youtube.com/watch?v=F03lK5q6ohM)

## **Tabla resumen: métricas comunes de equidad**

| Métrica               | Qué mide                                                  | Fórmula (Simplificada)                                    | Ejemplo de uso                          |
|-----------------------|----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------|
| Paridad Demográfica   | Tasas positivas iguales entre grupos                     | P(Y=1|A=a) = P(Y=1|A=b)                                   | Contratación, Aprobación de Préstamos   |
| Igualdad de Oportunidades | Igual TPR para individuos calificados                | P(Y=1|Y*=1, A=a) = P(Y=1|Y*=1, A=b)                       | Admisiones Universitarias               |
| Igualdad de Resultados   | Igual TPR y FPR entre grupos                         | TPR_a = TPR_b; FPR_a = FPR_b                              | Justicia Penal, Diagnóstico Médico      |
| Paridad Predictiva    | Igual precisión (PPV) entre grupos                       | P(Y*=1|Y=1, A=a) = P(Y*=1|Y=1, A=b)                       | Predicción de Impago de Préstamos       |
| Igualdad de Tratamiento| Misma proporción FP/FN entre grupos                     | Proporción FP/FN_a = Proporción FP/FN_b                   | Policía Predictiva, Detección de Fraude |
| Equidad Individual    | Individuos similares reciben resultados similares        | Distancia(Y(x), Y