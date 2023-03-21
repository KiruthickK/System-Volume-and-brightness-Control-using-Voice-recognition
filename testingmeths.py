import easygui
import os
msg = "Load application..."
title="Tom's Hardware Application Starter"
choices = ["Google Chrome","Slack","PuTTY"]
reply = easygui.buttonbox(msg, title,  choices=choices)
if reply == "Google Chrome":
   os.startfile("SysControllerVoiceBot.bat")
elif reply == "Slack":
   os.startfile("SysControllerVoiceBot.bat")
elif reply == "PuTTY":
   print("Done")
else:
   print("Done")
print("Hao")