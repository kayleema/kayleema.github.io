---
layout: minimal-post
title: "Map of Japan and USA Made Using CSS Grid"
summary: "Using just HTML and CSS"
icon: "/images/favicons/apps.png"
---

I've seen lots of maps in Japan using a simplified minimal boxy design and I think it looks kind of nice in an elegant
way and is useful for displaying information, so I thought I'd give it a try, using only HTML and CSS. Now that the need
to support IE11 has decreased I think it's safe now to use CSS grid for this kind of thing. 

I also made a map of the United States using the same technique which is something I don't think I've ever really seen
much before.


<style>

.map {
    display: grid;
    grid-template-columns: repeat(14, 1fr);
    grid-template-rows: repeat(10, 1fr);
    max-width: 100%;
    margin: 10px 0;
    background: #6678;
    border-radius: 40px;
    padding: 40px;
}
.map div {
    /*font-size: 11px;*/
    margin: -1px -1px 0 0;
    border: 1px solid #000;
    background: #eee;
    color: #000;
    /*font-weight: bold;*/
    padding: 6px;
    display: flex;
    justify-content: center;
    text-align:center;
    align-items: center;
    word-wrap: anywhere;
    line-height: 1;
}

.kagoshima, .okinawa, .miyazaki, .yamaguchi, .wakayama, .hiroshima, 
.okayama, .tokushima, .kochi, .nara, .mie, .kanagawa, .aichi, .shizuoka, .chiba, .hokkaido {
    box-shadow: 0 5px 0 black;
}

div.kanto {
    background: #094;
    color: #fff;
}
div.tohoku {
    background: #488;
    color: #fff;
}
div.hokuriku {
    background: #880;
    color: #fff;
}
div.chubu {
    background: #844;
    color: #fff;
}
div.kinki {
    background: #848;
    color: #fff;
}
div.shikoku {
    background: #440;
    color: #fff;
}
div.kyushu {
    background: #840;
    color: #fff;
}
div.chugoku {
    background: #080;
    color: #fff;
}
div.okinawa {
    background: #88f;
    color: #fff;
}
div.hokkaido {
    background: #448;
    color: #fff;
}

.hokkaido   {grid-column: 13 / 15;  grid-row: 1 / 4; border-radius: 11px;}
.aomori     {grid-column: 13 / 15;  grid-row: 5 / 5; border-radius: 11px 11px 0 0;}
.iwate      {grid-column: 14;  grid-row: 6 / 6;}
.miyagi     {grid-column: 14;  grid-row: 7 / 7;}
.akita      {grid-column: 13;  grid-row: 6 / 6;}
.yamagata   {grid-column: 13;  grid-row: 7 / 7;}
.fukushima  {grid-column: 13 / 15;  grid-row: 8 / 8;}
.ibaraki    {grid-column: 14;  grid-row: 10;}
.tochigi    {grid-column: 14;  grid-row: 9 / 9;}
.gunma      {grid-column: 13;  grid-row: 9 / 9;}
.saitama    {grid-column: 13;  grid-row: 10;}
.chiba      {grid-column: 14;  grid-row: 11 / 12; border-radius: 0 0 11px 0;}
.tokyo      {grid-column: 13;  grid-row: 11 / 12;}
.kanagawa   {grid-column: 13;  grid-row: 12; border-radius: 0 0 11px 0;}
.yamanashi  {grid-column: 12;  grid-row: 11;}
.nagano     {grid-column: 12;  grid-row: 9 / 11;}
.niigata    {grid-column: 12;  grid-row: 8 / 8;}
.toyama     {grid-column: 11;  grid-row: 8 / 8;}
.ishikawa   {grid-column: 10;  grid-row: 8 / 8; border-radius: 10px 0 0}
.fukui      {grid-column: 10;  grid-row: 9 / 9;}
.gifu       {grid-column: 11;  grid-row: 9 / 11;}
.shizuoka   {grid-column: 12;  grid-row: 12; border-radius: 0 0 0 11px;}
.aichi      {grid-column: 11;  grid-row: 11;}
.mie        {grid-column: 10;  grid-row: 11;}
.shiga      {grid-column: 10;  grid-row: 10;}
.kyoto      {grid-column:  9;  grid-row: 10; }
.osaka      {grid-column:  8;  grid-row: 11; }
.hyogo      {grid-column:  8;  grid-row: 10; }
.nara       {grid-column:  9;  grid-row: 11; }
.wakayama   {grid-column:  8/10;  grid-row: 12; border-radius: 0 0 11px 11px;}
.tottori    {grid-column:  7;  grid-row: 10;}
.shimane    {grid-column:  6;  grid-row: 10;}
.okayama    {grid-column:  7;  grid-row: 11;}
.hiroshima  {grid-column:  6;  grid-row: 11;}
.yamaguchi  {grid-column:  5;  grid-row: 10 / 12; border-radius: 11px 0 0 11px;}

