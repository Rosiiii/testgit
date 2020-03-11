#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file: getDataLight.py | Command-Line Beispiel: ./getDataLight.py
from spidev import SpiDev
import time
import os

# Speichern der Werte in einer Datei
def speichern(device,value):
    file = open(os.path.abspath(".") + "/ADC/" + str(device) + ".log","a")
    file.write("%s/%s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), value))
    file.close

# Werte festlegen
lightchannel = [0,1]    # MCP3008-Channel von den Lichtsensoren
maxvalue = 1023        # maximaler Rückgabewert vom Lichtsensor (nie mehr als 1023!)        - TODO (WERT PRÜFEN, ggf ändern)

# Initialisiere SPI
spi = SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

# Wert abfragen
for channel in lightchannel:
   adc = spi.xfer2([1, (8 + channel) << 4, 0])
   value = ((adc[1] & 3) << 8) + adc[2]
   #volt = round(value/maxvalue*3.3,4)
   #print(round(abs(maxvalue-value)/maxvalue*100,1))
   speichern(str(channel),round(abs(maxvalue-value)/maxvalue*100,1))

# SPI schließen
spi.close()
