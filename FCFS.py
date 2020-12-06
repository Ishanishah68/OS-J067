#function for finding all waiting time for all processes
def findWaitingTime(processes, n,bt, wt):
     wt[0] = 0 #waiting time for first process
     for i in range(1, n ): #calculating waiting time
        wt[i] = bt[i - 1] + wt[i - 1]  
        
def findTurnAroundTime(processes, n,bt, wt, tat): #function to calculate turn around time  
     for i in range(n): #calculating turn around time
        tat[i] = bt[i] + wt[i]   
        
def findavgTime( processes, n, bt): #function to calculate average time
    wt = [0] * n 
    tat = [0] * n  
    total_wt = 0
    total_tat = 0       
    findWaitingTime(processes, n, bt, wt) #function to calculate waiting time
    findTurnAroundTime(processes, n,bt, wt, tat)
    print( "Processes Burst time " + " Waiting time " +" Turn around time")
    
    for i in range(n): #calculating turn around and waiting time 
         total_wt = total_wt + wt[i] 
         total_tat = total_tat + tat[i] 
         print(" " + str(i + 1) + "\t\t" +  str(bt[i]) + "\t\t " + str(wt[i]) + "\t\t " +  str(tat[i]))
    print( "Average waiting time = "+str(total_wt / n))   
    print("Average turn around time = "+ str(total_tat / n)) 
processes = [ 1, 2, 3] 
n = len(processes) 
burst_time = [10, 5, 8] 
findavgTime(processes, n, burst_time) 
