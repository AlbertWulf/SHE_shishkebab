from scipy.special import beta
import docutils.utils.math
import matplotlib.pyplot as plt 
import numpy as np
import math
def get_hx_para(x,sigma_x):
    errConv = 1e-5
    nuX = np.arange(errConv,500,errConv)
    B = beta(nuX,0.5)
    F=nuX-(math.pi*(1+sigma_x*sigma_x/x/x))/(B*B)
    F_abs = np.abs(F)
    nuX_s = nuX[F_abs.argmin()]
    x0_s = x*beta(nuX_s,0.5)/math.sqrt(math.pi)

    return x0_s,nuX_s
