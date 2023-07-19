import psutil,datetime
from tabulate import tabulate

def Power_Consumption_By_Software():
    while True :
        print("\n")
        pid = None
        arr = [] 
        print("Choose any one options from below  \n press 1 to -> See all the applications/softwares currently running behind your device \n press 2 to -> Check the estimated power consumption of the currently running application/softwares\n press 3 to -> Exit from the programme")
        choice = int(input('Enter your choice : '))
        print("\n")
        
        #Phase 1 
        if choice == 1:
            for proc in psutil.process_iter(['pid', 'name']):
                pid = proc.info['pid']
                p = psutil.Process(pid) 
                created_time = datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
                arr += [[p.pid,p.name(),created_time,p.status()]]
    
            head = ["Process ID","Name of the Application","Process creation time \n  since the epoch","Status"]
            print(tabulate(arr,headers=head,tablefmt="grid"))
            print("Option {} successfully executed\n".format(choice))
            
        #Phase 2   
        elif choice==2:
            application_name = input("Enter the application name in .exe (Example -> python.exe) : ")
            print("\n")
            for proc in psutil.process_iter(['pid', 'name']):
                
                if proc.info['name'] == application_name:
                    pid = proc.info['pid']
                    p = psutil.Process(pid)
                    created_time = datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
                    percenage_of_cpu = p.cpu_percent(interval=1)
                    information_of_memory = p.memory_info()
                    usage_of_memory = information_of_memory.rss / (1024 ** 2)
                    measure_power_consumed_by_software = percenage_of_cpu * 0.1 + usage_of_memory * 0.01
                    
                    
                    arr += [[p.pid,p.name(),created_time,p.status(),measure_power_consumed_by_software]]
                    head = ["Process ID","Name of the Application","Process creation time \n   since the epoch ","Status","Predicted Power consumption \n(in watts)"]
                    print(tabulate(arr,headers=head,tablefmt="grid"))
                    print("Option {} successfully executed\n".format(choice))
                    
                      
            if pid is None:
                print("-------------------------------------------------------------")
                print("| Application either not found nor not running currently.   |")
                print("-------------------------------------------------------------")
         
        #choice 3       
        elif choice==3:
            print("\nexiting form the programme...")
            print("Option {} successfully executed\n".format(choice))
            exit()
        else :
            print("Access denied due to -> Invalid Choice / Run the script with administrative privileges.\n")

Power_Consumption_By_Software()
