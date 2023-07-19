# power_consumption_py
```python 
   

```
**Modules used** : psutil, datetime, and tabulate
Modules used : psutil, datetime, and tabulate 
**psutil** is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. Supported platforms 
**installation : pip install psutil** 
**datetime** works with dates and times. It provides a variety of classes for representing and manipulating dates and times, as well as for formatting and parsing dates and times in a variety of formats. 
**installation : pip install datetime** 
**Tabulate** is an open-source python package/module which is used to print tabular data in nicely formatted tables. 
**installation : pip install tabulate**

**Explanation of the programme :**
A normal function called **Power_Consumption_By_Software()** without any parameters or arguments delcearing inside it. The programm is userfriendly in which users have to select any one of the choices and relative answers will give by the programm/function. The whole code was develooped in three phases inside the function they are :
**Phase 1 ->** phase 1 code wiil the answer for the following question **See all the applications/softwares currently running behind your device ?** phase 1 code has written from line(13 to 23) :

```python 
   #**Phase 1**
   # when the user presses 1 the code proceeds inside the if statement
   if choice == 1:  
    # An iterator with name proc is created to access the objects
    for proc in psutil.process_iter(['pid', 'name']): 
        # The value of the key called 'pid' is assigned to the variable pid
         pid = proc.info['pid'] 
         #psutil.Process(pid) creates the tuple with details such as name pid(process id) etc.
         p = psutil.Process(pid) 
         #p.create_time() -> get number which is expressed as seconds sice the epoch time and with datetime module it will be converted into proper date along with time
         created_time = datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
        #All the varibles are stored inside the 2d array
         arr += [[p.pid,p.name(),created_time,p.status()]]
         head = ["Process ID","Name of the Application","Process creation time \n since the epoch","Status"]
         #printing the solution the phase 1 inside the table with an grid format 
         print(tabulate(arr,headers=head,tablefmt="grid")) 
         #printing the below line to know phase 1 is successfully executed
          print("Option {} successfully executed\n".format(choice))



    #Phase 2 
    # when the user presses 2 the code proceeds inside the if statement
    elif choice==2: 
        #create the input
         application_name = input("Enter the application name in .exe (Example -> python.exe) : ")  
         print("\n")#\n is the format specifier which means the new line
         # An iterator with name proc is created to access the objects
          for proc in psutil.process_iter(['pid', 'name']):
             # checking with entered user input with object key(name) : value pair if it matches the proceed inside to if 
            if proc.info['name'] == application_name: pid = proc.info['pid']
            #Getting the pid(process ID) of the specified application
             p = psutil.Process(pid) created_time = datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
             #% of CPU utilisation over one second
              percenage_of_cpu = p.cpu_percent(interval=1) 
              #Return a named tuple with variable fields depending on the platform representing memory information 
               # about the process p.memory_info() 
               information_of_memory = p.memory_info() usage_of_memory = information_of_memory.rss / (1024 ** 2)
               #Tells memory usage in Megabytes #based on CPU and memory utilisation, calculating the amount of energy used. 
               measure_power_consumed_by_software = percenage_of_cpu * 0.1 + usage_of_memory * 0.01 
               #Line (41 to 44) same as in phase 1
            if pid is None:
                 # in case the user entered the application which is not installed or not running in the background 
                 print("--------------------------------------------------------------------------") 
                 print("| Application either not found nor not running currently. |") 
                 print("--------------------------------------------------------------------------")
    #Phase 3 -> phase 3 code wiil the answer for the following question Exit from the programme ? phase 3 code has written from line(52 to 58) :

    #Phase 3 code : 
    # when the user presses 3 the code proceeds inside the if statement
    elif choice==3:
         print("\n exiting form the programme...") 
         print("Option {} successfully executed\n".format(choice)) 
         exit()
         #Totally exits form the programme 
         else : 
         #incase if its not option 1 or 2 or 3 you have entered then code goes to else block then prints the below line 
         print("Access denied due to -> Invalid Choice / Run the script with administrative privileges.\n")

#The whole phase 1, Phase 2 , and Phase 3 codes are placed inside the while loop which is set to True so that the programm wil be continuously executed until the user presses option 3/phase 3

while True : 
    print("\n") 
    #initiall pid variable is set to none
    pid = None 
    #initially arr(list) is set to empty
     arr = []  
     #The next line will display the questions and make it clear to the user which options the programme offers. 
     print("Choose any one options from below \n press 1 to -> See all the applications/softwares currently running behind your device \n press 2 to -> Check the estimated power consumption of the currently running application/softwares\n press 3 to -> Exit from the programme") 
     #choice will stores that value what ever the user enters if the values entered by the user are (1 or 2 or 3) then accordingly Phases 1, 2, and will be executed if not else block will be executed. 
     choice = int(input('Enter your choice : ')) print("\n") 
     #Phase 1 code 
     #Phase 2 code 
     #Phase 3 code

     #function call
     Power_Consumption_By_Software()

```

**OUTPUT :**
![Option1](https://github.com/gopichandu-tech/power_consumption_py/assets/70055677/489bd496-68e2-4aa5-8904-0be1f10c5a39)

![Option1_continue_Option3](https://github.com/gopichandu-tech/power_consumption_py/assets/70055677/b46f57fd-0eef-450a-957f-3fa4e9e77af0)

![Option2_application_not_running](https://github.com/gopichandu-tech/power_consumption_py/assets/70055677/6183d4d8-cd78-4a29-a332-2a2c707224a2)

![Option2_application_running](https://github.com/gopichandu-tech/power_consumption_py/assets/70055677/130c578c-0c01-4f27-bafb-78b263ea9e75)

![Option2_application_running_continue](https://github.com/gopichandu-tech/power_consumption_py/assets/70055677/56b545c9-76df-4a3c-a6e5-165ea1e0b1b4)
