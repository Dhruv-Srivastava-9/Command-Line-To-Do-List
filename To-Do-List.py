class To_Do_List:
    tasks = []
    keybinds = ["Q", "E", "X", "A"] #Keybinds available

    #Add a new task to the list
    def add_task(self):
        task = input("Enter a new Task: ")
        print("New Task Added!")
        self.tasks.append(task) #Add the task to the list

    #Remove task to remove the task in the list

    def remove_task(self):
        if self.tasks: #Check to see if the list is empty or not
            self.display_task()
            rev = input("Enter index to remove: ") #Index to remove
            if rev.isdigit(): #Check wether the rev variable is digit or not
                rev = int(rev) - 1 #Index correctly so if it displayes 1st task is at 1 and we type 1 its actual index is 0
                if 0 <= rev < len(self.tasks): #to check if the index is = 0 or <0
                    removed_task = self.tasks.pop(rev) #removes using .pop()
                    print(f"Task '{removed_task}' removed.") #printing
                else:
                    print("Invalid index.") #If index equal to or below than 0
            else:
                print("Invalid input. Please enter a valid index.") #when index is not integer/number
        else:
            print("No tasks to remove.") #if no tasks print this

    
    #Displayes the current tasks

    def display_task(self):
        if self.tasks: #check is the list empty
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1): #using a for loop print tasks and start the index as 1(Display only)
                print(f"{index}. {task}") #print the index and task in a way of for loop 1 2 3 4 index and the list on a seperate line
        else:
            print("No Tasks") #if no tasks to desplay 

    def exit_fuction():
        quit()

    
    def write_function(self):
        with open(self.filename, "w") as file:
            file.write("\n".join(self.tasks))
        print(f"To-Do List saved to {self.filename}")

    #Assign keybinds:

    def keybind(self):
        print("A = Add, D = Display, X = Remove, Z = Exit") #Display the use of keybinds assigned
        key = input("Choose the desired key bind to perform: ")
        key = key.upper()
        if key == "A": 
            self.add_task()
        elif key == "D":
            self.display_task()
        elif key == "X":
            self.remove_task()
        elif key == "Z":
            self.exit_function()
        elif key == "S":
            self.write_function
        
    
my_list = To_Do_List() #Creating a instance
while True: #Loop it  
    my_list.keybind()