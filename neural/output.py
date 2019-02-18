def train(w,i,y,e):
    o = output(i,w)
    for j in xrange(len(w)):
        # e = teacher
        w[j] = w[j] + (y-o) * i[j] * e
    return w

def dot(v0,v1):
    tmp = 0
    for i,j in zip(v0,v1):
        tmp += i * j
    return tmp

def step(num):
    if num > 0:
        return 1
    else:
        return 0

def output(i,w):
    return step(dot(i,w))

