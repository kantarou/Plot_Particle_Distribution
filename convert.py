import numpy as np

#-------------------------------------------------
# read functions
#-------------------------------------------------
def read_hiji(file_name):
    import csv
    #-------------------------------------------------
    #read init file
    #-------------------------------------------------
    def read_init():
        file_name = "init_data"
        reader = csv.reader(open(file_name+".csv", "rb"), delimiter=",")
        print file_name + " is opened.\n"
        
        width, height = 0, 0
        particle = 0
        fileNumber = 0

        for i in reader:
            width, height = int(i[0]), int(i[1])
            particle = int(i[2])
            fileNumber = int(i[3])

        return (width, height, particle)


    #-------------------------------------------------
    #read csv
    #-------------------------------------------------
    (width, height, particle) = read_init()
    #find max and min
    _max, _min = 0, 0
    reader = csv.reader(open(file_name + ".csv", "rb"), delimiter=",")
    for i in reader:
        _max = max(_max, i[2])
        _min = min(_min, i[2])

    #make image
    reader = csv.reader(open(file_name + ".csv", "rb"), delimiter=",")
    print file_name + " is opened.\n"

    image = np.zeros((height, width))
    for i in reader:
        image[i[1], i[0]] = float(i[2])/particle

    return image




#-------------------------------------------------
# read csv
#-------------------------------------------------
def read_csv(file_name="", mode = "hiji"):
    if mode is "hiji":
    	return read_hiji(file_name)
        # return read_hiji("./particle/" + "particle_dist" + "_0")
    else:
    	return read_professor(file_name)
        # return read_profssor("vert_reflect_bound_0.5_0_2_")


#-------------------------------------------------
# Main
#-------------------------------------------------
import csv
image = read_csv(file_name="particle_dist_0")

f = open("output.csv", "w")
output_csv = csv.writer(f, lineterminator='\n', delimiter=";")

for temp in xrange(9):
    output_csv.writerow(["# dammy data"])

for array in image:
	output_csv.writerow(array)

f.close()










