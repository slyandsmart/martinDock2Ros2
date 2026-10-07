import numpy as np 
import os
import sys
import matplotlib.pyplot as plt
import scipy as sp
import roboticstoolbox as rtb
from spatialmath import SE3

import exudyn as exu




k = 21 
p = np.pi

l = k*p

print (l)


robot = rtb.models.Panda()
print(robot)

Tep = SE3.Trans(0.6, -0.3, 0.1) * SE3.OA([0, 1, 0], [0, 0, -1])
sol = robot.ik_LM(Tep)         # solve IK
print(sol)

q_pickup = sol[0]
print(robot.fkine(q_pickup))    # FK shows that desired end-effector pose was achieved
qt = rtb.jtraj(robot.qr, q_pickup, 50)

#robot.plot(qt.q, backend='pyplot', movie='panda1.gif')



