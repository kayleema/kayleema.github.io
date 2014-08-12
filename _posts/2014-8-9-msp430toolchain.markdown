---
layout: post
title:  "MSP430 Toolchain on OSX Mavericks"
summary:  "Set up for programming the MSP430 microcontroller"
---

* Install XCode through the OSX App Store
* Open XCode, complete installation
* ``$ xcode-select --install     #installs the xcode command line utilities``
* ``$ sudo xcodebuild -license   #necessary for some reason``
* Download and install [MacPorts](https://www.macports.org/install.php)
* ``$ sudo port install msp430-gcc msp430-libc mspdebug``
