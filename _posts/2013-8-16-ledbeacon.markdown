---
layout: post
title:  "Simple LED Bank Circuit"
summary:  "Driving several strings of LEDs from a single low-voltage digital IO pin."
---

{% include /image-left.html url="http://i.imgur.com/TtEnjD6.png" description="Circuit Diagram" href="http://i.imgur.com/TtEnjD6.png" %}

## Controlling a large LED bank from a microcontroller.

### Calculations:
For the purpose of example calculations consider using a set of <a href="http://www.digikey.com/product-detail/en/SIR-34ST3F/511-1363-ND/638559">infrared LEDs</a> with V<sub>F</sub>=1.3v @ 100mA, and a <a href="http://www.digikey.com/product-detail/en/TIP102/TIP102-ND/1053752">TIP102 transistor</a>


Voltage across the string of 8 LEDs is (8)(1.3v)=9.4v.  <br/>
Take V<sub>BE</sub>=1.3v<br/>
Then, I<sub>B</sub>=(3.7v)/(1k ohms)=3.7mA.<br/>
Therefore, V<sub>CE</sub>=0.5v<br/>
Voltage accross 22ohm resistor:  V<sub>R</sub>=(22ohms)(100mA)=2.2v<br/>
Finally, we can calculate:  V<sub>ss</sub>=9.4v+0.5v+2.2v=<b>12.1v</b><br/>


<!--more-->
<hr style="clear:both;">

### Circuitikz Source for Diagram:
<pre style="font-size:12px;">
\begin{figure}[H]
\begin{circuitikz}
\draw[thick]
(0,3) node[above]{Vcc} (0,3) to[R=$22\Omega$, i=I] (0,0) to[leD, l=D1] 
(0,-1) to[leD, l=D2] (0,-2) ;
\draw[thick, dashed] (0,-2) -- (0,-3) ;
\draw[thick] (0,-3) to[leD, l=D7] (0,-4) to[leD, l=D8, -*] (0,-6) -- (3,-6) 
(0,-7) node[npn](npn){}
(0,-6) -- (npn.collector)
(npn.emitter) -- (0, -8) node[ground]{}
(npn.base) to[R=$1k\Omega$,-o] (-4,-7) node[left]{DIO};
\draw[thick]
(3,3) node[above]{Vcc} (3,3) to[R=$22\Omega$, i=I] (3,0) to[leD, l=D9] 
(3,-1) to[leD, l=D10] (3,-2) ;
\draw[thick, dashed](3,-2) -- (3,-3);
\draw[thick](3,-3) to[leD, l=D15] (3,-4) to[leD, l=D16] (3,-6);
\end{circuitikz}
\end{figure}
</pre>