def EXPMOD(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y>>1
        x = (x * x) % p

    return res

def EUCLIDES(a,b):
    if b == 0:
        return a
    else:
        return EUCLIDES(b, a%b)

def EUCLIDESEXT(a,b):
    if b == 0:
        return(a,1,0)
    else:
        (d,x1,y1) = EUCLIDESEXT(b, a%b)
        aux = a/b
        p= int(aux)
        (x,y) = (y1, x1-(p*y1))
        return(d,x,y)

def cifrado(M,N,E):
  a=EXPMOD(M, E, N)
  return a

def inverso(a,n):   
  if EUCLIDES(a,n) == 1:
    (p,x,y)=EUCLIDESEXT(a,n)
    m =x%n
    return m

e1 = 7
n = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
c1 = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
e2 = 11
c2 = 35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184
    
(d1, x1, y1) = EUCLIDESEXT(e1,e2)
(d2, x2, y2) = EUCLIDESEXT(c2,n)
if(d1==1 and d2==1):
  print("Puedo iniciar ataque")
  ic2=inverso(c2,n)
  
  if x1<0:
    x = EXPMOD(c1,-x1, n)
    y = EXPMOD(ic2,-y1, n)
  else :
    x = pow(c1,x1, n)
    y = pow(c2,y1,n)
  

  m = ((x * y))% n

cif=cifrado(m,n,e1)

print("N=",n)
print("C=",c1)
print("M=",m)
print("C=",cif)


