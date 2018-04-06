import torch
import numpy as np


print(list(map(float, str(torch.FloatTensor(5)[2:4]).split("\n")[1:-2])))
