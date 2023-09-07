# Sudenaz Yazıcı - 2210356008
import sys
import os
current_dir_path = os.getcwd()
def save_to_file(i):  # function that writes to output file
    writing_file_name = "output.txt"
    writing_file_path = os.path.join(current_dir_path, writing_file_name)

    with open(writing_file_path, "a") as f:
        f.write(i)

def create_matrix(number_of_rows, number_of_columns, data_list):#function that creates matrix for categories to access information easily

    category = []
    for i in range(number_of_rows):
        row_list = []
        for j in range(number_of_columns):
            row_list.append(data_list[i + j])
        category.append(row_list)
    return category

reading_file_name = "".join(sys.argv[1])  # taking input file's name as an input in the command line
reading_file_path = os.path.join(current_dir_path, reading_file_name)
with open(reading_file_path, "r") as f:
    category_dict = {}
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    line_data = f.readline().split(" ")
    while line_data != [""]:  # the program reads input file line by line until the empty line

        if "\n" not in line_data[-1]:
            line_data[-1] = line_data[-1] + "\n"  # since there is no \n at the last line
        line_data[-1] = line_data[-1][:-1]  # removing \n from the last item

        if line_data[0] == "CREATECATEGORY":
            line_data[2] = line_data[2].split("x")  # line_data[2] = "widthxheight"

            if line_data[1] not in category_dict:  # checking if the category is already created or not
                category_dict[line_data[1]] = []
                category_dict[line_data[1]] = int(line_data[2][0])*int(line_data[2][1])*"X"
                category_dict[line_data[1]] = [i for i in category_dict[line_data[1]]]
                category_dict[line_data[1]] = create_matrix(int(line_data[2][0]), int(line_data[2][1]),category_dict[line_data[1]])
                print("The category '{}' having {} seats has been created".format(line_data[1],int(line_data[2][0])*int(line_data[2][1])))
                save_to_file("The category '{}' having {} seats has been created".format(line_data[1],int(line_data[2][0])*int(line_data[2][1]))+"\n")
            else :
                print("Warning: Cannot create the category for the second time. The stadium has already {}.".format(line_data[1]))
                save_to_file("Warning: Cannot create the category for the second time. The stadium has already {}.".format(line_data[1])+"\n")
        elif line_data[0] == "SELLTICKET":
            def search_letters(seat):  # function that returns the index of letters
                for letter in letters:
                    if letter == seat:
                        return letters.index(letter)

            def ticket(i):
                if i == "student":
                    return "S"
                elif i == "full":
                    return "F"
                elif i == "season":
                    return "T"
            for i in category_dict.keys():  # repeating for all categories
                if line_data[3] == i:  # line_data[3] = category name
                    for j in line_data[4:]:  # since users can write as many seats as they want after the fourth item in the line
                        if "-" in j:  # checking seat ranges
                            j = j.split("-")
                            row = search_letters(j[0][:1])  # assigning letter's index to row variable
                            columns = [x for x in range(int(j[0][1:]),int(j[1])+1)]
                            for k in columns:
                                try:  # if the user tries to sell a seat/seats that their column number do not exist,the program gives an error
                                    if category_dict[line_data[3]][row][k] != "X":  # if the seat/seats are not empty
                                        print("Warning: The seats {} cannot be sold to {} due some of them have already been sold".format(j[0]+"-"+j[1],line_data[1]))
                                        save_to_file("Warning: The seats {} cannot be sold to {} due some of them have already been sold".format(j[0] + "-" + j[1], line_data[1])+"\n")
                                        break
                                    else :
                                        category_dict[line_data[3]][row][k] = ticket(line_data[2])  # changing the information about seats in categories
                                        if k == columns[-1]:
                                            print("Success: {} has bought {} at {}".format(line_data[1], j[0]+"-"+j[1], line_data[3]))
                                            save_to_file("Success: {} has bought {} at {}".format(line_data[1], j[0] + "-" + j[1],line_data[3])+"\n")
                                            break
                                except:
                                    if columns[-1] > len(category_dict[line_data[3]][0]) and row < len(category_dict[line_data[3]]):
                                        for k in columns:
                                            try:
                                                category_dict[line_data[3]][row][k] = "X"
                                            except:
                                                pass
                                        print("Error: The category ’{}’ has less column than the specified index {}!".format(line_data[3], j[0]+"-"+j[1]))
                                        save_to_file("Error: The category ’{}’ has less column than the specified index {}!".format(line_data[3], j[0] + "-" + j[1])+"\n")
                                        break
                                    elif columns[-1] < len(category_dict[line_data[3]][0]) and row > len(category_dict[line_data[3]]):
                                        print("Error: The category ’{}’ has less row than the specified index {}!".format(line_data[3], j[0] + "-" + j[1]))
                                        save_to_file("Error: The category ’{}’ has less row than the specified index {}!".format(line_data[3], j[0] + "-" + j[1]) + "\n")
                                        break
                                    elif columns[-1] > len(category_dict[line_data[3]][0]) and row > len(category_dict[line_data[3]]):
                                        for k in columns:
                                            try:
                                                category_dict[line_data[3]][row][k] = "X"
                                            except:
                                                pass
                                        print("Error: The category ’{}’ has less row and column than the specified index {}!".format(line_data[3], j[0] + "-" + j[1]))
                                        save_to_file("Error: The category ’{}’ has less row and column than the specified index {}!".format(line_data[3], j[0] + "-" + j[1]) + "\n")
                                        break
                        else:  # checking individual seats
                            row = search_letters(j[0])  # j[0] is the given letter
                            columns = [int(j[1:])]  # j[1:] is the seat number
                            for k in columns:
                                try:  # if the user tries to sell a seat/seats that their column number do not exist,the program gives an error
                                    if category_dict[line_data[3]][row][k] != "X":  # if the seat is not empty
                                        print("Warning: The seat {} cannot be sold to {} since it was already sold!".format(j, line_data[1]))
                                        save_to_file("Warning: The seat {} cannot be sold to {} since it was already sold!".format(j, line_data[1])+"\n")
                                        break
                                    else:
                                        category_dict[line_data[3]][row][k] = ticket(line_data[2])  # changing information about seat in categories
                                        if k == columns[-1]:
                                            print("Success: {} has bought {} at {}".format(line_data[1], j,line_data[3]))
                                            save_to_file("Success: {} has bought {} at {}".format(line_data[1], j,line_data[3])+"\n")
                                            break
                                except:
                                    if columns[-1] > len(category_dict[line_data[3]][0]) and row < len(category_dict[line_data[3]]):
                                        for k in columns:
                                            try:
                                                category_dict[line_data[3]][row][k] = "X"
                                            except:
                                                pass
                                        print("Error: The category ’{}’ has less column than the specified index {}!".format(line_data[3], j))
                                        save_to_file("Error: The category ’{}’ has less column than the specified index {}!".format(line_data[3], j)+"\n")
                                        break
                                    elif columns[-1] < len(category_dict[line_data[3]][0]) and row > len(category_dict[line_data[3]]):
                                        print("Error: The category ’{}’ has less row than the specified index {}!".format(line_data[3], j))
                                        save_to_file("Error: The category ’{}’ has less row than the specified index {}!".format(line_data[3], j) + "\n")
                                        break
                                    elif columns[-1] > len(category_dict[line_data[3]][0]) and row > len(category_dict[line_data[3]]):
                                        for k in columns:
                                            try:
                                                category_dict[line_data[3]][row][k] = "X"
                                            except:
                                                pass
                                        print("Error: The category ’{}’ has less row and column than the specified index {}!".format(line_data[3], j))
                                        save_to_file("Error: The category ’{}’ has less row and column than the specified index {}!".format(line_data[3], j)+"\n")
                                        break

        elif line_data[0] == "CANCELTICKET":
            def search_letters(seat):
                for letter in letters:
                    if letter == seat:
                        return letters.index(letter)
            def ticket(i):
                if i == "student":
                    return "S"
                elif i == "full":
                    return "F"
                elif i == "season":
                    return "T"
            for i in category_dict.keys():  #repeating for every category
                if line_data[1] == i:  # line_data[1] = category name
                    for j in line_data[2:]:
                        if "-" in j:
                            j = j.split("-")
                            row = search_letters(j[0][:1])
                            columns = [x for x in range(int(j[0][1:]),int(j[1])+1)]
                            for k in columns:
                                try:  # if the user tries to cancel seat/seats that their column number do not exist, the program gives an error
                                    if category_dict[line_data[1]][row][k] != "X" and columns[-1] <= len(category_dict[line_data[1]][0]) and row <= len(category_dict[line_data[1]]):
                                        category_dict[line_data[1]][row][k] = "X"
                                        if k == columns[-1]:
                                            print("Success: The seats {} at ’{}’ has been canceled and now ready to sell again".format(j[0]+"-"+j[1],line_data[1]))
                                            save_to_file("Success: The seats {} at ’{}’ has been canceled and now ready to sell again".format(j[0] + "-" + j[1], line_data[1])+"\n")
                                            break
                                    else:
                                        if k == columns[-1]:
                                            print("Error: The seats {} at ’{}’ has already been free! Nothing to cancel".format(j[0]+"-"+j[1],line_data[1]))
                                            save_to_file("Error: The seats {} at ’{}’ has already been free! Nothing to cancel".format(j[0] + "-" + j[1], line_data[1])+"\n")
                                            break
                                except:
                                    if columns[-1] > len(category_dict[line_data[1]][0]) and row <= len(category_dict[line_data[1]]):
                                        print("Error: The category ’{}’ has less column than the specified index {}!".format(line_data[1], j[0]+"-"+j[1]))
                                        save_to_file("Error: The category ’{}’ has less column than the specified index {}!".format(line_data[1], j[0] + "-" + j[1])+"\n")
                                        break
                                    elif columns[-1] <= len(category_dict[line_data[1]][0]) and row > len(category_dict[line_data[1]]):
                                        print("Error: The category ’{}’ has less row than the specified index {}!".format(line_data[1], j[0] + "-" + j[1]))
                                        save_to_file("Error: The category ’{}’ has less row than the specified index {}!".format(line_data[1], j[0] + "-" + j[1]) + "\n")
                                        break
                                    elif columns[-1] > len(category_dict[line_data[1]][0]) and row > len(category_dict[line_data[1]]):
                                        print("Error: The category ’{}’ has less row and column than the specified index {}!".format(line_data[1], j[0] + "-" + j[1]))
                                        save_to_file("Error: The category ’{}’ has less row and column than the specified index {}!".format(line_data[1], j[0] + "-" + j[1]) + "\n")
                                        break
                        else:
                            row = search_letters(j[0])
                            columns = [int(j[1:])]
                            for k in columns:
                                try:  # if the user tries to cancel seat/seats that their column number do not exist, the program gives an error
                                    if category_dict[line_data[1]][row][k] != "X":
                                        category_dict[line_data[1]][row][k] = "X"
                                        if k == columns[-1]:
                                            print("Success: The seat {} at ’{}’ has been canceled and now ready to sell again".format(j, line_data[1]))
                                            save_to_file("Success: The seat {} at ’{}’ has been canceled and now ready to sell again".format(j, line_data[1])+"\n")
                                            break
                                    else:
                                        if k == columns[-1]:
                                            print("Error: The seat {} at ’{}’ has already been free! Nothing to cancel".format(j,line_data[1]))
                                            save_to_file("Error: The seat {} at ’{}’ has already been free! Nothing to cancel".format(j,line_data[1])+"\n")
                                            break
                                except:
                                    if columns[-1] > len(category_dict[line_data[1]][0]) and row < len(category_dict[line_data[1]]):
                                        print("Error: The category ’{}’ has less column than the specified index {}!".format(line_data[1], j))
                                        save_to_file("Error: The category ’{}’ has less column than the specified index {}!".format(line_data[1], j)+"\n")
                                        break
                                    elif columns[-1] < len(category_dict[line_data[1]][0]) and row > len(category_dict[line_data[1]]):
                                        print("Error: The category ’{}’ has less row than the specified index {}!".format(line_data[1], j))
                                        save_to_file("Error: The category ’{}’ has less row than the specified index {}!".format(line_data[1], j) + "\n")
                                        break
                                    elif columns[-1] > len(category_dict[line_data[1]][0]) and row > len(category_dict[line_data[1]]):
                                        print("Error: The category ’{}’ has less row and column than the specified index {}!".format(line_data[1], j))
                                        save_to_file("Error: The category ’{}’ has less row and column than the specified index {}!".format(line_data[1], j) + "\n")
                                        break

        elif line_data[0] == "SHOWCATEGORY":
            category_dict[line_data[1]].reverse()
            new_letters = letters.copy()
            new_letters = new_letters[:len(category_dict[line_data[1]])]  # getting letters for every column
            new_letters.reverse()
            print("Printing category layout of {}".format(line_data[1]))
            save_to_file("Printing category layout of {}".format(line_data[1])+"\n")
            for i in range(len(category_dict[line_data[1]])):
                print(new_letters[i], end=" ")
                save_to_file(new_letters[i] + " ")
                for j in range(len(category_dict[line_data[1]][0])):  # len(category_dict[line_data[1][0]]) = number of columns
                    print(category_dict[line_data[1]][i][j], end="  ")
                    save_to_file("  {}".format(category_dict[line_data[1]][i][j]))
                print()
                save_to_file("\n")
            print("  ", end="")
            save_to_file("  ")
            for i in range(len(category_dict[line_data[1]][0])):
                print(i, end="  ")
                save_to_file(str(i)+"  ")
            print()
            save_to_file("\n")
            category_dict[line_data[1]].reverse()  #since we reversed it at the beginning, we need to reverse it again to avoid complications

        elif line_data[0] == "BALANCE":
            students = 0
            full_pay = 0
            season_ticket = 0
            for i in range(len(category_dict[line_data[1]])):
                students += category_dict[line_data[1]][i].count("S")
                full_pay += category_dict[line_data[1]][i].count("F")
                season_ticket += category_dict[line_data[1]][i].count("T")
            revenue = 10*students + 20*full_pay + 250*season_ticket
            print("Category report of ’{}’".format(line_data[1]))
            save_to_file("Category report of ’{}’".format(line_data[1])+"\n")
            print("_"*30)
            save_to_file("_"*30+"\n")
            print("Sum of students = {}, Sum of full pay = {}, Sum of season ticket={}, and Revenues = {} Dollars".format(students, full_pay, season_ticket, revenue))
            save_to_file("Sum of students = {}, Sum of full pay = {}, Sum of season ticket={}, and Revenues = {} Dollars".format(students, full_pay, season_ticket, revenue)+"\n")
        line_data = f.readline().split(" ")