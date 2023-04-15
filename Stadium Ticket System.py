import sys
open ('output.txt', 'w').close()
input = sys.argv[1]
with open(input, "r") as data:
    data = data.read()
    data = data.replace("\n"," ")
    data = data.split(" ")
    data.append("end of list")  #when data is reaching the end at the loop, it gives an index error. To avoid this, i put a new element at the end of the list.
count = 0
categories = dict()
category_seats = dict()
category_balance = dict()
category_ticket = dict()
def output(text):
    with open('output.txt', mode='a', encoding="utf-8") as x:
        x.write(str(text) + "\n")
    print(text)
def output_layout(text):
    with open('output.txt', mode='a', encoding="utf-8") as x:
        x.write(str(text))
    print(text, end = "")
def newcategory():
    if categories.__contains__(new_category):
        output(f"Warning: Cannot create the category for the second time. The stadium has already {new_category}")
    else:
        row, column = category_field.split("x")
        row = int(row)
        column = int(column)
        field = row * column
        categories[new_category] = category_field, row, column
        output(f"The category '{new_category}' having {field} seats has been created")        
def sellticket():
    balance = 0
    sum_of_students = 0
    sum_of_full = 0
    sum_of_season = 0
    keys_list = list(category_seats.keys())
    category = (customers[data[count]][1])
    if category_ticket.__contains__(category):
        pass
    else:
        category_ticket[category] = dict()
    if not keys_list.__contains__(category):
        category_seats[category] = []
    for i in seats:
        ticket_row = ord(i[0])-64
        ticket_column = i[1]
        if int(ticket_row) > int(categories[category][1]) and ticket_column > int(categories[category][2]):
            output(f"Error: The category '{category}' has less row and column than the specified index {i}!")
        elif int(ticket_row) > int(categories[category][1]):
            output(f"Error: The category '{category}' has less row than the specified index {i}!")
        elif int(ticket_column) > int(categories[category][2]):
            output(f"Error: The category '{category}' has less column than the specified index {i}!")
        elif category_seats[category].__contains__(i):
            output(f"Warning: The seat {i} cannot be sold to {data[count]} since it was already sold!")
        else:
            category_seats[category].append(i)
            output(f"Success: {data[count]} has bought {i} at {category}")
            if data[count+1] == "student":
                sum_of_students += 1
                balance += 10
                category_ticket[category][i]= "student"
            elif data[count+1] == "full":
                sum_of_full += 1
                balance += 20
                category_ticket[category][i]= "full"
            elif data [count+1] == "season":
                sum_of_season +=1
                balance += 250
                category_ticket[category][i]= "season"
    for j in seats_range:
        range_value = j.split("-")
        range_row = ord(range_value[0][0])-64
        range_column_start = int(range_value[0][1])
        range_column_end = int(range_value[1])
        for l in range(range_column_start, range_column_end+1):
            if int(range_row) > int(categories[category][1]) and l > int(categories[category][2]):
                output(f"Error: The category '{category}' has less row and column than the specified index {j}!")
        if int(range_row) > int(categories[category][1]):
            output(f"Error: The category '{category}' has less row than the specified index {j}!")
        for h in range(range_column_start, range_column_end+1):
            if h > int(categories[category][2]):
                output(f"Error: The category '{category}' has less column than the specified index {j}!")
                break
        else:
            success_printed = False
            for m in range(range_column_start, range_column_end+1):
                x = range_value[0][0] + str(m)
                if category_seats[category].__contains__(x):
                    output(f"Warning: The seats {j} cannot be sold to {data[count]} due some of them have already been sold")
                    break                 
                else:
                    if not success_printed:
                        output(f"Success: {data[count]} has bought {j} at {category}")  
                        success_printed = True
                    category_seats[category].append(x)
                    if data[count+1] == "student":
                        sum_of_students += 1
                        balance += 10
                        category_ticket[category][x]= "student"
                    elif data[count+1] == "full":
                        sum_of_full += 1
                        balance += 20
                        category_ticket[category][x]= "full"
                    elif data [count+1] == "season":
                        sum_of_season +=1
                        balance += 250
                        category_ticket[category][x]= "season"
    if category_balance.keys().__contains__(category):
        category_balance[category][0] += sum_of_students
        category_balance[category][1] += sum_of_full
        category_balance[category][2] += sum_of_season
        category_balance[category][3] += balance
    else:
        category_balance[category] = list([sum_of_students, sum_of_full, sum_of_season, balance])  
