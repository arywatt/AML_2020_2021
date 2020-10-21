import numpy as np
import math

ar = np.zeros(40)
bin_size = int(math.floor(255/40))

bin_indexes = [(2*i+1)*3 for i in range(41)]
print(bin_indexes)