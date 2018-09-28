import json
# lists
tables_as_dict = []
# class
class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = 0
        self.end_time = 0
        self.play_time_hours = 0
        self.play_time_minutes = 0
        self.available = True
        self.cost = 0.0

    def get_cost(self):
        total_minutes = ((self.play_time_hours * 60) + self.play_time_minutes)
        self.cost = total_minutes * 0.5
        return self.cost

    def as_dict(self):
        return self.__dict__

    def as_string(self):
        return "\nTable #: {0}\nStart time: {1}\nEnd time: {2}\nTotal time: {3} hours {4} minutes\nAvailable: {5}\nCost: {6}\n".format(self.table_number,self.start_time,self.end_time,self.play_time_hours,self.play_time_minutes,self.available,self.cost)

# for index in range(1,13):
#     table = Table(str(index))
#     tables_as_dict.append(table.__dict__)
#
# print("using a loop")
# print(tables_as_dict)

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

tables_as_dict = [table1.__dict__, table2.__dict__, table3.__dict__, table4.__dict__, table5.__dict__, table6.__dict__, table7.__dict__, table8.__dict__, table9.__dict__, table10.__dict__, table11.__dict__, table12.__dict__]


try:
    with open("current.json","r") as file_object:
        loaded_tables = json.load(file_object)
        for i in range(len(all_tables)):
            all_tables[i].available = loaded_tables[i]['available']
            all_tables[i].start_time = loaded_tables[i]['start_time']
except:
    with open("current.json", "w") as file_object:
        json.dump(tables_as_dict,file_object, indent=2)

# print(tables_as_dict)

# user interface while loop
while True:
    print("** Pool Table Menu **")
    menu_option = input("Enter 1 to start/end tables\n2 to view tables\n3 to quit: ")
    if(menu_option == '3'):
        break
    elif(menu_option == '2'):
            print(tables_as_dict)

    elif(menu_option == '1'):

        table_choice = int(input("Select the table: "))
        table_selector = all_tables[(table_choice - 1)]

        if(table_selector.available == True):
            table_start = input("Enter start time: ")
            table_selector.start_time = table_start
            table_selector.available = False
        elif(table_selector.available == False):
            table_end = str(input("Enter end time: "))
            table_selector.available = True
            table_selector.end_time = table_end
            string_table_start = str(table_selector.start_time)
            if(len(string_table_start) == 3):
                hours = int(string_table_start[0])
                minutes = int(string_table_start[1,3])
                start_total = hours * 60 + minutes
            elif(len(string_table_start) == 4):
                hours = int(string_table_start[:2])
                minutes = int(string_table_start[2:4])
                start_total = hours * 60 + minutes
            string_table_end = str(table_selector.end_time)
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
            table_selector.play_time_hours = hours
            table_selector.play_time_minutes = minutes
            table_selector.cost = table_selector.get_cost()
            with open("pool-9-27-18.txt","a") as file_object:
                file_object.write(table_selector.as_string())

    else:
        print("Enter a valid menu option.")

    tables_as_dict = [table1.__dict__, table2.__dict__, table3.__dict__, table4.__dict__, table5.__dict__, table6.__dict__, table7.__dict__, table8.__dict__, table9.__dict__, table10.__dict__, table11.__dict__, table12.__dict__]
    with open("current.json", "w") as file_object:
        json.dump(tables_as_dict,file_object, indent=2)

print("** Menu exited **")