.tokushima  {grid-column: 7;  grid-row: 14; border-radius: 0 0 11px 0;}
.kagawa     {grid-column: 7;  grid-row: 13; border-radius: 0 11px 0 0;}
.ehime      {grid-column: 6;  grid-row: 13; border-radius: 11px 0 0 0;}
.kochi      {grid-column: 6;  grid-row: 14; border-radius: 0 0 0 11px;}

.fukuoka    {grid-column: 2;  grid-row: 10; }
.saga       {grid-column: 1;  grid-row: 10; border-radius: 11px 0 0 0;}
.nagasaki   {grid-column: 1;  grid-row: 11; }
.kumamoto   {grid-column: 2;  grid-row: 11; }
.oita       {grid-column: 3;  grid-row: 10; border-radius: 0 11px 0 0;}
.miyazaki   {grid-column: 3;  grid-row: 11/13; border-radius: 0 0 11px 0;}
.kagoshima  {grid-column: 1 / 3;  grid-row: 12; border-radius: 0 0 0 11px;}

.okinawa {grid-column: 1; grid-row: 14;border-radius: 11px;}
</style>

<div class="map">
    <div class="hokkaido">北海道</div>

    <div class="aomori tohoku">青森</div>
    <div class="iwate tohoku">岩手</div>
    <div class="miyagi tohoku">宮城</div>
    <div class="akita tohoku">秋田</div>
    <div class="yamagata tohoku">山形</div>
    <div class="fukushima tohoku">福島</div>

    <div class="ibaraki kanto">茨城</div>
    <div class="tochigi kanto">栃木</div>
    <div class="gunma kanto">群馬</div>
    <div class="saitama kanto">埼玉</div>
    <div class="chiba kanto">千葉</div>
    <div class="tokyo kanto">東京</div>
    <div class="kanagawa kanto">神奈川</div>
    <div class="yamanashi kanto">山梨</div>
    <div class="nagano kanto">長野</div>

    <div class="niigata hokuriku">新潟</div>
    <div class="toyama hokuriku">富山</div>
    <div class="ishikawa hokuriku">石川</div>
    <div class="fukui hokuriku">福井</div>

    <div class="gifu chubu">岐阜</div>
    <div class="shizuoka chubu">静岡</div>
    <div class="aichi chubu">愛知</div>
    <div class="mie chubu">三重</div>

    <div class="shiga kinki">滋賀</div>
    <div class="kyoto kinki">京都</div>
    <div class="osaka kinki">大阪</div>
    <div class="hyogo kinki">兵庫</div>
    <div class="nara kinki">奈良</div>
    <div class="wakayama kinki">和歌山</div>

    <div class="tottori chugoku">鳥取</div>
    <div class="shimane chugoku">島根</div>
    <div class="okayama chugoku">岡山</div>
    <div class="hiroshima chugoku">広島</div>
    <div class="yamaguchi chugoku">山口</div>

    <div class="tokushima shikoku">徳島</div>
    <div class="kagawa shikoku">香川</div>
    <div class="ehime shikoku">愛媛</div>
    <div class="kochi shikoku">高知</div>

    <div class="fukuoka kyushu">福岡</div>
    <div class="saga kyushu">佐賀</div>
    <div class="nagasaki kyushu">長崎</div>
    <div class="kumamoto kyushu">熊本</div>
    <div class="oita kyushu">大分</div>
    <div class="miyazaki kyushu">宮崎</div>
    <div class="kagoshima kyushu">鹿児島</div>

    <div class="okinawa">沖縄</div>
