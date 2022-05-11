# Radio-Project
Project for 18358 where we are using LoRa radio to perform various actions in a raspberry Pi.

This project has been adapted from Adafruit's LoRa bidirectional packet radio communication project. 

The source code for that project is available here: https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/sending-data-using-a-lora-radio

We use the Adafruit LoRa Radio Bonnet with OLED - RFM95W @ 915MHz nodule for this project. 
The neat thing about this bonnet is that it comes with 3 buttons, each of which send a different packet when prompted. 

Therefore, it gives us potential to extract various kinds of information by programming our RPi to perform different actions on receiving different packets. To demonstrate, we shall send the current time according to python's time.time() function, although this could be expanded further into better applications like sharing weather and temperature data by connecting and using a temperature sensor and then sending data out via the packet radio.

In the first section of our code, we import the various libraries needed for our bidirectional communication, as well as the library (time) for our time computation. 

Our code works by setting up our buttons for the raspberry Pi and connects them to the right pins in the GPIO, then, we configure the OLED display and the packet radio, the OLED display being responsible for the data visuals, and the packet radio being our means of information transfer. '

Then, within a while loop, we write packets of data according to the button presses, then we transmit them, as well as, read any incoming packets and perform actions according to the requested command. The functions rfm69.receive() and rfm69.send(data) perform our reception and delivery of our packet radio data. 
