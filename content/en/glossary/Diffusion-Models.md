---
title: Diffusion Models
date: 2025-03-01
lastmod: 2026-04-02
description: A technique for generating images step-by-step from noise. The foundation of Stable Diffusion and DALL-E.
translationKey: diffusion-models
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/diffusion-models/
keywords:
- Image Generation
- Generative Model
- Text-to-Image
- Deep Learning
---

## What are Diffusion Models?

**Diffusion models are deep learning models that generate complex images like photographs and illustrations by starting with random noise and progressively removing that noise.** The name "diffusion" derives from the physics phenomenon of diffusion (ink spreading through water), and the models work through the reverse process to generate data. Recent popular image generation AIs like Stable Diffusion and DALL-E use this technology, making it essential for generating high-quality images from text prompts. Compared to traditional generative models (such as [GANs](GAN.md)), diffusion models offer more stable training and can generate diverse, high-quality outputs.

> **In a nutshell:** Starting from a static-like noise state, you gradually "clean" that noise step-by-step, and gradually a beautiful image emerges.

**Key points:**

- **What they do:** Generate new images through an iterative noise removal process starting from random noise
- **Why they matter:** Enable high-quality, diverse image generation with stable training; support conditional generation with text and other inputs
- **Who uses them:** Image generation AI companies, designers, creative industries, researchers

## Why they matter

Diffusion models have dramatically accelerated the practical implementation and quality improvement of image generation AI. Traditional image generation used [GANs](GAN.md) (Generative Adversarial Networks), but GANs suffered from unstable training and mode collapse (generating the same boring images repeatedly). Diffusion models, by contrast, train stably and generate more diverse, high-quality outputs.

From a business value perspective, diffusion models provide practical value in many areas: automatic marketing image generation, rapid product design prototyping, and synthetic medical images (training data augmentation). Through text-conditioned generation, images more accurately reflect user intent, significantly improving user experience.

## How it works

Diffusion models consist of two processes: the "forward process" and "reverse process."

The forward process occurs during the learning phase. Starting from a real image (e.g., a dog photo), random Gaussian noise is gradually added. The first step adds slight noise to the original image. The second step adds noise to the already-noisy image. Repeating this hundreds of times results in pure random noise. This process resembles diffusion in physics, hence the name "diffusion models."

The reverse process occurs during generation. A neural network (typically [U-Net](U-Net.md) architecture) learns how much noise to remove at each step. The model sees a noisy image and predicts "what image appears if I remove this noise?" After training, starting from pure random noise and removing noise step-by-step based on the model's predictions, a meaningful image gradually emerges.

For conditional generation with text prompts, a text prompt is added as input. Like [large language models](LLM.md), the text is converted to tokens and embedded into the neural network. At each denoising step, this text embedding is considered, so "red car" prompts guide denoising toward a red car.

From a computational perspective, this process is probabilistic. The forward process follows a known probability distribution (Gaussian), while the reverse process uses a neural network to estimate probability distributions. Mathematically, leveraging symmetry between the two processes enables efficient diffusion model training.

## Real-world use cases

**E-commerce product image generation**

Fashion e-commerce companies need millions of product images, but photographing everything is impractical. From text prompts like "blue silk dress, size M, for summer," multiple images from different angles and backgrounds can be auto-generated, visualizing products without inventory and improving customer experience.

**Medical imaging data augmentation**

Medical AI development faces limited training data due to privacy concerns. Diffusion models generate synthetic images from existing medical images, expanding training datasets. This realizes [privacy-preserving machine learning](Privacy-Preserving-ML.md) while improving model generalization.

**Design prototyping acceleration**

Game and anime design studios can instantly generate multiple character variations from text like "king-like appearance, blue outfit," letting designers select. This dramatically shortens design workflows.

## Benefits and considerations

Diffusion models' greatest benefit is stable training and output quality. They're easier to train than [GANs](GAN.md) and generate more diverse, high-quality images. Conditional generation lets users specify intent through text, increasing practicality. Applications span medicine, science, and many other domains.

However, considerations exist. Generation requires hundreds of steps, taking several seconds to tens of seconds per image. Real-time applications like video games aren't suitable. Generated image quality heavily depends on training data quality and diversity, making data preparation critical. Copyright issues also persist. Training data may infringe copyright holders' rights, and legal discussions continue.

## Related terms

- **[GANs (Generative Adversarial Networks)](GAN.md)** — The mainstream image generation technique before diffusion models
- **[U-Net](U-Net.md)** — The typical neural network architecture used in diffusion models
- **[Large Language Models](LLM.md)** — Used for text encoding in text-conditioned generation
- **[Conditional Generation](Conditional-Generation.md)** — Technique for generating images based on conditions like text

## Frequently asked questions

**Q: Why are diffusion models easier to train than [GANs](GAN.md)?**

A: [GANs](GAN.md) train adversarially with two models, making training unstable. Diffusion models train a single neural network with a simple objective, achieving higher stability.

**Q: Who owns the copyright of generated images?**

A: Legally, generated image copyright is complex. Rights relationships between training data authors, AI developers, and users are often unclear, with legislation still developing in each country.

**Q: Are there ways to generate images faster with diffusion models?**

A: Yes. Reducing steps (Diffusion Distillation) or using pre-distilled faster models improves generation speed. However, there's a quality-speed tradeoff.
