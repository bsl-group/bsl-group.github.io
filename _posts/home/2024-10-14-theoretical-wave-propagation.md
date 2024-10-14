---
title: "Theoretical wave propagation"
date: 2024-10-14
tags:
  ["normal-modes", "NACT"]
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: home
---
## A Brief Introduction to Normal Mode Seismology

All seismic motions occurring within a spherically symmetric body (which the Earth nearly is) can fully be described by a superposition of the natural modes of oscillation of that body - namely, the body's normal modes. Features of any physical object that violate spherical symmetry, such as rotation, ellipticity, and lateral heterogeneity in material properties, introduce "splitting" of the modes. In other words, a given normal mode in a non-spherically symmetric medium oscillates at a number of different nearby frequencies; this number is proportional to the inherent spatial length-scale of the mode, and the magnitude of the frequency differences is a function of the level of heterogeneity. Furthermore, modes oscillating at similar frequencies can exchange energy, which process is called "coupling".

Because the Earth is nearly spherically symmetric, the strength of lateral heterogeneity typically sampled by seismic waves of interest in global seismology is weak. As a result, its effects can be approximated by considering small perturbations to the properties of the spherically symmetric Earth, and neglecting terms that depend on quantities smaller than this small perturbation (i.e. higher order terms). This approximation is equivalent to considering traveling waves that are only scattered once by heterogeneity, and is called the Born Approximation.

## Non-linear Asymptotic Coupling Theory
Since 1995, we have been developing global mantle tomographic models based on full waveform seismograms and a theoretical mode-coupling 
approach called non-linear asymptotic coupling theory, as first applied by Xiang-Dong Li and Barbara Romanowicz (Li and Tanimoto, 1993; Li and Romanowicz, 1995).

Within the context of the aforedescribed Born Approximation, we can calculate the frequency shifts produced by lateral heterogeneity. With this knowledge, we can also compute the extent of coupling between modes proximate in frequency. Instead of accounting for coupling between all possible mode pairs (which entails large computational costs), global seismologists have typically only taken into account coupling between modes that share the same radial order. If we consider seismic waves traveling between two points on the Earth, this further approximation is equivalent to ignoring all but the average structure along the great circle path joining the points. Appropriately enough, this approximation is dubbed the "great circle" or "path average" approximation (PAVA; Woodhouse and Dziewonski, 1984).

In non-linear asymptotic coupling theory (NACT, Li and Romanowicz, 1995), we also account for coupling between modes that do not share the same radial order. In terms of travelling waves, this practice is equivalent to considering not only average structure, but also variations in material properties along the great circle path joining a source and receiver. Equivalently, we can say that NACT allows us to "follow" the seismic waves as they dive into the Earth and emerge back at the surface (see the figure to the right). Because of this advantage, NACT makes possible waveform modeling of surface wave overtones as well as body waves.

{% capture fig_img %}
![NACT](/images/theoretical_wave_propagation/Nact.gif)
{% endcapture %}

{% capture fig_caption %}
Non-linear Asymptotic Coupling Theory
{% endcapture %}