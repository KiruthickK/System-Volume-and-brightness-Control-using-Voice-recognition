import VoiceRecognition as VR
import VoiceOutput as V_OP
import VolumeControl as VC
import BrightnessControl as BC
#forincrease = ["increase the volume","up the volume"]
# volumeIncreaseCommands = ["Increase volume","volume Increase"]
IncreaseVolume = ["increase the volume","turn up the volume"]
VolumeMute = ["mute the volume","mute"]
VolumeUnMute = ["unmute the volume","unmute"]
DecreaseVolume = ["decrease the volume","turn down the volume"]
IncreaseBrightness = ["increase the brightness","turn up the brightness"]
DecreaseBrightness = ["decrease the brightness","turn down the brightness"]
FullBrightness = ["set the maximum brightness","turn up the brightness to maximum","maximum brightness","full brightness"]
FullLowBrightness = ["set the minimum brightness","turn down the brightness to minimum","minimum brightness","full low brightness"]
while(True):
    text = VR.SpeechToText()
    #todo
    # if(text ==""):
    #     continue
    text = text.lower()
    print("Received in main:"+text)
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
    if(text == "stop"):
        V_OP.speech("Thank you for using our service. Visit again!")
        exit
    
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

    
    
        
    

