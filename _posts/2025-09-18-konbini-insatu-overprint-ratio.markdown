---
layout: minimal-post
title: "How much does the convenience store enlarge the L-size photo prints"
summary: "For the purpose of accurate printing of ID photos"
icon: "/images/favicons/link.png"
---

**Information as of 2025-09-18**

When printing borderless prints at Lawson or FamilyMart convenience stores
the photo is slightly enlarged so that it can be printed borderless.

A L版(L size) photo print is of dimensions 127x89mm. 
Printing at a resolution of 600dpi results in a file 3000x2102 pixels.

Looking at a sample print, I have calculated the enlargement factor as approximately 104%.

Therefore, to produce a corresponding print feature of length `A` millimeters, the feature in the image file should be
`(A * 3000/127 / 1.04)` *pixels*

For example, to produce a 50mmx50mm ID photo, the size in the image should be 
`50 * 3000/127 / 1.04` → *1137mm*

Example: 30mmx40mm:  30mm * 3000px / 127mm / 1.04 = **681** ; 40mm * 3000px / 127mm / 1.04 = **909**

Happy printing.
