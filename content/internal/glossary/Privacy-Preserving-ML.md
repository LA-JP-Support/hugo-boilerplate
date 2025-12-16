+++
title = "Privacidad en Machine Learning (PPML)"
date = 2025-11-25
lastmod = 2025-12-05
translationKey = "privacy-preserving-machine-learning-ppml"
description = "Descubre el Aprendizaje Automático con Preservación de la Privacidad (PPML), métodos como Privacidad Diferencial, Cifrado Homomórfico, MPC y Aprendizaje Federado, para proteger datos sensibles en modelos de ML."
keywords = ["Aprendizaje Automático con Preservación de la Privacidad", "Privacidad Diferencial", "Cifrado Homomórfico", "Cómputo Multipartito", "Aprendizaje Federado"]
category = "Aprendizaje Automático"
type = "glossary"
draft = false
url = "/internal/glossary/Privacy-Preserving-ML/"

+++
## ¿Qué es el Aprendizaje Automático con Preservación de la Privacidad (PPML)?

El Aprendizaje Automático con Preservación de la Privacidad (PPML) es un término que engloba un conjunto de métodos y arquitecturas de sistemas diseñados para permitir el entrenamiento, despliegue y uso de modelos de aprendizaje automático sin exponer datos sensibles subyacentes. El PPML garantiza que los datos individuales—como información personal identificable (PII), historiales médicos, detalles financieros o información empresarial confidencial—no se filtren, reconstruyan ni vuelvan a identificar, incluso si los adversarios tienen acceso significativo al modelo o sus salidas.

