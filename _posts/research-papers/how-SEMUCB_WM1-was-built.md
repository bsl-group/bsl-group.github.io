---
title: "How SEMUCB-WM1 Was Built: A Whole-Mantle Shear Velocity Model"
date: 2025-05-17
tags:
  [earth-model, SEMUCB-WM1]
mathjax: "true"
toc: true
sidebar:
  nav: "all_posts_list"
excerpt: " SEMUCB-WM1 is a global radially anisotropic shear velocity model derived from fully numerical SEM-based forward modelling. It is parametrized in terms of isotropic S velocity (Voigt average) and the anisotropic parameter, xi "
header:
  teaser: "/images/semucb_wm1.png"
author: Utpal Kumar
---

<figure style="width: 640px; margin: 0 auto; text-align: left;">
<img style="width: 100%" src="/images/semucb_wm1.png">
</figure>

SEMUCB-WM1 is a radially anisotropic, shear-wave velocity model of Earth's entire mantle, developed through full-waveform inversion using a hybrid numerical technique. Here's a step-by-step outline of how it was constructed:

## Data Selection and Processing
The SEMUCB-WM1 model is built from a large, carefully curated dataset of long-period seismic waveforms that provide excellent sensitivity throughout the mantle. The dataset includes:

- Surface waves, including both fundamental modes and higher overtones, with periods down to 60 seconds.
- Body waves, primarily S and P waveforms, including SV components, with periods down to 32 seconds.
- Diffracted and multiply reflected phases, such as Sdiff (shear waves diffracted along the core–mantle boundary) and SPdiffKS, which enhance sensitivity to deep-mantle structures and ultra-low velocity zones (ULVZs).

By combining a wide range of wave types and periods, the dataset enables high-resolution imaging from the upper mantle down to the core–mantle boundary. The use of both overtone and body wave data ensures improved illumination of the deep Earth compared to conventional travel-time tomography.

## Hybrid Full-Waveform Inversion
To build SEMUCB-WM1, the authors used a hybrid full-waveform inversion technique that combines two powerful tools:

### Spectral Element Method (SEM) for Forward Modeling
- SEM is a high-accuracy numerical technique used to simulate 3D seismic wave propagation in the Earth.
- It captures complex effects such as wavefront healing, anisotropy, and surface reflections that are often neglected in approximate methods.
- In SEMUCB-WM1, SEM was used to compute synthetic seismograms at each iteration, providing a highly accurate comparison with observed waveforms.

### Nonlinear Asymptotic Coupling Theory (NACT) for Sensitivity Kernels
- NACT is used to efficiently compute how small changes in Earth structure affect the seismic waveforms.
- It provides finite-frequency sensitivity kernels that account for the wave's 3D travel path, improving upon simple ray-based approaches.
- While NACT is approximate, it is fast and accurate enough to guide model updates during inversion.


### Why This Hybrid Approach?
- Using SEM alone for both forward modeling and hessian computation is computationally expensive for global models.
- Using NACT alone lacks the forward accuracy needed to simulate complex wavefields.
- The hybrid approach balances efficiency and accuracy: SEM gives high-fidelity waveforms for data misfit evaluation, while NACT guides efficient inversion updates.

## Model Parameterization
The model resolves Voigt-averaged isotropic shear velocity ((\\(Vs\\))) and radial anisotropy (\\(\Xi = V_{SH}^2 / V_SV^2\\)).

Mantle properties are expressed using:
- Cubic B-splines radially (20 depth nodes from CMB to ~30 km depth)
- Spherical splines laterally (with spacing ~2° for (\\(Vs\\)), ~8° for (\\(Xi\\)))

## Smooth Crustal Layer Treatment
Instead of a complex, layered crust, a homogenized anisotropic crust is used:
- Crustal thickness is smoothed (30–60 km) and fitted to observed surface wave group velocity dispersion (25–60 s).
- This approach reduces numerical instability and computational cost in SEM simulations.

### Inversion Strategy
- The misfit between observed and synthetic waveforms is minimized using a Gauss–Newton optimization scheme.
- The inversion proceeds iteratively, starting with long-period data and gradually adding shorter-period waveforms.
- The 3D model is updated at each step, with careful treatment of prior information and data weighting to ensure convergence and physical plausibility.
- The model was built through iterative Gauss–Newton optimization, progressively incorporating:
  - Longer to shorter periods
  - Fundamental to overtone modes
  - Surface to body waves

- Each iteration involved updating the 3D model and the underlying 1D reference model.
- The optimization minimizes a misfit function combining waveform differences and model smoothness, using an approximate Hessian computed from NACT.

## Resolution and Uncertainty Analysis
SEMUCB-WM1’s reliability was validated through synthetic checkerboard and plume recovery tests using the same inversion setup.

- The model successfully resolves broad, vertically continuous low-velocity structures—such as plumes beneath Hawaii and Samoa—distinct from surrounding superplumes or LLSVPs.
- The vertical extent and shape of plumes are robust and not artifacts of limited ray coverage.
- These tests confirm SEMUCB-WM1’s ability to detect deep mantle plumes and ULVZ-rooted features with high confidence.


## Related papers
1. French, S. W., Y. Zheng, B. Romanowicz and K. Yelick (2015) Parallel Hessian assembly for Seismic Waveform inversion using Global updates, Proceedings of the 29th IEEE International Parallel and Distributed Processing Symposium (2015) doi:10.1109/IPDPS.2015.58.
1. French, S. and B. Romanowicz (2014) Whole-mantle radially anisotropic shear-velocity structure from spectral-element waveform tomography, Geophys. J. Int., 199, 1303-1327. download reprint. This work builds upon experienced gained over the last 25 years in whole waveform time domain global tomography, starting with theoretical developments using normal mode perturbation theory:
1. Li, X.-D., and B. Romanowicz (1995) Comparison of global waveform inversions with and without considering cross-branch modal coupling, Geophys. J. Int., 121(3), 695-709. and implementing seismic wavefield computations using the Spectral Element Method, first for the upper mantle (SEMum, SEMum2):
1. Lekic, V. and B. Romanowicz (2011) Inferring mantle structure by full waveform tomography using the Spectral Element Method, Geophys. J. Int., 185, 799-831, doi: 10.1111/j.1365-246X.2011.04969.x.
1. French, S., V. Lekic and B. Romanowicz (2013) Waveform Tomography Reveals Channeled Flow at the Base of the Oceanic Asthenosphere, Science, 342, 227- 230.
