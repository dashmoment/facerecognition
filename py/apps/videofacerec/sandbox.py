import sys, os
sys.path.append("../..")

# Import Matplotlib:
import matplotlib
matplotlib.use('Agg')
import matplotlib.cm as cm

# For Python2 backward comability:
from builtins import range

# import facerec modules
from facerec.feature import Fisherfaces, SpatialHistogram, Identity
from facerec.distance import EuclideanDistance, ChiSquareDistance
from facerec.classifier import NearestNeighbor
from facerec.model import PredictableModel
from facerec.validation import KFoldCrossValidation
from facerec.visual import subplot
from facerec.util import minmax_normalize
from facerec.serialization import save_model, load_model
# import numpy, matplotlib and logging
import numpy as np
# try to import the PIL Image module
try:
    from PIL import Image
except ImportError:
    import Image
import logging
import matplotlib.pyplot as plt
from facerec.lbp import LPQ, ExtendedLBP

import cv2


frame = cv2.imread('data/s1/1.pgm')
cv2.imshow("Image", frame)  
cv2.waitKey()  