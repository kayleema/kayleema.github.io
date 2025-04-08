---
layout: minimal-post
title: "A Fun Slidey Switch CSS Checkbox Design"
summary: "No other html elements required!"
icon: "/images/favicons/apps.png"
---

{% capture switchcss %}
.slideSwitchInput{
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
    transition: background-color 0.3s ease;
  }
  &:checked:after, &:active:after {
    background: deeppink;
  }
  &:checked:active:after {
    background: hotpink;
  }
  &:focus, &:active, &:hover {
    outline: none;
  }
}
{% endcapture %}


<style>
{{ switchcss }}
</style>

<div style="background: #eee; padding: 30px; margin: 30px; color: black;border-radius: 20px;">
<label style="display:flex;align-items:center;">It's a switch: <input type="checkbox" class="slideSwitchInput" /></label>
</div>

``` scss
{{ switchcss }}
```

