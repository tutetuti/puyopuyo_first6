# -*- coding: utf-8 -*-

#--------------------------------------------------
# ツモ譜全列挙テキストファイルを読み込んで画像化する
#--------------------------------------------------

from PIL import Image, ImageDraw

# 4色分の色名
a = 'A'
b = 'B'
c = 'C'
d = 'D'

# ぷよぷよキャンバスファイルを読み込む
im = Image.open('canvas.png').copy()
width = im.size[0]
height = im.size[1]
draw = ImageDraw.Draw(im)

# ツモ譜全列挙テキストファイルを読み込む
N = 6
path = 'puyo_first_'+str(N)+'.txt'
f = open(path)

# 全体の描画開始位置
global_x = 20
global_y = 50

# フィールドの描画開始位置
fx = global_x
fy = global_y

# ツモ譜の描画開始位置
tx = fx + 30*9
ty = global_y

# ツモ譜エリアにぷよ描画して画像ファイル出力
for tsumoline in f:
    tsumolist = tsumoline.split(',')
    tsumolist.pop(-1) #\nを除去
    for i, tsumo in enumerate(tsumolist):
        if tsumo == '全消し可':
            break
        if tsumo[0] == a:
            c1 = (255,0,0)
            c2 = (150,0,0)
        elif tsumo[0] == b:
            c1 = (0,0,255)
            c2 = (0,0,150)
        elif tsumo[0] == c:
            c1 = (0,255,0)
            c2 = (0,150,0)
        elif tsumo[0] == d:
            c1 = (255,255,0)
            c2 = (150,150,0)
        if tsumo[1] == a:
            c3 = (255,0,0)
            c4 = (150,0,0)
        elif tsumo[1] == b:
            c3 = (0,0,255)
            c4 = (0,0,150)
        elif tsumo[1] == c:
            c3 = (0,255,0)
            c4 = (0,150,0)
        elif tsumo[1] == d:
            c3 = (255,255,0)
            c4 = (150,150,0)
        draw.ellipse((tx+40*i+2,ty+2,tx+40*i+30-2,ty+30-2), fill=c1, outline=c2, width=3)
        draw.ellipse((tx+40*i+2,ty+30+2,tx+40*i+30-2,ty+60-2), fill=c3, outline=c4, width=3)
    im.save(str(N)+'/'+''.join(tsumolist)+'.png')
