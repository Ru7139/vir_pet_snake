#@save
# import collections
# import hashlib
# import math
# import os
# import random
# import re
# import shutil
# import sys
# import tarfile
# import time
# import zipfile
# from collections import defaultdict
# import pandas as pd
# import requests
# from IPython import display
# from matplotlib import pyplot as plt
# from matplotlib_inline import backend_inline

#@save
# import numpy as np
import torch
# import torchvision
# from PIL import Image
# from torch import nn
# from torch.nn import functional as F
# from torch.utils import data
# from torchvision import transforms


x = torch.arange(12)
print(x)
print(x.shape) # torch.Size([12])
print(x.numel(), "\n") # 12

x34 = x.reshape(3,4)
print(x34, "\n")

zero_tensor = torch.zeros((2,3,4))
print(zero_tensor)
