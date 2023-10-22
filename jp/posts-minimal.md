---
layout: minimal
title: 記事
lang: jp
subtext: "古い記事は多いですが、時々記事を書きます。"
---

<div class="switcher">
<a href="/posts-minimal.html">English</a>・<span>日本語</span>
</div>

<ul class="posts">
{% for post in site.posts %}
{% if post.lang == "jp" %}
<li>
<span class="date">{{ post.date | date_to_string }} &raquo;</span> <a href="{{ post.url }}">{{ post.title }}</a><br/>
<span class="subtitle">{{ post.summary }}</span>
</li>
{% endif %}
{% endfor %}
</ul>
