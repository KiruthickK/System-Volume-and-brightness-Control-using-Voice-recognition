# for sound
# For Acessing Speakers

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
#for brightness


def VolumeIncrease():
    #print("VolINC")
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb + 0.75 >= 0:
        currentVolumeDb = 0
    else:
        currentVolumeDb += 1
    volume.SetMasterVolumeLevel(currentVolumeDb, None)

# Code for Volume Decrease
def VolumeDecrease():
    #print("VolDEC")
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb - 0.25 <= -65.25:
        currentVolumeDb = -65.25
    else:
        currentVolumeDb -= 0.75
    volume.SetMasterVolumeLevel(currentVolumeDb, None)

# Code for Volume Mute
def VolumeMute():
    #volume.SetMute(0, None)
    currentVolumeDb = volume.GetMasterVolumeLevel()
    currentVolumeDb = -65.25
    volume.SetMasterVolumeLevel(currentVolumeDb, None)
def UnMute():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    currentVolumeDb = -60.0
    volume.SetMasterVolumeLevel(currentVolumeDb, None)

def VOLUME(vol):
    if(vol == 1):
        VolumeIncrease()
        #speech("Volume is increased")
        print("Volume is increased")
    elif(vol == 3):
        VolumeDecrease()
        #speech("Volume is Decreased")
        print("Volume is Decreased")
    # elif(vol == 2):
    #     BrightnessIncrease()
    #     #speech("Brightness is increased")
    #     print("Brightness is increased")
    # elif(vol == 4):
    #     BrightnessDecrease()
        #speech("Brightness is Decreased")
        print("Brightness is Decreased")
    elif(vol == 5):
        VolumeMute()
        print("Muted")

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate( IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
