import random

def generate_workload(number_of_processes, max_arrival_time, max_cpu_burst, min_io, max_io, min_cpu, max_cpu):
    processes = []
    for i in range(number_of_processes):
        process = {
            "PID": i,
            "arrival_time": random.randint(0, max_arrival_time),
            "bursts": []
        }
        '''process that contain PID and arrival time and burst , the arrival time generated randomly to range 0 to max_arrival_time from user'''
        number_of_bursts = random.randint(1, max_cpu_burst)#number of burst generate randomly from range 1 to max cpu bursts.
        for j in range(number_of_bursts):
            if j == 0 or j == number_of_bursts - 1: #for first and last burst let it be cpu burst
                if( j != 1  and j != number_of_bursts):
                    process["bursts"].append((random.randint(min_cpu, max_cpu), "CPU"))
            else:
                if ((j % 2) > 0): # let it be IO  if odd  number
                    process["bursts"].append((random.randint(min_io, max_io), "IO"))
                else:
                    if(j != number_of_bursts - 2): #as soon the cpu isn't the last burst before the last cpu 
                        process["bursts"].append((random.randint(min_cpu, max_cpu), "CPU"))
        processes.append(process) #append this process to the list of processes
    return processes #return the list of processes

def save_to_file(processes, filename): #get processes and file name which will be workloaded
    try: #try and finally to handle the error that occurs when opening and closing a file 
        f = open(filename, "w")
        for process in processes: #get each process from the list of processes
            f.write(f"{process['PID']} {process['arrival_time']}")  #first print the pid and the arrival time
            for burst in process["bursts"]: #then the bursts 
                f.write(f" {burst[0]}")
            f.write(f"\n")
    finally:
        f.close() # finally close the file            
number_of_processes=input("Number of processes\n")
max_arrival_time=input("Max arrival time\n")
max_cpu_burst= input("Max CPU burst\n")
min_io=input("minimum io bursts\n")
max_io=input("max io bursts\n")
min_cpu=input("min cpu bursts\n")
max_cpu=input("max cpuburst\n")
#print("The file is generated \n")
processes = generate_workload(int(number_of_processes),int(max_arrival_time), int(max_cpu_burst), int(min_io), int(max_io), int(min_cpu), int(max_cpu))
save_to_file(processes, "workload.txt")
print("The file is generated \n")