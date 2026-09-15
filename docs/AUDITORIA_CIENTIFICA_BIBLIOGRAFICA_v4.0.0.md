# Auditoría científica y bibliográfica — PDAC Nanotherapeutic Architecture v4.0.0

Fecha de auditoría: 2026-09-15

## Estado de corrección de esta release

Los hallazgos de prioridad alta identificados durante la auditoría se han corregido en el paquete entregado: el solver espacial usa ahora flujos conservativos para `div(D grad C)`; la dimensionalidad del score se explicita como fenomenológica/model-unit con normalización o unidades recíprocas en los pesos; la terminología de la penalización de optimización se cambió a exposición/control; la bibliografía anotada y las referencias señaladas del manuscrito fueron corregidas; se añadieron pruebas del solver y del benchmark analítico de Sobol; y se regeneraron outputs, tests y checksums. Los párrafos de hallazgos que siguen se conservan como trazabilidad de la auditoría original.

## Dictamen ejecutivo

**Estado:** publicable en Zenodo únicamente como *computational proof of concept / research software*, pero recomiendo corregir varios puntos antes de pulsar Publish. No debe describirse como modelo validado, predictor clínico ni optimizador terapéutico clínico.

### Hallazgos de prioridad alta

1. **Inconsistencia PDE–código en difusión espacial.** La documentación declara `∂C/∂t = ∇·(D(x,y)∇C) - ...`, pero `spatial.py` implementa `D(x,y) ∇²C - ...`. Para D espacialmente variable falta el término `∇D·∇C` (o, preferiblemente, una discretización conservativa por flujos en caras). Esto afecta directamente al significado físico del mapa espacial.
2. **Score ferroptótico dimensionalmente no cerrado.** `S=w1/GPX4+w2·ROS+w3·Fe2` combina magnitudes heterogéneas. Es válido como score fenomenológico si las variables se normalizan o si los pesos tienen unidades explícitas y se calibran; no es una ecuación bioquímica universal. El benchmark sintético no resuelve esta identificabilidad.
3. **Parámetros de transporte fenomenológicos sin calibración.** El prefactor `0.5·σ`, `γ=0.85`, `α=1.2`, los rangos de `ξ` y el puente `D_eff/D_ref` son hipótesis del modelo. Deben etiquetarse como tales en tablas/figuras y no atribuirse a Stokes–Einstein ni a una referencia experimental concreta.
4. **Bibliografía del manuscrito contiene una entrada provisional.** La referencia 30 (“Daher B et al... [ferroptosis-related PDAC literature]”) debe sustituirse por la cita completa de Cancer Research 2019, DOI 10.1158/0008-5472.CAN-18-3855.
5. **Bibliografía anotada de 60 referencias contiene entradas incompletas/incorrectas:** #22 sin DOI; #28 con título truncado; #37 con año incorrecto y sin datos bibliográficos; #43 incompleta; #47 sin DOI; #49 ambigua (dos volúmenes); #60 genérica y debe sustituirse por un estudio CPTAC/PDAC concreto.

### Hallazgos de prioridad media

6. `death_probability()` se llama “probability”, pero sin calibración probabilística es una **respuesta logística normalizada**. La documentación ya lo advierte; conviene renombrar la función o reforzar la advertencia.
7. PRCC: implementación correcta en su estructura básica (rangos, regresión residual con intercepto, df=n-k-1), pero los p-valores paramétricos no sustituyen evaluación de monotonicidad, corrección por multiplicidad ni incertidumbre de estructura. El bootstrap ayuda, pero falta un diagnóstico explícito de monotonicidad.
8. Sobol: los estimadores S1 (Saltelli) y ST (Jansen) son coherentes con entradas uniformes independientes. Faltan intervalos de confianza/convergencia para S1/ST. Los índices dependen fuertemente de rangos y distribuciones elegidos.
9. SDE: Euler–Maruyama es apropiado como prototipo, pero el recorte `maximum(...,1e-9)` introduce una condición de positividad artificial que modifica la distribución. Debe documentarse como *positivity clipping*, no como propiedad de la SDE original.
10. Optimización: la penalización `∫u²dt` se denomina `toxicity_weight`, pero no existe un modelo toxicológico. Debe llamarse penalización de exposición/control o dejar explícito que no representa toxicidad biológica.
11. El test de Sobol solo comprueba orden cualitativo de dos variables; conviene añadir comparación contra valores analíticos para el modelo aditivo.
12. Los tests actuales son de verificación/sanity, no validación científica. Se ejecutaron correctamente: **6/6 passed**.

## Revisión por módulo

### Transporte

La ecuación de Stokes–Einstein `D0=kBT/(6πηrH)` es adecuada como referencia para una partícula esférica diluida en un fluido Newtoniano. La extensión estérica exponencial es fenomenológica. La literatura de transporte tumoral y nanomedicina justifica la dependencia del transporte con tamaño, superficie y ECM, pero no valida por sí sola la forma exacta `exp[-γ(rH/ξ)^α]` ni el prefactor 0.5σ.

### Ferroptosis

La dirección cualitativa del modelo es consistente con la literatura: menor capacidad GPX4, mayor estrés oxidativo/lipid peroxidation y hierro lábil favorecen ferroptosis. Sin embargo, ROS total, Fe2 y GPX4 no son intercambiables con estados bioquímicos absolutos; deben tratarse como variables/proxies normalizados. La literatura también muestra defensas paralelas (FSP1, DHODH, GCH1/BH4), por lo que el modelo reducido no debe interpretarse como completo.

### PDAC

Existe soporte PDAC-específico sólido para vulnerabilidad a ferroptosis (p. ej., Badgley 2020 y Daher 2019) y para el papel de la desmoplasia/ECM en entrega terapéutica. Estos trabajos son preclínicos y no demuestran eficacia clínica de la arquitectura propuesta.

