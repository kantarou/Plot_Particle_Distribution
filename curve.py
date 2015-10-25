
import numpy as np
#-------------------------------------------------
# read functions
#-------------------------------------------------

def read_professor(file_name):
	import csv
	#open a csv file
	#file_name = str(raw_input("Please Enter File Name (you don't have to type '.csv'): "))
	reader = csv.reader(open(file_name + ".csv", "rb"), delimiter = ";")

	print file_name + " is opened.\n"

	#image = np.empty((width, height))
	#skip lines
	for i in xrange(9):
		reader.next()

	#Read data
	datas = []
	for line in reader:
		datas += [line]

	#Make image
	image = np.zeros((len(datas), len(datas[0])))
	i = 0
	for line in datas:
		j = 0
		for x in line:
			image[i, j] = float(x)
			j += 1
		i += 1

	return image



#-------------------------------------------------
# read csv
#-------------------------------------------------
def read_csv(file_name="", mode = "profssor"):
    if mode is "hiji":
    	return read_hiji(file_name)
        # return read_hiji("./particle/" + "particle_dist" + "_0")
    else:
    	return read_professor(file_name)
        # return read_profssor("vert_reflect_bound_0.5_0_2_")


#-------------------------------------------------
# Main
#-------------------------------------------------

#image = read_csv(file_name = "./particle/" + "particle_dist" + "_0")

image  = read_csv(mode = "luba", file_name = "./plot/normal/output")
image2 = read_csv(mode = "luba", file_name = "./plot/triangle/output")
#image3 = read_csv(mode = "lubash", file_name = "./professor2/diag_reflect_bound_0.90_0.00_3.00_")
arrayY = []
arrayX = []



"""
professor's data
"""
def forLine(image):
    import math
    arrayY = []
    arrayX = []
    for x in xrange(len(image[0])):
        arrayY = arrayY + [image[0][x]]
        arrayX = arrayX + [(x - 300)/ math.sqrt(2)]
    return (arrayX, arrayY)

def forDiag(image, layer):
    arrayY = []
    arrayX = []

    import math
    def function(x, layer):
        return -1 * x + 100 * math.sqrt(2) + 300 + 1 + layer
        #return (x - 50/math.sqrt(2)) - 50/math.sqrt(2)

    for x in xrange(len(image)):
    	temp = function(x, layer)
    	#print temp, x
    	if 0 <= temp < len(image):
            arrayY = arrayY + [image[temp][x]]
            arrayX = arrayX + [x - 50*math.sqrt(2) - 150]
            #arrayX = arrayX + [x*math.sqrt(2)]
    	else:
            arrayY = arrayY + [0]
            arrayX = arrayX + [x - 50*math.sqrt(2) - 150]
            #arrayX = arrayX + [x*math.sqrt(2)]
    return (arrayX, arrayY)


def forDiag(image, R, theta):
    import math
    def function(x, R):
        return math.tan(theta) * (x - R*math.cos(theta) - 300) + (R*math.sin(theta)+300)
        
    for x in xrange(len(image)):
        temp = function(x, layer)
        #print temp, x
        if 0 <= temp < len(image):
            arrayY = arrayY + [image[temp][x]]
            arrayX = arrayX + [x - 50*math.sqrt(2) - 150]
            #arrayX = arrayX + [x*math.sqrt(2)]
        else:
            arrayY = arrayY + [0]
            arrayX = arrayX + [x - 50*math.sqrt(2) - 150]
            #arrayX = arrayX + [x*math.sqrt(2)]
    return (arrayX, arrayY)



curve = forLine(image)
triangle = []

for layer in xrange(10):
    triangle += [forDiag(image2, layer)]


import matplotlib.pyplot
plot = matplotlib.pyplot
#plot.subplot(211)
plot.title("distribution")
#plot.imshow(image)
plot.plot(curve[0]  ,curve[1] , label = "normal")
for i in xrange(len(triangle)):
    plot.plot(triangle[i][0], triangle[i][1], label = "layer_" + str(i) )

plot.legend(loc="upper left")
plot.show()



