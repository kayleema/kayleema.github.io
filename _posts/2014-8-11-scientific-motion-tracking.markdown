---
layout: post
title:  "Scientific Motion Tracking with Blender"
summary:  "Motion tracking with a python csv export script."
icon: "/images/favicons/3d.png"
---

The following details a method for tracking the rotation and translation of a single object in 2D with Blender.

Requirements
---------------

* [Blender 2.70](http://www.blender.org/)

Tracking
--------------

* Open Blender
* Click the screen-layout dropdown on top ![screen layout dropdown](/images/blender1.png)
    * Choose the "Motion Tracking" option
* At the bottom of the largest screen area, select the open icon
    * Browse to your video file
* Select the "End" box at the bottom of the screen and change it to the number of frames in your video.
* Using the timeline at the bottom of the screen, make sure that you are at frame #1
* In the main tracking pane, hold down ctrl and click on the insect head.  This adds a tracker.
* With the new tracker selected, type "sy" to scale in the y-direction and "sx" to scale in the x-direction.  Type "r" to rotate, and "g" to translate. Make sure the marker only covers the locust’s face.
* On the right, expand the "tracking settings section and change Motion to "LocRot" and Match to "Keyframe".  Check "prepass" and "normalize"
* With the tracker selected click the track forward button, or type 
  control-t to track the marker through the entire footage.   ![track forward button](/images/blender2.png)
    * If the tracking stops partway through, manually move the tracker to the correct position and type control-t to continue.  I found this not to be necessary in my case.

Exporting
------------

* [Download the export script from GitHub](https://gist.github.com/7b96bba85ed81aba864a)  (Alternatively, you can run `git clone https://gist.github.com/7b96bba85ed81aba864a.git` in a terminal)
* Change the editor type for the right-side area to "Text Editor", by opening the menu on the lower-right of the right-hand-side pane.  ![editor type dropdown](/images/blender3.png)
* Click the "Open" button on the bottom of the text editor to open the markers.py file downloaded above.
* In the text editor change the line `OUT_DIR = '/tmp'` to refer to the directory where you want to save your output files.  Do not include a trailing slash in your directory path.
* Press the "Run Script" button at the bottom of the text editor. (you may need to scroll right in order to see it).  ![run script button](/images/blender4.png)
* A .csv file with the following format will be generated in the output directory specified:

        <frame_number>,<position-x>,<position-y>,<corner1-x>,<corner1-y>,...,<corner4-x>,<corner4-y>