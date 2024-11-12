n=int(input("Enter the no.of proceses:"))
at=[]
bt=[]
pid=[]
for i in range(n):
  at.append(int(input(f"Enter the arrival time of processor {i+1}: ")))
  bt.append(int(input(f"Enter the burst time of processor {i+1}: ")))
  pid.append(f"P{i+1}")
print()
print("PID  AT  BT")
for i in range(n):
   print(f"P{i+1}   ", at[i], " ",bt[i]) 

d={}
for j in range(n):
  d[f"P{j+1}"]=[at[j],bt[j]]

print()
overhead=int(input("Enter the no.of overhead unit: "))
print()
d = sorted(d.items(), key=lambda item: item[1][0])

CT=[]
idle=0
st=""
for i in range(len(d)):
    
    if(i==0):
       v=d[i][1][1]
       CT.append(v)
       st+=("|"+"_"*v+str(d[i][0])+"|")
        
    elif CT[i-1]<d[i][1][0]:
       v1=CT[i-1] + d[i][1][1]
       idle+=((d[i][1][0]-CT[i-1])+overhead)
       CT.append(idle+ v1)
       st+=("*"*idle+"|")
       st+=("_"*(d[i][1][1])+str(d[i][0])+"|")
       
    else:
       v2=(CT[i-1] + d[i][1][1])
       CT.append(v2)
       st+=("*"*overhead+"|")
       st+=("_"*(d[i][1][1])+str(d[i][0])+"|")

TT = []
for i in range(len(d)):
    TT.append(CT[i] - d[i][1][0])
 
WT = []
for i in range(len(d)):
    WT.append(TT[i] - d[i][1][1])
 
AWT = 0
for i in WT:
    AWT +=i
AWT = (AWT/n)

ATT = 0
for i in TT:
    ATT +=i
ATT = (ATT/n)

print("GANTT CHART"+"\n")
print(st+"\n")

print("PID    AT        BT      CT       TT          WT   ")
print("---------------------------------------------------")
for p in pid:
 for i in range(len(d)):
   if p==d[i][0]:
      print(d[i][0],"      ",d[i][1][0],"     ",d[i][1][1],"     ",CT[i],"      ",TT[i],"        ",WT[i],"     ")
print("Average Waiting Time: ",AWT)
print("Average Turnaround Time: ",ATT)
