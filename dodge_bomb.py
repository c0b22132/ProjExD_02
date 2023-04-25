import random
import sys

import pygame as pg


delta={
    pg.K_UP:(0,-1),
    pg.K_DOWN:(0,1),
    pg.K_LEFT:(-1,0),
    pg.K_RIGHT:(1,0),
    }  # 練習４keyと移動量の辞書


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct=kk_img.get_rect()  # 練習４kk_rctの設定
    kk_rct.center=900,400  # 練習４kkの初期配置
    bb_img=pg.Surface((20,20))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)  # 練習１circleの描画設定
    bb_img.set_colorkey((0,0,0))  # 練習１Surfaceの透明化
    x,y=random.randint(0,1600),random.randint(0,900)  # 練習２ランダムな座標の生成
    vx,vy=+1,+1  # 練習３速度vx,vyの設定
    bb_rct=bb_img.get_rect()  # 練習３bb_rctの設定
    bb_rct.center=x,y  # 練習３初期配置の設定

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        key_lst=pg.key.get_pressed()
        for k,mv in delta.items():  # 練習４k,mvに辞書の内容を入れる
            if key_lst[k]:  # 練習４keyに対応して移動
                kk_rct.move_ip(mv)
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx,vy)
        screen.blit(bb_img,bb_rct)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()