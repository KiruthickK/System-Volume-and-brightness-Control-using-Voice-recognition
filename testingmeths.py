IncreaseVolume = ["increase the volume","turn up the volume"]
DecreaseVolume = ["decrease the volume","turn down the volume"]
IncreaseBrightness = ["increase the brightness","turn up the brightness"]
DecreaseBrightness = ["decrease the brightness","turn down the brightness"]
text = "increase the brightness"
if(text in IncreaseVolume):
    print("Hey vol")
if(text in IncreaseBrightness):
    print("Hey Bri")
if(text in DecreaseBrightness):
    print("BYe Bri")
if(text in DecreaseVolume):
    print("Bye VOl")
