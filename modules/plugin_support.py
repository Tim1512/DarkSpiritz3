#!/usr/bin/python3
from dave import *
import sys, os
import os.path
RescoursesDir = os.getcwd() + "/modules"

sys.path.insert(0, RescoursesDir)
import logging

dashboard()
