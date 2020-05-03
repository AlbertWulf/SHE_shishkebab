import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np
import math
############
from ReadData import ReadData
from SHE import SHE
#####Parameters of experimental device#########
global pixel_width       #pixel width,unit:nm
pixel_width = 320e3 
lam_x = 0.124              # X-ray wavelength, unit:nm
dis_s2d = 5300e6           #sample-to-detector distance, unit:nm
############constant definition################
pi = math.pi
###############################################
init_data=ReadData("data/1.4/50k-132-1.401286.asc")
px_min = 122
px_max = 362
pz_min = 166
pz_max = 326
cen_px = (px_max+px_min)/2
cen_pz = (pz_max+pz_min)/2
I = init_data[pz_min:(pz_max+1),px_min:(px_max+1)]
plt.imshow(I[:,40:200])
plt.axis('off')
plt.colorbar()
#EI = np.sqrt(I)
#I_max = 0.05*np.max(I)
#########################
#x = pixel_width*np.arange(px_min-cen_px,px_max-cen_px+1)
#z = pixel_width*np.arange(pz_min-cen_pz,pz_max-cen_pz+1)
#s0 = 1/lam_x/dis_s2d
#s3 = s0*z
#s12 = s0*x
#Qz = 2*pi*s3
#Qx = 2*pi*s12
#Q = np.zeros((z.shape[0],x.shape[0]))
#for i in range(0,x.shape[0]):
#    for j in range(0,z.shape[0]):
#        Q[j,i] = math.sqrt(Qx[i]**2+Qz[j]**2)
#Q2d = np.zeros((z.shape[0],x.shape[0]))
#Q2d = Q
#I = I/I_max
#EI = EI/I_max
#A= SHE(2,Q,Qz,Qx,I,s0,x,z)
#plt.plot(A.squeeze())
#plt.show()