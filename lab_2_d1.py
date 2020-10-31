a = int(input())
b = int(input())
c = int(input())
D = (b**2)-(4 * a * c)
if D > 0:
    x1 = ((-b) + (D ** 0.5))/(a*2)
    x2 = ((-b) - (D ** 0.5))/(a*2)
    print(x1)
    print(x2)
elif D == 0:
    x =(-b/2*a)
    print(x)
elif D<0:
    print('корней нет')
    
    

    

    
    
    
    