# Bibliografía anotada — PDAC Nanotherapeutic Architecture v4.0.0

## Alcance y criterio de uso

Este documento reúne **60 referencias** que sustentan los componentes biológicos, biofísicos, estadísticos y de datos del proyecto. En cada entrada se indica de forma explícita **qué se utiliza en el proyecto**. “Utilizado” significa aquí que el trabajo sirve como fundamento de una ecuación, supuesto, variable, método computacional, estrategia de validación o fuente de datos; **no significa que los valores numéricos del artículo hayan sido copiados al modelo** salvo que se indique expresamente. Los parámetros aún no calibrados con datos humanos se mantienen como hipótesis/modelos fenomenológicos.

---

## A. Ferroptosis, GPX4, ROS, hierro y peroxidación lipídica

### 1. Dixon SJ, et al. (2012). *Ferroptosis: an iron-dependent form of nonapoptotic cell death*. Cell 149:1060–1072. DOI: 10.1016/j.cell.2012.03.042.
**Uso en el proyecto:** fundamento de la definición de ferroptosis como muerte regulada dependiente de hierro y estrés oxidativo; justifica que Fe²⁺ y ROS formen parte del núcleo biológico del modelo.

### 2. Yang WS, et al. (2014). *Regulation of ferroptotic cancer cell death by GPX4*. Cell 156:317–331. DOI: 10.1016/j.cell.2013.12.010.
**Uso en el proyecto:** fundamento para representar GPX4 como variable protectora frente a ferroptosis y para asignar una relación negativa entre actividad/concentración funcional de GPX4 y la salida ferroptótica.

### 3. Stockwell BR, et al. (2017). *Ferroptosis: A Regulated Cell Death Nexus Linking Metabolism, Redox Biology, and Disease*. Cell 171:273–285. DOI: 10.1016/j.cell.2017.09.021.
**Uso en el proyecto:** marco integrador para las relaciones entre metabolismo del hierro, ROS, lípidos y sistemas antioxidantes empleadas en el diseño conceptual del módulo de ferroptosis.

### 4. Dixon SJ, Stockwell BR. (2014). *The role of iron and reactive oxygen species in cell death*. Nature Chemical Biology 10:9–17. DOI: 10.1038/nchembio.1416.
**Uso en el proyecto:** apoyo para modelar conjuntamente hierro redox-activo y ROS como impulsores del daño oxidativo celular.

### 5. Yuan H, Li X, Zhang X, Kang R, Tang D. (2016). *Identification of ACSL4 as a biomarker and contributor of ferroptosis*. Biochemical and Biophysical Research Communications 478:1338–1343. DOI: 10.1016/j.bbrc.2016.08.124.
**Uso en el proyecto:** sustenta la futura extensión del modelo hacia susceptibilidad lipídica/ACSL4 y la interpretación de la peroxidación lipídica como componente mecanístico adicional.

### 6. Kagan VE, et al. (2017). *Oxidized arachidonic and adrenic PEs navigate cells to ferroptosis*. Nature Chemical Biology 13:81–90. DOI: 10.1038/nchembio.2238.
**Uso en el proyecto:** base para tratar la peroxidación de fosfolípidos como variable mecanística futura en las ODE/SDE, en lugar de limitar la salida a un score algebraico.

### 7. Doll S, et al. (2017). *ACSL4 dictates ferroptosis sensitivity by shaping cellular lipid composition*. Nature Chemical Biology 13:91–98. DOI: 10.1038/nchembio.2239.
**Uso en el proyecto:** justifica considerar la composición lipídica como modulador de sensibilidad y como posible covariable para futuras cohortes humanas.

### 8. Friedmann Angeli JP, et al. (2014). *Inactivation of the ferroptosis regulator Gpx4 triggers acute renal failure in mice*. Nature Cell Biology 16:1180–1191. DOI: 10.1038/ncb3064.
**Uso en el proyecto:** evidencia de la función central de GPX4 en el control de peróxidos lipídicos; apoya el signo protector de GPX4 en las ecuaciones.

### 9. Jiang L, et al. (2015). *Ferroptosis as a p53-mediated activity during tumour suppression*. Nature 520:57–62. DOI: 10.1038/nature14344.
**Uso en el proyecto:** soporte para reconocer que la sensibilidad ferroptótica depende de regulación tumoral más amplia; motiva no interpretar GPX4/ROS/Fe²⁺ como mecanismos aislados.

