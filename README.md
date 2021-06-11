# mb_PSRAM_64Mb_SPI_CP

Very simple CircuitPython module/driver for Espressif/Generic 64Mbit SPI PSRAM (Adafruit prdoduct ID: 4677 or similar). Works with RP2040, should work with other CircuitPython boards that have SPI.

This module is intended to make using the PSRAM as simple as possible. It only accepts an address (range 0-8388607) and a value (range 0-255). Values read from the PSRAM are returned as an integer (range 0-255).

Author: mark@marksbench.com

Version: 0.1, 2021-06-11

**NOTE(1): There is no guarantee that this software will work in the way you expect (or at all). Use at your own risk.

**NOTE(2): Writing and reading 64Mib over SPI is _not_ fast. If you're concerned about whether your program has crashed out over a long read or write loop, set up some sort of heartbeat - a periodically flashing LED, print statment, etc.

**NOTE(3): As this is PSRAM and not SRAM, do not exceed the maximum operating frequency or access the PSRAM outside its timing parameters as shown in the datasheet, or the PSRAM may not have enough time to do an internal refresh, causing a loss of data.

Prerequisites:
- RP2040 silicon (tested with Raspberry Pi Pico), should work with other MCUs with hardware or software SPI
- Tested with CircuitPython 6.2, 6.3, and 7.0.0-alpha.3
- PSRAM connected to hardware SPI port0 or port1 pins, should also work with SW SPI
- Dedicated /CS pin (can be any GP pin that's not already being used for SPI). Do not tie /CS to
  GND - the device requires state changes on /CS to function properly.

Usage:
- Set up hardware or software SPI. Polarity and phase are both 0.
- specify /CS pin (can be any GP pin that's not already being used for SPI):
  cs = GP#
- Create constructor:
  thisMemoryChipDeviceName = mb_PSRAM_64Mb_SPI_CP.mb_PSRAM_64Mb_CP(spi, cs)
- To write a single byte to an address:
  thisMemoryChipDeviceName.write_byte(address, value)
- To read a single byte from an address:
  thisMemoryChipDeviceName.read_byte(address)
- See mb_PSRAM_64Mb_SPI_CP_example.py

For more information, consult the Raspberry Pi Pico MicroPython SDK documentation at:
  https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf

and the CircuitPython documentation at:
  https://circuitpython.org

and the Adafruit 64Mbit PSRAM page and datasheet at:
  https://www.adafruit.com/product/4677
