import VoiceRecognition as VR
import VoiceOutput as V_OP
import VolumeControl as VC
import BrightnessControl as BC
import SpeechCommandDataset as DS

#driver program to run this project/application
FlagForServiceStart = False
FlagForConfirmation = False

while(True):
    text = VR.SpeechToText()
    if(text is None):
        continue
    text = text.lower()
    print("Command Received in main:"+text)
    if(text in DS.start):
        V_OP.speech("Service starting. Listening for voice commmand")
        FlagForServiceStart = True
        continue
    if(text in DS.stopCode):
        # V_OP.speech("Thank you for using our service. use again!")
        # exit()
        confirmation = "Do you really want to stop this program?"
        text = VR.SpeechToText()
        V_OP.speech(confirmation)
        while(True):
            if(text in DS.Yes):
                V_OP.speech("Thank you for using our service. use again!")
                exit()
            elif(text in DS.No):
                V_OP.speech("Listening for voice commmand")
                break
            else:
                V_OP.speech(confirmation)
            text = VR.SpeechToText()
    if(not FlagForServiceStart):
        print("Listenening but not recognising")
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
        elif(text in DS.stopCode):
            confirmation = "Do you really want to stop this program?"
            V_OP.speech(confirmation)
            text = VR.SpeechToText()
            while(True):
                if(text in DS.Yes):
                    V_OP.speech("Thank you for using our service. use again!")
                    exit()
                elif(text in DS.No):
                    V_OP.speech("Listening for voice commmand")
                    break
                else:
                    V_OP.speech(confirmation)
                text = VR.SpeechToText()
        else:
            V_OP.speech("Check your voice command. Did you just said "+text+"?")
            print("Check your voice command. Did you just said "+text+"?") 