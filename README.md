# DUNE SPINE Workshop 2026

This repository contains all necessary resources to participate in the 2026 SPINE workshop organized for the DUNE reconstruction groups (ND + FD, and their respective prototypes). This workshop aims to train new comers to use [SPINE](https://github.com/DeepLearnPhysics/spine), our machine-learning-based particle imaging detector reconstruction chain. You can find the workshop agenda [here](https://indico.cern.ch/event/1581241/timetable/#20260202).

## Software environment

For the workshop, we will use [this "Docker container"](https://hub.docker.com/layers/deeplearnphysics/larcv2/ub2204-cu121-torch251-larndsim/images/sha256-59d520c9e2a22b5a474daa8b91a01bf1fb6ef76a1047cbf57c2b09ddf82abe41).

Some notes below:

* The image is fairly large (multiple GBs). Please download in advance if you are using it locally. It can be used in both NVIDIA GPU and CPU running mode of our software.
* Supported GPUs include those with NVIDIA Volta (e.g. V100), Turing (e.g. RTX 2080Ti), Ampere (e.g. A100, RTX 3080) and Hopper architectures (e.g. H200). If you want an older architectures to be supported, such as Pascal, please [contact Kazu](mailto:kterao@slac.stanford.edu).
* We assume basic knowledge about _software container_, in particular `Docker`. If you are learning for the first time, we recommend to use/learn about `Apptainer` ([website](https://apptainer.org/docs/user/latest/)) instead of `Docker`.
    * You can pull a apptainer image as follows
```shell
$ apptainer pull docker://deeplearnphysics/larcv2:ub2204-cu121-torch251-larndsim
```https://hub.docker.com/layers/deeplearnphysics/larcv2/ub2204-cu121-torch251-larndsim/images/sha256-59d520c9e2a22b5a474daa8b91a01bf1fb6ef76a1047cbf57c2b09ddf82abe41
You can now launch a shell inside the apptainer with
```shell
$ apptainer exec --bind /path/to/workshop/folder/ /path/to/container.sif bash
```
For nersc:
```shell
$ salloc --nodes 1 --qos shared_interactive --time 00:30:00 --constraint gpu --gpus 1 --account=m5252 --image=deeplearnphysics/larcv2:ub2204-cu121-torch251-larndsim shifter /bin/bash
```

## Resources

1. The *configuration files* are packages with this repository.

2. You can find *data files* for the examples used in this workshop under:
- NERSC
```shell
/global/cfs/cdirs/m5252/dune/spine/larcv/ # Example MPV/MPR LArCV files prior to reconstruction
/global/cfs/cdirs/m5252/dune/spine/reco/  # Reconstructed HDF5 files
```
- Public
  - [Small LArCV files](https://s3df.slac.stanford.edu/data/neutrino/spine/workshop/larcv/) (Day 1)
    - [Generic](https://s3df.slac.stanford.edu/data/neutrino/spine/workshop/larcv/generic_small.root)
    - [ND-LAr](https://s3df.slac.stanford.edu/data/neutrino/spine/workshop/larcv/nd-lar_small.root)
    - [2x2](https://s3df.slac.stanford.edu/data/neutrino/spine/workshop/larcv/2x2_small.root)
    - [FSD](https://s3df.slac.stanford.edu/data/neutrino/spine/workshop/larcv/fsd_small.root)
    - [DUNE FD-HD 10kt-1x2x6](https://s3df.slac.stanford.edu/data/neutrino/spine/workshop/larcv/dune10kt-1x2x6_small.root)
    - [ProtoDUNE-SP](https://s3df.slac.stanford.edu/data/neutrino/spine/workshop/larcv/protodune-sp_small.root)
    - [ProtoDUNE-HD](https://s3df.slac.stanford.edu/data/neutrino/spine/workshop/larcv/protodune-hd_small.root)
    - [ProtoDUNE-VD](https://s3df.slac.stanford.edu/data/neutrino/spine/workshop/larcv/protodune-vd_small.root)
  - [Small corresponding reconstructed HDF5 files] TODO
  - [Medium reconstructed HDF5 files] TODO
  - [Physics datasets] TODO

3. The *network model parameters* for the inference tutorial are stored in a public area and pulled on the fly by SPINE when not cached, nothing to do here anymore!

## Jupyter notebooks

In this we briefly summarize how to setup a Jupyter notebook with the necessary dependencies to run SPINE. There are three options for DUNE collaborators:
* NERSC: This is the option we will use throughout this workshop, everyone should be using this
* EAF: This is FNAL's system, every DUNE collaborator should have access to this (good longer-term solution)
* Local: If you have a GPU on your laptop (or not!) you can run all (most!) of the notebooks presented in this workshop locally

### NERSC

Everyone participating in this workshop should have access to GPUs through NERSC, under project `m5252`. If you do not, please reach out to [Francois](mailto:drielsma@slac.stanford.edu).

The instructions to set up the `apptainer` container as a Jupyter kernel can be found here: [https://docs.nersc.gov/services/jupyter/how-to-guides/#shifter](https://docs.nersc.gov/services/jupyter/how-to-guides/#shifter)

Go to the NERSC Jupyter portal: [https://jupyter.nersc.gov/hub/home](https://jupyter.nersc.gov/hub/home)

### EAF

All DUNE collaborators should also have access to the **Elastic Analysis Facility (EAF)** at FNAL, equipped with GPUs. Here are some basic instructions to set things up.

Go to the EAF portal: [https://eaf.fnal.gov](https://eaf.fnal.gov)
* This requires FNAL VPN or being on-site
* See [https://eafdocs.fnal.gov/master/index.html](https://eafdocs.fnal.gov/master/index.html) for some basic documentation
* Choose FIFE/Neutrinos from the options
  * This will have the usual `/exp/dune/` file system mounted, similar to using the GPVM nodes

Run (in a terminal):
```bash
conda create --name apptainer-env apptainer
```
* This creates a conda environment which has `apptainer` installed. This is necessary as `apptainer` is needed to open the image which has the SPINE dependency configured

Create a new python kernel with
```bash
python -m ipykernel install --name spine-apptainer-kernel --display-name "SPINE Apptainer" --user
```

In the newly created `~/.local/share/jupyter/kernels/spine-apptainer-kernel` directory add the `run_kernel.sh` and `kernel.json` files as shown here:

`run_kernel.sh`
```bash
#!/bin/bash

source ~/.bashrc
conda activate apptainer-env
apptainer exec --bind /exp/dune/data/users \
               --bind ~ \
               --env "LD_PRELOAD=\"\"" \
               --env "LC_ALL=C.UTF-8" \
               --nv /exp/sbnd/data/users/brindenc/containers/larcv2_ub2204-cuda121-torch251-larndsim.sif python -m ipykernel $@

conda deactivate
```

`kernel.json`
```json
{
  "argv": [
    "~/.local/share/jupyter/kernels/spine-apptainer-kernel/run_kernel.sh",
    "-f",
    "{connection_file}"
  ],
  "display_name": "SPINE Apptainer",
  "language": "python"
}
```

**You should now be able to start a notebook with the SPINE Apptainer kernel and run SPINE!**

### Local

Most of the notebooks can be run strictly on CPU. The following notebooks will run significantly slower on CPU, however:
- Training/validation notebook
- Inference and HDF5 file making notebook

For all other notebooks, you can run them locally, provided that you download:
- Apptainer/docker container
- Necessary data
- [SPINE v0.9.4+](https://github.com/DeepLearnPhysics/spine)

You can also pull the docker image using docker (easier on Mac and Windows) directly. First install the docker desktop client from [https://docs.docker.com/desktop/](https://docs.docker.com/desktop/).

Once that is done and the client is running, simply do:
```shell
$ docker pull deeplearnphysics/larcv2:ub2204-cu121-torch251-larndsim
```
To see which images are present on your system, you can use docker images. It will look something like this:
```shell
$ docker images
REPOSITORY                TAG                                      IMAGE ID       CREATED         SIZE
deeplearnphysics/larcv2   ub22.04-cuda12.1-pytorch2.4.0-larndsim   e97e0c78dc4b   12 months ago   25GB
```
to run a shell in your image, simply do:
```shell
$ docker run -i -t e97e0c78dc4b bash
```



* [Ask Francois](mailto:drielsma@slac.stanford.edu) for questions or a request for a separate tutorial if interested.
