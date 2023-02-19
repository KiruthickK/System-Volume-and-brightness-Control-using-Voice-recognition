import screen_brightness_control as sbc

# Code for Increase Brightness
def BrightnessIncrease():
    #print("BrightINC")
    current_brightness = sbc.get_brightness()
    current_brightness[0] += 5
    sbc.set_brightness(current_brightness[0])

# Code for Decrease Brightness
def BrightnessDecrease():
    #print("BrightDEC")
    current_brightness = sbc.get_brightness()
    current_brightness[0] -= 5
    sbc.set_brightness(current_brightness[0]) 
while(True):
    inp = int(input("1 for up and 2 for down 3 for exit"))
    if(inp == 1):
        BrightnessIncrease()
    if(inp == 2):
        BrightnessDecrease()
    if(inp == 3):
        break
