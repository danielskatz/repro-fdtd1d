# repro-fdtd1d

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/danielskatz/repro-fdtd1d/master)

- Slides ([ppt](Computational_Reproducibility.pptx), [pdf](Computational_Reproducibility.pdf)) for the 3rd day (4 August) of the [FSCI 2021](https://www.force11.org/fsci/2021)
[W22 course: Research Reproducibility in Theory and Practice (biomedical focus)](https://www.force11.org/fsci/2021/course-list-abstracts#W22).
In this repository:

  - Notebook_Demonstration.ipynb is a demonstration notebook
  - Files in bin and script can be called by a terminal running inside Binder as described in the slides

- Slides ([ppt](https://github.com/danielskatz/repro-fdtd1d/blob/4fc0e0e8dd72a1c2d580cf9b8180ad61b8be9494/Computational_Reproducibility.pptx), [pdf](https://github.com/danielskatz/repro-fdtd1d/blob/4fc0e0e8dd72a1c2d580cf9b8180ad61b8be9494/Computational_Reproducibility.pdf)) for the 3rd day (12 August) of the [FSCI 2020](https://www.force11.org/fsci/2020)
[W20 course: Research Reproducibility in Theory and Practice (Examples and Focus on Biological Sciences)](https://www.force11.org/fsci/2020/fsci-2020-course-abstracts#W20).
In this repository:

  - Notebook_Demonstration.ipynb is a demonstration notebook
  - Files in bin and script can be called by a terminal running inside Binder as described in the slides

- Example Jupyter notebook for the 2nd day of the [FSCI 2018](https://www.force11.org/fsci/2018) [AM8 course on reproducibility](https://www.force11.org/fsci/2018/course-abstracts#AM8) and 2nd day of the [FSCI 2019](https://www.force11.org/fsci/2019) [AM3 course on reproducibility](https://www.force11.org/fsci/2019/course-abstracts#AM3)

  - Notebook_Demonstration.ipynb is a demonstration notebook
  - Makes use of a [data set](https://raw.githubusercontent.com/csoderberg/test_study/master/gapminder_copy.txt)
  - Also see slides 14 - 19 of https://speakerdeck.com/jhermann/jupyterhub-and-jupyter-notebook-a-view-under-the-hood?slide=14 for some info on the relationship between notebooks and various means of using/storing them
  - and this [image](https://zenodo.org/record/3332808/files/1728_TURI_Book%20sprint_45%20repo2docker_040619_v2_MK.jpg)

- Programs and examples for the computational reproducibility day of the [FSCI 2018](https://www.force11.org/fsci/2018) [AM8 course on reproducibility](https://www.force11.org/fsci/2018/course-abstracts#AM8) and [FSCI 2019](https://www.force11.org/fsci/2019) [AM3 course on reproducibility](https://www.force11.org/fsci/2018/course-abstracts#AM3)

  - fdtd_intro.ipynb is a Jupyter notebook that explains the theory and math behind the finite-difference time-domain method in 1 dimension, lightly adapted from: Understanding the Finite-Difference Time-Domain Method, John B. Schneider, http://www.eecs.wsu.edu/~schneidj/ufdtd, 2010.
  - fdtd1d.c is a C program that implements a 1D FDTD simulation of free space, and has a line that can be uncommented to insert a glass slab into the space
  - fdtd1d.py is a python program that is basically the same as the C program
  - fdtd1d.ipynb is a Jupyter notebook that steps through a bunch of examples of a 1D fdtd simulation and does some "science"