### 10. Zhang Y, et al. (2018). *BAP1 links metabolic regulation of ferroptosis to tumour suppression*. Nature Cell Biology 20:1181–1192. DOI: 10.1038/s41556-018-0178-0.
**Uso en el proyecto:** apoyo para futuras extensiones de regulación de SLC7A11/cistina y para la interpretación de la ferroptosis dentro de redes tumor-supresoras.

### 11. Bersuker K, et al. (2019). *The CoQ oxidoreductase FSP1 acts parallel to GPX4 to inhibit ferroptosis*. Nature 575:688–692. DOI: 10.1038/s41586-019-1705-2.
**Uso en el proyecto:** justifica documentar GPX4 como una defensa principal pero no única; FSP1 es candidato para una futura ampliación multivía del modelo.

### 12. Doll S, et al. (2019). *FSP1 is a glutathione-independent ferroptosis suppressor*. Nature 575:693–698. DOI: 10.1038/s41586-019-1707-0.
**Uso en el proyecto:** apoyo independiente para incorporar en futuras versiones una vía antioxidante paralela a GPX4 y evitar una interpretación excesivamente GPX4-céntrica.

### 13. Kraft VAN, et al. (2020). *GTP cyclohydrolase 1/tetrahydrobiopterin counteract ferroptosis through lipid remodeling*. ACS Central Science 6:41–53. DOI: 10.1021/acscentsci.9b01063.
**Uso en el proyecto:** fundamento para documentar GCH1/BH4 como defensa alternativa y posible variable de expansión de la red ferroptótica.

### 14. Mao C, et al. (2021). *DHODH-mediated ferroptosis defence is a targetable vulnerability in cancer*. Nature 593:586–590. DOI: 10.1038/s41586-021-03539-7.
**Uso en el proyecto:** base para considerar defensa mitocondrial frente a ferroptosis y futuras variables de heterogeneidad celular.

### 15. Lei G, Zhuang L, Gan B. (2022). *Targeting ferroptosis as a vulnerability in cancer*. Nature Reviews Cancer 22:381–396. DOI: 10.1038/s41568-022-00459-0.
**Uso en el proyecto:** marco actualizado para la interpretación oncológica del modelo y para mantener las predicciones como hipótesis terapéuticas, no como eficacia clínica demostrada.

### 16. Li J, et al. (2020). *Ferroptosis: past, present and future*. Cell Death & Disease 11:88. DOI: 10.1038/s41419-020-2298-2.
**Uso en el proyecto:** revisión de mecanismos y biomarcadores empleada para contextualizar variables ferroptóticas y limitaciones del modelo.

### 17. Tang D, Chen X, Kang R, Kroemer G. (2021). *Ferroptosis: molecular mechanisms and health implications*. Cell Research 31:107–125. DOI: 10.1038/s41422-020-00441-1.
**Uso en el proyecto:** soporte para la arquitectura mecanística y para distinguir inducción, defensa y ejecución de ferroptosis.

### 18. Conrad M, Pratt DA. (2019). *The chemical basis of ferroptosis*. Nature Chemical Biology 15:1137–1147. DOI: 10.1038/s41589-019-0408-1.
**Uso en el proyecto:** fundamento químico de oxidación lipídica y radicales; orienta la interpretación de ROS como proxy simplificado y no como descripción química completa.

### 19. Gao M, et al. (2015). *Glutaminolysis and transferrin regulate ferroptosis*. Molecular Cell 59:298–308. DOI: 10.1016/j.molcel.2015.06.011.
**Uso en el proyecto:** apoya la dependencia de ferroptosis respecto a disponibilidad de hierro/metabolismo y motiva futuras variables de transporte de hierro.

### 20. Gao M, Monian P, Pan Q, Zhang W, Xiang J, Jiang X. (2016). *Ferroptosis is an autophagic cell death process*. Cell Research 26:1021–1032. DOI: 10.1038/cr.2016.95.
**Uso en el proyecto:** sustenta que el sistema ferroptótico interactúa con otros procesos celulares y que el score actual es una reducción fenomenológica de una red más amplia.

---

## B. PDAC, ferroptosis y microambiente tumoral

