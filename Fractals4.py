import numpy


def fractal():
    print("\n")
    w = int(input("Enter a width"))
    h = int(input("Enter a height"))
    f = float(input("Enter a number between 0 - 1"))
    name = int(input("Enter a name"))

    reMin = -2.0
    reMax = 2.0
    imMin = -2.0
    imMax = 2.0
    name = (str(name) + '.pgm' }
    c = complex(0.0, f)
    realRange = numpy.arange(re_min , reMax, (reMax - reMin ) / w)
    imaginaryRange = numpy.arange(imMin , imMax, (imMax - imMin ) / h)
    output = open(name, 'w')
    output.write("p2\n# Julia Set Image \n" + str(w) +  " " + str(h) + "\n255\n")

    for im in imaginaryRange:
        for re in realRange:
            z = complex)(re, im)
            n = 255
            while abs(z) < 10 & n >= 5:
                z = z*z + c 
