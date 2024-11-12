class PrioritySchedulingProcess:
    def __init__(self, process_name, burst_time, waiting_time, turnaround_time, completion_time, priority):
        self.process_name = process_name
        self.burst_time = burst_time
        self.waiting_time = waiting_time
        self.turnaround_time = turnaround_time
        self.completion_time = completion_time
        self.priority = priority

def main():
    number_of_process = int(input("Enter the total number of Processes: "))

    processes = []
    ASCII_number = 65  # ASCII 'A'

    for i in range(number_of_process):
        process_name = chr(ASCII_number)
        print(f"\nEnter the details of process {process_name}:")
        burst_time = int(input("Enter the burst time: "))
        priority = int(input("Enter the priority: "))

        process = PrioritySchedulingProcess(process_name, burst_time, 0, 0, 0, priority)
        processes.append(process)

        ASCII_number += 1

    # Sort processes based on priority (higher priority first)
    processes.sort(key=lambda x: x.priority, reverse=True)

    total_waiting_time = 0
    total_turnaround_time = 0

    processes[0].waiting_time = 0
    processes[0].completion_time = processes[0].burst_time

    for i in range(1, number_of_process):
        processes[i].waiting_time = 0
        for j in range(i):
            processes[i].waiting_time += processes[j].burst_time

        processes[i].completion_time = processes[i - 1].completion_time + processes[i].waiting_time
        total_waiting_time += processes[i].waiting_time
        total_turnaround_time += processes[i].completion_time

    average_waiting_time = total_waiting_time / number_of_process
    average_turnaround_time = total_turnaround_time / number_of_process
    print("GANTT CHART\n")
    gc="|"
    for process in processes:
        gc+=(process.process_name+("_"*process.completion_time)+"|")
    print(gc)
    print()
    print("\n\nProcess Name\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    print("-------------------------------------------------------------------------")
    
        
    for process in processes:
        process.turnaround_time = process.completion_time
        print(f"{process.process_name}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
        print("-------------------------------------------------------------------------")

    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

if __name__ == "__main__":
    main()
