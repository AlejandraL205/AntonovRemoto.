# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:44:23 2020

@author: Male
"""

import numpy as np
a = np. array ([[-2, -6], [-4,3],[5,0],[4,-6]])
x=np.array([[2,-2,2],[-2,0,-3]])

print (a.dot(x))
#ordenar a
print ("a ordenado= ", np.sort(a))
#longitud
print ("longitud= " ,a.size)
#convertir a lista
print("lista = ", a.tolist())