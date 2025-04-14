#!/usr/bin/env python3
import os
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path) as f:
                print(f"# {file}")
                for line in f:
                    if line.startswith("#"):
                        print(line.strip())