### 21. Badgley MA, et al. (2020). *Cysteine depletion induces pancreatic tumor ferroptosis in mice*. Science 368:85–89. DOI: 10.1126/science.aaw9872.
**Uso en el proyecto:** evidencia PDAC-específica que conecta dependencia de cisteína/SLC7A11, GSH y ferroptosis; es uno de los principales fundamentos biológicos de aplicar el modelo ferroptótico a PDAC.

### 22. Xiao Y, Wang W, Wang G, et al. (2026). *Navigating the complexities of ferroptosis in pancreatic ductal adenocarcinoma: roles, mechanisms and potential applications*. Cell Death Discovery 12:117. DOI: 10.1038/s41420-026-02987-2.
**Uso en el proyecto:** revisión PDAC-específica para contextualizar GPX4, hierro, peroxidación, estrés oxidativo, vías alternativas de defensa y nanoterapia ferroptótica.

### 23. Provenzano PP, et al. (2012). *Enzymatic targeting of the stroma ablates physical barriers to treatment of pancreatic ductal adenocarcinoma*. Cancer Cell 21:418–429. DOI: 10.1016/j.ccr.2012.01.007.
**Uso en el proyecto:** fundamento de la representación del estroma PDAC como barrera física de perfusión/difusión y de la heterogeneidad espacial del transporte.

### 24. Olive KP, et al. (2009). *Inhibition of Hedgehog signaling enhances delivery of chemotherapy in a mouse model of pancreatic cancer*. Science 324:1457–1461. DOI: 10.1126/science.1171362.
**Uso en el proyecto:** evidencia de que el microambiente/estroma puede modificar la entrega terapéutica en PDAC; sustenta el puente transporte → exposición.

### 25. Jacobetz MA, et al. (2013). *Hyaluronan impairs vascular function and drug delivery in a mouse model of pancreatic cancer*. Gut 62:112–120. DOI: 10.1136/gutjnl-2012-302529.
**Uso en el proyecto:** apoya el papel de la matriz rica en hialuronano en la limitación del transporte y motiva la variabilidad espacial del estroma.

### 26. Feig C, et al. (2012). *The pancreas cancer microenvironment*. Clinical Cancer Research 18:4266–4276. DOI: 10.1158/1078-0432.CCR-11-3114.
**Uso en el proyecto:** marco general para la complejidad celular y matricial del microambiente PDAC y para justificar que el modelo de difusión actual es una aproximación reducida.

### 27. Whatcott CJ, et al. (2015). *Desmoplasia in primary tumors and metastatic lesions of pancreatic cancer*. Clinical Cancer Research 21:3561–3568. DOI: 10.1158/1078-0432.CCR-14-1051.
**Uso en el proyecto:** sustenta la relevancia de la desmoplasia y la heterogeneidad de matriz en PDAC, utilizadas conceptualmente en el módulo espacial.

### 28. Neesse A, Algül H, Tuveson DA, Gress TM. (2015). *Stromal biology and therapy in pancreatic cancer: a changing paradigm*. Gut 64:1476–1484. DOI: 10.1136/gutjnl-2015-309304.
**Uso en el proyecto:** soporte para interpretar el estroma como componente dinámico y no exclusivamente como barrera; informa las limitaciones del modelo espacial simplificado.

### 29. Hosein AN, Brekken RA, Maitra A. (2020). *Pancreatic cancer stroma: an update on therapeutic targeting strategies*. Nature Reviews Gastroenterology & Hepatology 17:487–505. DOI: 10.1038/s41575-020-0300-1.
**Uso en el proyecto:** guía conceptual para futuras extensiones de CAF, matriz, vasculatura e interacciones estroma-terapia.

### 30. Ho WJ, Jaffee EM, Zheng L. (2020). *The tumour microenvironment in pancreatic cancer — clinical challenges and opportunities*. Nature Reviews Clinical Oncology 17:527–540. DOI: 10.1038/s41571-020-0363-5.
**Uso en el proyecto:** contextualización clínica de la heterogeneidad del TME y cautela frente a extrapolaciones directas desde modelos computacionales/preclínicos.

---

## C. Nanomedicina, tamaño de partícula y transporte tumoral

### 31. Cabral H, et al. (2011). *Accumulation of sub-100 nm polymeric micelles in poorly permeable tumours depends on size*. Nature Nanotechnology 6:815–823. DOI: 10.1038/nnano.2011.166.
**Uso en el proyecto:** evidencia experimental para considerar el radio/tamaño hidrodinámico como determinante de penetración tumoral, especialmente relevante para el fuerte efecto de r_H en el modelo.

