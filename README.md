# Critical Infrastructure Spatial Index (CISI)

[![DOI](https://zenodo.org/badge/327351993.svg)](https://zenodo.org/badge/latestdoi/327351993)

This repository provides the code to:

- extract critical infrastructure assets from OSM data
- estimate the amount of infrastructure for given grid cells
- calculate the Critical Infrastructure Spatial Index (CISI)

It also provides a Jupyter Notebook and additional code to reproduce the figures
and supplementary material in Nirandjan et al. (2022).

## Global CISI visualizer

The CISI and the sub-score per system is visualized at a global scale via https://cisi-index.appspot.com/. This is only done for a resolution of 0.25 degrees for speed performance considerations. Have a look and discover where critical infrastructure is located!

## Data requirements

All critical infrastructure data is based on OpenStreetMap (OSM), which can be
freely downloaded from
[OpenStreetMap](https://wiki.openstreetmap.org/wiki/Planet.osm#Downloading) or
as smaller national/regional extracts from
[GeoFabrik](http://download.geofabrik.de/). In either case the `.osm.pbf` file
format is required.

The OSM planet file used in Nirandjan et al. (2022) was downloaded on January
8th, 2021. However, the latest release of planet.osm.pbf file can be used to run
the code.

The following datasets are used for the technical validation:

- Gridded global population distribution data is available from the WorldPop
  data portal (https://www.worldpop.org). In Nirandjan et al. (2022), global
  population distribution data of 2020 is used.
- Gridded global GDP data is available from
  https://datadryad.org/stash/dataset/doi:10.5061/dryad.dk1j0. In Nirandjan et
  al. (2022), we use the GDP_PPP_30arcsec file for 2015.

## Python requirements

Recommended option is to use [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)
to create an environment to work in for this project.

```bash
# Create an environment for the project and install packages
micromamba env create -f environment.yml
micromamba activate cisi
```

Requirements include:

- [geopandas](http://geopandas.org/)
- [matplotlib](https://matplotlib.org/)
- [snail](https://nismod.github.io/snail/)

## How to cite

If you use the CISI in your work, please cite the corresponding paper:

> Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized
> global dataset of critical infrastructure. _Sci Data_ 9, 150 (2022).
> https://doi.org/10.1038/s41597-022-01218-4

```tex
@article{Nirandjan2022_CISI,
  title={A spatially-explicit harmonized global dataset of critical infrastructure},
  author={Nirandjan, S., Koks, E.E., Ward, P.J. and Aerts, J.C.J.H.},
  journal={Scientific Data},
  volume={9},
  number={150},
  pages={13},
  year={2022}
}
```

This repository can be cited through its [Zenodo archive](https://zenodo.org/badge/latestdoi/327351993).

### License

Copyright (C) 2021 Sadhana Nirandjan, Elco Koks and contributors. All versions
released under the [MIT license](LICENSE).
