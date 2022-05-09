# Archimedes_pi.py
# Calculation of pi via Archimedes method
import numpy as np
#initialize 
N0 = [6,4]             # sumber of sizes for initial polygon
D0 = [1, np.sqrt(2)]   # side length for initial polygon 
Pi= np.pi              # Pi = 3.14159265....
print('pi =', Pi)
with open('pi.out','w') as fo:
    for n, D_n in zip(N0,D0):
        ss = 'Calculation starts with n = {:4d}'.format(n)
        print(ss)
        fo.write(ss+'\n')
        while n <= 45000000:
            p = n * D_n/2.0   # calculate result for pi
            pe = p-Pi          # Deviation from the real value
            ss= "n= {0:8d}, pi_n = {1:21.16f}, error= {2:.2e}".format(n,p,pe)
            print(ss)
            fo.write(ss+'\n')
            n *=2
            ah2 = (D_n/2)**2
            OD = np.sqrt(1 - ah2)
            D_n = np.sqrt((1-OD)**2 + ah2) # Lengh for the new side
