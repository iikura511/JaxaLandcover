JaxaLandcover
======================
Jaxaの高解像度土地利用土地被覆図（約10m解像度）から指定した範囲をラスター形式で切り出すプログラムです。

範囲の指定は緯度経度およびUTM座標（ゾーン54）で行えます。

使い方
------
ターミナルで以下のようなコマンドを入力します。
<pre>
$ extract\_bl.py bl\_template.txt　緯度経度の場合
$ extract\_utm.py utm\_template.txt　UYM座標の場合
</pre>

### template.txtの書き方 ###
例がアップされています。  
緯度経度の場合（単位は度）
<pre>
s\_lat= 40.3　　西端
e\_lat= 40.9　　東端
dlat= 0.001　　画素サイズ
s\_lon= 140.2　 南端
e\_lon= 140.8　 北端
dlon= 0.001　  画素サイズ
</pre>
UTM座標系の場合(単位はメートル）
<pre>
xs= 406200.0　　西端
xe= 442200.0　　東端
dx= 30.0　　　　 画素サイズ
ys= 4460750.0　 南端
ye= 4496750.0　 北端
dy= 30.0　　　　 画素サイズ
</pre>


必要なデータ
----------------
[高解像度土地利用土地被覆図ホームページ][link]
を利用して、利用するデータ（10m相当のGeoTff形式データ）を入手して下さい。
[link]: http://www.eorc.jaxa.jp/ALOS/lulc/lulc_jindex.htm
ファイルはプログラムと同じフォルダに入れて下さい。

利用するライブラリ
--------
Python2.7で動作を確認しています。

1. sys,numpy,scipy,osgeoが必要です。
2. 自作のライブラリを利用します。  
　　1.jaxa\_util  投影法変換とGEOTIFFの読み書きなど  

ライセンス
----------
Copyright &copy; 2016 Yoshikazu Iikura  
Distributed under the [MIT License][mit].

[MIT]: http://www.opensource.org/licenses/mit-license.php
