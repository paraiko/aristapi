from time import sleep
import time
import os
def get_cam_timestamp():
    	timestamp = os.stat('/dev/shm/mjpeg/cam.jpg').st_mtime
   	 return timestamp
def get_now():
    	timestamp = time.time()
    	return timestamp
def get_time_dif(first, second):
   	 dif = first - second
    	return dif
def main():
   	 sleep(60)
   	 while True:
        	if get_time_dif(get_now(), get_cam_timestamp()) > 10.0:
            	os.system('/sbin/shutdown -r now')
        	else:
            	sleep(60)

main()
