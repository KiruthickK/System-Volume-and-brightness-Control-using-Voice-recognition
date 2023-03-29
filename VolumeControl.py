# for sound
# For Acessing Speakers
import math
import VoiceOutput as V_OP
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate( IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#for storing volume level for recovering volume level for unmuting
VolumeLevelWhileMuting = 0.0

def VolumeIncrease():
    #print("VolINC")
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb == 0.0:
        V_OP.speech("Volume is already at its maximum level!")
        return
    if currentVolumeDb + 1 >= 0:
        currentVolumeDb = 0
    elif currentVolumeDb < -50:
        currentVolumeDb = -50
    elif currentVolumeDb <-20:
        currentVolumeDb += 10
    elif currentVolumeDb < -5:
        currentVolumeDb += 5
    else:
        currentVolumeDb += 1
    volume.SetMasterVolumeLevel(currentVolumeDb, None)
    V_OP.speech("volume Increased")

# Code for Volume Decrease
def VolumeDecrease():
    #print("VolDEC")
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb == -65.25:
        V_OP.speech("Volume is already at its minimum level!")
        return
    if currentVolumeDb - 15 <= -65.25:
        currentVolumeDb = -65.25
    elif currentVolumeDb > -5:
        currentVolumeDb -= 1
    elif currentVolumeDb > -20:
        currentVolumeDb -= 5
    elif currentVolumeDb <= -20 and currentVolumeDb > -50:
        currentVolumeDb -= 10
    elif currentVolumeDb <= -50 and currentVolumeDb > -60:
        currentVolumeDb -= 15
    else:
        currentVolumeDb -= 1
    volume.SetMasterVolumeLevel(currentVolumeDb, None)
    V_OP.speech("volume Decreased") 

# Code for Volume Mute, unmute and maximum volume
def VolumeMute():
    #volume.SetMute(0, None)
    V_OP.speech("System Volume is going to get muted!")
    global VolumeLevelWhileMuting
    VolumeLevelWhileMuting = volume.GetMasterVolumeLevel()
    if VolumeLevelWhileMuting == -65.25:
        V_OP.speech("Volume is already muted!")
        return
    currentVolumeDb = -65.25
    volume.SetMasterVolumeLevel(currentVolumeDb, None)
    
def VolumeFull():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb == 0.0:
        V_OP.speech("Volume is already at its maximum level!")
        return
    currentVolumeDb = 0.0
    volume.SetMasterVolumeLevel(currentVolumeDb, None)
    V_OP.speech("volume set to maximum level")
def UnMute(text):
    currentVolumeDb = volume.GetMasterVolumeLevel()
    # currentVolumeDb = 0.0
    if currentVolumeDb > -65.25:
        V_OP.speech("Volume is already unmuted!")
        return
    volume.SetMasterVolumeLevel(VolumeLevelWhileMuting, None)
    V_OP.speech(text+" Done successfully!")
def VolumeHalf():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb == 10.4:
        V_OP.speech("Volume is already at its half level!")
        return
    currentVolumeDb = -10.4
    volume.SetMasterVolumeLevel(currentVolumeDb, None)
    V_OP.speech("volume set to half level!")
def SayCurrentVolume():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if(currentVolumeDb < 0.0):
        currentVolumeDb = abs(currentVolumeDb)
        V_OP.speech("Current volume level is minus {:.2f} decibel!".format(currentVolumeDb))
    else:
        V_OP.speech("Current volume level is {:.2f} decibel!".format(currentVolumeDb))


# tests
# VolumeIncrease()
# currentVolumeDb = volume.GetMasterVolumeLevel()
# print(currentVolumeDb)
# SayCurrentVolume()