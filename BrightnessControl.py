import screen_brightness_control as sbc
import VoiceOutput as V_OP

# Code for Increase Brightness
def BrightnessIncrease():
    #print("BrightINC")
    current_brightness = sbc.get_brightness()
    if(current_brightness[0] == 100):
        V_OP.speech("Brightness is already at its maximum level!")
    if((current_brightness[0] + 10) >= 100):
        current_brightness[0] = 100
    else:
        current_brightness[0] += 10
    sbc.set_brightness(current_brightness[0])

# Code for Decrease Brightness
def BrightnessDecrease():
    #print("BrightDEC")
    current_brightness = sbc.get_brightness()
    if(current_brightness[0] == 0):
        V_OP.speech("Brightness is already at its minimum level!")
    if((current_brightness[0] - 10) <= 10):
        current_brightness[0] = 0
    else:
        current_brightness[0] -= 10
    
    sbc.set_brightness(current_brightness[0]) 
def BrightnessHalf():
    current_brightness = sbc.get_brightness()
    if(current_brightness[0] == 50):
        V_OP.speech("Brightness is already at its half level!")
    current_brightness[0] = 50
    sbc.set_brightness(current_brightness[0])
def BrightnessFull():
    current_brightness = sbc.get_brightness()
    if(current_brightness[0] == 100):
        V_OP.speech("Brightness is already at its maximum level!")
    current_brightness[0] = 100
    sbc.set_brightness(current_brightness[0])
def BrightnessFullLow():
    if(current_brightness[0] == 0):
        V_OP.speech("Brightness is already at its minimum level!")
    current_brightness = sbc.get_brightness()
    current_brightness[0] = 0
    sbc.set_brightness(current_brightness[0])
def SayCurrentBrightnessLevel():
    current_brightness = sbc.get_brightness()
    V_OP.speech("Current brightness level is "+ str(current_brightness[0]))
# current_brightness = sbc.get_brightness()
# print("Brightness before:",current_brightness)
# BrightnessFullLow()
# print("Brightness down")
# current_brightness = sbc.get_brightness()
# print("Brightness after:",current_brightness)
# BrightnessDecrease()