### 32. Chauhan VP, Stylianopoulos T, Boucher Y, Jain RK. (2011). *Delivery of molecular and nanoscale medicine to tumors: transport barriers and strategies*. Annual Review of Chemical and Biomolecular Engineering 2:281–298. DOI: 10.1146/annurev-chembioeng-061010-114300.
**Uso en el proyecto:** marco biofísico para perfusión, extravasación, difusión intersticial y barreras de transporte que motivan el módulo de entrega.

### 33. Chauhan VP, et al. (2011). *Fluorescent nanorods and nanospheres for real-time in vivo probing of nanoparticle shape-dependent tumor penetration*. Angewandte Chemie International Edition 50:11417–11420. DOI: 10.1002/anie.201104449.
**Uso en el proyecto:** sustenta que propiedades físicas de la nanopartícula, además del tamaño, pueden modificar penetración; motiva futuras variables de forma.

### 34. Wong C, et al. (2011). *Multistage nanoparticle delivery system for deep penetration into tumor tissue*. Proceedings of the National Academy of Sciences USA 108:2426–2431. DOI: 10.1073/pnas.1018382108.
**Uso en el proyecto:** soporte para estrategias donde el tamaño efectivo cambia para mejorar penetración; relevante para futuras extensiones de partículas responsivas.

### 35. Stylianopoulos T, et al. (2012). *Multistage nanoparticles for improved delivery into tumor tissue*. Methods in Enzymology 508:109–130. DOI: 10.1016/B978-0-12-391860-4.00006-9.
**Uso en el proyecto:** referencia metodológica para conceptualizar penetración tisular y diseño multietapa de nanotransporte.

### 36. Nance EA, et al. (2012). *A dense poly(ethylene glycol) coating improves penetration of large polymeric nanoparticles within brain tissue*. Science Translational Medicine 4:149ra119. DOI: 10.1126/scitranslmed.3003594.
**Uso en el proyecto:** evidencia general de que impedimento estérico y adhesión a matriz dependen de propiedades superficiales; sustenta el término de hindrance como aproximación fenomenológica.

### 37. Perry JL, Reuter KG, Kai MP, et al. (2012). *PEGylated PRINT nanoparticles: the impact of PEG density on protein binding, macrophage association, biodistribution, and pharmacokinetics*. Nano Letters 12(10):5304–5310. DOI: 10.1021/nl302638g.
**Uso en el proyecto:** apoyo conceptual para documentar que el parámetro de transporte efectivo no depende únicamente de radio; superficie/PEG son candidatos para futuras versiones. **No se extraen parámetros numéricos de esta referencia.**

### 38. Albanese A, Tang PS, Chan WCW. (2012). *The effect of nanoparticle size, shape, and surface chemistry on biological systems*. Annual Review of Biomedical Engineering 14:1–16. DOI: 10.1146/annurev-bioeng-071811-150124.
**Uso en el proyecto:** fundamento para considerar tamaño, forma y química superficial como determinantes biofísicos de transporte e interacción celular.

### 39. Sindhwani S, et al. (2020). *The entry of nanoparticles into solid tumours*. Nature Materials 19:566–575. DOI: 10.1038/s41563-019-0566-2.
**Uso en el proyecto:** obliga a interpretar con cautela modelos puramente EPR/difusivos; motiva incorporar transporte endotelial activo en futuras versiones.

### 40. Wilhelm S, et al. (2016). *Analysis of nanoparticle delivery to tumours*. Nature Reviews Materials 1:16014. DOI: 10.1038/natrevmats.2016.14.
**Uso en el proyecto:** contexto cuantitativo de las limitaciones de entrega de nanopartículas y justificación de separar transporte, exposición y respuesta biológica.

### 41. Jain RK, Stylianopoulos T. (2010). *Delivering nanomedicine to solid tumors*. Nature Reviews Clinical Oncology 7:653–664. DOI: 10.1038/nrclinonc.2010.139.
**Uso en el proyecto:** marco para las barreras fisiológicas de nanomedicina y para la arquitectura causal transporte → entrega → efecto.

