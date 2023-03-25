import difflib

#speech commands dataset, represented by python lists
IncreaseVolume = ["increase the volume","turn up the volume","increase volume","increase sound","i need more sound",
                  "i need more volume"]
VolumeMute = ["mute the volume","mute","mute volume","mute sound","no sound","no volume",
              "i want no volume","i want to mute my speakers","i want to mute my system volume"]
VolumeUnMute = ["unmute the volume","unmute","unmute volume","enable sound","enable volume",
                "unmute the sound","unmute sound"]
FullVolume = ["full volume","set volume to full","set volume to maximum","set volume full",
                "maximum volume","set the volume to maximum","set the sound to maximum"]
DecreaseVolume = ["decrease the volume","turn down the volume","decrease volume","decrease sound","reduce volume",
                  "reduce system volume","reduce the system volume","reduce the volume","reduce sound",
                  "reduce the system sound","reduce system sound"]
IncreaseBrightness = ["increase the brightness","turn up the brightness","increase brightness"]
DecreaseBrightness = ["decrease the brightness","turn down the brightness","decrease brightness","low brightness",
                      "lower the brightness","reduce the brightness"]
FullBrightness = ["set the maximum brightness","turn up the brightness to maximum","maximum brightness",
                  "set brightness to full","full brightness","set full brightness","set maximum brightness"]
FullLowBrightness = ["set the minimum brightness","turn down the brightness to minimum","minimum brightness",
                     "full low brightness"]
HalfVolume = ["half the volume","set volume to half","half volume","set half volume"]
BrightnessHalf = ["half the brightness","set brightness to half","half brightness","set half brightness"]
Stop = ["stop","top","pause","pause the program"]
start = ["start","start services","start service","continue","continue the program"]
stopCode = ["exit code","stop the program","exit","exit program","close the service","end the service",
            "terminate the program","exit the program"]
Yes = ["yes","yes stop the service","yes end the service","yes stop the program","yeah i want","yeah"]
No = ["no","i said by mistake","no i dont want","no i said by mistake","no i said by mistake sorry","nope"]

# Sample list of lists
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