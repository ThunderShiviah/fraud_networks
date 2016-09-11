from __future__ import absolute_import

import sys
if sys.version_info[:2] < (2, 7):
    m = "Python 2.7 or later is required for NetworkX (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

#import dispersion_trees.utilities.dispersion_trees
from fraud_networks import utilities
from fraud_networks.utilities.dispersion_trees import DispersionTree, DispersionEdges
