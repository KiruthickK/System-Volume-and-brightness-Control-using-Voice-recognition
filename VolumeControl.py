# for sound
# For Acessing Speakers

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#for brightness

#for storing volume level for recovering volume level for unmuting
VolumeLevelWhileMuting = 0.0
def VolumeIncrease():
    #print("VolINC")
    currentVolumeDb = volume.GetMasterVolumeLevel()
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

# Code for Volume Decrease
def VolumeDecrease():
    #print("VolDEC")
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb - 10 <= -65.25:
        currentVolumeDb = -65.25
    elif currentVolumeDb < -20:
        currentVolumeDb -= 10
    else:
        currentVolumeDb -= 1
    volume.SetMasterVolumeLevel(currentVolumeDb, None)

# Code for Volume Mute, unmute and maximum volume
def VolumeMute():
    #volume.SetMute(0, None)
    global VolumeLevelWhileMuting
    VolumeLevelWhileMuting = volume.GetMasterVolumeLevel()
    currentVolumeDb = -65.25
    volume.SetMasterVolumeLevel(currentVolumeDb, None)
def VolumeFull():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    currentVolumeDb = 0.0
    volume.SetMasterVolumeLevel(currentVolumeDb, None)
def UnMute():
    # currentVolumeDb = volume.GetMasterVolumeLevel()
    # currentVolumeDb = 0.0
    volume.SetMasterVolumeLevel(VolumeLevelWhileMuting, None)
def VolumeHalf():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    currentVolumeDb = -10.4
    volume.SetMasterVolumeLevel(currentVolumeDb, None)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate( IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


#tests
# VolumeIncrease()
# currentVolumeDb = volume.GetMasterVolumeLevel()
# print(currentVolumeDb)