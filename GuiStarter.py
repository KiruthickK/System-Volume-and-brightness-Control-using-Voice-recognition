import easygui
import os
msg = "Voice and Brightness control application..."
title="SysControllerVoiceBot"
choices = ["Start services","Exit"]
reply = easygui.buttonbox(msg, title,  choices=choices)
if reply == "Start services":
   os.startfile("SysControllerVoiceBot.bat")
   exit()
elif reply == "Exit":
   exit()
else:
   print("Done")