### 42. Chauhan VP, Jain RK. (2013). *Strategies for advancing cancer nanomedicine*. Nature Materials 12:958–962. DOI: 10.1038/nmat3792.
**Uso en el proyecto:** soporte para interpretar la optimización de propiedades de nanopartículas como problema multivariable y condicionado por el microambiente.

### 43. Cassani M, Fernandes S, Pagliari S, et al. (2025). *Unraveling the Role of the Tumor Extracellular Matrix to Inform Nanoparticle Design for Nanomedicine*. Advanced Science 12(2):e2409898. DOI: 10.1002/advs.202409898.
**Uso en el proyecto:** referencia reciente para interacción nanopartícula–ECM, impedimento estérico, tamaño y heterogeneidad de la matriz; apoya directamente el módulo espacial y sus futuras ampliaciones.

### 44. Netti PA, Berk DA, Swartz MA, Grodzinsky AJ, Jain RK. (2000). *Role of extracellular matrix assembly in interstitial transport in solid tumors*. Cancer Research 60:2497–2503.
**Uso en el proyecto:** fundamento clásico para relacionar arquitectura de ECM con transporte intersticial y para modelar heterogeneidad espacial de difusión.

### 45. Pluen A, Boucher Y, Ramanujan S, et al. (2001). *Role of tumor-host interactions in interstitial diffusion of macromolecules: cranial vs. subcutaneous tumors*. Proceedings of the National Academy of Sciences USA 98:4628–4633. DOI: 10.1073/pnas.081626898.
**Uso en el proyecto:** sustenta que el coeficiente de transporte efectivo depende del tejido/microambiente y no debe tratarse como una constante universal.

---

## D. Difusión y modelización biofísica/matemática

### 46. Einstein A. (1905). *Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten Teilchen*. Annalen der Physik 322:549–560. DOI: 10.1002/andp.19053220806.
**Uso en el proyecto:** fundamento histórico de la relación difusión–movilidad que conduce a la ecuación de Stokes–Einstein empleada en el núcleo biofísico.

### 47. Sutherland W. (1905). *LXXV. A dynamical theory of diffusion for non-electrolytes and the molecular mass of albumin*. The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science 9(54):781–785. DOI: 10.1080/14786440509463331.
**Uso en el proyecto:** fundamento histórico complementario de la relación Stokes–Einstein–Sutherland utilizada para estimar difusión a partir de radio, temperatura y viscosidad.

### 48. Crank J. (1975). *The Mathematics of Diffusion*, 2nd ed. Oxford University Press.
**Uso en el proyecto:** fundamento matemático de la ecuación de difusión y del solver espacial concentración-tiempo utilizado en v4.

### 49. Murray JD. (2002). *Mathematical Biology I: An Introduction*, 3rd ed. Springer, New York. DOI: 10.1007/b98868.

**Nota bibliográfica:** para formulaciones espaciales avanzadas puede citarse además *Mathematical Biology II: Spatial Models and Biomedical Applications*, 3rd ed. (2003).
**Uso en el proyecto:** referencia general para formulación e interpretación de modelos ODE/PDE biológicos, estabilidad y construcción de modelos mecanísticos reducidos.

### 50. Higham DJ. (2001). *An algorithmic introduction to numerical simulation of stochastic differential equations*. SIAM Review 43:525–546. DOI: 10.1137/S0036144500378302.
**Uso en el proyecto:** fundamento numérico para la discretización tipo Euler–Maruyama empleada/contemplada en el módulo SDE de ruido biológico.

---

## E. Incertidumbre, LHS, PRCC, Sobol, calibración y optimización

### 51. McKay MD, Beckman RJ, Conover WJ. (1979). *A comparison of three methods for selecting values of input variables in the analysis of output from a computer code*. Technometrics 21:239–245. DOI: 10.1080/00401706.1979.10489755.
**Uso en el proyecto:** referencia fundacional del Latin Hypercube Sampling (LHS) empleado para explorar eficientemente el espacio paramétrico.

### 52. Marino S, Hogue IB, Ray CJ, Kirschner DE. (2008). *A methodology for performing global uncertainty and sensitivity analysis in systems biology*. Journal of Theoretical Biology 254:178–196. DOI: 10.1016/j.jtbi.2008.04.011.
**Uso en el proyecto:** referencia principal para la combinación LHS–PRCC, análisis de monotonicidad e interpretación de sensibilidad global en modelos biológicos.

