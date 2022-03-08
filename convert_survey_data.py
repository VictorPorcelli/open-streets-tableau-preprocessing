file = open("Citywide_Mobility_Survey_-_May_2020.csv","r")
outfile = open("reformatted_cms_may2020.csv","w")
outfile.write("Question, Rating, Id \n")

questions_indeces = []
questions = []
for line in file:
    if line.find("person_id") != -1:
        line = line.split(",")
        for val in line:
            if val.find("attitude") != -1:
                questions_indeces.append(line.index(val))
                questions.append(val)
    else:
        line = line.split(",")
        for question in questions_indeces:
            outfile.write(str(questions[questions_indeces.index(question)])+","+str(line[question])+","+str(line[0])+"\n")

outfile.close()
file.close()
    
