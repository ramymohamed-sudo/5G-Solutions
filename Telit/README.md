
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

