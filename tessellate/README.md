# Introduction

The following repository contains code for tessellating representative volume elements (RVE) of alloys. The RVE is generated using Neper, a software package for polycrystal generation and meshing ([LINK](https://neper.info/)). The intention of the code is to make certain features of Neper more accessible, as well as provide additional features that is not natively implemented in Neper (e.g., CSL boundaries). That said, Neper still has more features not provided by the code (e.g., transforming, triple-scale RVEs, multiple distributions). As such, users are advised to directly use Neper instead if greater customisability is desired.

The code was developed by Janzen Choi as part of his PhD candidature, supervised by Jay Kruzic, Ondrej Muránksy, and Mark Messner. The code was used to develop a microstructure-informed crystal plasticity model for predicting the elevated-temperature creep of Alloy 617. It is worth noting that the developers of Neper contributed to the development code, namely for answering so many questions on their discussion board ([LINK](https://github.com/neperfepx/neper/discussions)).

# Preparation

1) Install Neper using the official instructions ([LINK](https://github.com/neperfepx/neper)).
2) Open WSL and go to your working directory.
3) Run `git clone https://github.com/janzennnnn/cpfem_tessellate` to clone the repository.
4) Run `cd crystal_plasticity/src` to go to the source directory of the program.

# Using the Program

1) Run `cd crystal_plasticity/src` to go to the source directory of the program.
2) Create a Python file (e.g., `main.py`).
3) Edit the Python file using the provided API class to customise the RVE - instructions on how to do this are in the next subsection of this document.
4) Run the Python file from the source directory (e.g., run `python3 main.py`) - this will create a `results` directory, where the output of the program will be located.

# Using the API

To use the API, first import the API class via `from modules.api import API`. Then, create an instance of the API class via `api = API()`. From here, you can call the API functions to customise the shape, structure, and texture of the RVE, as well as export images and statistics of the RVE.

## API Functions

The following section contains brief descriptions of the available API functions.
##

#### Define the 2D / 3D domain of the RVE
`api.define_square(<shape_length>)`

`api.define_cube(<shape_length>)`
* `shape_length` is the length of the RVE (in arbitrary units)
* Issues may arise if `shape_length` is not an integer
##

#### Generate a tessellation of parent grains based on the equivalent radius and sphericity distributions
`api.add_grains(<equivalent_radius_mu>, <equivalent_radius_sigma>, <sphericity_mu>, <sphericity_sigma>)`
* `equivalent_radius_mu` is the mu value for the lognormal distribution of the equivalent radius of the grains (in arbitrary units)
* `equivalent_radius_sigma` is the sigma value for the lognormal distribution of the equivalent radius of the grains (in arbitrary units)
* `sphericity_mu` is the mu value for the lognormal distribution of 1-sphericity of the grains
* `sphericity_sigma` is the sigma value for the lognormal distribution of 1-sphericity of the grains
* The equivalent radius of a grain is defined as the radius of a sphere with the equivalent volume of the grain
* The sphericity of a grain is defined as the ratio between the surface area of a sphere with the equivalent volume of the grain and the surface area of the grain
##

#### Loads a tessellation of parent grains based on a path
`api.load_grains(<path>)`
* `path` is the relative path to the tessellation file
* The domain is automatically defined upon loading the tessellation
* The function will not run if the tessellation has twins
* Note that this function was added due to the tessellation of the parent grains taking comparably longer to execute
##

#### Insert twin structures into the tessellation
`api.add_twins(<twin_width_mu>, <twin_width_sigma>, <twin_width_min>)`
* `twin_width_mu` is the mu value for the lognormal distribution of the widths of the twins
* `twin_width_sigma` is the sigma value for the lognormal distribution of the widths of the twins
* `<twin_width_min>` is the minimum value for the widths of the twins
##

#### Insert crystallographic orientation of the tessellation
`api.add_orientation_random()`
* This function applies random orientations to the grains (and twins, if they are added)

`api.add_orientation_csl(<csl_sigma>)`
* `csl_sigma` is the sigma value as a string
* Available values for `csl_sigma` include `"3"`, `"5"`, `"7"`, `"9"`, `"11"`, `"13a"`, `"13b"`, `"15"`, `"17a"`, `"17b"`, `"19a"`, `"19b"`, `"21a"`, `"21b"`, `"23"`, `"25a"`, `"25b"`, `"27a"`, `"27b"`, `"29a"`, `"29b"`, `"31a"`, `"31b"`, `"33c"`, `"35a"`, and `"35b"`
* The sigma value defines the coincidence site lattice (CSL) boundaries, and thus, the misorientation between the grains and twin structures
* This function ensures the CSL relationship between the grains and twins, and is thus only available for tessellations with twins
##

#### Generate a tetrahedral mesh from the tessellation
`api.mesh()`
* Creates a `.msh` file
##

#### Export a file of a certain format using the tessellation
`api.export_file(<format>)`
* `format` is the format of the output file
* Available values for `format` include `"tess"`, `"tesr"`, `"sim"`, `"geo"`, `"ply"`, `"stl"`, `"obj"`, `"3dec"`, `"vtk"`, and `"ori"`
##

#### Export the grain / twin / cell / voxel statistics
`api.export_grains()`

`api.export_twins()`

`api.export_cells()`

`api.export_voxels(<resolution>)`
* `resolution` is the length of each voxel
##

#### Visualise the tessellation / mesh
`api.visualise_tess()`

`api.visualise_mesh()`
##

#### Store auxiliary files
`api.store_auxiliary()`
* Opts out of removing the auxiliary files when the program finishes
##

#### Force start the generation process
`api.force_start()`
* Note that this function ignores all the implemented error checks, and is thus not recommended for typical use
##

## Example

The following is an example of how the API can be used.

```
from modules.api import API

api = API()
api.define_square(500)
api.add_grains(2.94032, 0.99847, -1.6229, 0.40402)
api.add_twins(1.46831, 0.79859)
api.add_orientation_csl("3")
api.visualise_tessellation()
```
