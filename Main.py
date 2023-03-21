import VoiceRecognition as VR
import VoiceOutput as V_OP
import os
import VolumeControl as VC
import BrightnessControl as BC
import SpeechCommandDataset as DS
#forincrease = ["increase the volume","up the volume"]
# volumeIncreaseCommands = ["Increase volume","volume Increase"]

flag = False
while(True):
    text = VR.SpeechToText()
    if(text is None):
        continue
    text = text.lower()
    print("Command Received in main:"+text)
    if(text in DS.start):
        V_OP.speech("Service starting")
        flag = True
        continue
    if(text in DS.stopCode):
        V_OP.speech("Thank you for using our service. use again!")
        exit()
    if(not flag):
        print("Listenening but not recognising")
    if(flag):
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
        elif(text in DS.HalfVolume):
            VC.VolumeHalf()
            V_OP.speech("volume set to half level!")
        
        #for brightness
        elif(text in DS.IncreaseBrightness):
            # VC.VolumeIncrease()
            # print("here")
            # V_OP.speech("Increased")
            # print("Brightness increased")
            # print("Increased the volume")
            BC.BrightnessIncrease()
            V_OP.speech("Brightness Increased")
        elif(text in DS.DecreaseBrightness):
            # VC.VolumeDecrease()
            BC.BrightnessDecrease()
            V_OP.speech("Brightness decreased")
            # V_OP.speech("Decreased") 
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
            flag = False
            V_OP.speech("Service stopping, until you start again")
            # exit()
        elif(text in DS.stopCode):
            V_OP.speech("Thank you for using our service. use again!")
            exit()
        else:
            V_OP.speech("Check your voice command. Did you just said "+text+"?")
    
        
    

