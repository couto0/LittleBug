# LittleBug: Efficient printf debug tool

## Introduction
Inspired in the original [BigBug](https://github.com/atakansarioglu/bigbug) by [Atakan SARIOGLU](https://github.com/atakansarioglu), this project was made initially to be a simpler cross-platform version (since I'm a linux user).

If you are an embedded system developer, sometimes you will need to figure out what's going on in your board, and, unlike conventional computers that have screens and many debugging tools, embedded systems sometimes can be a black box.

Printing information via serial port can help solve a lot of problems, showing what is happening or not, but, on the other hand, it can cause some timing problems, since print functions are slow, and can be even slower if there are many characters.

The most efficient way to use a print function is printing the minimum amount of characters. But printing short messages can be very confusing if there are too many of them.

## The solution
Without compromising both efficiency and readability, this simple program turns one or more characters sent from your device to your serial monitor into human readable messages.

Instead of sending "wifi connection is working" through serial port, which has 27 characters, you can send a simple "w", which has only 2 characters (including "\n"), and this program will show you
~~~~
wifi connection is working
~~~~
Just by adding this line to `abbreviations_list` file:
~~~~
w wifi connection is working
~~~~

## Requirements
Just `python3.7` and `pyserial` library. Works with any device that can print anything on your computer's serial port.

## Usage
In the same directory `littlebug.py` is located in, create a file named `abbreviations_list` containing the abbreviation followed by the description that will be showed. Just use an space to separate them, like this:
~~~~
hw Hello World!
w wifi connection is working
~~~~

In your firmware, add something like this:
~~~~c
printf("hw\n");
~~~~
and when your device prints "hw" will appear to you:
~~~~
Hello World!
~~~~

You can also print formated information, just add `{}` where you want to display the numbers/strings:
~~~~
s0 Sensor 0 measurement: {}
~~~~
and in your firmware:
~~~~c
printf("s0 %d\n", value);
~~~~
In this case, you will get something like this:
~~~~
Sensor 0 measurement: 723
~~~~


Adjust the baudrate and serialport variables in the beggining of the main file according to your device, and simply execute `littlebug.py` while the device prints the information on the serial port and *voilà!*
