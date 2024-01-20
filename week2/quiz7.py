def Square_root_Q7(number):
    c=number
    g=c/2
    i=0
    while(abs(g*g*g-c)>0.000000000001):
        g=2*g/3+c/(3*g*g)
        i=i+1
        print("%d:%.13f"%(i,g))

Square_root_Q7(10)