def cancelticket():
    for b in cancel_seats:
        cancel_ticket_row = ord(b[0])-64
        cancel_ticket_column = b[1:]
        if int(cancel_ticket_row) > int(categories[cancel_category][1]) and cancel_ticket_column > int(categories[cancel_category][2]):
            output(f"Error: The category '{cancel_category}' has less row and column than the specified index {b}!")
        elif int(cancel_ticket_row) > int(categories[cancel_category][1]):
            output(f"Error: The category '{cancel_category}' has less row than the specified index {b}!")
        elif int(cancel_ticket_column) > int(categories[cancel_category][2]):
            output(f"Error: The category '{cancel_category}' has less column than the specified index {b}!")
        elif not category_seats[cancel_category].__contains__(b):
            output(f"Error: The seat {b} at ’{cancel_category}’ has already been free! Nothing to cancel")
        else:
            category_seats[cancel_category].remove(b)
            if category_ticket[cancel_category][b] == "student":     
                category_balance[cancel_category][0] -= 1
                category_balance[cancel_category][3] -= 10
            elif category_ticket[cancel_category][b] == "full":
                category_balance[cancel_category][1] -= 1
                category_balance[cancel_category][3] -= 20
            elif category_ticket[cancel_category][b] == "season":
                category_balance[cancel_category][2] -=1
                category_balance[cancel_category][3] -= 250
            del category_ticket[cancel_category][b]
            output(f"Success: The seat {b} at '{cancel_category}' has been canceled and now ready to sell again")
def balance():
    output(f"Category report of '{balance_category}'")
    output("-------------------------------")
    output(f"Sum of students = {category_balance[balance_category][0]}, Sum of full pay = {category_balance[balance_category][1]}, Sum of season ticket = {category_balance[balance_category][2]}, and Revenues = {category_balance[balance_category][3]} Dollars")
def showcategory():
    output(f"Printing category layout of {show_category}")
    output("")
    for v in reversed(range(categories[show_category][1])):
        layout_letter = chr(v + 65)
        output_layout(layout_letter+" ")
        for c in range(categories[show_category][1]):
            layout_ticket = str(layout_letter) + str(c)
            if category_seats[show_category].__contains__(layout_ticket):
                if category_ticket[show_category][layout_ticket] == "student":
                    output_layout("S"+"  ")
                elif category_ticket[show_category][layout_ticket] == "full":
                    output_layout("F"+"  ")
                elif category_ticket[show_category][layout_ticket] == "season":
                    output_layout("T"+"  ")
            else:
                output_layout("X"+"  ")
        output_layout("\n")
    for z in range(categories[show_category][1]):
        if z < 10:
            output_layout("  "+str(z))
        else:
            output_layout(" "+str(z))
    output_layout("\n")

for i in data: #I know this is not the best solution for the finding the commands. With readlines() method commands can be reached easily and executed. But i will always using readlines(), i want to try something different for this time.
    count +=1 #this is just index of the i
    if i == "CREATECATEGORY":
        new_category = data[count]
        category_field = data[count+1]
        newcategory()
    elif i == "SELLTICKET":
        customers = dict()
        customers_seat = dict()
        seats = []
        seats_range = []
        customers[data[count]] = data[count+1], data[count+2]
        j = 2
        while data[count+j] != "SELLTICKET" and data[count+j] != "CREATECATEGORY" and data[count+j] != "CANCELTICKET" and data[count+j] != "BALANCE" and data[count+j] != "SHOWCATEGORY" and data[count+j] != "end of list":
            j += 1
            if data[count+j].__contains__("-"):
                seats_range.append(data[count+j])  #I seperated normal seats and ranged seats(like A0-6) because it will be easier to execute inputs when i seperate to 2 lists.
            else:
                seats.append(data[count+j])
        seats.pop()   #This is for delete the command at the beginning of the list.
        sellticket()
    elif i == "CANCELTICKET":
        cancel_seats = []
        cancel_category = data[count]
        n = 0
        while data[count+n] != "SELLTICKET" and data[count+n] != "CREATECATEGORY" and data[count+n] != "CANCELTICKET" and data[count+n] != "BALANCE" and data[count+n] != "SHOWCATEGORY" and data[count+n] != "end of list":
            n += 1
            cancel_seats.append(data[count+n])
        cancel_seats.pop()
        cancelticket()
    elif i == "BALANCE":
        balance_category = data[count]
        balance()
    elif i == "SHOWCATEGORY":
        show_category = data[count]
        showcategory()
