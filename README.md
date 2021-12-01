# Py4research: A step-by-step tutorial on how to build a Python package for research

Py4research provides a thorough tutorial on how to build and upload a Python package for research, which is going to be presented at the "X Workshop do Programa de Pós-Graduação em Ciência da Computação". Apart from the tutorial itself, we also implemented a straightforward package to illustrate how to build its package.

---

## Guidelines

1. Every needed piece of information is elucidated in this **README**;
2. **Installation** is also straightforward and well-explained;
3. If there is a problem, please do not **hesitate** and call us.

---

## Installation

The installation process is straightforward as the package is hosted at PyPI, and the dependencies are listed on the `requirements.txt` file. One can install the package with either command, as follows:

```bash
pip install py4research
```

```bash
pip install -r requirements.txt
```

Additionally, the source files for the lecture are presented in LaTeX. Thus, one might need an additional compiler or even Overleaf to build the files into a PDF file.

---

## Getting Started

This section provides an overview of the "build your python package" tutorial and the main package description.

### Tutorial

The tutorial is written in Portuguese in a slide-based format. The contents are available in the `slides` folder and compiled to PDF using a LaTeX compiler.

### Py4research

Py4research is a standard package composed of a single `math` module composed of two sub-modules: `clustering` and `random`. Essentially, the idea is to provide a simple framework that can foster research and help the community deploy their official implementations to PyPI.

### Documentation

Every good code should come with information on how to use it, correct? Documentation is pretty straightforward to be built, as follows:

```
cd docs
pip install -r requirements.txt
```

After entering the documentation folder and installing the required dependencies, one can build its HTML version:

```
make clean
make html
```

The HTML will be available inside a `_build` folder, inside the `docs` folder.

### Unitary Tests

The first method that we offer is running solo the pytest command. This will realize all the implemented tests and return an output declaring whether they passed or failed.

```pytest tests/```

An exciting addition to the solo pytest is the coverage module. Despite offering the same outputs from the pytest, it will also offer a report that documents how much the tests cover percent of the code.

```coverage run -m pytest tests/```

```coverage report -m```

---

## Support

It is inevitable to make mistakes or create some bugs. If there is any problem or concern, we will be available at this repository or gustavo.rosa@unesp.br.

---
