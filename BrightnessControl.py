import screen_brightness_control as sbc

# Code for Increase Brightness
def BrightnessIncrease():
    #print("BrightINC")
    current_brightness = sbc.get_brightness()
    if((current_brightness[0]) >= 100):
        current_brightness[0] = 100
    else:
        current_brightness[0] += 10
    sbc.set_brightness(current_brightness[0])

# Code for Decrease Brightness
def BrightnessDecrease():
    #print("BrightDEC")
    current_brightness = sbc.get_brightness()
    if((current_brightness[0]) <= 10):
        current_brightness[0] = 0
    else:
        current_brightness[0] -= 10
    
    sbc.set_brightness(current_brightness[0]) 
def BrightnessHalf():
    current_brightness = sbc.get_brightness()
    current_brightness[0] = 50
    sbc.set_brightness(current_brightness[0])
def BrightnessFull():
    current_brightness = sbc.get_brightness()
    current_brightness[0] = 100
    sbc.set_brightness(current_brightness[0])
def BrightnessFullLow():
    current_brightness = sbc.get_brightness()
    current_brightness[0] = 0
    sbc.set_brightness(current_brightness[0])
# current_brightness = sbc.get_brightness()
# print("Brightness before:",current_brightness)
# BrightnessFullLow()
# print("Brightness down")
# current_brightness = sbc.get_brightness()
# print("Brightness after:",current_brightness)
# BrightnessDecrease()