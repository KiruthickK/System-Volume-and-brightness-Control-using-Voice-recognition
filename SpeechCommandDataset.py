import difflib

#speech commands dataset, represented by python lists
IncreaseVolume = ["increase the volume","turn up the volume","increase volume","increase sound","i need more sound",
                  "i need more volume","increase the system volume","turn up the sound","raise the volume","make the sound louder",
                  "increase the sound","increase sound","increase the system volume level","increase volume level",
                  "increase the volume level"]
DecreaseVolume = ["decrease the volume","turn down the volume","decrease volume","decrease sound","reduce volume",
                  "reduce system volume","reduce the system volume","reduce the volume","reduce sound",
                  "reduce the system sound","reduce system sound","reduce the volume level",
                  "decrease the volume level","decrease volume level","make it quieter","lower the volume",
                  "make the sound quieter"]
VolumeMute = ["mute the volume","mute","mute volume","mute sound","no sound","no volume",
              "i want no volume","i want to mute my speakers","i want to mute my system volume",
              "minimum volume"]
VolumeUnMute = ["unmute the volume","unmute","unmute volume","enable sound","enable volume",
                "unmute the sound","unmute sound"]
FullVolume = ["full volume","set volume to full","set volume to maximum","set volume full",
                "maximum volume","set the volume to maximum","set the sound to maximum",
                "set the volume to maximum level","set volume to maximum level",
                "set volume to max level","set sound to max level","set sound to maximum level"]
IncreaseBrightness = ["increase the brightness","turn up the brightness","increase brightness",
                      "increase the brightness level","increase brightness level","raise the brightness","make the screen brighter",
                      "increase screen brightness","increase the display brightness","make the display brighter",
                      "brighten the screen","brighten the display","turn up the brightness level","turn up the display brightness",
                      "turn up the screen brightness","increase the screen brightness level","increase the display brightness level"]
DecreaseBrightness = ["decrease the brightness","turn down the brightness","decrease brightness","low brightness",
                      "lower the brightness","reduce the brightness","reduce the brightness level",
                      "decrease the brightness level","decrease brightness level","reduce brightness level",
                      "decrease screen brightness","decrease screen brightness level"]
FullBrightness = ["set the maximum brightness","turn up the brightness to maximum","maximum brightness",
                  "set brightness to full","full brightness","set full brightness","set maximum brightness",
                  "set brightness to maximum level"]
FullLowBrightness = ["set the minimum brightness","turn down the brightness to minimum","minimum brightness",
                     "full low brightness","full low level brightness"]
HalfVolume = ["half the volume","set volume to half","half volume","set half volume",
              "set volume to half level","half the volume level"]
BrightnessHalf = ["half the brightness","set brightness to half","half brightness","set half brightness",
                  "set the brightness to half level","set half level brightness",
                  "set brightness to half level"]
Stop = ["stop","top","pause","pause the program"]
start = ["start","start services","start service","continue","continue the program"]
stopCode = ["exit code","stop the program","exit","exit program","close the service","end the service",
            "terminate the program","exit the program"]
Yes = ["yes","yes stop the service","yes end the service","yes stop the program","yeah i want","yeah"]
No = ["no","i said by mistake","no i dont want","no i said by mistake","no i said by mistake sorry","nope"]

# for matching the input voice command with matching voice command in dataset
lists = [IncreaseVolume,VolumeMute,VolumeUnMute,FullVolume,DecreaseVolume,IncreaseBrightness,DecreaseBrightness,
         FullBrightness,FullLowBrightness,HalfVolume,BrightnessHalf,Stop,start,stopCode,Yes,No]

# The string we want to find matches for
def MatchCommand(query):
    matches = []
    # Find the best matches for each list
    for lst in lists:
        match = difflib.get_close_matches(query, lst)
        matches.extend(match)
    # Remove duplicates from the list of matches
    matches = list(set(matches))
    return matches
#for testing 
# matches = MatchCommand("i want")
# print(f"Matches for {'i want'}: {matches}")