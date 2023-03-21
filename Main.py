import VoiceRecognition as VR
import VoiceOutput as V_OP
import os
import VolumeControl as VC
import BrightnessControl as BC
#forincrease = ["increase the volume","up the volume"]
# volumeIncreaseCommands = ["Increase volume","volume Increase"]
IncreaseVolume = ["increase the volume","turn up the volume","increase volume","increase sound","i need more sound"]
VolumeMute = ["mute the volume","mute","mute volume","mute sound","no sound"]
VolumeUnMute = ["unmute the volume","unmute","unmute volume","full volume","set volume to full","set volume to maximum"]
DecreaseVolume = ["decrease the volume","turn down the volume","decrease volume","decrease sound"]
IncreaseBrightness = ["increase the brightness","turn up the brightness","increase brightness"]
DecreaseBrightness = ["decrease the brightness","turn down the brightness","decrease brightness"]
FullBrightness = ["set the maximum brightness","turn up the brightness to maximum","maximum brightness","full brightness"]
FullLowBrightness = ["set the minimum brightness","turn down the brightness to minimum","minimum brightness","full low brightness"]
HalfVolume = ["half the volume","set volume to half","half volume"]
BrightnessHalf = ["half the brightness","set brightness to half"]
Stop = ["stop","top","close the service","end the service"]
start = ["start","start services"]
stopCode = ["exit code","stop the program","exit","exit program"]
flag = False
while(True):
    text = VR.SpeechToText()
    if(text is None):
        continue
    text = text.lower()
    print("Received in main:"+text)
    if(text in start):
        V_OP.speech("Service starting")
        flag = True
    if(text in stopCode):
        V_OP.speech("Thank you for using our service. use again!")
        exit()
    else:
        print("Listenening but not recognition")
    if(flag):
        print("Service running")
        if(text in IncreaseVolume ):#(text == "increase"):
            VC.VolumeIncrease()
            V_OP.speech("volume Increased")
            print("Increased the volume")
        if(text in DecreaseVolume):
            VC.VolumeDecrease()
            V_OP.speech("volume Decreased")     
        if(text in VolumeMute):
            V_OP.speech("System Volume is going to get muted!")
            VC.VolumeMute()
        if(text in VolumeUnMute):
            VC.UnMute()
            V_OP.speech("volume Unmuted!")
        if(text in Stop):
            flag = False
            V_OP.speech("Service stopping, until you start again")
            # exit()
        if(text in stopCode):
            V_OP.speech("Thank you for using our service. use again!")
            exit()
        
        #for brightness
        if(text in IncreaseBrightness):
            # VC.VolumeIncrease()
            # print("here")
            # V_OP.speech("Increased")
            print("Brightness increased")
            # print("Increased the volume")
            BC.BrightnessIncrease()
            V_OP.speech("Brightness Increased")
        if(text in DecreaseBrightness):
            # VC.VolumeDecrease()
            BC.BrightnessDecrease()
            V_OP.speech("Brightness decreased")
            # V_OP.speech("Decreased") 
        if(text in FullBrightness):
            BC.BrightnessFull()
            V_OP.speech("Brightness set to maximum")
        if(text in FullLowBrightness):
            BC.BrightnessFullLow()
            V_OP.speech("Brightness set to minimum")

    
    
        
    

