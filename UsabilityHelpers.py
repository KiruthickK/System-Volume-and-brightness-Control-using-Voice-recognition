import shutil
import colorama 
from colorama import Fore, Back, Style
colorama.init()
def SingleLinePrinter():
    width = shutil.get_terminal_size().columns
    print(Fore.GREEN +("-"*width)+ Style.RESET_ALL)
def DesignPrinter():
    width = shutil.get_terminal_size().columns
    width = width/2
    width = int(width)-1
    print(((Fore.WHITE +"="+Fore.RED +"#") * width+"=")+ Style.RESET_ALL)
    # print(("=#" * width)+"=")
def PrintRightSide(text):
    # Get the current console width
    width = shutil.get_terminal_size().columns
    padding = width - len(text)
    print(" " * padding + text)
DesignPrinter()
# SingleLinePrinter()