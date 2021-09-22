

""" Please check band, mode (NB1/2/CAT0/auto) before any tshoot"""


import IoTSixfabTelit
from time import sleep
node = IoTSixfabTelit.IoT()

node.setupGPIO()    # channel is already in use
node.enable()
# node.disable()
print("Check the configured bandwidth")
node.sendATComm("AT#BND=?","OK")
# node.sendATComm("AT#BND=?","OK\r\n")



# node.getBandConfiguration()

# node.setMode(node.CATNB1_MODE)
# sleep(1)
# node.setNBIoTBand(node.LTE_B3) - it seems that the band is set to auto
# sleep(1)
# node.getBandConfiguration()

# node.getQueryNetworkInfo()
# node.getNetworkRegStatus()
# node.connectToOperator()

