from imutils import paths
import numpy as np
import argparse
import cv2
import os

def dhash(image, hashSize=8):