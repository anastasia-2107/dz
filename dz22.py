import os
import time
file = ".venv/pyvenv.cfg"

if os.path.exists(file):
    directory, name = os.path.split(file)
    atime = os.path.getatime(file)
    t = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime))
    print(f"{name} ({directory}) - время последнего доступа к файлу {t}")
else:
    print(f"Файл {file} не существует")
