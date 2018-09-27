import json
# lists
current_tables = []
# class
class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = 0
        self.end_time = 0
        self.play_time_hours = 0
        self.play_time_minutes = 0
        self.available = True

    def as_dict(self):
        return self.__dict__

    def as_string(self):
        return "\nTable #: {0}\nStart time: {1}\nEnd time: {2}\nTotal time: {3} hours {4} minutes\nAvailable: {5}\n".format(self.table_number,self.start_time,self.end_time,self.play_time_hours,self.play_time_minutes,self.available)


# for index in range(1,13):
#     table = Table(str(index))
#     current_tables.append(table.__dict__)
#
# print("using a loop")
# print(current_tables)

# class objects
table1 = Table("1")
table2 = Table("2")
table3 = Table("3")
table4 = Table("4")
table5 = Table("5")
table6 = Table("6")
table7 = Table("7")
table8 = Table("8")
table9 = Table("9")
table10 = Table("10")
table11 = Table("11")
table12 = Table("12")

all_tables = [table1,table2,table3,table4,table5,table6,table7,
table8,table9,table10,table11,table12]

current_tables = [table1.__dict__, table2.__dict__, table3.__dict__, table4.__dict__, table5.__dict__, table6.__dict__, table7.__dict__, table8.__dict__, table9.__dict__, table10.__dict__, table11.__dict__, table12.__dict__]


try:
    with open("current.json","r") as file_object:
        loaded_tables = json.load(file_object)
        for i in range(len(all_tables)):
            all_tables[i].available = loaded_tables[i]['available']
            all_tables[i].start_time = loaded_tables[i]['start_time']
except:
    with open("current.json", "w") as file_object:
        json.dump(current_tables,file_object, indent=2)

# print(current_tables)

# user interface while loop
while True:
    print("** Pool Table Menu **")
    menu_option = input("Enter the table number or type 'v' to view all: ")
    if(menu_option == 'q'):
        break

    if(menu_option == '1'):

        #table = current_tables[int(menu_option) - 1]

        #menu options for tables
        if(table1.available == True):
            table_start = input("Enter start time: ")
            table1.start_time = table_start
            table1.available = False
        elif(table1.available == False):
            table_end = str(input("Enter end time: "))
            table1.available = True
            table1.end_time = table_end
            string_table_start = str(table1.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table1.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table1.play_time_hours = hours
            table1.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table1.as_string())

    elif(menu_option == '2'):
        if(table2.available == True):
            table_start = input("Enter start time: ")
            table2.start_time = table_start
            table2.available = False
        elif(table2.available == False):
            table_end = str(input("Enter end time: "))
            table2.available = True
            table2.end_time = table_end
            string_table_start = str(table2.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table2.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table2.play_time_hours = hours
            table2.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table2.as_string())

    elif(menu_option == '3'):
        if(table3.available == True):
            table_start = input("Enter start time: ")
            table3.start_time = table_start
            table3.available = False
        elif(table3.available == False):
            table_end = str(input("Enter end time: "))
            table3.available = True
            table3.end_time = table_end
            string_table_start = str(table3.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table3.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table3.play_time_hours = hours
            table3.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table3.as_string())

    elif(menu_option == '4'):
        if(table4.available == True):
            table_start = input("Enter start time: ")
            table4.start_time = table_start
            table4.available = False
        elif(table4.available == False):
            table_end = str(input("Enter end time: "))
            table4.available = True
            table4.end_time = table_end
            string_table_start = str(table4.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table4.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table4.play_time_hours = hours
            table4.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table4.as_string())

    elif(menu_option == '5'):
        if(table5.available == True):
            table_start = input("Enter start time: ")
            table5.start_time = table_start
            table5.available = False
        elif(table5.available == False):
            table_end = str(input("Enter end time: "))
            table5.available = True
            table5.end_time = table_end
            string_table_start = str(table5.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table5.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table5.play_time_hours = hours
            table5.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table5.as_string())

    elif(menu_option == '6'):
        if(table6.available == True):
            table_start = input("Enter start time: ")
            table6.start_time = table_start
            table6.available = False
        elif(table6.available == False):
            table_end = str(input("Enter end time: "))
            table6.available = True
            table6.end_time = table_end
            string_table_start = str(table6.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table6.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table6.play_time_hours = hours
            table6.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table6.as_string())


    elif(menu_option == '7'):
        if(table7.available == True):
            table_start = input("Enter start time: ")
            table7.start_time = table_start
            table7.available = False
        elif(table7.available == False):
            table_end = str(input("Enter end time: "))
            table7.available = True
            table7.end_time = table_end
            string_table_start = str(table7.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table7.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table7.play_time_hours = hours
            table7.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table7.as_string())

    elif(menu_option == '8'):
        if(table8.available == True):
            table_start = input("Enter start time: ")
            table8.start_time = table_start
            table8.available = False
        elif(table8.available == False):
            table_end = str(input("Enter end time: "))
            table8.available = True
            table8.end_time = table_end
            string_table_start = str(table8.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table8.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table8.play_time_hours = hours
            table8.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table8.as_string())

    elif(menu_option == '9'):
        if(table9.available == True):
            table_start = input("Enter start time: ")
            table9.start_time = table_start
            table9.available = False
        elif(table9.available == False):
            table_end = str(input("Enter end time: "))
            table9.available = True
            table9.end_time = table_end
            string_table_start = str(table9.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table9.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table9.play_time_hours = hours
            table9.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table9.as_string())

    elif(menu_option == '10'):
        if(table10.available == True):
            table_start = input("Enter start time: ")
            table10.start_time = table_start
            table10.available = False
        elif(table10.available == False):
            table_end = str(input("Enter end time: "))
            table10.available = True
            table10.end_time = table_end
            string_table_start = str(table10.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table10.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table10.play_time_hours = hours
            table10.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table10.as_string())

    elif(menu_option == '11'):
        if(table11.available == True):
            table_start = input("Enter start time: ")
            table11.start_time = table_start
            table11.available = False
        elif(table11.available == False):
            table_end = str(input("Enter end time: "))
            table11.available = True
            table11.end_time = table_end
            string_table_start = str(table11.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table11.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table11.play_time_hours = hours
            table11.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table11.as_string())

    elif(menu_option == '12'):
        if(table12.available == True):
            table_start = input("Enter start time: ")
            table12.start_time = table_start
            table12.available = False
            print(table12.available)
        elif(table12.available == False):
            table_end = str(input("Enter end time: "))
            table12.available = True
            table12.end_time = table_end
            string_table_start = str(table12.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table12.end_time)
            if(len(string_table_end) == 3):
                hours = int(string_table_end[0])
                minutes = int(string_table_end[1,3])
                end_total = hours * 60 + minutes
            elif(len(string_table_end) == 4):
                hours = int(string_table_end[:2])
                minutes = int(string_table_end[2:4])
                end_total = hours * 60 + minutes
            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            table12.play_time_hours = hours
            table12.play_time_minutes = minutes
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table12.as_string())

    elif(menu_option == 'v'):
            print(current_tables)

    else:
        print("Enter a valid table number or enter 'q' to quit.")


    current_tables = [table1.__dict__, table2.__dict__, table3.__dict__, table4.__dict__, table5.__dict__, table6.__dict__, table7.__dict__, table8.__dict__, table9.__dict__, table10.__dict__, table11.__dict__, table12.__dict__]
    with open("current.json", "w") as file_object:
        json.dump(current_tables,file_object, indent=2)




print("** Menu exited **")