</div>

The map of Japan is colored based on 地方 (region) and the map of the United States is colored based on "census regions"
since it seems like there isn't as much of a standard way of dividing the US into regions compared with Japanese 地方
which are more commonly used.

<style>
.usamap {
    display: grid;
    grid-template-columns: repeat(14, 1fr);
    grid-template-rows: repeat(20, 1fr);
    max-width: 100%;
    margin: 10px 0;
    background: #6678;
    border-radius: 40px;
    padding: 40px;
grid-auto-flow: column;
}
.usamap div {
    margin: -1px -1px 0 0;
    border: 1px solid #000;
    /*background: #eee;*/
    /*color: #000;*/
    /*font-weight: bold;*/
    padding: 6px;
    display: flex;
    justify-content: center;
    text-align:center;
    align-items: center;
    word-wrap: anywhere;
    line-height: 1;
    color: #fff;
}
.AK, .HI {
    grid-column: 1;
} .AK { grid-column-end: 3; }
.WA, .OR, .CA {
    grid-column: 2;
}
.ID, .NV, .AZ {
    grid-column: 3;
} .AZ { grid-column-end: 5; }
.MT, .WY, .UT {
    grid-column: 4;
} .MT, .WY { grid-column-end: 6; }
.CO, .NM {
    grid-column: 5;
}
.ND, .SD, .NE, .KS, .OK, .TX {
    grid-column: 6 / 8;
}
.MN, .IA, .MO, .AR, .LA {
    grid-column: 8;
} .MO, .AR, .LA { grid-column-end: 10; }
.WI, .IL {
    grid-column: 9;
}
.IN, .KY, .TN, .MS {
    grid-column: 10;
} .KY, .TN { grid-column-end: 12; }
.MI, .OH, .AL {
    grid-column: 11;
}
.NY, .PA, .WV, .VA, .NC, .GA, .FL {
    grid-column: 12;
} .NY, .VA, .NC { grid-column-end: 14; }
.VT, .CT, .NJ, .MD, .SC {
    grid-column: 13;
}
.NH, .MA, .RI, .DE {
    grid-column: 14;
}
.ME {
    grid-column: 15;
}

.AK, .ME {
    grid-row: 1 / 3;
}
.VT, .NH {
    grid-row: 2;
} 
.MI, .NY, .MA {
    grid-row: 3;
} .MI { grid-row-end: 5; }
.WA, .ID, .MT, .ND, .MN, .WI, .PA, .CT, .RI {
    grid-row: 4;
} .WA, .MT, .MN, .WI,.PA { grid-row-end: 6; } .ID { grid-row-end: 8; }
.SD, .OH, .NJ {
    grid-row: 5;
} .SD, .OH { grid-row-end: 7; }
.OR, .WY, .IA, .IL, .IN, .WV, .MD, .DE {
    grid-row: 6;
} .OR, .WY, .IA, .IL { grid-row-end: 8; }
.NE, .KY, .VA {
    grid-row: 7;
}
.CA, .NV, .UT,  .CO, .KS, .MO, .TN, .NC {
    grid-row: 8;
} .CA { grid-row-end: 12; } .NV, .UT, .CO { grid-row-end: 10; }
.OK, .AR, .MS, .AL, .GA, .SC {
    grid-row: 9;
} .MS, .AL { grid-row-end: 12; } .GA {grid-row-end: 11; }
.AZ, .NM, .TX, .LA {
    grid-row: 10 / 12;
} .TX { grid-row-end: 13; }
.FL {
    grid-row: 11 / 14;
}
.HI {
    grid-row: 13;
}

