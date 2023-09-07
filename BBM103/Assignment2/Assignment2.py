# Sudenaz Yazıcı - 2210356008
import os

current_dir_path = os.getcwd()

def save_to_file(i):
    writing_file_name = "doctors_aid_outputs.txt"
    writing_file_path = os.path.join(current_dir_path, writing_file_name)

    with open(writing_file_path, "a") as f:
        f.write(i+"\n")

def create(x,y):  # x = patient_list   y = data
    if [y] in x:
        save_to_file("Patient {} cannot be recorded due to duplication.".format(y[0]))
    else:
        x += [y]
        save_to_file("Patient {} is recorded.".format(y[0]))

def remove_patient(x,y):  # x = patient_list   y = data
    for j in range(len(x)):
        if y[0] == x[j][0]:
            del x[j]
            save_to_file("Patient {} is removed.".format(y[0]))
            return 0
    save_to_file("Patient {} cannot be removed due to absence.".format(y[0]))

def probability(x,y):  # x = patient_list   y = data
    for k in range(len(x)):

        if y[0] == x[k][0]:
            floats = []
            floats.append(x[k][1]) # adding diagnosis accuracy
            floats.append(x[k][3]) # adding disease incidence
            floats.append(x[k][5]) # adding treatment risk
            floats = [eval(number) for number in floats]
            prob = (floats[1]/(floats[1] + 1-floats[0]))*100 # (rate of people having the disease)/(rate of people having the disease + probability of wrong calculation)
            prob = ("{:.2f}".format(prob))
            prob = float(prob)
            prob = str(prob) + "%"
            save_to_file("Patient {} has a probability of {} of having {}.".format(x[k][0],prob,x[k][2]))
            return 0
    save_to_file("Probability for {} cannot be calculated due to absence.".format(y[0]))

def recommendation(x, y): # x = patient_list   y = data
    for k in range(len(x)):
        if y[0] == x[k][0]:
            floats = []
            floats.append(x[k][1]) # adding diagnosis accuracy
            floats.append(x[k][3]) # adding disease incidence
            floats.append(x[k][5]) # adding treatment risk
            floats = [eval(number) for number in floats]
            prob = (floats[1]/(floats[1] + 1-floats[0]))*100
            prob = ("{:.2f}".format(prob))
            prob = float(prob)
            floats[2]=floats[2]*100
            if prob > floats[2]:
                save_to_file("System suggests {} to have the treatment.".format(x[k][0]))
            else:
                save_to_file("System suggests {} NOT to have the treatment.".format(x[k][0]))

def show_list():
    save_to_file("Patient\tDiagnosis\tDisease\t\tDisease\tTreatment\t\tTreatment")
    save_to_file("Name\tAccuracy\tName\t\tIncidence\tName\t\tRisk")
    save_to_file("-"*75)
    for patient in patient_list:
        floats = []
        floats.append(patient[1])
        floats.append(patient[5])
        floats = [eval(number) for number in floats]
        floats[0] = floats[0] * 100
        floats[1] = floats[1] * 100
        floats[0] = str(floats[0]) + "%"
        floats[1] = str(floats[1]) + "%"
        save_to_file(patient[0]+"\t"+floats[0]+"\t"+patient[2]+"\t\t"+patient[3]+"\t"+patient[4]+"\t\t"+floats[1])

def read_file():
    reading_file_name = "doctors_aid_inputs.txt"
    reading_file_path = os.path.join(current_dir_path, reading_file_name)
    with open(reading_file_path, "r") as f:
        global patient_list
        patient_list = []
        for line in "doctors_aid_inputs.txt":
            line_list = f.readline().split(" ",1)
            command = line_list[0]
            if "\n" not in line_list[-1]:
                line_list[-1]=line_list[-1]+"\n" # since there is no \n at the last line

            if command == "create":
                data = line_list[1].split(", ")
                data[-1]= data[-1][:-1] # removing \n from the last item
                create(patient_list, data)
            elif command == "remove":
                data = [line_list[1]]
                data[-1] = data[-1][:-1] # removing\n from the last item
                remove_patient(patient_list, data)
            elif command == "probability":
                data = [line_list[1]]
                data[-1] = data[-1][:-1] # removing \n from the list item
                probability(patient_list,data)
            elif command == "recommendation":
                data = [line_list[1]]
                data[-1] = data[-1][:-1] # removing \n from the last item
                recommendation(patient_list,data)
            elif command == "list\n":
                show_list()
read_file()