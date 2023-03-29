import shutil

def PrintRightSide(text):
    # Get the current console width
    width = shutil.get_terminal_size().columns
    padding = width - len(text)
    print(" " * padding + text)