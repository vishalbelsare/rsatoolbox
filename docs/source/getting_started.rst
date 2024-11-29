.. _getting_started:

Getting started
===============

To install the latest release of rsatoolbox:

.. code-block:: sh

    pip install rsatoolbox


To get the bleeding edge or "pre-release" version:

.. code-block:: sh

    pip install --pre rsatoolbox


Or if you're using a Conda environment:

.. code-block:: sh

    conda install -c conda-forge rsatoolbox


To use rsatoolbox:

.. code-block:: python

    import numpy, rsatoolbox
    data = rsatoolbox.data.Dataset(numpy.random.rand(10, 5))
    rdms = rsatoolbox.rdm.calc_rdm(data)
    rsatoolbox.vis.show_rdm(rdms)

Also make sure your setup meets the requirements to run the toolbox with the relevant toolboxes installed (see requirements.txt). 

As in introduction, we recommend having a look at the Jupyter notebooks in ``demos``.

