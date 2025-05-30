---
layout: minimal-post
title: "How can just finding an input in a unit test be sooooo hard?"
summary: "Locating an input in a react unit test can an eternity especially when using materialui it seems"
icon: "/images/favicons/apps.png"
---

## The test results:  Rendering 300 inputs and getting one by label

[//]: # (<!--* 簡単なラベルの隣に簡単な入力欄)
[//]: # (* 簡単なラベルの中に簡単な入力欄)
[//]: # (* マテリアルUIの入力欄-->)

<table>
<thead>
<tr>
    <th></th>
    <th>A simple input inside a simple label</th>
    <th>a simple input <strong>beside</strong> a simple label</th>
    <th>A Material UI Input</th>
</tr>
</thead>
<tbody>
<tr>
    <td>HappyDOM</td>
    <td>7ms</td>
    <td>30ms</td>
    <td>117ms</td>
</tr>
<tr>
    <td>JSDOM</td>
    <td>39ms</td>
    <td>1,686ms</td>
    <td>19,138ms</td>
</tr>
</tbody>
</table>


*(execution time of `screen.getByLabelText`)*

See the simple source code for this test:  [github.com/kayleema/react-testing-performance](https://github.com/kayleema/react-testing-performance)

300 inputs is a lot but it's not that crazy of an amount, 
and it doesn't seem like finding an input in the dom is something so complicated that
a poorly performant algorithm would be unavoidable. Furthermore, in my investigation
I got the impression that the slowdown was extremely exponential with respect to the number
of inputs rendered on the page.

I wonder what crazy things Material UI is doing to make the performance so bad. It looks like Material UI
creates a few extra DOM elements per input but that alone doesn't explain the performance problems in my opinion.

Here we sit at the brink of a general AI singularity at the cusp of surpassing the power of the human mind and here I
find myself sitting, waiting 20 seconds to just find an input on a webpage that can fit on my screen. 
It's disappointing.
