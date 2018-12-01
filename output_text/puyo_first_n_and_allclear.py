# -*- coding: utf-8 -*-

#--------------------------------------------------
# ぷよぷよのＮ手目までのツモ譜(全消し判定付き)を全列挙したテキストファイルを生成する
#--------------------------------------------------
import copy

# 何手目までを列挙するか指定する
N = 6

# 4色分の色名
a = 'A'
b = 'B'
c = 'C'
d = 'D'

# Ｎ手目までのツモ譜の総数と全消し(all clear)ツモ数をカウントする変数
count = 0
countac = 0

# これから書き込むテキストファイルを準備
f = open('puyo_first_'+str(N)+'.txt', 'w')

# ツモ譜(tsumofu)を入力すると、続きの+n手目までのツモ譜を全列挙する再帰関数
def TsumoNextN(n,tsumofu):
    global count
    global countac
    if n <= 0:
        na = 0 #number of a
        nb = 0 #number of b
        nc = 0 #number of c
        nd = 0 #number of d
        ac = 0 #allclear途中計算メモ用
        for tsumo in tsumofu:
            if tsumo[0] == a:
                na+=1
            elif tsumo[0] == b:
                nb+=1
            elif tsumo[0] == c:
                nc+=1
            else:
                nd+=1
            if tsumo[1] == a:
                na+=1
            elif tsumo[1] == b:
                nb+=1
            elif tsumo[1] == c:
                nc+=1
            else:
                nd+=1
            if na >= 4 and nb == 0 and nc == 0 and nd == 0:
                ac+=1
            elif na >= 4 and nb >= 4 and nc == 0 and nd == 0:
                ac+=1
            elif na >= 4 and nb >= 4 and nc >= 4 and nd == 0:
                ac+=1
            f.write(tsumo[0])
            f.write(tsumo[1])
            f.write(',')
        if ac > 0:
            f.write('全消し可,')
            countac+=1
        f.write('\n')
        count+=1
        print(str(count)+'('+str(countac)+')')
    else:
        sym = FindSymmetry(tsumofu)
        tsumocandidates = []
        for i, puyolist_i in enumerate(sym):
            if len(puyolist_i) >= 2:
                tsumocandidates.append((puyolist_i[0],puyolist_i[1]))
            for j, puyolist_j in enumerate(sym):
                if j>=i:
                    tsumocandidates.append((puyolist_i[0],puyolist_j[0]))
        for tsumo in tsumocandidates:
            nexttsumofu = tsumofu.copy()
            nexttsumofu.append(tsumo)
            TsumoNextN(n-1,nexttsumofu)

# ツモ譜(tsumofu)を入力すると、ぷよの色対称性を出力する関数
# [[a,b,c,d]：色に区別がないとき
# [[a],[b,c],[d]]：色bと色cに対称性があるとき
# [[a,b],[c,d]]：色aと色bに、色cと色dにそれぞれ対称性があるとき
# [[a],[b],[c],[d]]：対称性がないとき
def FindSymmetry(tsumofu):
    symmetry = [[a,b,c,d]]
    for tsumo in tsumofu:
        sym = []
        for puyolist in symmetry:
            sym1 = [puyo for puyo in puyolist if puyo in tsumo]
            sym2 = list(set(puyolist)-set(sym1))
            if sym1:
                sym.append(sorted(sym1))
            if sym2:
                sym.append(sorted(sym2))
        symmetry = sym
    return symmetry

# 最初の2手はABCDタイプを除けば8通り。それぞれについて続きのN-2手を求める。
TsumoNextN(N-2,[(a, a), (a, a)])
TsumoNextN(N-2,[(a, a), (b, b)])
TsumoNextN(N-2,[(a, a), (a, b)])
TsumoNextN(N-2,[(a, a), (b, c)])
TsumoNextN(N-2,[(a, b), (a, a)])
TsumoNextN(N-2,[(a, b), (c, c)])
TsumoNextN(N-2,[(a, b), (a, b)])
TsumoNextN(N-2,[(a, b), (a, c)])
#TsumoNextN(N-2,[(a, b), (c, d)]) ABCDタイプを含める場合に追加

# 生成したファイルを閉じる
f.close()
