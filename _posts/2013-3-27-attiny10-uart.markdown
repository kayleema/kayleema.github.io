---
layout: post
title:  "An Interrupt-Driven UART Library for the Attiny10"
summary:  "An efficient way to implement serial communications on one of the smallest microcontrollers"
---

The ATtiny10 lacks any hardware communication capabilities. My library solves
this problem by implementing a system to asynchronously receiving messages over
a serial datalink. The implementation contained within serial-tiny10.h uses 
interrupts and timers to sample the incoming signal. This allows you to do 
other things with the processor while simultaneously receiving data. I hope 
that this project will make it easier to build more complex and connected 
projects with the ATtiny10.

Note, the library depends on the delay loops contained in delay_accurate.h. 
It was necessary to create these new delay loops as the ones included in 
avr-libc are not compatible with the ATtiny10--they seem to assume the 
availability of certain instructions not implemented in the ATtiny10.

The entire project is available in a [GitHub repository here](https://github.com/keeganmann/attiny10-software-uart)


Here's an example piece of code using the library:

<script src="https://gist.github.com/kayleemann/11252490.js"></script>

I'm interested in hearing from you if you find this library useful.
