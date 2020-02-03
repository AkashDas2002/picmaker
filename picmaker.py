import math

fout = open("image.ppm", 'w')

fout.write("P3\n500 500\n255\n")

def makeString(i, j, k):
    return str(i) + " " + str(j) + " " + str(k) + " "

def geoMean(m,n):
    return math.floor(math.sqrt((m+1)*(n+1))) % 255

def average(m,n):
    return math.floor((m + n) / 2) % 255

def harmonicMean(m,n):
    return math.floor(2.0 / (1.0 / (m + 1)) + (1.0 / (n + 1))) % 255


for x in range(500):
    for y in range(500):
        fout.write(makeString(average(x,y), geoMean(x,y), harmonicMean(x,y)))
    fout.write("\n")
fout.close()
