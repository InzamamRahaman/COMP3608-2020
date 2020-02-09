import numpy as np 


E = np.random.choice(a=[0, 1], size=(5000, 20))
x = np.random.random(20)

d = E @ x + np.random.normal(size=5000)

fp = open('E.npy', 'wb')
np.save(fp, E)
fp.close()

fp = open('d.npy', 'wb')
np.save(fp, d)
fp.close()