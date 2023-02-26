# Advanced complex arithmetic
import cmath
z = 2+3j 
print(z)

a=cmath.phase(z)
print(a)

a1=cmath.polar(z) # (3.605551275463989, 0.982793723247329)
print(a1)
#Exponential and logarithmic functions 

a2=cmath.exp(z) # (-7.315110094901103+1.0427436562359045j)  
print(a2)

a3=cmath.log(z) # (1.2824746787307684+0.982793723247329j) 
print(a3)

a4=cmath.log10(-100) # (2+1.3643763538418412j)
print(a4)

a5=cmath.rect(2, cmath.pi/2) # (0+2j)
print(a5)


#Square roots:
 
b1=cmath.sqrt(z) # (1.6741492280355401+0.8959774761298381j)
print(b1)

#Trigonometric functions and their inverses:
b2=cmath.sin(z)  # (9.15449914691143-4.168906959966565j) 
print(b2)

b3=cmath.cos(z)  # (-4.189625690968807-9.109227893755337j) 
print(b3)

b4=cmath.tan(z)  # (-0.003764025641504249+1.00323862735361j) 
print(b4)
 
b5=cmath.asin(z) # (0.5706527843210994+1.9833870299165355j) 
print(b5)
 
b6=cmath.acos(z) # (1.0001435424737972-1.9833870299165355j)
print(b6)
 
b7=cmath.atan(z) # (1.4099210495965755+0.22907268296853878j) 
print(b7)
 
b8=cmath.sin(z)**2 + cmath.cos(z)**2 # (1+0j)
print(b8)



#Hyperbolic functions and their inverses:
c1=cmath.sinh(z)  # (-3.59056458998578+0.5309210862485197j) 
print(c1)

c2=cmath.cosh(z)  # (-3.7245455049153224+0.5118225699873846j)
print(c2)  
c3=cmath.tanh(z)  # (0.965385879022133-0.009884375038322495j)  
print(c3)
c4=cmath.asinh(z) # (0.5706527843210994+1.9833870299165355j) 
print(c4) 
c5=cmath.acosh(z) # (1.9833870299165355+1.0001435424737972j)
print(c5)  
c6=cmath.atanh(z) # (0.14694666622552977+1.3389725222944935j)  
print(c6)
c7=cmath.cosh(z)**2 - cmath.sin(z)**2  # (1+0j)  
print(c7)
c8=cmath.cosh((0+1j)*z) - cmath.cos(z) # 0j
print(c8)



#Basic complex arithmetic
z = 2+3j # A complex number 
print(z)
w = 1-7j 
print(w)