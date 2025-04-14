#!/bin/bash
ethernet_connected=$(nmcli device status | grep ethernet | grep connected)
if [ -n "$ethernet_connected" ]; then
    nmcli radio wifi off
else
    nmcli radio wifi on
fi
