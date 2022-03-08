#40,70
#lat/long

file = open("sample_accidents_coded_19-21.csv","r")

new_file = open("markers.txt","w")

for line in file:
    line = line.split(",")
    if line[1].find("no") != -1 and line[1].find("Open") == -1:
        new_file.write("var circle = L.circleMarker(["+str(line[2])+", "+str(line[3].replace("\n","")+"], { \n"))
        new_file.write("    color: 'green', \n")
        new_file.write("    fillColor: 'green', \n")
        new_file.write("    fillOpacity: 1.0, \n")
        new_file.write("    radius: 3 \n")
        new_file.write("    }).addTo(mymap); \n")
        new_file.write("\n")
    elif line[1].find("yes") != -1 and line[1].find("Open") == -1:
        new_file.write("var circle = L.circleMarker(["+str(line[2])+", "+str(line[3].replace("\n","")+"], { \n"))
        new_file.write("    color: 'red', \n")
        new_file.write("    fillColor: 'red', \n")
        new_file.write("    fillOpacity: 1.0, \n")
        new_file.write("    radius: 3 \n")
        new_file.write("    }).addTo(mymap); \n")
        new_file.write("\n")

file.close()
new_file.close()
