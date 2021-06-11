"""
mb_PSRAM_64Mb_SPI_CP_example.py

Example CircuitPython script for 64Mbit SPI PSRAM with RP2040 (Raspberry Pi Pico).
Should work with other CircuitPython-capable devices with hardware of software SPI

Author: mark@marksbench.com

Version: 0.1, 2021-06-11

**NOTE: There is no guarantee that this software will work in the way you expect (or at all).
**Use at your own risk.

To use:
- Upload the mb_PSRAM_64Mb_SPI_CP.py file to your board into the /lib folder.
- Connect the PSRAM to the Pi Pico (RP2040), for testing (and to use this example script
  without modification) I suggest the following:

        PSRAM    |    Pi Pico
        1(/CE)   |    GP1 (Pin 2)
        2(SO)    | GP4, (SPI0 RX, Pin 6)
        3(SIO[2])|      NC
        4(Vss)   |    GND, (Pin 38)
        5(SI)    | GP7, (SPI0 TX, Pin 10)
        6(SCK)   | GP6, (SPI0 SCK, Pin 9)
        7(SIO[3])|      NC
        8(Vcc)   |   3V3 OUT, (Pin 36)

- To write a value: memory.write_byte(address, value)
- To read a value: value = memory.read_byte(address), value will be an int of range 0-255.
- You should get an error if the address or value is out of range.
- You need to lock and unlock the SPI bus as required in your own script (example below).


"""


import mb_PSRAM_64Mb_SPI_CP

import bitbangio
import busio
import digitalio
from board import *
import time


# Set up SPI with the pinout arrangement listed above
spi = busio.SPI(GP6, MOSI=(GP7), MISO=(GP4))

# Try to lock the SPI bus so the MCU and PSRAM are the only things talking on it
while not spi.try_lock():
    pass

# Set up the SPI bus speed, phase, and polarity.
# 1000000 should work in most situations but you can adjust down or up to find a good
# balance of performance and stability/power consumption.
# Phase and polarity are often (but not always) zero.
spi.configure(baudrate=4000000, phase=0, polarity=0)

cs = GP1 # This will be different on other boards - for the Raspberry Pi Pico it's GPx


# Create constructor to use driver
memory = mb_PSRAM_64Mb_SPI_CP.mb_PSRAM_64Mb_SPI_CP(spi, cs)


# Write a byte to the PSRAM. In this case, we'll write 238 to address 1234567.
memory.write_byte(1234567, 238)

# Write another byte to PSRAM, this time 51 to address 7654321.
memory.write_byte(7654321, 51)

# Now read the value stored in address 1234567 (should be 238).
value = memory.read_byte(1234567)
print("Value read:", value)

# Now read the value stored in address 7654321 (should be 51).
value = memory.read_byte(7654321)
print("Value read:", value)

# And finally, now that we're done with the PSRAM we should unlock the SPI bus.
spi.unlock()


# That's all there is to it
