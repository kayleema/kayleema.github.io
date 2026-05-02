---
layout: minimal-post
title: "Demo of Vertical CJK Writing with contenteditable"
summary: "webでの縦書き入力"
icon: "/images/favicons/apps.png"
---

<div
    style="
        writing-mode: vertical-rl;
        max-height: 200px;
        width: 50%;
        border: 1px solid #8884;
        margin: 30px auto;
        padding: 30px;
        border-radius: 3px; 
        overflow-x: auto;
    "
    contenteditable="true"
>
    <p>
        日本語を縦書きで入力できます。
    </p>
    <p>
        デスクトップとAndroidのChromeでは動きはほとんど合っているけれど、
    </p>
    <p>
        Safariの場合はすこすバグが発生してしまいます。
        カーソルの位置がずれたり、
        テキストの表示やスクロるがおかしくなります。
        あと変換中のポップアップは縦書きにならなくて、
        変なところに表示されます。
        残念です。
    </p>
    <p>
        入力してみてください。
    </p>
</div>
