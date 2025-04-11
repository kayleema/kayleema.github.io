---
layout: minimal-post
title: "A Fun Slidey Switch CSS Checkbox Design"
summary: "No other html elements required!"
icon: "/images/favicons/apps.png"
---

{% capture switchcss %}
.slideSwitchInput{
  cursor: pointer;
  background: none !important;
  appearance: none;
  outline: none;
  border: none;
  width: 40px;
  height: 24px;
  &:before {
    display: block;
    background: white;
    content: "";
    width: 20px;
    height: 20px;
    border-radius: 100%;
    position: absolute;
    z-index: 100;
    transform: translate(2px, 2px);
    transition: transform 0.3s ease, background-color 0.3s ease;
  }
  &:checked:before {
    transform: translate(20px, 2px);
    background: pink;
  }
  &:after {
    display: block;
    background: pink;
    content: "";
    width: 42px;
    height: 24px;
    border-radius: 12px;
    position: absolute;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
  }
  &:checked:after, &:active:after {
    background: deeppink;
  }
  &:checked:active:after {
    background: hotpink;
  }
  &:checked:hover:before {
    background: white;
  }
  &:hover:after {
    box-shadow: inset 0 0 10px 2px hotpink;
  }
  &:checked:hover:after {
    box-shadow: inset 0 0 10px 2px #0003;
  }
  &:focus, &:active, &:hover {
    outline: none;
  }
}
{% endcapture %}


<style>
{{ switchcss }}
</style>

<div style="background: #eee; padding: 30px; margin: 30px 0; color: black;border-radius: 20px;">
<label style="display:flex;align-items:center;">It's a switch: <input type="checkbox" class="slideSwitchInput" /></label>
</div>

``` scss
/* just add this css to an <input type=checkbox />*/
{{ switchcss }}
```
<hr/>

## A Longer Variation 🤪
{% capture longvariationcss %}
.longvariation {
  &:after {
    width: 202px;
  }
  &:checked:before {
    transform: translate(180px, 2px);
  }
}
{% endcapture %}
<style>{{ longvariationcss }}</style>

<div style="background: #eee; padding: 30px; margin: 30px 0; color: black;border-radius: 20px;">
<label style="display:flex;align-items:center;">
It's an even more exciting switch!:  
<input type="checkbox" class="slideSwitchInput longvariation" />
</label>
</div>

```scss
/* just add this css class in addition to the base one */
{{ longvariationcss }}
```

## More Variations:

<style>
.retrovariation {
  &:before, &:after {
    border-radius: 0;
  }
  &:before {
    color: white;
    width: 14px;
  }
  &:after {
    background: #000;
    outline: 2px solid #fff;
  }
  &:hover:before, &:checked:hover:before {
    opacity: 0.75;
  }
  &:checked {
    &:before {
      background: black;
      width: 14px;
      margin-left: 7px;
    }
    &:after {
      background: white;
      outline: 2px solid white;
    }
  }
  &:hover:after, &:checked:hover:after {
    box-shadow: none;
  }
  &:checked:hover:before {
    background: black;
  }
  &:hover:after {
    outline: 2px solid white;
  }
  &:active:before {
    background: white;
  }
  &:checked:active:after, &:active:after {
    background: black;
  }
}
</style>

<div style="background: #000; padding: 30px; margin: 30px 0; border-radius: 20px;">
<label style="display:flex;align-items:center;font-family:monospace;">
Retro version: <input type="checkbox" class="slideSwitchInput retrovariation" />
</label>
</div>

<style>
.emojivariation {
  &:before, &:checked:before, &:checked:hover:before {
    content: "☺️";
    font-size: 20px;
    background: transparent;
    margin-top: 0px;
    line-height: 1.0;
  }
}
</style>

<div style="background: #eee; padding: 30px; margin: 30px 0; border-radius: 20px;">
<label style="display:flex;color:deeppink;align-items:center;font-family:serif;">
Cute emoji version:  <input type="checkbox" class="slideSwitchInput emojivariation" />
</label>
</div>

<style>
:root {
  --mycolor: #a4a;
}
.sktoggle {
  background: red;
  width: 30px;
  height: 30px;
  appearance: none;
}
</style>

<!--<div style="background: #eee; padding: 30px; margin: 30px 0; border-radius: 20px;">
<label style="display:flex;color:black;align-items:center;">
A more skeumorphic version:  <input type="checkbox" class="sktoggle" />
</label>
</div>-->


