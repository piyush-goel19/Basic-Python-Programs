import webbrowser
import time
num_of_breaks = 3
break_count = 0
print("Your Schedule begins from ",time.ctime())
while (break_count < num_of_breaks):
        time.sleep(5)
        if (break_count == 1):
            webbrowser.open("https://www.youtube.com/watch?v=Um7pMggPnug")
        elif (break_count == 0):
            webbrowser.open("https://www.youtube.com")
        else :
            webbrowser.open("https://www.edx.org")
        break_count = break_count + 1