### 53. Sobol IM. (2001). *Global sensitivity indices for nonlinear mathematical models and their Monte Carlo estimates*. Mathematics and Computers in Simulation 55:271–280. DOI: 10.1016/S0378-4754(00)00270-6.
**Uso en el proyecto:** fundamento matemático de los índices globales de sensibilidad basados en descomposición de varianza implementados en v4.

### 54. Saltelli A, et al. (2010). *Variance based sensitivity analysis of model output. Design and estimator for the total sensitivity index*. Computer Physics Communications 181:259–270. DOI: 10.1016/j.cpc.2009.09.018.
**Uso en el proyecto:** referencia para estimación eficiente de índices Sobol de primer orden y efecto total y para la interpretación de interacciones.

### 55. Saltelli A, Ratto M, Andres T, et al. (2008). *Global Sensitivity Analysis: The Primer*. Wiley.
**Uso en el proyecto:** marco metodológico para selección de métodos de sensibilidad, interpretación de S1/ST y buenas prácticas de análisis global.

### 56. Efron B, Tibshirani RJ. (1993). *An Introduction to the Bootstrap*. Chapman & Hall/CRC.
**Uso en el proyecto:** fundamento del bootstrap utilizado para obtener intervalos de confianza de los coeficientes de sensibilidad y evaluar estabilidad estadística.

### 57. Byrd RH, Lu P, Nocedal J, Zhu C. (1995). *A limited memory algorithm for bound constrained optimization*. SIAM Journal on Scientific Computing 16:1190–1208. DOI: 10.1137/0916069.
**Uso en el proyecto:** fundamento del algoritmo L-BFGS-B utilizado para calibrar parámetros/pesos con restricciones físicas.

---

## F. Datos humanos, cohortes y reproducibilidad

### 58. Cancer Genome Atlas Research Network. (2017). *Integrated Genomic Characterization of Pancreatic Ductal Adenocarcinoma*. Cancer Cell 32:185–203.e13. DOI: 10.1016/j.ccell.2017.07.007.
**Uso en el proyecto:** fundamento de TCGA-PAAD como futura cohorte humana para variables moleculares y clínicas; se utilizará para calibración/estratificación cuando se incorporen datos descargados y documentados.

### 59. GTEx Consortium. (2020). *The GTEx Consortium atlas of genetic regulatory effects across human tissues*. Science 369:1318–1330. DOI: 10.1126/science.aaz1776.
**Uso en el proyecto:** fundamento para utilizar GTEx como referencia de tejido pancreático no tumoral y construir comparaciones tumor–tejido sano, respetando las restricciones de acceso de cada nivel de datos.

### 60. Cao L, Huang C, Zhou DC, et al.; Clinical Proteomic Tumor Analysis Consortium. (2021). *Proteogenomic characterization of pancreatic ductal adenocarcinoma*. Cell 184(19):5031–5052.e26. DOI: 10.1016/j.cell.2021.08.023.
**Uso en el proyecto:** estudio proteogenómico PDAC de referencia para anclar la futura integración CPTAC/PDC y evitar asumir que RNA de GPX4 equivale directamente a abundancia o actividad proteica. La versión exacta del dataset y su accession deberán registrarse en `DATA_PROVENANCE_TEMPLATE.csv` antes de cualquier análisis humano.

---

## Cómo se conectan las referencias con los módulos de v4

| Módulo del proyecto | Referencias principales |
|---|---|
| Ferroptosis / GPX4 / ROS / Fe²⁺ | 1–20 |
| Biología específica de PDAC y estroma | 21–30 |
| Nanopartículas y penetración tumoral | 31–45 |
| Stokes–Einstein, PDE y SDE | 46–50 |
| LHS–PRCC, Sobol, bootstrap y optimización | 51–57 |
| Datos humanos y validación externa | 58–60 |

## Nota de rigor científico

Las referencias anteriores **sustentan la arquitectura y las decisiones metodológicas**, pero la versión v4.0.0 no debe describirse como clínicamente validada. En particular: (i) los parámetros fenomenológicos de entrega requieren calibración; (ii) el benchmark de calibración incluido en la release utiliza datos sintéticos; (iii) los índices de sensibilidad describen el comportamiento del modelo dentro de los rangos asumidos; y (iv) TCGA/GTEx/CPTAC son fuentes propuestas para la siguiente fase de validación humana, no evidencia ya incorporada en los resultados v4.0.0.

