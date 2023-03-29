import VoiceRecognition as VR
import VoiceOutput as V_OP
import VolumeControl as VC
import BrightnessControl as BC
import SpeechCommandDataset as DS
import UsabilityHelpers as UH

#driver program to run this project/application
FlagForServiceStart = False

UH.DesignPrinter()
V_OP.speech("Welcome to system volume and brightness controller using voice commands. You can say 'A voice assistant for controlling system volume and brightness'.")
V_OP.speech("Say 'start' to start services to listen to your voice commands, then start giving your voice commands to make adjustments with the system volume and brightness.")
V_OP.speech("You can ask 'current volume' or 'current brightness' to know the current volume or brightness level.")
V_OP.speech("You can say 'stop' to pause the services for a while, and you can say 'exit' to terminate this program.")
UH.DesignPrinter()
V_OP.speech("Now started listening for voice commands.")
while(True):
    text = VR.SpeechToText()
    if(text is None):
        print("Empty text....")
        continue
    text = text.lower()
    UH.PrintRightSide("User:"+text)
    if(text in DS.start):
        V_OP.speech("Service starting. Listening for voice commands")
        FlagForServiceStart = True
        continue
    if(text in DS.stopCode):
        confirmation = "Do you really want to stop this program?"
        V_OP.speech(confirmation)
        while(True):
            text = VR.SpeechToText()
            if(text is None):
                print("Empty text...")
                V_OP.speech("please confirm. "+ confirmation)
                continue
            UH.PrintRightSide("User:"+text)
            text = text.lower()
            if(text in DS.Yes):
                V_OP.speech("Thank you for using our service. use again!")
                UH.DesignPrinter()
                exit()
            elif(text in DS.No):
                V_OP.speech("Listening for voice commands")
                FlagForServiceStart = True
                break
            else:
                V_OP.speech("please confirm. "+ confirmation)
            
        continue
    if(not FlagForServiceStart):
        print("Listenening but not recognising until services start again...")
    if(FlagForServiceStart):
        #for volume control
        if(text in DS.IncreaseVolume ):
            VC.VolumeIncrease()
            # print("Increased the volume")
        elif(text in DS.DecreaseVolume):
            VC.VolumeDecrease()    
        elif(text in DS.VolumeMute):
            VC.VolumeMute()
        elif(text in DS.VolumeUnMute):
            VC.UnMute(text)
        elif(text in DS.FullVolume):
            VC.VolumeFull()
        elif(text in DS.HalfVolume):
            VC.VolumeHalf()
        
        #for brightness
        elif(text in DS.IncreaseBrightness):
            BC.BrightnessIncrease()
        elif(text in DS.DecreaseBrightness):
            BC.BrightnessDecrease()
        elif(text in DS.FullBrightness):
            BC.BrightnessFull()
        elif(text in DS.FullLowBrightness):
            BC.BrightnessFullLow()
        elif(text in DS.BrightnessHalf):
            BC.BrightnessHalf()

        #for stopping services and code
        elif(text in DS.Stop):
            FlagForServiceStart = False
            FlagForPrintServiceRunning = False
            V_OP.speech("Service stopping, until you start again")
        #for returning current voice and brightness level
        elif(text in DS.C_Bri_Level):
            BC.SayCurrentBrightnessLevel()
        elif(text in DS.C_Vol_Level):
            VC.SayCurrentVolume()
        #receiving confirmation and then terminating the program
        elif(text in DS.stopCode):
            confirmation = "Do you really want to stop this program?"
            V_OP.speech(confirmation)
            while(True):
                text = VR.SpeechToText()
                if(text is None):
                    print("Empty text...")
                    V_OP.speech("please confirm. "+ confirmation)
                    continue
                UH.PrintRightSide("User:"+text)
                text = text.lower()
                if(text in DS.Yes):
                    V_OP.speech("Thank you for using our service. use again!")
                    UH.DesignPrinter()
                    exit()
                elif(text in DS.No):
                    V_OP.speech("Listening for voice commands")
                    FlagForServiceStart = True
                    break
                else:
                    V_OP.speech("please confirm. "+ confirmation)
                
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
                