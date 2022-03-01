# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:16:46 2021

@author: 30060006
"""
import numpy as np
import matplotlib.pylab as plt
import convis

retina = convis.retina.Retina()
print(retina)

inp = np.ones((100,20,20))
output = retina(inp)
    
inp = np.ones((2000,20,20))
output = retina.run(inp,dt=100)

convis.plot_5d_time(output[0])
title('On Cells (1 line = 1 pixel)')
figure()
convis.plot_5d_matshow(output[0][:,:,::50,:,:])
title('Every 50th frame of activity')
figure()
# dimension 2 is time, so we mean over all others
# to get the average activity
convis.plot_5d_time(output[0].mean((0,1,3,4)))
convis.plot_5d_time(output[1].mean((0,1,3,4)))
title('Mean Activitiy of On and Off Cells')

