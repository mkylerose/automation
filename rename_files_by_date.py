#!/usr/bin/env python3
import os
import time
folder = "./"
for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if os.path.isfile(path):
        timestamp = os.path.getmtime(path)
        date_str = time.strftime("%Y%m%d", time.localtime(timestamp))
        new_name = f"{date_str}_{filename}"
        os.rename(path, os.path.join(folder, new_name))
