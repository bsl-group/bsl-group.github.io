---
permalink: "/members/utpalkumar/"
classes:
  - wide
github: "https://github.com/earthinversion"
author: Utpal Kumar
---

<strong>Geophysicist | Geodesist | Seismologist | Open-source Developer</strong>

I am currently working as a postdoctoral researcher at UC Berkeley. My research focuses on seismic data analysis, structural health monitoring, and understanding deep Earth structures. I am working on codes to develop a 3D elastic model of deep structure beneath the Yellowstone hotspot using an approach called "box tomography"


In addition to my research, I have experience in cloud computing, high-performance computing, and single-board computers, 
which I have applied in various projects. This includes working with platforms like AWS, GCP, 
as well as supercomputing environments such as STAMPEDE2, ANVIL, Savio and PERLMUTTER (and CORI). 
My work involves developing innovative solutions for structural health monitoring and advancing real-time seismic response analysis. 
I am committed to applying these skills to further research in computational seismology and structural health monitoring.


#### Enhanced Mid-Mantle Resolution of the Yellowstone Mantle Plume Using Full Waveform Inversion and Box Tomography (AGU 2024)

The Yellowstone mantle plume is characterized by a narrow, low shear-velocity feature in the lower mantle, 
showing a horizontal deflection at approximately 1000 km depth (Nelson and Grand, 2018), akin to other plumes and subducted slabs, 
suggesting a rheological change at that level. To improve resolution at mid-mantle depths, we utilize full waveforms of body and surface waves.

Using 'box tomography', we integrate global and regional solvers based on the Spectral Element Method (SEM). The global 3D solver, SPECFEM3D_globe (Tromp et al., 2008), is used for wavefield calculations outside the region of interest, while RegSEM (Cupillard et al., 2012) is employed for computations within the region of interest. The background global 3D model, SEMUCB_WM1 (French and Romanowicz, 2014), which faintly resolves a low-velocity plume beneath Yellowstone extending to the core-mantle boundary (French and Romanowicz, 2015), serves as the basis for initial wavefield computations, recorded at the box boundaries. This includes body waveforms from distant earthquakes for illuminating mid- to lower-mantle structures.

For box tomography, we first compute the necessary global wavefields in the reference 3D model down to a 20 s period, recording these fields on the box boundaries. Inversion iterations within the box reduce the cutoff period from 40 s to 20 s and expand the depth range. The crustal structure is constrained using surface wave dispersion data down to a 16 s period. We will present our results, derived from multiple iterations where the inverse step uses Gauss-Newton optimization and a physics-based Hessian computed with normal mode perturbation theory (NACT, Li and Romanowicz, 1995).
