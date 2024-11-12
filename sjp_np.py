#n = int(input('Enter no of processes: '))
n=5
at = []
bt = []
pid = []

# Input arrival times and burst times
"""for i in range(n):
    at.append(int(input(f"Enter the arrival time of processor {i + 1}: ")))
    bt.append(int(input(f"Enter the burst time of processor {i + 1}: ")))
    pid.append(f"P{i + 1}")"""

at=[3,1,4,0,2]
bt=[1,4,2,6,3]
pid=["P1","P2","P3","P4","P5"]
d=[[1, 3, 0],[4, 1, 1], [2, 4, 2], [6, 0 ,3], [3, 2, 4]]

d.sort(key=lambda x: x[1])
s="|"+"_"*d[0][0]+"P"+str(d[0][2]+1)+"|"
d[0].append(d[0][0])
c=d[0][0]
d.sort(key=lambda x: x[0])
for i in d:
  if i[1]!=0:
    s+="_"*i[0]+"P"+str(i[2]+1)+"|"
    c+=i[0]
    i.append(c)

print(s)
# Initialize variables
tat = []
WT = []

d.sort(key=lambda x: x[2])
# Print process details
print('\nPID\tAT\tBT\tCT\tTAT\tWT')
for i in d:
    p="P"+str(i[2]+1)
    tt=i[3]-i[1]
    wt=tt-i[0]
    tat.append(tt)
    WT.append(wt)
    print(f"{p}\t{i[1]}\t{i[0]}\t{i[3]}\t{tt}\t{wt}")

# Print average metrics
print('Average Waiting Time = ', sum(WT)/n)
print('Average Turnaround Time = ', sum(tat)/n)
