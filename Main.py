import VoiceRecognition as VR
import VoiceOutput as V_OP
import VolumeControl as VC
import BrightnessControl as BC
import SpeechCommandDataset as DS

#driver program to run this project/application
FlagForServiceStart = False
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=")
V_OP.speech("Welcome to system volume and brightness controller using voice commands. simply VoiceBot. Say 'start' to start services to listen to your voice commands, then start giving your voice commands..")
V_OP.speech("You can say 'stop' to pause the services for a while, and you can say 'exit' to terminate this program.\n")
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=")
while(True):
    text = VR.SpeechToText()
    if(text is None):
        print("Empty text....")
        continue
    text = text.lower()
    print("Command Received in main:"+text)
    if(text in DS.start):
        V_OP.speech("Service starting. Listening for voice command")
        FlagForServiceStart = True
        continue
    if(text in DS.stopCode):
        # V_OP.speech("Thank you for using our service. use again!")
        # exit()
        confirmation = "Do you really want to stop this program?"
        V_OP.speech(confirmation)
        text = VR.SpeechToText()
        while(True):
            if(text in DS.Yes):
                V_OP.speech("Thank you for using our service. use again!")
                print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=")
                exit()
            elif(text in DS.No):
                V_OP.speech("Listening for voice command")
                FlagForServiceStart = True
                break
            else:
                print("Empty text....")
                V_OP.speech("please confirm. "+ confirmation)
            text = VR.SpeechToText()
        continue
    if(not FlagForServiceStart):
        print("Listenening but not recognising until services start again...")
    if(FlagForServiceStart):
        print("Service running...")
        if(text in DS.IncreaseVolume ):#(text == "increase"):
            VC.VolumeIncrease()
            V_OP.speech("volume Increased")
            # print("Increased the volume")
        elif(text in DS.DecreaseVolume):
            VC.VolumeDecrease()
            V_OP.speech("volume Decreased")     
        elif(text in DS.VolumeMute):
            V_OP.speech("System Volume is going to get muted!")
            VC.VolumeMute()
        elif(text in DS.VolumeUnMute):
            VC.UnMute()
            V_OP.speech(text+" Done successfully!")
        elif(text in DS.FullVolume):
            VC.VolumeFull()
            V_OP.speech("volume set to maximum level")
        elif(text in DS.HalfVolume):
            VC.VolumeHalf()
            V_OP.speech("volume set to half level!")
        
        #for brightness
        elif(text in DS.IncreaseBrightness):
            BC.BrightnessIncrease()
            V_OP.speech("Brightness Increased")
        elif(text in DS.DecreaseBrightness):
            BC.BrightnessDecrease()
            V_OP.speech("Brightness decreased") 
        elif(text in DS.FullBrightness):
            BC.BrightnessFull()
            V_OP.speech("Brightness set to maximum")
        elif(text in DS.FullLowBrightness):
            BC.BrightnessFullLow()
            V_OP.speech("Brightness set to minimum")
        elif(text in DS.BrightnessHalf):
            BC.BrightnessHalf()
            V_OP.speech("Brightness set to half level!")

        #for stopping services and code
        elif(text in DS.Stop):
            FlagForServiceStart = False
            V_OP.speech("Service stopping, until you start again")

        #receiving confirmation and then terminating the program
        elif(text in DS.stopCode):
            confirmation = "Do you really want to stop this program?"
            V_OP.speech(confirmation)
            text = VR.SpeechToText()
            while(True):
                if(text in DS.Yes):
                    V_OP.speech("Thank you for using our service. use again!")
                    print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=")
                    exit()
                elif(text in DS.No):
                    # print("Listening for voice command")
                    V_OP.speech("Listening for voice command")
                    FlagForServiceStart = True
                    break
                else:
                    # print("Please confirm. "+confirmation)
                    V_OP.speech("Please confirm. "+confirmation)
                text = VR.SpeechToText()
            continue
        else:
            # print("Check your voice command. Did you just said "+text+"?") 
            V_OP.speech("Check your voice command. Did you just said "+text+"?")
            matches = DS.MatchCommand(text)
            # print("Do you mean ")
            if(len(matches) != 0):
                V_OP.speech("Do you mean ")
            for i in range(0,len(matches)):
                MediateText = (i == len(matches) - 1) and "." or ", or"
                V_OP.speech(matches[i] + MediateText)
                # print(matches[i] + MediateText)
            # print("If you said anything by mistake or you are talking to someone else, you can simply pause this program by saying 'pause' or 'stop'")
            V_OP.speech("If you said anything by mistake or you are talking to someone else, you can simply pause this program by saying 'pause' or 'stop'")
                