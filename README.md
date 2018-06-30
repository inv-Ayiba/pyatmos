# pyatmos

A Docker image for [Atmos](https://github.com/VirtualPlanetaryLaboratory/atmos) and a Python package for interacting with Atmos, for NASA FDL 2018 astrobiology challenges.

Initial work by Adam Cobb and Atilim Gunes Baydin.

Work in progress. Documentation to follow soon.

## How to install

You can clone this repository and install the `pyatmos` package. You need to have Docker installed in your system.

The Python package pulls the latest Docker image for atmos from the FDL GitLab registry, here: https://gitlab.com/frontierdevelopmentlab/astrobiology/pyatmos/container_registry

### Prerequisites
* Install [Docker CE](https://www.docker.com/community-edition) for your system

### Install the package

```
git clone git@gitlab.com:frontierdevelopmentlab/astrobiology/pyatmos.git
cd pyatmos
pip install .
```
