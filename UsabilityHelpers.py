import shutil
def DesignPrinter():
    width = shutil.get_terminal_size().columns
    width = width/2
    width = int(width)-1
    print(("=#" * width)+"=")
def PrintRightSide(text):
    # Get the current console width
    width = shutil.get_terminal_size().columns
    padding = width - len(text)
    print(" " * padding + text)
# DesignPrinter()