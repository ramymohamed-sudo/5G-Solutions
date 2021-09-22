
Step(1):
git clone --branch development https://github.com/ramymohamed-sudo/5G-Solutions.git Telit 

Step(2):
cd Telit/Telit/

Step(3):
sudo python3 setup.py install

Step(4):
Either run the telit_initialize.py file to start the module
python3 telit_initialize.py
or run the following commands in python
python3
import IoTSixfabTelit
from time import sleep
node = IoTSixfabTelit.IoT()
node.setupGPIO()    
node.enable()
print("Check the configured bandwidth")
node.sendATComm("AT#BND=?","OK")
node.disable()

