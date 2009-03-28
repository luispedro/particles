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

from __future__ import division
import ConfigParser
import optparse
import numpy as np
import random

parser = optparse.OptionParser()
parser.add_option('--config-file', action='store', dest='configfile', default='particles.ini')
options,args = parser.parse_args()
config = ConfigParser.ConfigParser()
config.readfp(file(options.configfile))

generalconfig = dict(config.items('General'))
if 'seed' in generalconfig:
    random.seed(int(generalconfig['seed']))
    np.random.seed(int(generalconfig['seed']))

if 'save-video' in generalconfig and generalconfig['save-video'] not in ('False','false','None'):
    import sys
    print >>sys.stderr, 'save-video option not implemented!'
    sys.exit(1)

tracks = generate_tracks(config.items('Generation'))
video = generate_video(tracks)
positions = detect_particles(video)
results = link_tracks(positions)
statistics = compute_statistics(tracks,results)


# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
