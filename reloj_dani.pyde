j = 0
o = 0
n = 0
def setup ():
    size (300, 300)
def draw():
    background(67, 247, 171)
    global j
    global o
    global n
    fill(0, 3, 1)
    circle(j, 35, 60)
    if j > height:
       j = 0
    else:
       j = map(second(), 0, 59, 0, height)
    circle(o, 140, 70)
    if o > height:
       o = 0
    else:
       o = map(minute(), 0, 59, 0, height)
    circle(n, 250, 80)
    if n > height:
       n = 0
    else:
       n = map(hour(), 0, 59, 0, height)
