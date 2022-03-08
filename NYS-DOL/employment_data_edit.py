file = open("restaurant_employment.csv","r")
outfile = open("restaurant_employment_reformatted.csv","w")
outfile.write("Date, Restaurant Employment \n")

for line in file:
    if line.find("Year") == -1:
        line = line.split(",")
        for val in line:
            if line.index(val) != 0 and line.index(val) != len(line) -1:
                date = str(line.index(val))+"/1/"+line[0]
                outfile.write(date+","+str(val)+"\n")

file.close()
outfile.close()
        
