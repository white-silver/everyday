from output import *

if __name__ == '__main__':
    #each list's last element is bias(constant)
    x1 = [[0,0,0,1],[0,0,1,1],[0,1,0,1],[0,1,1,1],[1,0,0,1],[1,0,1,1],[1,1,0,1],[1,1,1,1]]
    #y = teacher
    y1 = [0,0,0,0,1,1,1,1]
    weight1 = [0,0,0,0]
    weight2 = [0,0,0,0]
    a1 = []
    a2 = []
    A = []
    V1 = [0,0,0]
    y2 = [0,0,0,0,1,1,1,1]
    e = 0.1
    
    #times of repeat 
    rep = 100

    for i in xrange(rep):
        for x,y in zip(x1,y1):
            weight1 = train(weight1,x,y,e)
            weight2 = train(weight2,x,y,e)
    for i in xrange(len(x1)):        
        a1.append(output(x1[i],weight1))
    for i in xrange(len(x1)):
        a2.append(output(x1[i],weight2))
    
    for i in xrange(len(a1)):
        A.append([a1[i],a2[i],1])
    
    for i in xrange(rep):
        for a,y in zip(A,y2):
            V1 = train(V1,a,y,e)
    
    #debug print
    print weight1
    print weight2
    print V1
    for x in x1:
        print output([output(x,weight1),output(x,weight2)],V1)
