---
layout: post
title: "CSS Spinners of all Shapes and Sizes"
summary: "A bespoke collection"
---

Let's spin round and round！ (*´∀`)♪

# Design Constraints

I have restricted myself to only loading spinners that require a single html div. In addition, excepting the last one,
all of the spinners don't depend on the page background color. I have also assumed a relatively modern browser in order
to keep the required CSS clean, short, and free of ugly hacks.

## Minimal viable spinner

<style>
    .minimal1 {
        width: 50px;
        height: 50px;
        border: 7px solid;
        border-color: #888 transparent transparent;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }
    
    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }
</style>
<div class="minimal1"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="collapseExample">
  <pre class="card card-body">
    .minimal1 {
        width: 50px;
        height: 50px;
        border: 7px solid;
        border-color: #888 transparent transparent;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Double whirl

<style>
    .minimal {
        width: 50px;
        height: 50px;
        border: 7px solid;
        border-color: transparent #888;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }
</style>
<div class="minimal"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#minimalcode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="minimalcode">
  <pre class="card card-body">
    .minimal {
        width: 50px;
        height: 50px;
        border: 7px solid;
        border-color: transparent #888;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Comet

<style>
    .whirlpool {
        width: 50px;
        height: 50px;
        border: 7px solid;
        border-style: solid solid none none;
        border-color: #888 transparent transparent ;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }
</style>
<div class="whirlpool"></div>


<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#minimalwhirlpool" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="minimalwhirlpool">
  <pre class="card card-body">
    .whirlpool {
        width: 50px;
        height: 50px;
        border: 7px solid;
        border-style: solid solid none none;
        border-color: #888 transparent transparent ;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Whirlpool

<style>
    .whirlpool2 {
        width: 50px;
        height: 50px;
        border-width: 7px 7px 7px 0;
        border-style: solid;
        border-color: #888 #888 #8000 #888 ;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }
    .whirlpool2:after {
    }
</style>
<div class="whirlpool2"></div>


<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#whirlpool2code" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="whirlpool2code">
  <pre class="card card-body">
    .whirlpool2 {
        width: 50px;
        height: 50px;
        border-width: 7px 7px 0 7px;
        border-style: solid solid  solid  solid;
        border-color: #888 transparent transparent #888 ;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Spinning on track

<style>
    .track {
        width: 50px;
        height: 50px;
        border: 7px solid;
        border-color: #888 #88888822 #88888822;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }
</style>
<div class="track"></div>


<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#trackcode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="trackcode">
  <pre class="card card-body">
    .track {
        width: 50px;
        height: 50px;
        border: 7px solid;
        border-color: #888 #88888822 #88888822;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Flash

<style>
    .blinker {
        display: inline-block;
        animation: blinkanimation 1.7s infinite ease-in-out;
        font-size: 20px;
    }
    
    @keyframes blinkanimation {
      0%, 100% {
        opacity: 0.2;
      }
      50% {
        opacity: 0.8;
      }
    }
</style>
<div class="blinker">loading...</div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#blinkercode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="blinkercode">
  <pre class="card card-body">

    .blinker {
        display: inline-block;
        animation: blinkanimation 1.7s infinite ease-in-out;
        font-size: 20px;
    }
    
    @keyframes blinkanimation {
      0%, 100% {
        opacity: 0.2;
      }
      50% {
        opacity: 0.8;
      }
    }

  </pre>
</div>

<hr/>

## Triple fade

<style>
    .triplefade {
        display: block;
        width: 20px;
        height: 20px;
        background: #0000;
        border-radius: 50%;
        animation: triplefader 1s infinite ease-in-out;
    }
    
    @keyframes triplefader {
      0%, 100% {
        box-shadow: #8880 30px 0, #8880 60px 0, #8880 90px 0;
      }
      30% {
        box-shadow: #888f 30px 0, #8880 60px 0, #8880 90px 0;
      }
      50% {
        box-shadow: #888f 30px 0, #888f 60px 0, #8880 90px 0;
      }
      80% {
        box-shadow: #888f 30px 0, #888f 60px 0, #888f 90px 0;
      }
    }
</style>
<div class="triplefade"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#triplefadecode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="triplefadecode">
  <pre class="card card-body">
    .triplefade {
        display: block;
        width: 20px;
        height: 20px;
        background: #0000;
        border-radius: 50%;
        animation: triplefader 1s infinite ease-in-out;
    }

    @keyframes triplefader {
      0%, 100% {
        box-shadow: #8880 30px 0, #8880 60px 0, #8880 90px 0;
      }
      30% {
        box-shadow: #888f 30px 0, #8880 60px 0, #8880 90px 0;
      }
      50% {
        box-shadow: #888f 30px 0, #888f 60px 0, #8880 90px 0;
      }
      80% {
        box-shadow: #888f 30px 0, #888f 60px 0, #888f 90px 0;
      }
    }

  </pre>
</div>

<hr/>

## Dots

<style>
    .dots {
        margin: 50px;
        width: 10px;
        height: 10px;
        background: transparent;
        border-radius: 100%;
        box-shadow: #888 20px 20px,
                    #888 -20px -20px,
                    #888 20px -20px,
                    #888 -20px 20px;
        animation: spin 2s infinite linear;
    }
</style>
<div class="dots"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#dotscode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="dotscode">
  <pre class="card card-body">
    .dots {
        margin: 50px;
        width: 10px;
        height: 10px;
        background: transparent;
        border-radius: 100%;
        box-shadow: #888 20px 20px,
                    #888 -20px -20px,
                    #888 20px -20px,
                    #888 -20px 20px;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Dots Extra

<style>
    .dotsExtra {
        margin: 50px;
        width: 10px;
        height: 10px;
        background: transparent;
        border-radius: 100%;
        box-shadow: #888  20px  20px,
                    #888 -20px -20px,
                    #888  20px -20px,
                    #888 -20px  20px,
                    #888 0 27px,
                    #888 27px 0,
                    #888 -27px 0,
                    #888 0 -27px;
        animation: spin 2s infinite linear;
    }
</style>
<div class="dotsExtra"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#dotsextracode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="dotsextracode">
  <pre class="card card-body">
    .dotsExtra {
        margin: 50px;
        width: 10px;
        height: 10px;
        background: transparent;
        border-radius: 100%;
        box-shadow: #888  20px  20px,
                    #888 -20px -20px,
                    #888  20px -20px,
                    #888 -20px  20px,
                    #888 0 27px,
                    #888 27px 0,
                    #888 -27px 0,
                    #888 0 -27px;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Dazzling spinner of many colors

<style>
    .dotsDazzle {
        margin: 50px;
        width: 10px;
        height: 10px;
        background: transparent;
        border-radius: 100%;
        box-shadow: red  20px  20px,
                    orange -20px -20px,
                    yellow  20px -20px,
                    green -20px  20px,
                    blue 0 27px,
                    purple 27px 0,
                    indigo -27px 0,
                    crimson 0 -27px;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }
</style>
<div class="dotsDazzle"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#dotsDazzlecode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="dotsDazzlecode">
  <pre class="card card-body">
    .dotsDazzle {
        margin: 50px;
        width: 10px;
        height: 10px;
        background: transparent;
        border-radius: 100%;
        box-shadow: red  20px  20px,
                    orange -20px -20px,
                    yellow  20px -20px,
                    green -20px  20px,
                    blue 0 27px,
                    purple 27px 0,
                    indigo -27px 0,
                    crimson 0 -27px;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Flip

<style>
    .flip {
        margin: 50px;
        width: 50px;
        height: 50px;
        background: #888;
        border-radius: 100%;
        animation: flip 1s infinite ease-in-out;
    }
    
    
    @keyframes flip {
      0%, 100% {
        transform: scaleX(0);
      }
      50% {
        transform: scaleX(1);
      }
    }
</style>
<div class="flip"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#flipcode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="flipcode">
  <pre class="card card-body">
    .flip {
        margin: 50px;
        width: 50px;
        height: 50px;
        background: #888;
        border-radius: 100%;
        animation: flip 1s infinite ease-in-out;
    }

    @keyframes flip {
      0%, 100% {
        transform: scaleX(0);
      }
      50% {
        transform: scaleX(1);
      }
    }

  </pre>
</div>

<hr/>

## Flip Colors

<style>
    .flipcolors {
        margin: 50px;
        width: 50px;
        height: 50px;
        background: #aa6;
        border-radius: 100%;
        animation: flip 1s infinite ease-in-out, colors 2s infinite steps(1);
    }
    
    @keyframes flip {
      0%, 100% {
        transform: scaleX(0);
      }
      50% {
        transform: scaleX(1);
      }
    }
    
    @keyframes colors {
      0%, 100% {
        background: #44f;
      }
      50% {
        background: #f44;
      }
    }
</style>
<div class="flipcolors"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#flipcolorscode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="flipcolorscode">
  <pre class="card card-body">

    .flipcolors {
        margin: 50px;
        width: 50px;
        height: 50px;
        background: #aa6;
        border-radius: 100%;
        animation: flip 1s infinite ease-in-out, colors 2s infinite steps(1);
    }
    
    @keyframes flip {
      0%, 100% {
        transform: scaleX(0);
      }
      50% {
        transform: scaleX(1);
      }
    }
    
    @keyframes colors {
      0%, 100% {
        background: #44f;
      }
      50% {
        background: #f44;
      }
    }

  </pre>
</div>

<hr/>

## Timepiece

<style>
    .times {
        width: 50px;
        height: 50px;
        border: 5px solid #8888;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }
.times:after {
    width: 18px; height: 4px;
    border-radius: 50%;
    content: "";
    display: block;
position: absolute;
    background: #888;
    margin-top: 18px;
    margin-left: 20px;
}
.times:before {
    width: 6px; height: 6px;
    border: 2px solid #888;
    background: #eee;
    content: "";
    display: block;
    position: absolute;
    margin: auto;
    border-radius: 50%;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 2;
}
</style>
<div class="times"></div>


<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#timepiececode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="timepiececode">
  <pre class="card card-body">

    .times {
        width: 50px;
        height: 50px;
        border: 5px solid #8888;
        border-radius: 100%;
        animation: spin 2s infinite linear;
    }
    .times:after {
        width: 18px; height: 4px;
        border-radius: 50%;
        content: "";
        display: block;
        position: absolute;
        background: #888;
        margin-top: 18px;
        margin-left: 20px;
    }
    .times:before {
        width: 6px; height: 6px;
        border: 2px solid #888;
        background: #eee;
        content: "";
        display: block;
        position: absolute;
        margin: auto;
        border-radius: 50%;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 2;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Emoji Spin

<style>
    .emoji {
        display: inline-block;
        animation: spin 2s infinite linear;
        font-size: 40px;
    }
    
    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }
</style>
<div class="emoji">⚙️</div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#emojispincode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="emojispincode">
  <pre class="card card-body">
    .emoji {
        display: inline-block;
        animation: spin 2s infinite linear;
        font-size: 40px;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Emoji Flip

<style>
    .emojiflip {
        display: inline-block;
        animation: flipy 2s infinite ease-in-out;
        font-size: 40px;
        opacity: 0.5;
    }
    
    @keyframes flipy {
      0%, 100% {
        transform: rotate3d(0,0,0,0);
      }
      50% {
        transform: rotate3d(0,1,0,180deg);
      }
    }
</style>
<div class="emojiflip">🤔</div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#emojiflipcode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="emojiflipcode">
  <pre class="card card-body">

    .emojiflip {
        display: inline-block;
        animation: flipy 2s infinite ease-in-out;
        font-size: 40px;
        opacity: 0.5;
    }
    
    @keyframes flipy {
      0%, 100% {
        transform: rotate3d(0,0,0,0);
      }
      50% {
        transform: rotate3d(0,1,0,180deg);
      }
    }

  </pre>
</div>

<hr/>

## Emoji Bounce

<style>
    .emojibounce {
        display: inline-block;
        animation: bounce 1s infinite ease-in-out;
        font-size: 40px;
        opacity: 0.5;
    }
    
    @keyframes bounce {
      0%, 100% {
        transform: scale(1.2);
      }
      50% {
        transform: scale(0.9);
      }
    }
</style>
<div class="emojibounce">❤️</div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#emojibouncecode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="emojibouncecode">
  <pre class="card card-body">

    .emojibounce {
        display: inline-block;
        animation: bounce 1s infinite ease-in-out;
        font-size: 40px;
        opacity: 0.5;
    }
    
    @keyframes bounce {
      0%, 100% {
        transform: scale(1.2);
      }
      50% {
        transform: scale(0.9);
      }
    }

  </pre>
</div>

<hr/>

## Emoji Rock

<style>
    .emojitremble {
        display: inline-block;
        animation: tremble 1s infinite ease-in-out;
        font-size: 40px;
    }
    
    @keyframes tremble {
      0%, 100% {
        transform: rotate(0);
      }
      50% {
        transform: rotate(-10deg);
      }
    }
</style>
<div class="emojitremble">🚀</div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#emojitremblecode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="emojitremblecode">
  <pre class="card card-body">

    .emojitremble {
        display: inline-block;
        animation: tremble 1s infinite ease-in-out;
        font-size: 40px;
    }
    
    @keyframes tremble {
      0%, 100% {
        transform: rotate(0);
      }
      50% {
        transform: rotate(-10deg);
      }
    }

  </pre>
</div>

<hr/>

## Space

<style>
    .sol {
        margin: 90px;
        width: 10px;
        height: 10px;
        background: yellow;
        border-radius: 100%;
        box-shadow: red 50px 50px 0 0;
        animation: spin 10s infinite linear;
    }
.sol:after {
        content: "";
        display: block;
        position: absolute;
        width: 10px;
        height: 10px;
        background: #ffc;
        border-radius: 100%;
        box-shadow: aqua 30px 30px, yellow 0 0 10px, yellow 0 0 10px;
        animation: spin 5s infinite linear;
}
.sol:before {
        content: "";
        display: block;
        position: absolute;
        width: 10px;
        height: 10px;
        background: blue;
        border-radius: 100%;
        box-shadow: green 20px 20px;
        animation: spin 2s infinite linear;
}
</style>
<div class="sol"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#solcode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="solcode">
  <pre class="card card-body">

    .sol {
        margin: 90px;
        width: 10px;
        height: 10px;
        background: yellow;
        border-radius: 100%;
        box-shadow: red 50px 50px 0 0;
        animation: spin 10s infinite linear;
    }
    .sol:after {
        content: "";
        display: block;
        position: absolute;
        width: 10px;
        height: 10px;
        background: #ffc;
        border-radius: 100%;
        box-shadow: aqua 30px 30px, yellow 0 0 10px, yellow 0 0 10px;
        animation: spin 5s infinite linear;
    }
    .sol:before {
        content: "";
        display: block;
        position: absolute;
        width: 10px;
        height: 10px;
        background: blue;
        border-radius: 100%;
        box-shadow: green 20px 20px;
        animation: spin 2s infinite linear;
    }

    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }

  </pre>
</div>

<hr/>

## Faded swipe

<style>
.fadedSwipe {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(to right, #888 10%, #88888800 42%);
  animation: spin 1.4s infinite linear;
  transform: translateZ(0);
}
.fadedSwipe:before {
  width: 50%;
  height: 50%;
  background: #888;
  border-radius: 100% 0 0 0;
  display: block;
  content: '';
}
.fadedSwipe:after {
  background: white;/*background*/
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}
    
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>

<div class="fadedSwipe"></div>

<p><br/>
  <a class="btn btn-light" data-toggle="collapse" href="#fadedSwipecode" role="button" aria-expanded="false" aria-controls="collapseExample">
    View Code
  </a>
</p>
<div class="collapse" id="fadedSwipecode">
  <pre class="card card-body">
    .fadedSwipe {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(to right, #888 10%, #88888800 42%);
        animation: spin 1.4s infinite linear;
        transform: translateZ(0);
    }
    .fadedSwipe:before {
        width: 50%;
        height: 50%;
        background: #888;
        border-radius: 100% 0 0 0;
        display: block;
        content: '';
    }
    .fadedSwipe:after {
        background: white;/*background*/
        width: 75%;
        height: 75%;
        border-radius: 50%;
        content: '';
        margin: auto;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
    }

    @keyframes spin {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }

  </pre>
</div>


