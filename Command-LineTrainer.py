# This Programms runs a Timer for a Pyramid-Intervall training
# where the pause is as long the exercise


#import time for the time.sleep(x) funktion what will pause the code for 1 second
import time

def Duration (a = 0):

    # The user can determine the length of the Rounds in minutes. If one does not enter the correct format one gets a second change
    Input = True
    global Min
    while Input == True:
        try:
            Min = float(input ("How long would you like to train (in minutes): "))
            Input = False
        except ValueError:
            print("No valid input! Try This Format: 1.5 (min)")
    txt = "\nYour trining time will be {} minutes or {} seconds.\nLets go:"
    print (txt.format(Min, Min * 60))
    
def StufenInt (Min):
  
    seconds = 0
    switch = 0
    Set = 0
    untill = Min * 60

    #start the timer.
    while Set < untill:
        while switch == 0:    # Timer runs forword
            try:
               
                print(str(seconds).zfill(3)) #.zfill() determants amount of digits shown

                seconds += 1
                Set += 1
                time.sleep(1)
                
                if Set == untill:
                    stop          # will give NameError since "stop" not defined
            
            except NameError:     # catches the name Error and deactivates timer
                switch = 3
            
    # Stop the timer with by Kernel interrupt (Cont + c) and sets the switch = 1 which lets the timer count backwords
            except KeyboardInterrupt:
                switch = 1
                seconds = seconds -1
                Set += 1
                print("\tTake a Breake! \tTime remain:",untill - Set,"sec")
                

    # Starts a loop which counts down and when the counter is at 0 sets a = 0 to start a new round
            try:
                while switch == 1:                # timer runs backwords
                    print (str(seconds).zfill(3))
                    seconds = seconds -1
                    Set +=  1

                    if Set == untill:
                        stop
            
                    time.sleep(1)
                    if seconds == 0:
                        print("\tLets go again!\tTime remain:{} sec".format(untill - Set))
                        switch = 0
            except NameError:
                switch = 3            
    print("The exercise is done. Good Job!")
    
def Again (again = True):
    try:
        while True:
            Again = input ("Would you like to go again? (j/n)")
         
            if Again == "j":
                Continue
            elif Again == "n":
                import notAModule
            else:
                print ("This is not a valid input. Try again!")
    
    except NameError:
        again = True
    except ModuleNotFoundError:
        again = False
     
    return again

print ("This is a timer for the Step-Intervall traing method.\nWhere your Rest Period is as long as your exercise periode.")
print ("Start your rest periode by interrupting the kernel (control + c)")
print ()
Round = True

s = KeyboardInterrupt

while Round == True:
    Duration()
    StufenInt(Min)
    Round = Again()

print("You have done well. Get a shower and some Rest!")   

