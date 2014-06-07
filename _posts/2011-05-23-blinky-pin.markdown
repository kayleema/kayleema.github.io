---
layout: post
title:  "Blinky Pin!"
summary:  "A fun blinky pin circuit using a 555 timer."
---
It's fun to make a permanent electronic circuit you can use even if its a painfully simple circuit like this one.  I added blinking lights to a pin from my FIRST Robotics Competition team.  It turns out that a 9-volt battery is too heavy for a pin, so I ended up making it into a necklace.


<div class="row">
<div class="col-xs-3 col-md-3">
{% include /image.html url="http://keeganmann.files.wordpress.com/2011/05/pin.jpg?w=148" description="The front of the pin" href="http://keeganmann.files.wordpress.com/2011/05/anim1.gif" %}
</div>
<div class="col-xs-3 col-md-3">
{% include /image.html url="http://keeganmann.files.wordpress.com/2011/05/pinback.jpg?w=148" description="The back of the pin with electronics visible." href="http://keeganmann.files.wordpress.com/2011/05/pinback.jpg" %}
</div>
<div class="col-xs-3 col-md-3">
{% include /image.html url="http://keeganmann.files.wordpress.com/2011/05/anim2.gif" description="The blinking pin!" href="http://keeganmann.files.wordpress.com/2011/05/anim2.gif" %}
</div>
</div>

In order to hold everything together I just used tons of hot glue. I made the electronics as small as I could on a little piece of perfboard.  

The Circuit
-------------
{% include /image-right.html url="/img/pinsch.png" description="LED Flasher Schematic" href="/img/pinsch.png" %}

I used a 555 timer IC in as an astable multivibrator with a bypass diode to get a 50% duty cycle.


The six LEDs are connected to the output of a standard 555 timer based astable multivibrator. When the output goes high, however, the voltage across the LEDs is lower because the "high" output of the 555 timer doesn't go all the way to the supply voltage though it does go all the way to ground when the output is low. As a consequence, three of the LEDs light dimmer (I should have used smaller resistors for those). This is more noticeable at lower supply voltages.  The diode is present in order to achieve a 50% duty cycle.  Capacitor $$C_1$$ charges through $$R_2$$ and discharges through $$R_1$$.

Circuit Theory
-----------------
The THR output turns the Q output high when higher than $$2/3$$ of the supply voltage and turns it low when lower than $$1/3$$.  The DIS or "discharge" pin is connected to ground when the Q output is high so that the capacitor can discharge.

The time it takes for the capacitor $$C_1$$ to charge through $$R_2$$ or discharge through $$R_1$$ can be found by solving the following series of differential equations for  $$ V_c $$ .

$$V_r = I \cdot R$$
  (for the Resistor)<br/>
$$I = C \frac{dV_c}{dt}$$
  (for the Resistor)<br/>
$$V_s = V_r + V_c $$
  (Resistor and capacitor are in series, so voltages add up)<br/>
Yielding,<br/>
$$V_c = V_s + (Vo - V_s) e^{\frac{-t}{(R C)}}$$

$$C_1$$ charges from $$1/3$$ of $$V_s$$ to $$2/3$$ of $$V_s$$.  Therefore, we substitute $$Vo = V_s / 3$$ and $$V_c = 2 / 3 \cdot V_s$$ and solve for t yielding:
$$t = ln(2) \cdot R \cdot C$$

Therefore, assuming $$R_1 = R_2$$ so that the duty cycle is 50%,
The period is:    $$T = 2 \cdot ln(2) \cdot R \cdot C$$<br/>
The frequency is:    $$f = 1 / ( 2 \cdot ln(2) \cdot R \cdot C)$$<br/>

<em>
For a more detailed explanation of the 555 timer, see <a href="http://www.doctronics.co.uk/555.htm" target="_blank">this page</a>.
</em>


<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$',''], ['\\(','\\)']]}});
</script>