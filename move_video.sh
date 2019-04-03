#!/bin/bash
if mountpoint -q /media/pi/FREECOM; then
    		sudo mv /var/www/media/*.mp4 /mnt/NAS/
    		sudo mv /var/www/media/*.jpg /mnt/NAS/
fi
