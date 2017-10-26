---
layout: post
title:  "ThingSpeak with Arduino and Processing"
summary:  "Light Sensor and Motion Sensor Using ThingSpeak, Arduino, and Processing"
---

["Thingspeak.com"](http://www.thingspeak.com) allows one to post information gathered by a networked device in real time.  I decided that I would test out the system with a simple light sensor.  Then, I went further by developing a new Processing application which detects motion using a webcam and posts it to a ThingSpeak channel.

I've been working with microcontrollers for some time, but Thingspeak.com is a great way to connect those microcontrollers to the world.

Light Sensor Development
------------

First, I made a simple program to learn how to send an HTTP GET request to thingspeak.com: <a href="https://docs.google.com/leaf?id=0B2ZbLCPalrgEZWZjNWMxYjYtZTZmYS00YTExLThkNWYtYzI0ZjYxYWY4YzRm&amp;hl=en">thingspeaktest.zip</a>. The program sends any numeric key press as a value to the thingspeak server.



Then I made the circuit to interface the light sensor to the Arduino.

<div>
{% include /image-left.html url="http://www.ladyada.net/images/sensors/cdsanasch.gif" description="Connecting the light sensitive resistor to the Arduino." href="http://www.ladyada.net/images/sensors/cdsanasch.gif" %}
{% include /image-left.html url="http://keeganmann.files.wordpress.com/2011/04/photo.jpg?w=300" description="Closeup of the finished circuit." href="http://keeganmann.files.wordpress.com/2011/04/photo.jpg" %}
</div>


The code I uploaded to the Arduino couldn't be simpler:

<script src="https://gist.github.com/a4d43618d4c1ae9a273a.js"></script>

Then, I modified my original processing app so that it forwards data received from the arduino to the server: [click here to download](https://docs.google.com/leaf?id=0B2ZbLCPalrgEZDdjMzVlYTYtMjhlMy00ZDlhLWJjYTMtNjc0ODc2YWIzYzZi&amp;sort=name&amp;layout=list&amp;num=50)

{% include /image.html url="http://keeganmann.files.wordpress.com/2011/04/screen-shot-2011-04-15-at-2-12-19-am.png?w=300" description="Screen Shot of Processing App" href="http://keeganmann.files.wordpress.com/2011/04/screen-shot-2011-04-15-at-2-12-19-am.png" %}

Motion Sensor Development
------------

After making the system with the light sensor, I had the idea to make a motion sensor using a webcam.

The Processing application essentially does the following:

* Takes the difference between frames continuously for thirty seconds (at only 2 frames per second to not overload the CPU).

* At the end of the thirty seconds, takes the max difference between frames and interprets this as the movement value.

* Sends this movement value to ThingSpeak.com

{% include /image.html url="http://keeganmann.files.wordpress.com/2011/04/screenshotmotion.png?w=300" description="Screenshot of the Processing app displaying in the background the motion currently occuring in the frame." href="http://keeganmann.files.wordpress.com/2011/04/screenshotmotion.png" %}


Results
---------

[Click here for a live graph of the <strong>light sensor data</strong>](https://www.thingspeak.com/channels/360/charts/1?height=400&amp;width=600&amp;timescale=1&amp;yaxis=Light%20level&amp;xaxis=Time&amp;title=Photocell%20in%20my%20Room)(Not active)

<a href="https://thingspeak.com/channels/539/charts/1?height=400&amp;width=600">Click here for a live graph of the <strong>motion data</strong>.</a> (Not Active)

{% include /image.html url="http://keeganmann.files.wordpress.com/2011/04/lightwave-annote.png?w=300" description="My first bit of output from the system after leaving it running over night. Click for live graph of data." href="https://thingspeak.com/channels/360/charts/1?height=400&amp;width=600&amp;yaxis=Light%20level&amp;xaxis=Time&amp;title=Photocell%20in%20my%20Room" %}

After getting it to work, I checked the output after leaving it over night. I was surprised to find that in the dark, the output was a regular sawtooth wave. What is the source of this strange signal? Noize? No. I actually have a clock on the wall which displays the time as the number of dots illuminated for each digit. The sawtooth signal is due to the last digit of the time incrementing—pretty cool!

