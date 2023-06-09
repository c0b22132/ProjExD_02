import random
import sys

import pygame as pg


delta={
    pg.K_UP:(0,-1),
    pg.K_DOWN:(0,1),
    pg.K_LEFT:(-1,0),
    pg.K_RIGHT:(1,0),
    }  # 練習４keyと移動量の辞書


def check_bound(scr_rct:pg.Rect,obj_rct:pg.Rect)->tuple[bool,bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引数1:画面SurfaceのRect
    引数2:こうかとん、又は、爆弾SurfaceのRect
    戻り値:横方向、縦方向のはみ出し判定結果(画面内:True/画面外:False)
    """
    yoko,tate=True,True
    if obj_rct.left<scr_rct.left or scr_rct.right<obj_rct.right:
        yoko=False
    if obj_rct.top<scr_rct.top or scr_rct.bottom<obj_rct.bottom:
        tate=False
    return yoko,tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct=kk_img.get_rect()  # 練習４kk_rctの設定
    kk_rct.center=900,400  # 練習４kkの初期配置
    accs=[a for a in range(1,11)]  # 演習２の加速度リスト
    bb_img=pg.Surface((20,20))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)  # 練習１circleの描画設定
    bb_img.set_colorkey((0,0,0))  # 練習１Surfaceの透明化
    x,y=random.randint(0,1600),random.randint(0,900)  # 練習２ランダムな座標の生成
    vx,vy=+1,+1  # 練習３速度vx,vyの設定
    bb_rct=bb_img.get_rect()  # 練習３bb_rctの設定
    bb_rct.center=x,y  # 練習３初期配置の設定
    tmr = 0
    timer=0
    """
    演習１の途中
    kk_rz={
        (0,0):pg.transform.rotozoom(kk_img,0,1.0),
        (-1,0):pg.transform.rotozoom(kk_img,0,1.0),
        (-1,+1):pg.transform.rotozoom(kk_img,45,1.0),
        (0,+1):pg.transform.rotozoom(pg.transform.flip(kk_img,True,False),90,1.0),
        (+1,+1):pg.transform.rotozoom(pg.transform.flip(kk_img,True,False),135,1.0),
        (+1,0):pg.transform.rotozoom(pg.transform.flip(kk_img,True,False),180,1.0),
        (+1,-1):pg.transform.rotozoom(pg.transform.flip(kk_img,True,False),225,1.0),
        (0,-1):pg.transform.rotozoom(pg.transform.flip(kk_img,True,False),270,1.0),
        (-1,-1):pg.transform.rotozoom(kk_img,-45,1.0),
        }
    """

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        avx,avy=vx*accs[min(tmr//1000,9)],vy*accs[min(tmr//1000,9)]  # 演習２の加速度をavx,avyで速度にする
        key_lst=pg.key.get_pressed()
        for k,mv in delta.items():  # 練習４k,mvに辞書の内容を入れる
            if key_lst[k]:  # 練習４keyに対応して移動
                kk_rct.move_ip(mv)
        if check_bound(screen.get_rect(),kk_rct)!=(True,True):
            for k,mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0],-mv[1])
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(avx,avy)
        yoko,tate=check_bound(screen.get_rect(),bb_rct)
        if not yoko:  # 練習５
            vx*=-1
        if not tate:  # 練習５
            vy*=-1
        if kk_rct.colliderect(bb_rct):  # こうかとんがぶつかった時の判定
            timer=tmr+300  # こうかとんがぶつかった後の猶予時間
            kk_img=pg.transform.rotozoom(pg.image.load("ex02/fig/4.png"),-10,1.5)
        if tmr==timer:  # こうかとんがぶつかってから終わるまでのタイマー
            return
        screen.blit(bb_img,bb_rct)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()