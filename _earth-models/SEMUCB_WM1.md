---
title: "SEMUCB_WM1"
date: 2013-10-13
tags:
  [earth-model, SEMUCB-WM1]
toc: true
sidebar:
  nav: "all_posts_list"
excerpt: " SEMUCB-WM1 is a global radially anisotropic shear velocity model derived from fully numerical SEM-based forward modelling. It is parametrized in terms of isotropic S velocity (Voigt average) and the anisotropic parameter, xi "
header:
  teaser: "/images/semucb_wm1.png"
author: Barbara Romanowicz
---

<figure style="width: 640px; margin: 0 auto; text-align: left;">
<img style="width: 100%" src="/images/semucb_wm1.png">
</figure>

## Broad plumes rooted at the base of the mantle beneath major hotspots
- Download [SEMUCB_WM1 model and codes](https://github.com/bsl-group/SEMUCB-WM1-Model) to read it and plot it
- There are two codes, depending on the specific purpose:
  1. To obtain values of the model (Vs and xi) at a particular (radius, lon, lat) or to obtain values at a particular radius on an N x N grid - useful for plotting purposes and direct comparison with other models, download: (tar and gzipped files). Note: the values of the model in the crust are not interpretable. See French and Romanowicz (2014) for details of the crustal model.
  2. To predict waveforms, dispersion curves, or travel times of particular phases using SEMUCB_WM1, here is a code that allows you to construct 1D depth profiles of the model at a particular (lat, lon) location: (tar and gzipped files)


- Download the Model NetCDF files from IRIS EMC <a href="https://ds.iris.edu/ds/products/emc-semucb-wm1/" class="btn btn--success">here</a>


- __You must use this code for these purposes__. Indeed, it is important to remember that the mantle model needs to be combined with the crustal model that was constructed at the same time. Using our mantle model with another crustal model will not lead to a fair assessment. Our crustal model is not a standard model like crust2.0 or crust1.0, it is a smooth crustal model designed to fit a global dispersion dataset (Shapiro and Ritzwoller, 2002) as well as our waveform dataset, and it is adjusted at each iteration of the inversion. To construct a 3D description of the model on a grid, you should pay close attention to the Moho depths - which are not realistic in the oceans (saturated to 30 km) but are designed to be equivalent to a real crustal models for seismic waves of periods > 30 s.

- It is straightforward to construct a 3D grid model from the 1D profiles obtained with the code provided.

## Abstract of recent Nature (2015) paper
Plumes of hot upwelling rock rooted in the deep mantle have been proposed as a possible origin of hotspot volcanoes, but this idea is the subject of vigorous debate. On the basis of geodynamic computations, plumes of purely thermal origin should comprise thin tails, only several hundred kilometres wide, and be difficult to detect using standard seismic tomography techniques. Here we describe the use of a whole-mantle seismic imaging technique— combining accurate wavefield computations with information contained in whole seismic waveforms4—that reveals the presence of broad (not thin), quasi-vertical conduits beneath many prominent hotspots. These conduits extend from the core–mantle boundary to about 1,000 kilometres below Earth’s surface, where some are deflected horizontally, as though entrained into more vigorous upper-mantle circulation. At the base of the mantle, these conduits are rooted in patches of greatly reduced shear velocity that, in the case of Hawaii, Iceland and Samoa, correspond to the locations of known large ultralow-velocity zones. This correspondence clearly establishes a continuous connection between such zones and mantle plumes. We also show that the imaged conduits are robustly broader than classical thermal plume tails, suggesting that they are long-lived, and may have a thermochemical origin. Their vertical orientation suggests very sluggish background circulation below depths of 1,000 kilometres. Our results should provide constraints on studies of viscosity layering of Earth’s mantle and guide further research into thermochemical convection.

French, S. W. and B. Romanowicz (2015) Broad plumes Rooted At The Base Of The Earth's Mantle Beneath Major Hotspots, Nature, 525, 95-99.

## Related papers
1. French, S. W., Y. Zheng, B. Romanowicz and K. Yelick (2015) Parallel Hessian assembly for Seismic Waveform inversion using Global updates, Proceedings of the 29th IEEE International Parallel and Distributed Processing Symposium (2015) doi:10.1109/IPDPS.2015.58.
1. French, S. and B. Romanowicz (2014) Whole-mantle radially anisotropic shear-velocity structure from spectral-element waveform tomography, Geophys. J. Int., 199, 1303-1327. download reprint. This work builds upon experienced gained over the last 25 years in whole waveform time domain global tomography, starting with theoretical developments using normal mode perturbation theory:
1. Li, X.-D., and B. Romanowicz (1995) Comparison of global waveform inversions with and without considering cross-branch modal coupling, Geophys. J. Int., 121(3), 695-709. and implementing seismic wavefield computations using the Spectral Element Method, first for the upper mantle (SEMum, SEMum2):
1. Lekic, V. and B. Romanowicz (2011) Inferring mantle structure by full waveform tomography using the Spectral Element Method, Geophys. J. Int., 185, 799-831, doi: 10.1111/j.1365-246X.2011.04969.x.
1. French, S., V. Lekic and B. Romanowicz (2013) Waveform Tomography Reveals Channeled Flow at the Base of the Oceanic Asthenosphere, Science, 342, 227- 230.