Las tecnologías centrales en PPML incluyen **Privacidad Diferencial**, **Cifrado Homomórfico**, **Cómputo Multipartito Seguro (MPC)** y **Aprendizaje Federado**. Estos métodos permiten a las organizaciones aprovechar el poder del ML cumpliendo con estrictas normativas de privacidad como el [Reglamento General de Protección de Datos de la UE (GDPR)](https://gdpr-info.eu/), HIPAA y CCPA.  
- Introducción en profundidad: [Microsoft Research – Privacy Preserving Machine Learning](https://www.microsoft.com/en-us/research/blog/privacy-preserving-machine-learning-maintaining-confidentiality-and-preserving-trust/)
- Revisión y taxonomía: [arXiv: Privacy-Preserving Machine Learning: Methods, Challenges and Directions](https://arxiv.org/abs/2108.04417)

## ¿Por qué es importante la privacidad en el Aprendizaje Automático?

### Exposición de Datos Sensibles

El aprendizaje automático depende de grandes conjuntos de datos, que a menudo contienen información altamente sensible. Sin salvaguardas de privacidad, estos datos pueden exponerse a través de:
- Acceso directo a datos sin procesar durante la ingestión, preprocesamiento o entrenamiento.
- Filtraciones indirectas a través de modelos entrenados, especialmente en entornos de deep learning donde puede ocurrir overfitting o memorización.
- Acceso no autorizado durante la inferencia mediante APIs o salidas de modelos.

### Riesgos de Filtración de Modelos

La investigación ha demostrado que los modelos entrenados pueden memorizar y filtrar inadvertidamente datos de entrenamiento, incluso cuando el acceso se limita a las APIs del modelo. Los atacantes pueden aprovechar estas vulnerabilidades mediante técnicas de inferencia de membresía, inversión de modelos o extracción de datos de entrenamiento.
- [Ataques de Extracción de Modelos e Inferencia de Membresía](https://arxiv.org/pdf/1804.11238)

### Cumplimiento Normativo

Leyes como el [GDPR](https://gdpr-info.eu/), HIPAA en EE.UU. y otras, regulan estrictamente cómo pueden ser recolectados, procesados y compartidos los datos personales y otros datos sensibles. El incumplimiento puede resultar en graves sanciones legales y financieras.

### ML Colaborativo y Silos de Datos

En sectores como la salud y las finanzas, los datos suelen estar aislados entre organizaciones. El PPML permite análisis colaborativos y construcción de modelos sin comprometer la propiedad de los datos o el cumplimiento.
- [ScienceDirect: Privacy Preserving Machine Learning](https://www.sciencedirect.com/topics/computer-science/privacy-preserving-machine-learning)

## ¿Cómo se utiliza el ML con Preservación de la Privacidad?

Las técnicas de PPML se integran a lo largo del ciclo de vida del ML:

- **Recolección de Datos:** Los datos se anonimizan o seudonimizan antes de ingresar al pipeline de entrenamiento. Se pueden emplear técnicas criptográficas para la agregación segura.
- **Entrenamiento de Modelos:** Los algoritmos de preservación de la privacidad (por ejemplo, DP, MPC, HE) aseguran que el modelo entrenado no pueda filtrar registros individuales.
- **Inferencia del Modelo:** Técnicas como la inferencia cifrada y el control de acceso protegen las entradas y salidas sensibles de usuarios frente a exposiciones no autorizadas.
- **Compartición y Despliegue de Modelos:** Los mecanismos de PPML aseguran que compartir modelos con terceros o desplegarlos en la nube/periferia no implique violaciones de privacidad.

Para una visión estructurada de fases y garantías, ver [arXiv: Privacy-Preserving Machine Learning: Methods, Challenges and Directions](https://arxiv.org/abs/2108.04417).

## Técnicas Clave de PPML

### 1. Privacidad Diferencial (DP)

**Definición:**  
La Privacidad Diferencial es un marco matemáticamente riguroso que cuantifica y limita la información que una computación o modelo revela sobre cualquier punto de datos en su conjunto.
- "Un mecanismo es diferencialmente privado si la eliminación o adición de un solo dato no afecta significativamente la salida." ([Wikipedia: Differential Privacy](https://en.wikipedia.org/wiki/Differential_privacy))

**Mecanismos:**  
- **Inyección de Ruido:** Se añade ruido aleatorio a las consultas de datos o actualizaciones del modelo, dificultando estadísticamente inferir la presencia o ausencia de un registro.
- **Presupuesto de Privacidad (ε):** Controla el equilibrio entre privacidad y utilidad. Un ε más bajo implica mayor privacidad (pero menor utilidad).
- **Composición:** La pérdida de privacidad se acumula a través de múltiples consultas o épocas; se requiere contabilidad cuidadosa.

**Propiedades Clave:**
- Garantías de privacidad demostrables y cuantificables.
- Resiliencia frente a atacantes con información auxiliar.
- Ampliamente adoptada en la industria (por ejemplo, [telemetría](/en/glossary/telemetry/) de Google Chrome, iOS de Apple y Windows de Microsoft).

**Limitaciones:**
- Puede degradar la precisión del modelo, especialmente con ε bajos.
- Contabilidad de privacidad compleja en tareas iterativas o en streaming.

**Lecturas y Herramientas:**
- [Ted Desfontaines: A Glossary of Differential Privacy Terms](https://desfontain.es/blog/differential-privacy-glossary.html)
- [TensorFlow Privacy Toolkit](https://github.com/tensorflow/privacy)
- [Differential Privacy in Practice (MSR)](https://www.microsoft.com/en-us/research/publication/collecting-telemetry-data-privately/)
- [The ABCs of Differential Privacy](https://towardsdatascience.com/abcs-of-differential-privacy-8dc709a3a6b3)

### 2. Cifrado Homomórfico (HE)

**Definición:**  
Técnica criptográfica que permite realizar cálculos directamente sobre datos cifrados, de modo que el resultado descifrado coincide con el resultado de la operación sobre los datos en claro.
- "HE soporta sumas y/o multiplicaciones sobre cifrados, permitiendo computación externalizada con preservación de privacidad." ([Nightfall AI: Homomorphic Encryption](https://www.nightfall.ai/ai-security-101/homomorphic-encryption))

**Tipos:**
- **Cifrado Homomórfico Parcial (PHE):** Sólo soporta una operación (aditiva o multiplicativa).
- **Cifrado Homomórfico Parcial (SHE):** Soporta operaciones limitadas.
- **Cifrado Homomórfico Completo (FHE):** Permite cualquier cálculo sobre cifrados.

**Aplicaciones en ML:**
- Los propietarios de datos cifran datos sensibles y los comparten con un servidor para entrenamiento o inferencia.
- El servidor opera sobre datos cifrados; sólo el propietario puede descifrar los resultados.

**Ventajas:**
- Los datos permanecen cifrados de extremo a extremo; no hay exposición de datos en claro.
- Permite externalizar cálculos de forma segura (nube o terceros).

**Limitaciones:**
- Muy intensivo computacionalmente (especialmente FHE).
- Práctico para modelos simples; la investigación avanza en eficiencia.

**Lecturas y Herramientas:**
- [Apple ML Research: Homomorphic Encryption](https://machinelearning.apple.com/research/homomorphic-encryption)
- [Microsoft SEAL Homomorphic Encryption Library](https://github.com/Microsoft/SEAL)
- [Exploring FHE and Concrete-ML](https://medium.com/@clusterprotocol.io/exploring-the-world-of-fully-homomorphic-encryption-fhe-and-concrete-ml-a-step-towards-934d9478a3ac)

### 3. Cómputo Multipartito Seguro (MPC)

**Definición:**  
Enfoque criptográfico que permite que múltiples partes computen conjuntamente una función sobre sus datos privados, sin revelar esos datos entre sí.
- "Los protocolos MPC permiten computar sobre datos distribuidos, garantizando privacidad incluso entre partes desconfiadas entre sí." ([GeeksforGeeks: Secure Multiparty Computation](https://www.geeksforgeeks.org/blogs/what-is-secure-multiparty-computation/))

**Cómo Funciona:**
- Cada parte cifra o comparte secretamente sus datos.
- El cálculo conjunto se realiza con protocolos como circuitos ofuscados o Shamir’s Secret Sharing.
- Sólo se revela el resultado; las entradas individuales permanecen secretas.

**Casos de Uso:**
- Detección colaborativa de fraude entre bancos sin exponer datos de clientes.
- Análisis médicos seguros entre hospitales.

**Ventajas:**
- Diseño de protocolos flexible para escenarios ML diversos.
- Privacidad fuerte incluso en entornos adversarios.

**Limitaciones:**
- Mayor carga computacional y de comunicación.
- Requiere sincronización entre participantes.

**Lecturas y Herramientas:**
- [Cyfrin: Multi-Party Computation (MPC) Overview](https://www.cyfrin.io/blog/multi-party-computation-secure-private-collaboration)
- [EzPC: Easy Secure Multi-Party Computation](https://www.microsoft.com/en-us/research/project/ezpc-easy-secure-multi-party-computation/)
- [What is MPC? Medium](https://medium.com/openware/what-is-multi-party-computation-mpc-c108ca10e15d)

### 4. Aprendizaje Federado (FL)

**Definición:**  
Paradigma ML distribuido donde los modelos se entrenan colaborativamente en dispositivos u organizaciones descentralizadas, sin centralizar los datos en bruto.
- "El aprendizaje federado permite entrenar modelos en datos distribuidos, mejorando la privacidad y reduciendo la transferencia de datos." ([IBM Research: What is Federated Learning?](https://research.ibm.com/blog/what-is-federated-learning))

**Cómo Funciona:**
- Un modelo global se distribuye a nodos locales (dispositivos, organizaciones).
- Cada nodo entrena el modelo en sus datos locales, enviando sólo actualizaciones del modelo (no datos) a un servidor central.
- El servidor agrega las actualizaciones para refinar el modelo global.

**Ventajas:**
- Los datos en bruto nunca salen del dispositivo u organización.
- Soporta despliegues a gran escala en el mundo real (ej. teclados móviles, salud).

**Limitaciones:**
- Las actualizaciones de modelos pueden filtrar información; suele combinarse con DP.
- Datos no-IID, conectividad poco fiable y nodos rezagados son desafíos.

**Lecturas y Herramientas:**
- [DataCamp: Federated Learning Guide](https://www.datacamp.com/blog/federated-learning)
- [GeeksforGeeks: What is Federated Learning?](https://www.geeksforgeeks.org/machine-learning/collaborative-learning-federated-learning/)

## Modelos de Amenazas y Tipos de Ataques en PPML

### Modelos de Amenaza Comunes

- **Adversario honesto pero curioso:** Sigue el protocolo, pero intenta inferir datos privados.
- **Adversario malicioso:** Se desvía del protocolo para extraer o contaminar datos.
- **Atacante externo:** Busca extraer información sensible del modelo o las comunicaciones.

### Tipos de Ataque Específicos

- **Ataques de Inferencia de Membresía:**  
  Los atacantes determinan si una muestra específica se usó en el entrenamiento (ver [Shokri et al., 2017](https://ieeexplore.ieee.org/document/7958568)).
- **Ataques de Inversión de Modelo:**  
  Reconstrucción de características o datos de entrada a partir de las salidas o gradientes del modelo.
- **Extracción de Datos de Entrenamiento:**  
  Extraer datos de entrenamiento textuales o casi textuales de modelos, especialmente LLMs.
- **Ataques de Envenenamiento:**  
  Manipulación maliciosa de los datos de entrenamiento para inducir filtraciones o comportamientos incorrectos del modelo. ([Property Inference from Poisoning](https://arxiv.org/pdf/2101.11073.pdf))
- **Ataques a Actualizaciones de Modelos:**  
  Inferir datos sensibles comparando el estado del modelo antes y después de actualizaciones ([Analyzing Information Leakage of Updates to Natural Language Models](https://www.microsoft.com/en-us/research/publication/analyzing-information-leakage-of-updates-to-natural-language-models/)).

## Despliegues en la Industria, Kits y Frameworks

### Despliegues en la Industria

- **Microsoft**  
    - [Predicción de texto personalizada en Office](https://insider.office.com/en-us/blog/text-predictions-in-word-outlook)
    - [Telemetría de Windows con Privacidad Diferencial](https://www.microsoft.com/en-us/research/publication/collecting-telemetry-data-privately/)
    - [Viva Insights: Analítica de empleados con DP](https://docs.microsoft.com/en-us/viva/insights/Privacy/differential-privacy)
    - [Análisis seguro de imágenes médicas con CryptFlow](https://www.microsoft.com/en-us/research/publication/secure-medical-image-analysis-with-cryptflow/)
- **Salud:**  
    - Aprendizaje federado para construcción colaborativa de modelos diagnósticos ([IBM Research – Federated Learning](https://research.ibm.com/blog/what-is-federated-learning))
- **Finanzas:**  
    - Modelos de detección de fraude usando MPC entre bancos.

### Kits y Frameworks

- **[TensorFlow Privacy](https://github.com/tensorflow/privacy):** Herramientas de privacidad diferencial para TensorFlow.
- **[PySyft](https://github.com/OpenMined/PySyft):** Aprendizaje federado, DP y MPC para PyTorch/TensorFlow.
- **[Microsoft SEAL](https://github.com/Microsoft/SEAL):** Biblioteca de cifrado homomórfico.
- **[EzPC](https://www.microsoft.com/en-us/research/project/ezpc-easy-secure-multi-party-computation/):** Compilador MPC para código de ML.
- **[ML Privacy Meter](https://github.com/privacytrustlab/ml_privacy_meter):** Kit de evaluación de riesgos de privacidad.
- **[PrivacyML (MIT)](https://www.csail.mit.edu/research/privacyml-privacy-preserving-framework-machine-learning):** Framework general de ML con preservación de privacidad.
- **[PPML-Resource (GitHub)](https://github.com/Ye-D/PPML-Resource):** Lista curada de recursos.

## Compromisos y Limitaciones

- **Utilidad vs. Privacidad:**  
  Mayor privacidad (menor ε, criptografía más fuerte) reduce la precisión del modelo y/o incrementa el ruido.
- **Sobrecarga Computacional:**  
  Las técnicas criptográficas (HE, MPC) siguen siendo intensivas en recursos, especialmente con modelos grandes.
- **Usabilidad:**  
  Integrar estas técnicas en flujos de trabajo ML existentes puede requerir cambios significativos.
- **Cobertura de Amenazas:**  
  Ningún método cubre todos los tipos de ataque; se recomienda defensa en capas.

**Análisis en profundidad de compromisos:**  
- [ScienceDirect: Preserving data privacy in machine learning systems](https://www.sciencedirect.com/science/article/pii/S0167404823005151)
- [IRJET: PPML Techniques, Challenges and Research Directions (PDF)](https://www.irjet.net/archives/V11/i3/IRJET-V11I360.pdf)

## Investigación en Curso y Futuras Direcciones

- **Privacidad Diferencial Avanzada:**  
  Contabilidad de privacidad más precisa y ajuste eficiente de modelos privados ([Differentially private fine-tuning of language models](https://www.microsoft.com/en-us/research/publication/differentially-private-fine-tuning-of-language-models/)).
- **Datos Sintéticos Privados:**  
  Datos sintéticos de alta fidelidad para IA generativa sin filtrar registros reales ([Private Synthetic Data for Generative AI](https://www.microsoft.com/en-us/research/blog/the-crossroads-of-innovation-and-privacy-private-synthetic-data-for-generative-ai/)).
- **Avances en Aprendizaje Federado:**  
  Manejo de datos no-IID, [robustez adversarial](/en/glossary/adversarial-robustness/), integración DP/HE.
- **Computación Confidencial:**  
  Entornos de ejecución confiables basados en hardware (TEE) para ML seguro y escalable ([Azure Confidential Computing](https://azure.microsoft.com/en-us/solutions/confidential-compute/)).
- **Verificación Formal:**  
  Garantías de privacidad de extremo a extremo en el pipeline de ML.
- **Alineación Normativa y de Políticas:**  
  Traducción de garantías técnicas de privacidad en cumplimiento ([EU Trustworthy AI](https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence)).

**Revisiones de Investigación:**  
- [ResearchGate: PPML Techniques, Challenges And Research Directions](https://www.researchgate.net/publication/379244515_Privacy-Preserving_Machine_Learning_Techniques_Challenges_And_Research_Directions)


## Tabla Resumen: Técnicas de PPML

| **Técnica**                   | **Meta de Privacidad**          | **Ventajas**                        | **Limitaciones**                          | **Herramientas/Proyectos Ejemplo**  |
|-------------------------------|---------------------------------|-------------------------------------|-------------------------------------------|-------------------------------------|
| Privacidad Diferencial         | Protección de datos individuales| Garantías matemáticas, escalable    | Pérdida de utilidad, ajuste de ε          | TensorFlow Privacy, PySyft          |
| Cifrado Homomórfico           | Computación sobre datos cifrados| Datos nunca expuestos, privacidad fuerte | Alta carga, operaciones limitadas         | Microsoft SEAL                      |
| Cómputo Multipartito Seguro    | Cómputo colaborativo seguro     | Privacidad fuerte, flexible         | Sobrecarga de comunicación/cómputo        | EzPC, CrypTen                       |
| Aprendizaje Federado          | Sin compartir datos en bruto     | Escalable, colaborativo             | Vulnerable a ataques de inferencia        | PySyft, TensorFlow Federated        |

## Recomendaciones para Practicantes

1. **Realizar Modelado de Amenazas:** Evalúe riesgos de privacidad y vectores de ataque para su caso de uso ML.
2. **Técnicas en Capas:** Combine métodos PPML (por ejemplo, FL + DP) para una protección más sólida.
3. **Monitorear y Medir:** Cuantifique riesgos de privacidad y monitoree filtraciones de información.
4. **Alineación Normativa:** Asegure que los resguardos técnicos cumplen con regulaciones.
5. **Aprovechar Herramientas Abiertas:** Use frameworks open-source para facilitar la adopción.
6. **Mantenerse Actualizado:** Siga la investigación y actualice prácticas conforme evolucionan los métodos.

## Lecturas y Recursos Adicionales

- [Microsoft Research: Privacy Preserving Machine