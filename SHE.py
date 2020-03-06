#SHE 
import numpy as np
import math
pixel_width = 320e3
def SHE(order,Q,Qz,Qx,I,s0,x,z):
    cos_theta = Q*0 
    Y00 = Q*0
    Y20 = Q*0
    Y40 = Q*0
    Sp00 = Q*0
    Sp20 = Q*0
    Sp40 = Q*0
    S00 = Q*0
    S20 = Q*0
    S40 = Q*0
    


    for ix in range(0,Qx.shape[0]):
        for iz in range(0,Qz.shape[0]):
            ## runtime error:Q[iz,iz] can be zero
            cos_theta[iz,ix] = Qz[iz]/Q[iz,ix]
            Y00[iz,ix] = 1
            Y20[iz,ix] = math.sqrt(5/4)*(3*cos_theta[iz,ix]**2-1)
            Y40[iz,ix] =3/8*(35*cos_theta[iz,ix]**4-30*cos_theta[iz,ix]**2+3)
            #WZ SHE Eq27
            ## runtime error:Q[iz,iz] can be zero
            Sp00[iz,ix] = math.pi/2*abs(Qx[ix]/Q[iz,ix])*Y00[iz,ix]*I[iz,ix]
            Sp20[iz,ix] = math.pi/2*abs(Qx[ix]/Q[iz,ix])*Y20[iz,ix]*I[iz,ix]
            Sp40[iz,ix] = math.pi/2*abs(Qx[ix]/Q[iz,ix])*Y40[iz,ix]*I[iz,ix]
    max_Q = 2*math.pi*s0*math.sqrt((z.max())**2+(x.max())**2)
    min_Q = 0
    RQ = max_Q-min_Q
    dQ = 2*math.pi*s0*pixel_width
    NQ = math.ceil(RQ/dQ)
    QQ = np.zeros((NQ,1)).squeeze()
    SQ00 = np.zeros((NQ,1)).squeeze()
    SQ20 = np.zeros((NQ,1)).squeeze()
    SQ40 = np.zeros((NQ,1)).squeeze()
    for i in range(1,NQ):
        QQ[i] = min_Q+dQ*(i-1)
        Qr_min = min_Q + dQ*(i-1.5)
        Qr_max = min_Q + dQ*(i-0.5)
        SQ00[i] = np.mean(Sp00[(Q>Qr_min) & (Q<Qr_max)])
        SQ20[i] = np.mean(Sp20[(Q>Qr_min) & (Q<Qr_max)])
        SQ40[i] = np.mean(Sp40[(Q>Qr_min) & (Q<Qr_max)])
    
    
    SQ00 = np.convolve(SQ00,[1/3,1/3,1/3],mode='same')
    SQ20 = np.convolve(SQ20,[1/3,1/3,1/3],mode='same')
    SQ40 = np.convolve(SQ40,[1/3,1/3,1/3],mode='same')
    for i in range(1,NQ):
        QQ[i] = min_Q+dQ*(i-1)
        Qr_min = min_Q + dQ*(i-1.5)
        Qr_max = min_Q + dQ*(i-0.5)
        index = np.where((Q>Qr_min) & (Q<Qr_max))
        S00[index] = SQ00[i]
        S20[index] = SQ20[i]
        S40[index] = SQ40[i]

    index = np.where((QQ>2*math.pi*s0*pixel_width*(math.sqrt(2)*12.5)) & (QQ<=min(Qz.max(),Qx.max())))
    Q_1d = QQ[index]
    S_1d = S20[index]
    S00Y00 = S00*Y00
    S20Y20 = S20*Y20
    S40Y40 = S40*Y40
    return S00Y00


    


            



