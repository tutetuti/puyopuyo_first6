# -*- coding: utf-8 -*-

#--------------------------------------------------
# ぷよぷよキャンバスを生成する
#--------------------------------------------------

from PIL import Image, ImageDraw

width = 550
height = 500
canvas = Image.new("RGB",(width,height),color=(255,255,255))

draw = ImageDraw.Draw(canvas)

# 全体の描画開始位置
global_x = 20
global_y = 50

# フィールドの描画開始位置
fx = global_x
fy = global_y

# ツモ譜の描画開始位置
tx = fx + 30*9
ty = global_y

# フィールド生成
for i in range(8):
    draw.rectangle((fx+30*i,fy+30*12,fx+30*(i+1),fy+30*13), fill=(89,67,49))
for i in range(12):
    draw.rectangle((fx,fy+30*i,fx+30,fy+30*(i+1)), fill=(89,67,49))
for i in range(12):
    draw.rectangle((fx+30*7,fy+30*i,fx+30*8,fy+30*(i+1)), fill=(89,67,49))
for i in range(9):
    draw.line((fx+30*i,fy,fx+30*i,fy+30*13), fill=(250,220,220), width=1)
for i in range(14):
    draw.line((fx,fy+30*i,fx+30*8,fy+30*i), fill=(250,220,220), width=1)

# ツモ譜エリア生成
for i in range(6):
    draw.line((tx+40*i,ty+30,tx+40*i+30,ty+30), fill=(214,255,238), width=1)
    draw.rectangle((tx+40*i,ty,tx+40*i+30,ty+60), outline=(150,150,150))
for i in range(6):
    draw.line((tx+40*i,ty+30+75,tx+40*i+30,ty+30+75), fill=(214,255,238), width=1)
    draw.rectangle((tx+40*i,ty+75,tx+40*i+30,ty+60+75), outline=(150,150,150))

canvas.save("canvas.png")
