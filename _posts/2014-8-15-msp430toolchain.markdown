---
layout: post
title:  "MSP430 Toolchain on OSX Mavericks"
summary:  "Developing for the MSP430 and the TI Launchpad Development Kit on OSX"
icon: "/images/favicons/chipicon.png"
---

![Mavericks MSP430](/images/mav.jpg "MSP430")

* Install XCode through the OSX App Store
* Open XCode, complete installation
* ``$ xcode-select --install     #installs the xcode command line utilities``
* ``$ sudo xcodebuild -license   #necessary for some reason``
* Download and install [MacPorts](https://www.macports.org/install.php)
* ``$ sudo port install msp430-gcc msp430-libc mspdebug``

Install the Drivers for the TI Launchpad
----------
* Install [GIT](http://git-scm.com)
* Clone the updated kext provided by Bert JW Regeer:
        $ git clone https://github.com/colossaldynamics/ez430rf2500.git
* Instructions for installing the kext are provided in the repository README file.

Compiling and Uploading Test Code to the TI Launchpad
----------
Create the folowing files in a new directory

File ``main.c`` (text program code)
```c
#include  <msp430g2553.h>

volatile unsigned int i = 0;

void main(void){
    WDTCTL = WDTPW + WDTHOLD;
    P1DIR |= 0x01;
    for (;;){
        P1OUT ^= 0x01;                          
        for(i=0; i< 20000; i++){
        }
    }
}
```

File ``Makefile`` (Defines compilation of the code)

```make
DEVICE=msp430g2452
CC=msp430-gcc
CFLAGS=-Os -Wall -g -mmcu=$(DEVICE)
OBJS=main.o
SRCS=main.c

all: main.elf

main.c: watchdog.h

main.elf: $(OBJS)
	$(CC) $(CFLAGS) -o main.elf $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -fr main.elf $(OBJS)

flash: main.elf
	mspdebug rf2500 "prog main.elf"

size: main.elf
	msp430-size main.elf

#for managing header file dependencies
depend: .depend

.depend: $(SRCS)
	rm -f ./.depend
	$(CC) $(CFLAGS) -MM $^ -MF  ./.depend;

include .depend
```

Change the ``DEVICE`` variable to match the one on the TI Launchpad

Compile the program:

```terminal
$ make
$ make flash
$ make verify
```

You're done!  The program running on the microcontroller should now be blinking the LED on the Launchpad.
