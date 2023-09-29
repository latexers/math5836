


'''
A Python program  

'''
import numpy as np 

import matplotlib.pyplot as plt


import random


def function_name(a,b):
  #  函数主体
   para_sum = a + b
  #  返回值
  #  return para_sum
 
def sum_numpy(a):
  #a = [[1, 12, 3], [51, 6, 17], [7, 18, 9]]
  sum = 0
  for x in range(a.shape[0]):
     for y in range(a.shape[1]):
        for z in range(a.shape[2]):
           sum += a[x][y][z]
           sum += a[x,y,z]
  for x in range(len(a)):
    for y in range(len(a[x])):
        print(x, y, ' *' , a[x][y] )
        sum = sum + a[x][y]
  return sum 
    

def add(a):
  sum = a + b
  pass

add(3)


def numpy_lists():

 x = np.zeros(15)
 y = np.ones(15)
 z = x + y

 k = y * 10

 '''print(x)
 print(y)
 print (z)
 print(k)'''

 magic = np.random.rand(3,4)
  
 magic_three = np.random.rand(3,4,2)
 # homework, write a function for summing 3D magic
 magic_one = np.random.rand(10)

 #print(magic)
 #print(magic_one)
 print(magic_three)
 print(magic.shape)

 magic_sum = sum_numpy(magic)
 print( magic_sum, ' is magic sum')





def main(): 

 
    numpy_lists()
  
 



if __name__ == '__main__':
    main()