### Espacial

La intención física `∇·(D∇C)` es adecuada para difusión con coeficiente heterogéneo, pero el solver actual no implementa exactamente ese operador. **Recomiendo corregir este punto antes de congelar v4.0.0.**

### Calibración y validación

El holdout sintético produce R²≈0.995, RMSE≈0.017 y MAE≈0.014; esto verifica que el procedimiento puede recuperar una relación generada por una familia de modelo muy próxima a la que se ajusta. No mide generalización biológica ni clínica. La separación conceptual calibración/validación está bien documentada.

### Sensibilidad

Resultados reproducidos en esta auditoría:
- PRCC: r_H -0.9407; ξ +0.7367; GPX4 -0.2251; ROS +0.7207; Fe2 +0.5171.
- Sobol S1: r_H 0.7929; ξ 0.0563; GPX4 0.0188; ROS 0.0747; Fe2 0.0329.
- Sobol ST: r_H 0.8273; ξ 0.0499; GPX4 0.0232; ROS 0.1242; Fe2 0.0438.

La dominancia de r_H es un resultado del modelo y de los rangos asumidos, no evidencia de dominancia clínica.

### Optimización

La solución reproducida es aproximadamente `[1,1,1,0.5,0,0,0]` unidades de modelo. Es un óptimo matemático condicionado por ODE, pesos, límites y presupuesto. No es un régimen terapéutico.

## Correcciones bibliográficas verificadas

### Bibliografía anotada `REFERENCIAS_BIBLIOGRAFICAS_60.md`

- **#22** añadir DOI `10.1038/s41420-026-02987-2`.
- **#28** título completo: *Stromal biology and therapy in pancreatic cancer: a changing paradigm*. DOI existente correcto `10.1136/gutjnl-2015-309304`.
- **#37** corregir a: Perry JL, Reuter KG, Kai MP, et al. (2012). *PEGylated PRINT nanoparticles: the impact of PEG density on protein binding, macrophage association, biodistribution, and pharmacokinetics*. Nano Letters 12(10):5304–5310. DOI `10.1021/nl302638g`.
- **#43** completar: Cassani M, Fernandes S, Pagliari S, et al. (2025). *Unraveling the Role of the Tumor Extracellular Matrix to Inform Nanoparticle Design for Nanomedicine*. Advanced Science 12(2):e2409898. DOI `10.1002/advs.202409898`.
- **#47** añadir DOI `10.1080/14786440509463331`; volumen 9(54):781–785.
- **#49** separar/precisar Murray: *Mathematical Biology I: An Introduction*, 3rd ed., Springer, 2002, DOI `10.1007/b98868`; si se usa el volumen espacial, citar también *Mathematical Biology II: Spatial Models and Biomedical Applications* (2003).
- **#60** sustituir la entrada genérica por: Cao L, Huang C, Zhou DC, et al.; Clinical Proteomic Tumor Analysis Consortium. (2021). *Proteogenomic characterization of pancreatic ductal adenocarcinoma*. Cell 184(19):5031–5052.e26. DOI `10.1016/j.cell.2021.08.023`.

### Bibliografía del manuscrito DOCX

- **#2** es real y actual: Siegel RL, Kratzer TB, Wagle NS, Sung H, Jemal A. *Cancer statistics, 2026*. CA Cancer J Clin. 2026;76(1):e70043. DOI `10.3322/caac.70043`.
- **#30** sustituir placeholder por: Daher B, Parks SK, Durivault J, et al. (2019). *Genetic Ablation of the Cystine Transporter xCT in PDAC Cells Inhibits mTORC1, Growth, Survival, and Tumor Formation via Nutrient and Oxidative Stresses*. Cancer Research 79(15):3877–3890. DOI `10.1158/0008-5472.CAN-18-3855`.
- **#58** GSE199102 es correcto, pero la publicación asociada debe citarse como Hwang WL, Jagadeesh KA, Guo JA, et al. (2022). *Single-nucleus and spatial transcriptome profiling of pancreatic cancer identifies multicellular dynamics associated with neoadjuvant treatment*. Nature Genetics 54:1178–1191. DOI `10.1038/s41588-022-01134-8`. GSE199102 corresponde al componente GeoMx/DSP; GSE202051 corresponde al snRNA-seq.
- **#59** GSE132956 existe y contiene 10 muestras PDAC y 5 normales por microarray, pero GEO indica “Citation missing”; debe citarse como **dataset GEO**, no como artículo revisado por pares.
- **#60** sustituir la mención genérica CPTAC/PDC por Cao et al. 2021 (DOI anterior) y, en paralelo, conservar PDC como fuente de datos/provenance cuando se use un dataset concreto.

## Coherencia con datos humanos

TCGA-PAAD, GTEx, GEO y CPTAC/PDC están correctamente planteados como fuentes futuras. La arquitectura debe mantener: RNA ≠ proteína ≠ actividad; ROS/Fe2 requieren medición/proxy explícito; ξ no se deriva automáticamente de transcriptómica; los accesos concretos deben congelarse antes de validación externa.

## Dictamen para Zenodo

**No recomiendo pulsar Publish todavía** si se pretende que v4.0.0 sea la versión científica congelada. Antes haría como mínimo: (1) corregir el operador espacial; (2) normalizar/explicitar unidades del score; (3) corregir las referencias indicadas; (4) reemplazar el placeholder del manuscrito; (5) regenerar outputs, tests y SHA-256; (6) actualizar ZIP y solo entonces publicar.

Si se mantienen estos puntos sin corregir, el depósito sigue siendo defendible como prototipo computacional, pero contiene una discrepancia matemática real entre documentación y solver y una bibliografía no totalmente normalizada.
