import serial

# Set here the baudrate and serial port your device is connected to
serialport = '/dev/ttyUSB0'
baudrate = 115200
uart = serial.Serial(serialport, baudrate)
translations = {}


# Picks the abbreviations contained in the file and put them in a dictionary
with open('abbreviations_list', 'r') as f:
    for line in f:
        line = line.rstrip().split(' ',  1)
        abbrev = line[0]
        human_message = line[1]
        translations[abbrev] = human_message


# Read the data from UART and translate it to human readable messages
while(1):
    mcu_message = uart.readline().decode()
    mcu_message = mcu_message.split()
    abbrev = mcu_message[0]
    payload = mcu_message[1:]
    if payload:
        print(translations[abbrev].format(*payload))
    else:
        print(translations[abbrev])
