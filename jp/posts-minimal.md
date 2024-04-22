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
{% for post in site.categories["jp"] %}
<li>

<span class="date">{{ post.date | date: "%Y年%m月%d日" }}</span>

{% if post.icon %}
<img src="{{ post.icon }}"           height="16px" />
{% else %}
<img src="/images/favicons/link.png" height="16px" />
{% endif %}


<span>
    <a href="{{ post.url }}">{{ post.title }}</a><br/>
    <span class="subtitle">{{ post.summary }}</span>
</span>

</li>
{% endfor %}
</ul>
