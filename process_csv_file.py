# This code shows how to open a csv file
# called 'txtScores.csv' and extract, parse,
# and process its contents and write results
# to another file called 'csvAverages.csv'

# filenames - same folder - just use name of file
input_filename = 'csvScores.csv'
output_filename = 'csvAverages.csv'

# open the files and assign the objects that
# are returned to a variables
my_input_file = open(input_filename,'r')
my_output_file = open(output_filename,'w')

#get the first line using readline() – headers
firstline = my_input_file.readline()			#reads first line only
headers = firstline.strip().split(',')		# use strip and split – returns list
print(headers)						# print

#put the first line in the output file
my_output_file.write("Name,Average Score \n")

# loop through each line in the input file
# data type of each line is a string
for line in my_input_file:
    # need to create name and avg variables in this section

    ################ Your code goes here  ################
    row = line[:-1].split(",")
    name = row[0] + " " + row[1]
    avg = (int(row[2] + row[3] + row[4]))/3

    #write the name and the average score to the output file
    my_output_file.write(name + ',' + str(int(avg)) + '\n')


# close the files
my_input_file.close()
my_output_file.close()

print("Finished processing file.")
