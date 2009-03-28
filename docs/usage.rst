==================
Particles Usage
==================

To call particles, use the main particles.py script:

python particles.py

A particles.ini file configures all the parameters (there too many to be confortably passed on 
the command line) 

particles.ini
~~~~~~~~~~~~~~

The particles.ini file follows standard ini syntax with sections denoted by square brackets (e.g.,*[Section]*) and values as *name=value* pairs. Here's an example file:

::

    [General]
    seed=0
    save-video=False
    [Generation]
    model=brownian


General Section
----------------

    * seed: Random seed. An integer or "None". If not None, it is used to initalise the 
    random number generator
    * save-video: Whether to save the video to a file.

Generation Section
------------------

    * model: Currently only 'brownian' is supported.

