# Labwise Workshop Material

Material for the LabWise workshop.

## Getting Started

The included Jupiter notebooks can be launched using Binder. Simply press the button below:
[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/bruzen/labwise)

That will take you to a webpage *http://mybinder.org:/repo/bruzen/labwise*  where you may select from files to view. On that page, click on the Jupiter notebook called *LabWise.ipynb*  to view the workshop material.

### Requirements

The python environment including library requirements beyond those included in the Anaconda are specified in the environment.yml files. Instructions for using this file to create your own local conda environment may be found here:

http://conda.pydata.org/docs/using/envs.html#create-an-environment

To create an environment from the file, type on the command line:

```
conda env create -f environment.yml
```

To activate the environment:

Linux, OS X:  ```source activate labwise```

Windows: ```activate labwise```

### Jupiter Notebook

Once you have created a local environment, you may launch a Jupiter notebook on your own machine by typing:


```
jupyter notebook
```

It will will tell you the url for the active localhost. Ensure that page is open in a web browser, and that page, as with Binder, click on the Jupiter notebook called *LabWise.ipynb*  to view the workshop material.

Help with the Jupiter notebook can be found here *http://jupyter.readthedocs.io/en/latest/content-quickstart.html*.


