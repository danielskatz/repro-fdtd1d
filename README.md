# repro-fdtd1d

Programs and examples for the computational reproducibility day of the [FSCI 2018](https://www.force11.org/fsci/2018) [AM8 course on reproducibility](https://www.force11.org/fsci/2018/course-abstracts#AM8)

- fdtd_intro.ipynb is a Jupyter notebook that explains the theory and math behind the finite-difference time-domain method in 1 dimension, lightly adapted from: Understanding the Finite-Difference Time-Domain Method, John B. Schneider, http://www.eecs.wsu.edu/~schneidj/ufdtd, 2010.
- fdtd1d.c is a C program that implements a 1D FDTD simulation of free space, and has a line that can be uncommented to insert a glass slab into the space
- fdtd1d.py is a python program that is basically the same as the C program
- fdtd1d.ipynb is a Jupyter notebook that steps through a bunch of examples of a 1D fdtd simulation and does some "science"
