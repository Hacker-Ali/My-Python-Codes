def current_datetime():
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return (f"[{dt_string}]\n") 

def play(song):

    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from pygame import mixer 

    mixer.init() 
    mixer.music.load(f"{song}.mp3") 
    mixer.music.set_volume(1) 
    mixer.music.play() 
    
    while True: 
        query=input("Type Done to exit.\n")
        query=query.lower()
        if query == "done":
            mixer.music.stop()
            with open(f"{song}.txt" , "a") as file:
                file.write(current_datetime())
                print("Record updated successfully!")
            break
        else :
            pass
            
def reminder():
    while True:
        try:
            eye_repeat=int(input("After how many minutes you want to get notified for relaxing your eyes:\t"))*60
            physical_repeat=int(input("After how many minutes you want to get notified for relaxing your body:\t"))*60
            water_repeat=int(input("After how many minutes you want to get notified to drink water:\t"))*60
            break
        except Exception as error :
            print (" TIME SHOULD BE IN MINUTES AND SHOULD BE NATURAL NUMBER", 
                " \n THAT'S WHY GIVE THE VLUES AGAIN")


    import time
    timei = time.time()
    while True:
        timef = time.time()
        delta_time = timef-timei
        if delta_time//1 == 0:
            continue 
        else:
            if (delta_time//1)%eye_repeat == 0 :
                play("eyes")
            elif (delta_time//1)%physical_repeat == 0 :
                play("physical")
            elif (delta_time//1)%water_repeat == 0 :
                play("water")
            else:
                pass
            
def main():

    task = int(input("Choose correct option:\n[1]Run Reminder\n[2]Fecth Previous Record\n"))
    if task == 1 :
        reminder()
    elif task == 2:
        def submain():
            rtf = int(input("Choose correct option:\n[1]Fetch eyes activity record\n[2]Fetch physical activity record\n[3]Fetch water drinking record\n "))
            try:
                if rtf == 1 :
                    with open("eyes.txt") as file:
                        print("You did eyes activity at these times")
                        for lines in file:
                            print(lines , end="")
                    main()
                elif rtf == 2 :
                    with open("physical.txt") as file:
                        print("You did physical activity at these times")
                        for lines in file:
                            print(lines, end="")
                    main()
                elif rtf == 3 :
                    with open("water.txt") as file:
                        print("You drank water at these times")
                        for lines in file:
                            print(lines, end="")
                    main()
                else:
                    submain()
            except Exception as error1:
                print("Please add something to your record first!")
                main()
        submain()
    else :
        main()

main()
