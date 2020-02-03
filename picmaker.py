fout = open("image.ppm", 'w')

fout.write("P3\n256 256\n255\n")

def makeString(i, j, k):
    return str(i) + " " + str(j) + " " + str(k) + " "

for x in range(256):
    for y in range(256):
        fout.write(makeString(x*y % 255, x*y*x % 255, (x*y*y) % 255))
    fout.write("\n")
fout.close()
