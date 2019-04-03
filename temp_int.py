from subprocess import check_output
from re import findall
from time import sleep, strftime, time
def get_CPUtemp():
		CPUtemp=check_output(['vcgencmd','measure_temp']).decode('UTF-8')
		CPUtemp=float(findall('\d+\.\d+',CPUtemp)[0])
		return(CPUtemp)
def write_CPUtemp(CPUtemp):
		with open('/dev/shm/mjpeg/user_annotate.txt','w') as log:
		  log.write('{0}{1}{2}'.format('CPU: ',str(CPUtemp),'C '))
while True:
		CPUtemp = get_CPUtemp()
		write_CPUtemp(CPUtemp)
		sleep(10) 
