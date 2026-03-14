---
layout: single
title: "Resume"
permalink: /resume/
author_profile: true
---

## Experience

### Applied Scientist — Ambient Perceptual Technologies (Amazon AGI)
*June 2022 – Present · Sunnyvale, CA*

- Developed and productionized a unified "world encoder" for multi-task training across 17 Alexa locales (KWS, LV ASR, DVAD). Architected locale- and task-specific decoders on a shared encoder backbone, reducing cross-locale model duplication while achieving production-level parity. Deployed to scale in Spanish locales, currently undergoing live A/B testing before ramping across 6 additional locales.
- Built and productionized on-device Device Voice Activity Detection (DVAD) models to determine whether speech was directed to Alexa devices. Served as the gating component for the Alexa+ en_US launch, operating in production at scale.
- Developed production-grade keyword spotting models for automotive applications with limited in-domain data and challenging acoustic conditions, achieving 56% lower FRR and 71% lower FA on enhanced Siri certification tests compared to previous baselines.
- Designed and deployed a QAT-enabled model architecture across 10 Alexa locales, improving FRR by ~8.5% in offline evaluations and online recall by 4–16%, depending on locale.
- Improved fairness across gender-based cohorts, reducing FRR for feminine-sounding voices by 10.1% and for masculine-sounding voices by 7.8%, resulting in a 27% relative reduction in FRR gap across 16 locales.
- Implemented Quantization-Aware Training (QAT) and Knowledge Distillation (KD)-based model compression methods, demonstrating that sub-8-bit models maintain performance on par with full-precision variants.
- Developed and launched ML models for Amazon Greenwood auto devices in UK and Spain, achieving ~41% and ~64% FRR improvements respectively, enabling product launch in EU markets.

### Software Development Engineer — Amazon Web Services (AWS)
*June 2021 – June 2022 · Santa Clara, CA*

- Designed and implemented a scalable metrics framework to evaluate annotation quality across multiple modalities, improving dataset reliability and downstream model performance.
- Re-architected the internal labeling workflow to dynamically partition workloads by label category, mitigating class imbalance and reducing annotator cognitive load.

### Software Development Engineering Intern — Amazon (Alexa)
*May 2020 – July 2020 · Seattle, WA*

- Designed and implemented a feature within Alexa Smart Home (SHCC), enabling spatial visualization of device groupings by overlaying contextual metadata onto home layout topology.
- Contributed to the Context and Targeting (Spaces) system, improving customers' ability to manage and visualize smart home device groups.

### Graduate Student Researcher — Purdue University
*August 2020 – May 2021 · West Lafayette, IN*

- Proposed a novel personalization framework for Federated Learning by unifying knowledge distillation with user-specific optimal teacher models, improving client-level performance in heterogeneous data settings.
- Introduced new metrics to evaluate performance and fairness in personalized FL systems beyond average accuracy. Work presented at the ICML 2021 Federated Learning Workshop and published on arXiv.

---

## Education

### Purdue University — West Lafayette, IN
*M.S. in Computer Science (Machine Learning, Data Science — Thesis Track) · GPA: 4.0 · May 2021*

### SSN College of Engineering — Chennai, India
*B.E. in Computer Science and Engineering · CGPA: 8.79/10 · May 2019*

---

## Publications

**New Metrics to Evaluate the Performance and Fairness of Personalized Federated Learning**
Poster at the Federated Learning Workshop, ICML 2021. Also on arXiv. *(June 2021)*

**Unifying Distillation with Personalization in Federated Learning**
arXiv. *(May 2021)*

**DeepTrace: A Generic Framework for Time Series Forecasting**
International Work-Conference on Artificial Neural Networks (IWANN), Gran Canaria, Spain. *(June 2019)*

**Forecasting Food Sales in a Multiplex Using Dynamic Artificial Neural Networks**
Computer Vision Conference (CVC), Las Vegas, USA. *(April 2019)*

**Convolutional Long Short-Term Memory Neural Networks for Hierarchical Species Prediction**
Conference and Labs of the Evaluation Forum (CLEF), Avignon, France. *(September 2018)*
