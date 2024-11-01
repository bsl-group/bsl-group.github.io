---
title: "Introduction to the DFDM"
date: 2024-04-18
tags:
  []
toc: true
sidebar:
  nav: "all_posts_list"
category: research-papers
excerpt: "We implement the distributional finite difference method for 3D seismic wave propagation, which show promise for improving accuracy, flexibility, and efficiency against the Spectral Element Method"
header:
  teaser: "/images/introduction-to-the-DFDM/fig.jpg"
author: Chao Lyu
---


## Abstract
We have extended the distributional finite difference method (DFDM) to simulate the seismic-wave propagation in 3D regional earth models. DFDM shares similarities to the discontinuous finite element method on a global scale and to the finite difference method locally. Instead of using linear staggered finite-difference operators, we employ DFDM operators based on B-splines and a definition of derivatives in the sense of distributions, to obtain accurate spatial derivatives. The weighted residuals method used in DFDM's locally weak formalism of spatial derivatives accurately and naturally accounts for the free surface, curvilinear meshing, and solid-fluid coupling, for which it only requires setting the shear modulus and the continuity condition to zero. The computational efficiency of DFDM is comparable to the spectral element method (SEM) due to the more accurate mass matrix and a new band-diagonal mass factorization. Numerical examples show that the superior accuracy of the band-diagonal mass and stiffness matrices in DFDM enables fewer points per wavelength, approaching the spectral limit, and compensates for the increased computational burden due to four Lebedev staggered grids. Specifically, DFDM needs 2.5 points per wavelength, compared to the five points per wavelength required in SEM for 0.5% waveform error in a homogeneous model. Notably, while maintaining the same accuracy in the solid domain, DFDM demonstrates superior accuracy in the fluid domain compared to SEM. To validate its accuracy and flexibility, we present various 3D benchmarks involving homogeneous and heterogeneous regional elastic models and solid-fluid coupling in both Cartesian and spherical settings.

## Download
Download the paper <a href="https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JB027576" class="btn btn--success">here</a>
