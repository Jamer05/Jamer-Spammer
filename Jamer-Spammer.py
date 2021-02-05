import pyautogui
from time import sleep

a= '''
    8                               8""""8                        ""8"" 8"""88             
    8  eeeee eeeeeee eeee eeeee     8      eeeee eeeee eeeeeee      8   8    8 eeeee e     
    8e 8   8 8  8  8 8    8   8     8eeeee 8   8 8   8 8  8  8      8e  8    8 8  88 8     
    88 8eee8 8e 8  8 8eee 8eee8e        88 8eee8 8eee8 8e 8  8      88  8    8 8   8 8e    
e   88 88  8 88 8  8 88   88   8    e   88 88    88  8 88 8  8      88  8    8 8   8 88    
8eee88 88  8 88 8  8 88ee 88   8    8eee88 88    88  8 88 8  8      88  8eeee8 8eee8 88eee 
'''
print(a)
x = int(input('Enter how many messages do you want to send:' ))  #input how many messages or comments you want to send

msgString = input("Message: ")

def name():

    nameList = msgString   
    return nameList    #return the random name it just generated

while True:      #forever loop
    pyautogui.typewrite(f" {name()}")  #type message
    sleep(.001)                        #A bit delay of 100 ms
    pyautogui.typewrite("\n")          #New line, here 'Enter' to send text
    sleep(.0001)                           #delay

    x = x - 1         #decrement x value by 1

    if x == 0:       
        break         #get out of the loop and finish
#EOL


