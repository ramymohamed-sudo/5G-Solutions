
Step(1):
git clone --branch development https://github.com/ramymohamed-sudo/5G-Solutions.git Telit 
<br />
Step(2):
cd Telit/Telit/
<br />
Step(3):
sudo python3 setup.py install
<br />
Step(4):
Either run the telit_initialize.py file to start the module
<br />
python3 telit_initialize.py
<br />
<br />
or run the following commands in python
<br />
python3
<br />
import IoTSixfabTelit
<br />
from time import sleep
<br />
node = IoTSixfabTelit.IoT()
<br />
node.setupGPIO()   
<br /> 
node.enable()
<br />
print("Check the configured bandwidth")
<br />
node.sendATComm("AT#BND=?","OK")
<br />
node.disable()


VIP: for the mqtt codes and databases
In the python script for each sensor:
0- Install/configure the batteries (linux commands)
1- run the python code/method for the battery level, etc
2- change the sensors hostnames to pi01 to pi08
3- make use of these names (envirnoment variables when send data via the publisher code)
4- Once this is completed for one sensor - put everything on github and just use git clone

