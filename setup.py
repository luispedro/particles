# -*- coding: utf-8 -*-
# Copyright (C) 2009 Particle Authors (see AUTHORS.txt)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

import setuptools
long_description = '''\
Particles is a particle simulator and tracker.

You can simulate a set of particles moving in 2D-space
in either pure Brownian motion or with conservation of momentum.
With an added noise model, particles generates a movie of the particles
moving.

Additionally, you can use standard particle tracking algorithms (currently,
the Hungarian algorithm) to track these particles and collect statistics.
Particles can also generate a movie the tracking results for visualisation 
purposes.

Finally, you can compare the inferred tracks with the simulated tracks
in order to evaluate how good your algorithm is.
'''


classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    ]

setuptools.setup(name = 'Particles', version = '0.1',
      description = 'A Particle Simulator and Tracker',
      long_description = long_description,
      author = 'Spring 09 Class of 98111 (CMU)',
      author_email = 'lpc@cmu.edu',
      license = 'MIT',
      platforms = ['Any'],
      classifiers = classifiers,
      url = 'http://code.google.com/p/particles/',
      packages = setuptools.find_packages(exclude='tests'),
      )


# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
