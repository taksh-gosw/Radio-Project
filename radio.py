# SPDX-FileCopyrightText: 2018 Brent Rubell for Adafruit Industries
#
# SPDX-License-Identifier: MIT

#Adapted for 18358 by Takshsheel Goswami

"""
Example for using the RFM69HCW Radio with Raspberry Pi.

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries
"""
# Import Python System Libraries
import time
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import the SSD1306 module.
import adafruit_ssd1306
# Import the RFM9X radio module.
import adafruit_rfm9x

# Button A
btnA = DigitalInOut(board.D5)
btnA.direction = Direction.INPUT
btnA.pull = Pull.UP

# Button B
btnB = DigitalInOut(board.D6)
btnB.direction = Direction.INPUT
btnB.pull = Pull.UP

# Button C
btnC = DigitalInOut(board.D12)
btnC.direction = Direction.INPUT
btnC.pull = Pull.UP


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# 128x32 OLED Display
reset_pin = DigitalInOut(board.D4)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
# Clear the display.
display.fill(0)
display.show()
width = display.width
height = display.height

# Configure Packet Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, 915.0)
prev_packet = None

while True:
    packet = None
    # draw a box to clear the image
    display.fill(0)
    display.text('RasPi Radio', 35, 0, 1)

    # check for packet rx
    packet = rfm69.receive()
    if packet is None:
        display.show()
        display.text('- Waiting for PKT -', 15, 20, 1)
    #Here, we keep waiting with this display till we receive
    #a  packet.
    else:
        # Display the packet text and rssi
        display.fill(0)
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        display.text('RX: ', 0, 0, 1)
        display.text(packet_text, 25, 0, 1)
        #Here we could perform various actions based on
        #what the text is, example, temperature detection
        #(A) for temp detection
        #(B) for current time
        #(C) for both in sequence.
        time.sleep(1)

    #Fall through is intentional. First we read then we write.

    if not btnA.value:
        # Send Button A
        display.fill(0)
        button_a_data = bytes("Button A!\r\n","utf-8")
        rfm69.send(button_a_data)
        display.text('Sent Button A!', 25, 15, 1)

    elif not btnB.value:
        # Send Button B
        display.fill(0)
        button_b_data = bytes("Button B!\r\n","utf-8")
        rfm69.send(button_b_data)
        display.text('Sent Button B!', 25, 15, 1)
    elif not btnC.value:
        # Send Button C
        display.fill(0)
        button_c_data = bytes("Button C!\r\n","utf-8")
        rfm69.send(button_c_data)
        display.text('Sent Button C!', 25, 15, 1)

    display.show()
    time.sleep(0.1)
