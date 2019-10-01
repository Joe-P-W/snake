import os
import shutil

os.system("python -m pip install pygame")
path = os.getcwd()
print(path)

shutil.move(f"{path}\logic_files\play_snake.py", f"{path}\play_snake.py")
shutil.move(f"{path}\\run_installation.py", f"{path}\logic_files\\run_installation.py")

    
exit_ = input("Press enter to exit the installation")
