import screen_brightness_control as sbc
import VoiceOutput as V_OP

# Code for Increase Brightness
def BrightnessIncrease():
    #print("BrightINC")
    current_brightness = sbc.get_brightness()
    if(current_brightness[0] == 100):
        V_OP.speech("Brightness is already at its maximum level!")
        return
    if((current_brightness[0] + 10) >= 100):
        current_brightness[0] = 100
    else:
        current_brightness[0] += 10
    sbc.set_brightness(current_brightness[0])
    V_OP.speech("Brightness Increased")

# Code for Decrease Brightness
def BrightnessDecrease():
    #print("BrightDEC")
    current_brightness = sbc.get_brightness()
    if(current_brightness[0] == 0):
        V_OP.speech("Brightness is already at its minimum level!")
        return
    if((current_brightness[0] - 10) <= 10):
        current_brightness[0] = 0
    else:
        current_brightness[0] -= 10
    sbc.set_brightness(current_brightness[0]) 
    V_OP.speech("Brightness decreased") 
    
def BrightnessHalf():
    current_brightness = sbc.get_brightness()
    if(current_brightness[0] == 50):
        V_OP.speech("Brightness is already at its half level!")
        return
    current_brightness[0] = 50
    sbc.set_brightness(current_brightness[0])
    V_OP.speech("Brightness set to half level!")
def BrightnessFull():
    current_brightness = sbc.get_brightness()
    if(current_brightness[0] == 100):
        V_OP.speech("Brightness is already at its maximum level!")
        return
    current_brightness[0] = 100
    sbc.set_brightness(current_brightness[0])
    V_OP.speech("Brightness set to maximum")
def BrightnessFullLow():
    current_brightness = sbc.get_brightness()
    if(current_brightness[0] == 0):
        V_OP.speech("Brightness is already at its minimum level!")
        return
    current_brightness[0] = 0
    sbc.set_brightness(current_brightness[0])
    V_OP.speech("Brightness set to minimum")
def SayCurrentBrightnessLevel():
    current_brightness = sbc.get_brightness()
    V_OP.speech("Current brightness level is "+ str(current_brightness[0]) + " percentage")

