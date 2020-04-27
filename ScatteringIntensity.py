from scipy.special import gamma
import math
import numpy as np
from scipy import special

def ScatteringIntensity(params,Qz,Qx,I):
    d = params[0]
    K = params[1]
    B = params[2]
    D0 = params[5]
    nuD = params[6]
    nuT = params[7]
    T0 = params[8]
    sigmaD = params[9]
    sigmaT = params[10]
    D = params[11]
    T = params[12]
    def hx(X0,nuX,x):
        def GAMMA(nuX):
            M = 1
            while nuX >168:
                nuX = nuX-1
                M = M*nuX
            GA = gamma(nuX)
            return GA,M
        GA,M = GAMMA(nuX)
        gammaX = GA*M
        powerX = 2*nuX-1
        h_x = 2/gammaX*((x/X0)^powerX) * math.exp(-(x/X0)^2)
        
        return h_x
        N1 = 151
        N2 = 151



    def FormFactor(D,T,sigmaD,sigmaT):
        N1 = 151
        N2 = 152
        d = np.zeros((N1))
        hd = np.zeros((N1))
        d0 = max(0,(D - sigmaD * 5))
        t0 = max(0,(T-sigmaT*5))
        dD = sigmaD*10/N1
        dT = sigmaT*10/N2
        IntD = 0.0
        IntT = 0.0
        Vz2Av = 0.0
        Vxy2Av = 0.0
        for i in range(0,N1):
            d[i] = d0 + dD*(i-0.5)
            hd[i] = hx(D0,nuD,d[i])
            IntD = IntD + hd[i]*dD
            Vxy = math.pi*d[i]/4
            Vxy2Av = Vxy2Av + Vxy**2*hd[i]*dD

        hd = hd/IntD
        Vxy2Av = Vxy2Av/IntD
        t = np.zeros((N2))
        ht = np.zeros((N2))
        for j in range(0,N2):
            t[i] = t0 + dT*(j-0.5)
            ht[i] = hx(T0,nuT,t[i])
            IntT = IntT + ht[j]*dT
            Vz2Av = Vz2Av + t[j]**2*ht[j]*dT
        ht = ht/IntT
        Vz2Av = Vz2Av/IntT
        V2Av = abs(Vxy2Av*Vz2Av)
        FQ2Av = np.zeros((Qz.shape[0],Qx.shape[0]))
        FQAv = np.zeros((Qz.shape[0],Qx.shape[0]))
        Fx2Av = 0
        FxAv = 0
        Fz2Av = 0
        FzAv = 0
        for iz in Qz:
            for ix in Qx:
                z = Qz[iz]
                x = Qx[ix]
                for i in range(0,N1):
                    if x == 0:
                        Fx = math.pi*d[i]**2/4
                    else :
                        Fx = math.pi**2/4*2*special.jv(1,d[i]*x/2)/(d[i]*Qx/2)
                        Fx2Av = Fx2Av + Fx**2*hd[i]*dD
                for j in range(0,N2):
                    if z == 0:
                        Fz = t[j]
                    else:
                        Fz = t[j]*math.sin(t[j]*z/2)/(t[j]*z/2)
                    Fz2Av = Fz2Av + Fz**2*ht[j]*dT
                FQ2Av[iz,ix] = Fx2Av*Fz2Av
                FQAv[iz,ix] = FxAv*FzAv
        FQAv2 = np.abs(FQAv)*np.abs(FQAv)/V2Av
        FQ2Av = np.abs(FQ2Av)/V2Av
        betaQ = FQAv2/FQ2Av
        return FQ2Av,betaQ
    FQ2Av,betaQ = FormFactor(D,T,sigmaD,sigmaT)
    
    def conv_N(L,sigmaL,N,sigmaN,Q):
        Z = (N/sigmaN)**2-1
        











           

