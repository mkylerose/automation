#!/bin/bash
find /tmp -type f -mtime +3 -exec rm {} \;
echo "Old temp files deleted."
