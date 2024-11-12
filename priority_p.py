# class Process:
#     def __init__(self, no, at, bt, rt, ct, wt, tat, pri, temp):
#         self.no = no
#         self.at = at
#         self.bt = bt
#         self.rt = rt
#         self.ct = ct
#         self.wt = wt
#         self.tat = tat
#         self.pri = pri
#         self.temp = temp


# def read(i):
#     print("\nProcess No:", i)
#     no = i
#     at = int(input("Enter Arrival Time: "))
#     bt = int(input("Enter Burst Time: "))
#     rt = bt
#     pri = int(input("Enter Priority: "))
#     temp = pri
#     return Process(no, at, bt, rt, 0, 0, 0, pri, temp)


# def main():
#     print("<--Highest Priority First Scheduling Algorithm (Preemptive)-->\n")
#     n = int(input("Enter Number of Processes: "))
#     processes = [read(i + 1) for i in range(n)]
#     remaining = n
#     execution_order = []  # Track the order of execution
#     gantt_chart = "|"  # Initialize the Gantt chart

#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if processes[j].at > processes[j + 1].at:
#                 processes[j], processes[j + 1] = processes[j + 1], processes[j]

#     max_val = processes[0].temp
#     max_index = 0
#     for j in range(n):
#         if processes[j].at <= processes[0].at:
#             if processes[j].temp > max_val:
#                 max_val = processes[j].temp
#                 max_index = j
#     i = max_index
#     c = processes[i].ct = processes[i].at + 1
#     processes[i].rt -= 1
#     execution_order.append(processes[i].no)
#     gantt_chart += str(processes[i].no) + "_" * (processes[i].ct - 1) + "|"

#     if processes[i].rt == 0:
#         processes[i].temp = float("-inf")
#         remaining -= 1

#     while remaining > 0:
#         max_val = processes[0].temp
#         max_index = 0
#         for j in range(n):
#             if processes[j].at <= c:
#                 if processes[j].temp > max_val:
#                     max_val = processes[j].temp
#                     max_index = j
#         i = max_index
#         processes[i].ct = c = c + 1
#         processes[i].rt -= 1
#         execution_order.append(processes[i].no)
#         gantt_chart += str(processes[i].no) + "_"  + "|"

#         if processes[i].rt == 0:
#             processes[i].temp = float("-inf")
#             remaining -= 1

#     print("\nProcessNo\tAT\tBT\tPri\tCT\tTAT\tWT")
#     avgtat = 0
#     avgwt = 0
#     for i in range(n):
#         processes[i].tat = processes[i].ct - processes[i].at
#         avgtat += processes[i].tat
#         processes[i].wt = processes[i].tat - processes[i].bt
#         avgwt += processes[i].wt
#         print(f"P{processes[i].no}\t\t{processes[i].at}\t{processes[i].bt}\t{processes[i].pri}\t"
#               f"{processes[i].ct}\t{processes[i].tat}\t{processes[i].wt}")

#     avgtat /= n
#     avgwt /= n
#     print(f"\nAverage TurnAroundTime={avgtat}\nAverage WaitingTime={avgwt}")

#     # Print the order of execution in the Gantt chart format
#     print("\nGANTT CHART\n")
#     print(gantt_chart)


# if __name__ == "__main__":
#     main()



class Process:
    def __init__(self,pid,at,bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        
        self.remaining_time = bt
        
        self.start = None
        self.exit = None
        
        self.tat = None
        self.wt = None
        
    def turnaround(self,exit):
        self.exit = exit
        self.tat = self.exit - self.at
        return self.tat
        
    def wait(self):
        self.wt = self.tat - self.bt
        return self.wt
        
def srtf(processes):
    processes = sorted(processes, key=lambda p:p.at)
    queue = []
    completed = []
    current = 0
    table = []
    
    while processes or queue:
        if processes != [] and processes[0].at <= current:
            queue.append(processes.pop(0))
        if queue != []:
            queue = sorted(queue, key=lambda p: p.remaining_time)
            process = queue.pop(0)
            
            process.start = current
            process.remaining_time -= 1
            
            if process.remaining_time == 0:
                process.exit = current + 1
                process.tat = process.turnaround(process.exit)
                process.wt = process.wait()
                
                completed.append((process.pid, process.start, process.exit, process.tat, process.wt))
                table.append((process.pid,process.at,process.bt,process.tat,process.wt))
                
            else:
                if completed == []:
                    completed.append((process.pid, process.start,current + 1, None, None))
                
                elif completed[-1][0] != process.pid:
                    completed.append((process.pid, process.start,current + 1, None, None))
                    
                queue.append(process)
        current += 1
    return (completed, table)
    
if __name__ == "__main__":
    process_list = [
            Process(1,0,2),
            Process(2,3,5),
            Process(3,4,7),
            Process(4,4,6)]
    
    completed_seq, table_seq = srtf(process_list)
    
    wt = 0
    print("PID  AT  BT  TAT WT")
    
    for p in table_seq:
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}")
        wt += p[4]
    awt = wt/4
    print("Average: ", awt)
    
    for p in range(len(completed_seq)):
        if p != 0:
            if completed_seq[p][0] == completed_seq[p-1][0]:
                print(f" {completed_seq[p][1]} {completed_seq[p][0]} {completed_seq[p][2]} ",end=" ")
            else:
                print(f"| {completed_seq[p][1]} {completed_seq[p][0]} {completed_seq[p][2]} |",end=" ")
        
        else:
            print(f" | {completed_seq[p][1]} {completed_seq[p][0]} {completed_seq[p][2]} | ",end=" ")
