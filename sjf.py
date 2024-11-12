"""
bt=[1,4,2,6,3]
at=[3,1,4,0,2]	
d=[[1, 3, 0],[4, 1, 1], [2, 4, 2], [6, 0 ,3], [3, 2, 4]]"""
def preemptive(n,d,at,bt): 
    i = 0
    ll = []
    for i in range(0, sum(bt)):
        l = [j for j in d  if j[1] <= i]
        l.sort(key=lambda x: x[0])
        d[d.index(l[0])][0] -= 1
        for k in d:
            if k[0] == 0:
                t = d.pop(d.index(k))
                ll.append([k, i + 1])
    ct = [0] * (n)
    tat = [0] * (n)
    wt = [0] * (n )
    for i in ll:
        ct[i[0][2]] = i[1] 
    for i in range(len(ct)):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
    print('PID\tBT\tAT\tCT\tTAT\tWT')
    for i in range(len(ct)):
        print("{}\t{}\t{}\t{}\t{}\t{}".format("P"+str(i+1),bt[i], at[i], ct[i], tat[i], wt[i]))
    print('Average Waiting Time = ', sum(wt)/len(wt))
    print('Average Turnaround Time = ', sum(tat)/len(tat))

def non_preemptive(d): 
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
            
    print("GANTT CHART \n")
    print(s)
    tat = []
    WT = []
    d.sort(key=lambda x: x[2])
    print('\nPID\tAT\tBT\tCT\tTAT\tWT')
    for i in d:
        p="P"+str(i[2]+1)
        tt=i[3]-i[1]
        wt=tt-i[0]
        tat.append(tt)
        WT.append(wt)
        print(f"{p}\t{i[1]}\t{i[0]}\t{i[3]}\t{tt}\t{wt}")
    print('Average Waiting Time = ', sum(WT)/n)
    print('Average Turnaround Time = ', sum(tat)/n)
       
if __name__=="__main__":
    n = int(input('Enter no of processes: '))
    d = [0] * (n )
    at = [0] * (n )
    bt = [0] * (n )
    for i in range(n):
        at[i] = int(input('Enter the arrival time for process {} : '.format(i + 1)))
        bt[i] = int(input('Enter the burst time for process {} : '.format(i + 1))) 
        d[i] = [bt[i], at[i], i]
    ch=int(input("Enter 1 for preemptive and 2 for non-preemptive:"))
    print()
    if ch==1:
        preemptive(n,d,at,bt)
    else:
        non_preemptive(d)