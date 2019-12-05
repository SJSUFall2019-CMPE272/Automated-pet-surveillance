import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import math

mcp = Adafruit_MCP3008.MCP3008(clk=18,cs=25,miso=23,mosi=24)
sampleWindow = 1

while True:
    starttime = time.time()
    signalmax = 0
    signalmin = 1024
    
    while(time.time() - starttime) < sampleWindow:
        sample = mcp.read_adc(0)
        if sample<1024:
            if sample>signalmax: signalmax = sample
            if sample<signalmin: signalmin = sample
    peaktopeak = signalmax-signalmin
    N = (peaktopeak * 3.3)/1024
    
    print(N)