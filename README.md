# Notebooks for "Noise Characterization and Error Mitigation in Near-Term Quantum Computers"

* Christopher J. Wood
* IBM Quantum, T. J. Watson Research Center, Yorktown Heights, NY, USA

## Introduction

This repository contains Jupyter notebooks used to run the experiments and generate the figures in the proceedings article *Noise Characterization and Error Mitigation in Near-Term Quantum Computers*.

## Notebooks

1. [Interleaved Randomized Benchmarking](https://github.com/chriseclectic/ncemntqc/blob/master/notebooks/1_irb.ipynb)
2. [Quantum Process Tomography](https://github.com/chriseclectic/ncemntqc/blob/master/notebooks/2_qpt.ipynb)
3. [Measurement Error Characterization](https://github.com/chriseclectic/ncemntqc/blob/master/notebooks/3_meas_char.ipynb)
4. [Measurement Error Mitigation](https://github.com/chriseclectic/ncemntqc/blob/master/notebooks/4_meas_mit.ipynb)

## Installation

This code in this repository requires Python and [Qiskit](https://qiskit.org) to run. A conda environment containing all the required dependencies can be installed with

```
$ conda env create -f environment.yml
```

To run experiments and generate data an IBM Quantum Experience account is also required. The saved experimental data can be loaded and used for running simulations and analysis used without an account.

Note that the measurement error mitigation notebooks currently require code from a development branch of [qiskit-ignis](https://github.com/qiskit/qiskit-ignis) which is specified in the `environment.yml` file.
