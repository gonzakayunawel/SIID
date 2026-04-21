### 1.4. Método de Análisis Estocástico para la Toma de Decisiones (MAET)

Para facilitar la transferencia tecnológica de los conceptos probabilísticos a proyectos de gestión, se propone el Método de Análisis Estocástico para la Toma de Decisiones (MAET). El método se apoya en la teoría de probabilidades y el análisis estocástico para abordar el análisis de la dinámica de sistemas de gestión. Mientras que el análisis proba- bilístico suele enfocarse en eventos estáticos o aislados, el análisis estocástico se ocupa de procesos que evolucionan en el tiempo. En entornos como la cadena de valor industrial, las variables no son fijas, sino que constituyen una sucesión de estados aleatorios interdependientes. Por tanto, el término estocástico subraya la importancia del flujo, la secuencia y la evolución temporal. El método se estructura en cuatro fases:

#### Fase I: Arquitectura del Sistema (Identificación de Variables)

Esta fase consiste en la formalización matemática del dominio de estudio. Se define el espacio muestral como el conjunto de todos los estados posibles del sistema y se seleccionan las variables aleatorias (discretas o continuas) que permiten caracterizar su comportamiento.

Fundamento: Identificación de la distribución de probabilidad subyacente (PMF/PDF) de los observables.

Objetivo: Establecer una línea base de datos estocásticos para el monitoreo de la operación.

#### Fase II: Mapeo de Riesgos (Intersección de Eventos)

En esta etapa se cuantifica la probabilidad de ocurrencia de escenarios críticos. Se utilizan operaciones de conjuntos para definir estados de fallo, centrando el análisis en la probabilidad conjunta y la intersección de eventos.

Fundamento: Evaluación de la independencia estadística entre variables y cálculo de probabilidades de eventos compuestos.

Objetivo: Determinar las configuraciones de variables que resultan en la pérdida de continuidad operativa o saturación de capacidad.

#### Fase III: Motor de Inferencia (Actualización Bayesiana)

Se implementa un modelo de diagnóstico basado en el Teorema de Bayes. Esta fase permite calcular la probabilidad a posteriori de un evento no observable (estado crítico futuro) a partir de evidencia observable en tiempo real.

Fundamento: Aplicación de probabilidad condicional para la actualización de niveles de confianza ante nuevos datos.

Objetivo: Transformar señales tempranas en indicadores de riesgo cuantitativos para la toma de decisiones proactiva.

#### Fase IV: Análisis de Flujo (Modelamiento de Tiempos de Ciclo)

Se analiza la dimensión temporal del sistema mediante la convolución de variables aleatorias. Esta fase modela procesos secuenciales donde el tiempo total es la suma de etapas independientes con distintas tasas de llegada o servicio.

Fundamento: Uso de distribuciones Gamma, Erlang o Hipoexponenciales para re- presentar la acumulación de retardos.

Objetivo: Identificar cuellos de botella estocásticos y optimizar la capacidad de respuesta del sistema frente a la variabilidad de la demanda.

```
    | Mapeo de Observables                    | Escensarios Críticos              | Diagnóstico Proactivo                | Optimización de Capacidad

    [I. Arquitectura del Sistema]     -->     [II. Mapeo de Riesgos]      -->      [III. Motor de Inferencia]     -->    [IV. Análisis de Flujo]

    | Espacio Muestral y Variables Aleatorias | Eventos Compuestos e Intersección | Prob. Condicional y Teorema de Bayes | Convolución y Tiempos de Ciclo
```