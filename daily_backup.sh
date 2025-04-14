#!/bin/bash
src="$HOME/Documents"
dest="/mnt/backup"
timestamp=$(date +"%Y%m%d_%H%M%S")
zipfile="$dest/backup_$timestamp.zip"
zip -r "$zipfile" "$src"
echo "Backup completed: $zipfile"
