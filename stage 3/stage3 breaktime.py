import time
import webbrowser
total_breaks=3
break_count=0
print("this program started on:" +time.ctime())
while break_count<total_breaks :
    time.sleep(7)
    webbrowser.open("https://www.youtube.com/watch?v=8367ETnagHo")
    break_count=break_count+1 

    
