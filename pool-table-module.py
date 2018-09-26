import json
# lists
current_tables = []
# class
class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = 0000
        self.end_time = 0000
        self.available = True

    def as_dict(self):
        return self.__dict__

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

# user interface while loop
while True:
    print("** Pool Table Menu **")
    menu_option = input("Enter the table number: ")
    if(menu_option == 'q'):
        break

    if(menu_option == '1'):
        #menu options for tables
        if(table1.available == True):
            table_start = input("Enter start time: ")
            table1.start_time = table_start
            table1.available = False
        elif(table1.available == False):
            table_end = input("Enter end time: ")
            table1.available = True
            table1.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table1.as_dict(),file_object, indent=2)

    elif(menu_option == '2'):
        if(table2.available == True):
            table_start = input("Enter start time: ")
            table2.start_time = table_start
            table2.available = False
        elif(table2.available == False):
            table_end = input("Enter end time: ")
            table2.available = True
            table2.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table2.as_dict(),file_object, indent=2)

    elif(menu_option == '3'):
        if(table3.available == True):
            table_start = input("Enter start time: ")
            table3.start_time = table_start
            table3.available = False
        elif(table3.available == False):
            table_end = input("Enter end time: ")
            table3.available = True
            table3.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table3.as_dict(),file_object, indent=2)

    elif(menu_option == '4'):
        if(table4.available == True):
            table_start = input("Enter start time: ")
            table4.start_time = table_start
            table4.available = False
        elif(table4.available == False):
            table_end = input("Enter end time: ")
            table4.available = True
            table4.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table4.as_dict(),file_object, indent=2)

    elif(menu_option == '5'):
        if(table5.available == True):
            table_start = input("Enter start time: ")
            table5.start_time = table_start
            table5.available = False
        elif(table5.available == False):
            table_end = input("Enter end time: ")
            table5.available = True
            table5.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table5.as_dict(),file_object, indent=2)

    elif(menu_option == '6'):
        if(table6.available == True):
            table_start = input("Enter start time: ")
            table6.start_time = table_start
            table6.available = False
        elif(table6.available == False):
            table_end = input("Enter end time: ")
            table6.available = True
            table6.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table6.as_dict(),file_object, indent=2)

    elif(menu_option == '7'):
        if(table7.available == True):
            table_start = input("Enter start time: ")
            table7.start_time = table_start
            table7.available = False
        elif(table7.available == False):
            table_end = input("Enter end time: ")
            table7.available = True
            table7.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table7.as_dict(),file_object, indent=2)

    elif(menu_option == '8'):
        if(table8.available == True):
            table_start = input("Enter start time: ")
            table8.start_time = table_start
            table8.available = False
        elif(table8.available == False):
            table_end = input("Enter end time: ")
            table8.available = True
            table8.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table8.as_dict(),file_object, indent=2)

    elif(menu_option == '9'):
        if(table9.available == True):
            table_start = input("Enter start time: ")
            table9.start_time = table_start
            table9.available = False
        elif(table9.available == False):
            table_end = input("Enter end time: ")
            table9.available = True
            table9.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table9.as_dict(),file_object, indent=2)

    elif(menu_option == '10'):
        if(table10.available == True):
            table_start = input("Enter start time: ")
            table10.start_time = table_start
            table10.available = False
        elif(table10.available == False):
            table_end = input("Enter end time: ")
            table10.available = True
            table10.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table10.as_dict(),file_object, indent=2)

    elif(menu_option == '11'):
        if(table11.available == True):
            table_start = input("Enter start time: ")
            table11.start_time = table_start
            table11.available = False
        elif(table11.available == False):
            table_end = input("Enter end time: ")
            table11.available = True
            table11.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table11.as_dict(),file_object, indent=2)

    elif(menu_option == '12'):
        if(table12.available == True):
            table_start = input("Enter start time: ")
            table12.start_time = table_start
            table12.available = False
        elif(table12.available == False):
            table_end = input("Enter end time: ")
            table12.available = True
            table12.end_time = table_end
            with open("pool-9-25-18.json", "a") as file_object:
                json.dump(table12.as_dict(),file_object, indent=2)

    else:
        print("Enter a valid table number or enter 'q' to quit.")

print("** Menu exited **")







































# comment