.CZ, .DC, .GU, .PR, .VI {
    grid-row: 20;
}

.HI, .CA, .AK, .HI, .FL, .TX {
    border-bottom-left-radius: 20px;
}
.HI, .AK, .FL, .TX, .ME, .DE, .SC, .RI {
    border-bottom-right-radius: 20px;
}
.HI, .AK, .HI, .AK, .ME, .WA, .MI, .VT {
    border-top-left-radius: 20px;
}
.HI, .HI, .AK, .ME, .WI, .DE {
    border-top-right-radius: 20px;
}

.WA, .OR, .CA, .NV, .ID, .MT, .WY, .UT, .CO, .NM, .AZ {
    background: #844;
}
.ND, .SD, .NE, .KS, .MO, .IA, .MN, .WI, .IL, .IN, .MI, .OH {
    background: #880;
}
.PA, .NY, .NJ, .RI, .CT, .MA, .VT, .NH, .ME {
    background: #848;
}
.OK, .AR, .LA, .MS, .AL, .GA, .FL, .TN, .KY, .WV, .VA, .NC, .SC, .MD, .DE, .TX {
    background: #080;
}

.AK, .HI {
    background: #448;
}
.HI {
    background: #27a;
}

.AK, .HI, .CA, .AZ, .NM, .TX, .LA, .MS, .AL, .FL, .SC, .DE, .ME {
    box-shadow: 0 5px 0 black;
}
.usamap div:hover, .map div:hover {
    box-shadow: 0 5px 0 0 black, -0px 5px 0px 5px #0003;
    z-index: 100;
    transform: translateY(-5px);
    transition: 0.3s;
}
.usamap div, .map div {
    transition: 0.3s;
    cursor: pointer;
}
.usamap div:active,  .map div:active {
    transform: translateY(-15px);
    transition: 0.1s;
}
</style>

<div class="usamap">
<div class="AL">AL</div>
<div class="AK">AK</div>
<div class="AZ">AZ</div>
<div class="AR">AR</div>
<div class="CA">CA</div>
<div class="CO">CO</div>
<div class="CT">CT</div>
<div class="DE">DE</div>
<div class="FL">FL</div>
<div class="GA">GA</div>
<div class="HI">HI</div>
<div class="ID">ID</div>
<div class="IL">IL</div>
<div class="IN">IN</div>
<div class="IA">IA</div>
<div class="KS">KS</div>
<div class="KY">KY</div>
<div class="LA">LA</div>
<div class="ME">ME</div>
<div class="MD">MD</div>
<div class="MA">MA</div>
<div class="MI">MI</div>
<div class="MN">MN</div>
<div class="MS">MS</div>
<div class="MO">MO</div>
<div class="MT">MT</div>
<div class="NE">NE</div>
<div class="NV">NV</div>
<div class="NH">NH</div>
<div class="NJ">NJ</div>
<div class="NM">NM</div>
<div class="NY">NY</div>
<div class="NC">NC</div>
<div class="ND">ND</div>
<div class="OH">OH</div>
<div class="OK">OK</div>
<div class="OR">OR</div>
<div class="PA">PA</div>
<div class="RI">RI</div>
<div class="SC">SC</div>
<div class="SD">SD</div>
<div class="TN">TN</div>
<div class="TX">TX</div>
<div class="UT">UT</div>
<div class="VT">VT</div>
<div class="VA">VA</div>
<div class="WA">WA</div>
<div class="WV">WV</div>
<div class="WI">WI</div>
<div class="WY">WY</div>
</div>

Maybe some time I'll make this into a more popular react component or something. I think it would be cool to have an
easy way to make these kinds of maps.
