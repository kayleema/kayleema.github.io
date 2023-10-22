---
layout: minimal
title: Posts
subtext: "Just some random articles I've put up for fun. Some of them are from a really long time ago."
---

<div class="switcher">
<span>English</span>・<a href="/jp/posts-minimal.html">日本語</a>
</div>

<ul class="posts">
{% for post in site.posts %}
{% if post.lang %}
{% else %}
<li>
<span class="date">{{ post.date | date_to_string }} &raquo;</span> <a href="{{ post.url }}">{{ post.title }}</a><br/>
<span class="subtitle">{{ post.summary }}</span>
</li>
{% endif %}
{% endfor %}
</ul>
