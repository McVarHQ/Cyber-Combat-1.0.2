import pygame, arcade, time, random, math, pickle, os, os.path, mysql.connector
from pygame import mixer

# initialize
pygame.init()
pygame.mixer.init()
filepath = os.path.dirname(__file__)


def mod(x):
    if x < 0:
        x = x * -1
    else:
        pass
    return x


def player(x, y, c=10, moving=False, fire=False, c2=5):
    global g, m, n, player_shots, player_img, bullet, player_dy
    if moving:
        n += 1
    if n > c * 2:
        n = 1
    if fire:
        if m == 1:
            shm.play()
            player_shots += 1
            bullet = True
        else:
            bullet = False
        m += 1

    if m > c2 * 2:
        m = 1
    [a, b] = pygame.mouse.get_pos()
    r = math.atan2((b - y), (a - x))
    l = 360 - (r * 57.2958)
    if l > 360:
        l -= 360
    if l > 75 and l < 105:
        if (n <= c):
            if m <= c2 or fire == False:
                h = 0
                screen.blit(pimg_f, (int(x), int(y + h)))
                player_img = pimg_f
                player_dy = 128
            elif m > c2 and m <= c2 * 2:
                h = 2
                screen.blit(pimg_ff, (int(x), int(y + h)))
                player_img = pimg_ff
                player_dy = 150
        else:
            if m <= c2 or fire == False:
                h = 0
                screen.blit(pimg_f1, (int(x), int(y + h)))
                player_img = pimg_f1
                player_dy = 128
            elif m > c2 and m <= c2 * 2:
                h = 2
                screen.blit(pimg_ff1, (int(x), int(y + h)))
                player_img = pimg_ff1
                player_dy = 150
    else:
        player_dy = 128
    if l > 255 and l < 285:
        if (n <= c):
            if m <= c2 or fire == False:
                h = 0
                screen.blit(pimg_b, (int(x), int(y + h)))
                player_img = pimg_b
            elif m > c2 and m <= c2 * 2:
                h = -2
                screen.blit(pimg_bf, (int(x), int(y + h)))
                player_img = pimg_bf
        else:
            if m <= c2 or fire == False:
                h = 0
                screen.blit(pimg_b1, (int(x), int(y + h)))
                player_img = pimg_b1
            elif m > c2 and m <= c2 * 2:
                h = -2
                screen.blit(pimg_bf1, (int(x), int(y + h)))
                player_img = pimg_bf1
        ang = 270
    if l >= 105 and l <= 255:
        if m <= c2 or fire == False:
            rot = pygame.transform.rotate(pwimg_l, 180 + l)
            h = 0
        elif m > c2 and m <= c2 * 2:
            rot = pygame.transform.rotate(pwimg_lf, 180 + l)
            h = 2
        apos = (x - rot.get_rect().width / 2 + 73 + h, y - rot.get_rect().height / 2 + 35)
        if n <= c or moving == False:
            screen.blit(pimg_l, (int(x), int(y)))
            player_img = pimg_l
        elif n > c and n <= c * 2:
            screen.blit(pimg_l1, (int(x), int(y)))
            player_img = pimg_l1
        screen.blit(rot, (int(apos[0]), int(apos[1])))
        ang = l
    if (l >= 0 and l <= 75) or (l >= 285 and l <= 360):
        if m <= c2 or fire == False:
            rot = pygame.transform.rotate(pwimg_r, l)
            h = 0
        elif m > c2 and m <= c2 * 2:
            rot = pygame.transform.rotate(pwimg_rf, l)
            h = -2
        apos = (x - rot.get_rect().width / 2 + 57 + h, y - rot.get_rect().height / 2 + 35)
        if n <= c or moving == False:
            screen.blit(pimg_r, (int(x), int(y)))
            player_img = pimg_r
        elif n > c and n <= c * 2:
            screen.blit(pimg_r1, (int(x), int(y)))
            player_img = pimg_r1
        screen.blit(rot, (int(apos[0]), int(apos[1])))
        ang = l


def guard(guard_sprite, x, y, c2=10):
    global o, guard_shots, player_health, app_guard_x, app_guard_y, guard_img, enemy_list
    a, b = (player_x, player_y)
    r = math.atan2((b - y), (a - x))
    l = 360 - (r * 57.2958)
    dist = math.sqrt((player_x - x) ** 2 + (player_y - x) ** 2)
    if dist <= 750:
        if o == 1:
            shm.play()
            guard_shots += 1
            player_health -= agentgun_damage2
        o += 1
        if o > c2 * 2:
            o = 1
        if l > 360:
            l -= 360
        if l > 75 and l < 105:
            app_guard_x = x
            app_guard_y = y - 27
            if o <= c2:
                h = 0
                x1, y1 = (x, y + h)
                guard_img = gimg_f
            elif o > c2 and o <= c2 * 2:
                h = 2
                x1, y1 = (app_guard_x, app_guard_y + h)
                guard_img = gimg_ff
        else:
            app_guard_x = x
            app_guard_y = y
        if l > 255 and l < 285:
            if o <= c2:
                h = 0
                x1, y1 = (x, y + h)
                guard_img = gimg_b
            elif o > c2 and o <= c2 * 2:
                h = 2
                x1, y1 = (x, y + h)
                guard_img = gimg_bf
        if l >= 105 and l <= 255:
            if o <= c2:
                rot = pygame.transform.rotate(gwimg_l, 180 + l)
                h = 0
            elif o > c2 and o <= c2 * 2:
                rot = pygame.transform.rotate(gwimg_lf, 180 + l)
                h = 2
            apos = (x - rot.get_rect().width / 2 + 75 + h, y - rot.get_rect().height / 2 + 34)
            x1, y1 = (x, y)
            guard_img = gimg_l
            screen.blit(rot, (int(apos[0]), int(apos[1])))
        if (l >= 0 and l <= 75) or (l >= 285 and l <= 360):
            if o <= c2:
                rot = pygame.transform.rotate(gwimg_r, l)
                h = 0
            elif o > c2 and o <= c2 * 2:
                rot = pygame.transform.rotate(gwimg_rf, l)
                h = -2
            apos = (x - rot.get_rect().width / 2 + 55 + h, y - rot.get_rect().height / 2 + 34)
            x1, y1 = (x, y)
            guard_img = gimg_r
            screen.blit(rot, (int(apos[0]), int(apos[1])))
    else:
        l = 0
        rot = pygame.transform.rotate((gwimg_r), l)
        apos = (x - rot.get_rect().width / 2 + 55, y - rot.get_rect().height / 2 + 34)
        x1, y1 = (x, y)
        guard_img = gimg_r
        try:
            screen.blit(rot, (int(apos[0]), int(apos[1])))
        except:
            pass
    guard_sprite.image = guard_img
    guard_sprite.rect = pygame.Rect(x, y, soldier_dx, soldier_dy)


def grenade(img, t, b):
    global player_health
    x, y = t
    dist = math.sqrt((player_x - x) ** 2 + (player_y - y) ** 2)
    if dist <= 100:
        if b == 1:
            player_health -= grenade_damage
            explode_music.play()
            screen.blit(grenade2_img, (int(x - img.get_rect().width / 2), int(y - img.get_rect().height / 2)))
            return True
        elif b > 1:
            screen.blit(grenade2_img, (int(x - img.get_rect().width / 2), int(y - img.get_rect().height / 2)))
            return False
    else:
        if b <= 1:
            screen.blit(img, (int(x), int(y)))
        return False


def grenade_guard(guard_sprite, x, y, c2=2):
    global guard_shots, player_health, grenade_x, grenade_y, guard_img, enemy_list, wpos, rot, spos, \
        rx, ry, grenade_xc, g_acc, g_grenade, gt0, zxcv
    position = pygame.mouse.get_pos()
    a, b = (player_x, player_y)
    r = math.atan2((b - y), (a - x))
    l = 360 - (r * 57.2958)
    dist = math.sqrt((player_x - x + 64) ** 2 + (player_y - y + 50) ** 2)
    if dist <= 750:
        if zxcv == 1:
            gt0 = time.time()
            zxcv += 1
        gt1 = time.time()
        p = gt1 - gt0
        if p >= c2:
            g_grenade.append([r, x + 75, y + 34, 1, grenade_img])
            shm.play()
            guard_shots += 1
            zxcv = 1
        if l > 360:
            l -= 360
        if l >= 90 and l < 270:
            if p <= c2:
                rot = pygame.transform.rotate(grwimg_l, 180 + l)
                h = 0
                apos = (x - rot.get_rect().width / 2 + 65 + h, y - rot.get_rect().height / 2 + 40)
                wpos = apos
            elif p > c2 and p <= c2 * 2:
                rot = pygame.transform.rotate(grwimg_lf, 180 + l)
                h = 2
                apos = (x - rot.get_rect().width / 2 + 65 + h, y - rot.get_rect().height / 2 + 40)
                wpos = apos
            x1, y1 = (x, y)
            guard_img = grimg_l
            rx = 45
            ry = 28
        if (l >= 0 and l < 90) or (l >= 270 and l <= 360):
            if p <= c2:
                rot = pygame.transform.rotate(grwimg_r, l)
                h = 0
            elif p > c2 and p <= c2 * 2:
                rot = pygame.transform.rotate(grwimg_rf, l)
                h = -2
            apos = (x - rot.get_rect().width / 2 + 62 + h, y - rot.get_rect().height / 2 + 40)
            wpos = apos
            x1, y1 = (x, y)
            guard_img = grimg_r
            rx = 95
            ry = 28
        grenade_x += grenade_xc
        grenade_y += grenade_yc
        gr_pos = (grenade_x, grenade_y)
    else:
        l = 0
        rot = pygame.transform.rotate((grwimg_r), l)
        apos = (x - rot.get_rect().width / 2 + 62, y - rot.get_rect().height / 2 + 40)
        wpos = apos
        x1, y1 = (x, y)
        guard_img = grimg_r
        rx = 95
        ry = 28
    guard_sprite.image = guard_img
    guard_sprite.rect = pygame.Rect(x1, y1, soldier_dx, soldier_dy)


def commander(guard_sprite, x, y, c1=10, c2=2):
    global o2, guard_shots, player_health, grenade_x, grenade_y, guard_img, enemy_list, wpos2, rot2, spos, \
        rx, ry, grenade_xc, g_acc, g_grenade, ct0, jklm
    position = pygame.mouse.get_pos()
    a, b = (player_x, player_y)
    r = math.atan2((b - y), (a - x))
    l = 360 - (r * 57.2958)
    dist = math.sqrt((player_x - x + 64) ** 2 + (player_y - y + 64) ** 2)
    if dist <= 750:
        if jklm == 1:
            ct0 = time.time()
            jklm += 1
        ct1 = time.time()
        p = ct1 - ct0
        if p >= c2:
            g_grenade.append([r, x + 75, y + 34, 1, grenade_img])
            shm.play()
            guard_shots += 1
            ct0 = time.time()

        if o2 == 1:
            shm.play()
            guard_shots += 1
            player_health -= agentgun_damage2
        o2 += 1

        if o2 >= c1 * 2:
            o2 = 1

        if l > 360:
            l -= 360
        if l >= 90 and l < 270:
            if o2 <= c1:
                rot2 = pygame.transform.rotate(cwimg_l, 180 + l)
                h = 0
                apos = (x - rot2.get_rect().width / 2 + 65 + h, y - rot2.get_rect().height / 2 + 40)
                wpos2 = apos
            elif o2 > c1 and o2 <= c1 * 2:
                rot2 = pygame.transform.rotate(cwimg_lf, 180 + l)
                h = 2
                apos = (x - rot2.get_rect().width / 2 + 65 + h, y - rot2.get_rect().height / 2 + 40)
                wpos2 = apos
            x1, y1 = (x, y)
            guard_img = cimg_l
            rx = 45
            ry = 28
        if (l >= 0 and l < 90) or (l >= 270 and l <= 360):
            if o2 <= c1:
                rot2 = pygame.transform.rotate(cwimg_r, l)
                h = 0
            elif o2 > c1 and o2 <= c1 * 2:
                rot2 = pygame.transform.rotate(cwimg_rf, l)
                h = -2
            apos = (x - rot2.get_rect().width / 2 + 62 + h, y - rot2.get_rect().height / 2 + 40)
            wpos2 = apos
            x1, y1 = (x, y)
            guard_img = cimg_r
            rx = 95
            ry = 28
    else:
        l = 0
        rot2 = pygame.transform.rotate((cwimg_r), l)
        apos = (x - rot2.get_rect().width / 2 + 62, y - rot2.get_rect().height / 2 + 40)
        wpos2 = apos
        x1, y1 = (x, y)
        guard_img = cimg_r
    guard_sprite.image = guard_img
    guard_sprite.rect = pygame.Rect(x1, y1, soldier_dx, soldier_dy)


def skull_crusher(guard_sprite, x, y, c1=10, c2=2, c3=5):
    global o3, guard_shots, player_health, grenade_x, grenade_y, guard_img, enemy_list, wpos3, rot3, spos, \
        rx, ry, grenade_xc, g_acc, g_grenade, gt0, gt1, zxcv, qwerty, sqlist, st0
    position = pygame.mouse.get_pos()
    xc = 60
    a, b = (player_x, player_y)
    r = math.atan2((b - y), (a - x))
    l = 360 - (r * 57.2958)
    dist = math.sqrt((player_x - x) ** 2 + (player_y - x) ** 2)
    if dist <= 950:
        if zxcv == 1:
            gt0 = time.time()
            zxcv += 1
        gt1 = time.time()
        p = gt1 - gt0

        o3 += 1
        if o3 >= c1 * 2:
            o3 = 1
        if l > 360:
            l -= 360

        if p >= c3 and p < c3 * 2:
            if qwerty == 1:
                st0 = time.time()
                qwerty += 1
            st1 = time.time()
            p2 = st1 - st0
            if p2 >= c2:
                g_grenade.append(
                    [r, x + xc - missile_img.get_rect().width / 2, y + 44 - missile_img.get_rect().height / 2, 1,
                     missile_img])
                shm.play()
                guard_shots += 1
                st0 = time.time()
            if l >= 90 and l < 270:
                xc = 60
                rot3 = pygame.transform.rotate(scwimg_lc, 180 + l)
                h = 0
                apos = (x - rot3.get_rect().width / 2 + 60 + h, y - rot3.get_rect().height / 2 + 44)
                wpos3 = apos
                guard_img = scimg_l
            if (l >= 0 and l < 90) or (l >= 270 and l <= 360):
                xc = 67
                rot3 = pygame.transform.rotate(scwimg_rc, l)
                h = 0
                apos = (x - rot3.get_rect().width / 2 + 67 + h, y - rot3.get_rect().height / 2 + 44)
                wpos3 = apos
                guard_img = scimg_r
        if p < c3 or p >= c3 * 2:
            if o3 == 1:
                shm.play()
                guard_shots += 1
                if player_x <= 465:
                    if player_y <= 443 - player_dy or player_y >= 605:
                        player_health -= 0
                    else:
                        player_health -= minigun_damage
                else:
                    player_health -= minigun_damage

            if l >= 90 and l < 270:
                xc = 60
                if o3 <= c1:
                    rot3 = pygame.transform.rotate(scwimg_l, 180 + l)
                    h = 0
                    apos = (x - rot3.get_rect().width / 2 + 60 + h, y - rot3.get_rect().height / 2 + 44)
                    wpos3 = apos
                elif o3 > c1 and o3 <= c1 * 2:
                    rot3 = pygame.transform.rotate(scwimg_lf, 180 + l)
                    h = 2
                    apos = (x - rot3.get_rect().width / 2 + 60 + h, y - rot3.get_rect().height / 2 + 44)
                    wpos3 = apos
                x1, y1 = (x, y)
                guard_img = scimg_l
                rx = 45
                ry = 28
            if (l >= 0 and l < 90) or (l >= 270 and l <= 360):
                xc = 67
                if o3 <= c1:
                    rot3 = pygame.transform.rotate(scwimg_r, l)
                    h = 0
                elif o3 > c1 and o3 <= c1 * 2:
                    rot3 = pygame.transform.rotate(scwimg_rf, l)
                    h = -2
                apos = (x - rot3.get_rect().width / 2 + 67 + h, y - rot3.get_rect().height / 2 + 44)
                wpos3 = apos
                x1, y1 = (x, y)
                guard_img = scimg_r
                rx = 95
                ry = 28
            if p >= c3 * 2:
                gt0 = time.time()
    else:
        rot3 = pygame.transform.rotate(scwimg_l, 180 + l)
        h = 0
        apos = (x - rot3.get_rect().width / 2 + 60 + h, y - rot3.get_rect().height / 2 + 44)
        wpos3 = apos
        guard_img = scimg_l
    guard_sprite.image = guard_img
    guard_sprite.rect = pygame.Rect(x, y, soldier_dx, soldier_dy)


def tguard(guard_sprite, x, y, c2=10):
    global o, guard_shots, player_health, app_guard_x, app_guard_y, guard_img, enemy_list
    a, b = (player_x, player_y)
    r = math.atan2((b - y), (a - x))
    l = 360 - (r * 57.2958)
    dist = math.sqrt((player_x - x) ** 2 + (player_y - x) ** 2)
    if dist <= 750:
        if l > 360:
            l -= 360
        if o == 1 and l >= 105 and l <= 250:
            shm.play()
            guard_shots += 1
            player_health -= agentgun_damage2
        o += 1
        if o > c2 * 2:
            o = 1
        if l <= 135:
            l = 135
        if l >= 225:
            l = 225
        if l >= 135 and l <= 225:
            if o <= c2:
                rot = pygame.transform.rotate(twimg_l, 180 + l)
                h = 0
            elif o > c2 and o <= c2 * 2:
                rot = pygame.transform.rotate(twimg_lf, 180 + l)
                h = -2
            apos = (x - rot.get_rect().width / 2 + 75 + h, y - rot.get_rect().height / 2 + 34)
            x1, y1 = (x, y)
            guard_img = timg_l
            screen.blit(rot, (int(apos[0]), int(apos[1])))
    else:
        l = 0
        rot = pygame.transform.rotate((twimg_l), l)
        apos = (x - rot.get_rect().width / 2 + 75, y - rot.get_rect().height / 2 + 34)
        x1, y1 = (x, y)
        guard_img = timg_l
        screen.blit(rot, (int(apos[0]), int(apos[1])))
    guard_sprite.image = guard_img
    guard_sprite.rect = pygame.Rect(x, y, soldier_dx, soldier_dy)


def bg(x, y):
    try:
        screen.blit(bgimg, (int(x), int(y)))
    except:
        pass


def pointer():
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    screen.blit(point_img, (int(x) - 32, int(y) - 32))


def game_over():
    global go, asdf, t0, score_value, myrecords
    bgm.stop()
    intro_music.stop()
    time.sleep(2)
    if asdf == 1:
        t0 = time.time()
    screen.fill((arcade.color.BLACK))
    screen.blit(goimg, (100, -100))
    go_music.play()
    score(int(sc_wd / 2), int(sc_ht / 2) + 100)
    try:
        with open((os.path.join(filepath, 'score1.dat')), 'rb') as file:
            score2 = pickle.load(file)
    except:
        score2 = 0
    if score_value > score2:
        score2 = score_value
    highscore = font.render('Highscore: ' + str(score2), True, arcade.color.WHITE)
    screen.blit(highscore, (int(sc_wd / 2), int(sc_ht / 2) + 150))
    asdf += 1
    t1 = time.time()
    if t1 - t0 >= 2:
        go = True
    pygame.display.update()


def lvl_complete():
    global go, asdf, t0, score_value
    bgm.stop()
    intro_music.stop()
    time.sleep(2)
    if asdf == 1:
        t0 = time.time()
    screen.fill((arcade.color.BLACK))
    screen.blit(lvlimg, (0, -94))
    lvl_music.play()
    score(int(sc_wd / 2), int(sc_ht / 2) + 200)
    try:
        with open((os.path.join(filepath, 'score1.dat')), 'rb') as file:
            score2 = pickle.load(file)
    except:
        score2 = 0
    if score_value > score2:
        score2 = score_value
    highscore = font.render('Highscore: ' + str(score2), True, arcade.color.WHITE)
    screen.blit(highscore, (int(sc_wd / 2), int(sc_ht / 2) + 250))
    asdf += 1
    t1 = time.time()
    if t1 - t0 >= 5:
        go = True
    pygame.display.update()
    with open((os.path.join(filepath, 'score1.dat')), 'wb') as file:
        pickle.dump(score2, file)


def health_bar(x, y):
    global player_health
    screen.blit(health_bg, (int(x), int(y)))
    per = (player_health / 100) * 100
    w = ((per / 100) * 320)
    if w <= 0:
        w = o
    scale = pygame.transform.scale(health_high, (int(w), 23))
    screen.blit(scale, (int(x), int(y)))
    if player_health >= 100:
        player_health = 100
    if player_health < 60:
        scale = pygame.transform.scale(health_med, (int(w), 23))
        screen.blit(scale, (int(x), int(y)))
    if player_health < 30:
        scale = pygame.transform.scale(health_low, (int(w), 23))
        screen.blit(scale, (int(x), int(y)))


def g_healthbar(x, y, h):
    scale1 = pygame.transform.scale(health_bg, (139, 10))
    screen.blit(scale1, (int(x), int(y)))
    per = (h / 40) * 100
    w = ((per / 100) * 139)
    if w <= 0:
        w = o
    scale = pygame.transform.scale(health_high, (int(w), 10))
    screen.blit(scale, (int(x), int(y)))
    if h >= 40:
        h = 40
    if h < 20:
        scale = pygame.transform.scale(health_med, (int(w), 10))
        screen.blit(scale, (int(x), int(y)))
    if h < 10:
        scale = pygame.transform.scale(health_low, (int(w), 10))
        screen.blit(scale, (int(x), int(y)))


def sc_healthbar(x, y):
    global sc_health
    screen.blit(health_bg, (int(x), int(y)))
    per = (sc_health / 100) * 100
    w = ((per / 100) * 320)
    if w <= 0:
        w = 0
    scale = pygame.transform.scale(sc_health_high, (int(w), 23))
    screen.blit(scale, (int(x), int(y)))
    if sc_health >= 100:
        sc_health = 100
    if sc_health < 60:
        scale = pygame.transform.scale(health_med, (int(w), 23))
        screen.blit(scale, (int(x), int(y)))
    if sc_health < 30:
        scale = pygame.transform.scale(health_low, (int(w), 23))
        screen.blit(scale, (int(x), int(y)))


def pause_screen():
    pygame.mouse.set_visible(True)
    screen.blit(pause_img, (0, 0))
    pygame.display.update()


def score(x, y):
    try:
        score = font.render('Score: ' + str(score_value), True, arcade.color.WHITE)
    except:
        pass
    screen.blit(score, (int(x), int(y)))


# icons
icon = pygame.image.load(os.path.join(filepath, 'icons/logo2.png'))

goimg = pygame.image.load(os.path.join(filepath, 'icons/wasted1.jpg'))
lvlimg = pygame.image.load(os.path.join(filepath, 'icons/complete.jpg'))

pimg_f = pygame.image.load(os.path.join(filepath, 'icons/player_f.png'))
pimg_ff = pygame.image.load(os.path.join(filepath, 'icons/player_ff.png'))
pimg_f1 = pygame.image.load(os.path.join(filepath, 'icons/player_f1.png'))
pimg_ff1 = pygame.image.load(os.path.join(filepath, 'icons/player_ff1.png'))
pimg_b = pygame.image.load(os.path.join(filepath, 'icons/player_b.png'))
pimg_bf = pygame.image.load(os.path.join(filepath, 'icons/player_bf.png'))
pimg_b1 = pygame.image.load(os.path.join(filepath, 'icons/player_b1.png'))
pimg_bf1 = pygame.image.load(os.path.join(filepath, 'icons/player_bf1.png'))
pimg_l = pygame.image.load(os.path.join(filepath, 'icons/player_l.png'))
pimg_l1 = pygame.image.load(os.path.join(filepath, 'icons/player_l1.png'))
pimg_r = pygame.image.load(os.path.join(filepath, 'icons/player_r.png'))
pimg_r1 = pygame.image.load(os.path.join(filepath, 'icons/player_r1.png'))
pwimg_r = pygame.image.load(os.path.join(filepath, 'icons/agent-gun_r.png'))
pwimg_rf = pygame.image.load(os.path.join(filepath, 'icons/agent-gun_rf.png'))
pwimg_l = pygame.image.load(os.path.join(filepath, 'icons/agent-gun_l.png'))
pwimg_lf = pygame.image.load(os.path.join(filepath, 'icons/agent-gun_lf.png'))

grenade_img = pygame.image.load(os.path.join(filepath, 'icons/grenade.png'))
missile_img = pygame.image.load(os.path.join(filepath, 'icons/missile.png'))
grenade2_img = pygame.image.load(os.path.join(filepath, 'icons/grenade2.png'))
esc_img = pygame.image.load(os.path.join(filepath, 'icons/paused.jpg'))

guard_x = int()
guard_y = int()
guard_xc = guard_yc = 0
gimg_f = pygame.image.load(os.path.join(filepath, 'icons/guard_f.png'))
gimg_ff = pygame.image.load(os.path.join(filepath, 'icons/guard_ff.png'))
gimg_b = pygame.image.load(os.path.join(filepath, 'icons/guard_b.png'))
gimg_bf = pygame.image.load(os.path.join(filepath, 'icons/guard_bf.png'))
gimg_r = pygame.image.load(os.path.join(filepath, 'icons/guard_r.png'))
gimg_l = pygame.image.load(os.path.join(filepath, 'icons/guard_l.png'))
gwimg_l = pygame.image.load(os.path.join(filepath, 'icons/guard-gun_l.png'))
gwimg_lf = pygame.image.load(os.path.join(filepath, 'icons/guard-gun_lf.png'))
gwimg_r = pygame.image.load(os.path.join(filepath, 'icons/guard-gun_r.png'))
gwimg_rf = pygame.image.load(os.path.join(filepath, 'icons/guard-gun_rf.png'))
guard_img = pygame.Surface

grguard_x = int()
grguard_y = int()
grguard_xc = grguard_yc = 0
grimg_r = pygame.image.load(os.path.join(filepath, 'icons/gr-guard_r.png'))
grimg_l = pygame.image.load(os.path.join(filepath, 'icons/gr-guard_l.png'))
grwimg_l = pygame.image.load(os.path.join(filepath, 'icons/grguard-gun_l.png'))
grwimg_r = pygame.image.load(os.path.join(filepath, 'icons/grguard-gun_r.png'))
grwimg_rf = pygame.image.load(os.path.join(filepath, 'icons/grguard-gun_r.png'))
grwimg_lf = pygame.image.load(os.path.join(filepath, 'icons/grguard-gun_l.png'))
grguard_img = pygame.Surface

cimg_r = pygame.image.load(os.path.join(filepath, 'icons/com_r.png'))
cimg_l = pygame.image.load(os.path.join(filepath, 'icons/com_l.png'))
cwimg_l = pygame.image.load(os.path.join(filepath, 'icons/com-gun_l.png'))
cwimg_r = pygame.image.load(os.path.join(filepath, 'icons/com-gun_r.png'))
cwimg_rf = pygame.image.load(os.path.join(filepath, 'icons/com-gun_rf.png'))
cwimg_lf = pygame.image.load(os.path.join(filepath, 'icons/com-gun_lf.png'))

scimg_r = pygame.image.load(os.path.join(filepath, 'icons/mando2_r.png'))
scimg_l = pygame.image.load(os.path.join(filepath, 'icons/mando2_l.png'))
scwimg_l = pygame.image.load(os.path.join(filepath, 'icons/minigun_l.png'))
scwimg_r = pygame.image.load(os.path.join(filepath, 'icons/minigun_r.png'))
scwimg_lf = pygame.image.load(os.path.join(filepath, 'icons/minigun_lf.png'))
scwimg_rf = pygame.image.load(os.path.join(filepath, 'icons/minigun_rf.png'))
scwimg_lc = pygame.image.load(os.path.join(filepath, 'icons/minigun_lc.png'))
scwimg_rc = pygame.image.load(os.path.join(filepath, 'icons/minigun_rc.png'))

pause_img = pygame.image.load(os.path.join(filepath, 'icons/paused.jpg'))
timg_l = pygame.image.load(os.path.join(filepath, 'icons/turret_l.png'))
twimg_l = pygame.image.load(os.path.join(filepath, 'icons/turret-gun_l.png'))
twimg_lf = pygame.image.load(os.path.join(filepath, 'icons/turret-gun_lf.png'))

bgimg = pygame.image.load(os.path.join(filepath, 'icons/bg.png'))

point_img = pygame.image.load(os.path.join(filepath, 'icons/pointer.png'))

health_bg = pygame.image.load(os.path.join(filepath, 'icons/health-bg.png'))
health_high = pygame.image.load(os.path.join(filepath, 'icons/health-high.png'))
sc_health_high = pygame.image.load(os.path.join(filepath, 'icons/sc_health-high.png'))
health_med = pygame.image.load(os.path.join(filepath, 'icons/health-med.png'))
health_low = pygame.image.load(os.path.join(filepath, 'icons/health-low.png'))

# music
bgm = pygame.mixer.Sound(os.path.join(filepath, 'music/gt.wav'))
shm = pygame.mixer.Sound(os.path.join(filepath, 'music/shot3.wav'))
go_music = pygame.mixer.Sound(os.path.join(filepath, 'music/wasted-music.wav'))
explode_music = pygame.mixer.Sound(os.path.join(filepath, 'music/explosion.wav'))
lvl_music = pygame.mixer.Sound(os.path.join(filepath, 'music/lvl-complete.wav'))
intro_music = pygame.mixer.Sound(os.path.join(filepath, 'music/pvz.wav'))

sc_wd = 1500
sc_ht = 750

pstart_pos = [300, int(sc_ht / 2)]
right = False
left = False
player_range = 500
player_dy = 128
player_dx = 128
player_x = pstart_pos[0]
player_y = pstart_pos[1]
player_yc = player_xc = 0
player_img = pimg_r
player_health = 100
player_shots = 0
weapon = 'gun'
ammo = 10

go = False
soldier_dx = 128
soldier_dy = 128
guard_health = 40
grguard_health = 40
sc_health = 100
n = 1
m = 1
g = False
fire = False

rot = pygame.Surface
rot2 = pygame.Surface
rot3 = pygame.Surface

wpos = tuple()
wpos2 = tuple()
wpos3 = tuple()
spos = tuple()

grenade_x = int()
grenade_y = int()
grenade_xs = grenade_ys = 5
grenade_xc = grenade_yc = 0
g_grenade = []
g_missile = []

pause_value = 0
pause_list = [False, True]
pause = False

estart_pos = [[911, 508], [2308, 290], [3055, 291], [3765, 530], [4318, 388], [4662, 284], [5164, 533],
              [5810, 286], [6336, 440], [6810, 295], [7644, 414]]

loc = [[911, 508], [2308, 290], [3055, 291], [3765, 530], [4318, 388], [4662, 284], [5164, 533],
       [5810, 286], [6336, 440], [6810, 295], [7644, 414]]

guard_shots = 0
o = 1
o2 = 1
o3 = 1
bullet = False

agentgun_damage = 10
agentgun_damage2 = 5
minigun_damage = 10
grenade_damage = 20

bg_x = 0
bg_y = 0
bg_yc = bg_xc = 0
bg_ht = 664
bg_wd = 8120

running = True
boss = False

asdf = 1
zxcv = 1
jklm = 1
qwerty = 1
go = False
t0 = float()
gt0 = float()
ct0 = float()
st0 = float()

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
score_x = 10
score_y = 10

font2 = pygame.font.Font('freesansbold.ttf', 24)

# enemy_list=[['Type', [x,y], health]]
enemy_list = []
g_spritelist = []

for i in range(11):
    if i in [10]:
        j = ['grguard', loc[i], guard_health]
        enemy_list.append(j)
        g_sprite = pygame.sprite.Sprite
        g_sprite.image = grimg_r
        g_sprite.rect = pygame.Rect(j[1][0], j[1][1], soldier_dx, soldier_dy)
        g_spritelist.append(g_sprite)
    else:
        j = ['guard', loc[i], guard_health]
        enemy_list.append(j)
        g_sprite = pygame.sprite.Sprite
        g_sprite.image = gimg_r
        g_sprite.rect = pygame.Rect(j[1][0], j[1][1], soldier_dx, soldier_dy)
        g_spritelist.append(g_sprite)

# create screen
screen = pygame.display.set_mode((sc_wd, sc_ht), pygame.RESIZABLE)

# title &bg
pygame.display.set_caption('SUPER DUPER GAME')
pygame.display.set_icon(icon)
bgm.play(-1)
while running:
    screen.fill((arcade.color.BLACK))
    if player_health <= 0:
        game_over()
        if go == True:
            pygame.quit()
            running = False
        continue
    if enemy_list == []:
        lvl_complete()
        if go == True:
            pygame.quit()
            running = False
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_value += 1
                if pause_value > 1:
                    pause_value = 0
                pause = pause_list[pause_value]
                if pause:
                    bgm.stop()
                    intro_music.play()
                else:
                    intro_music.stop()
                    bgm.play()
            if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                pygame.quit()
                running = False
            if event.key == pygame.K_w:
                g = True
                player_yc = -10
            if event.key == pygame.K_s:
                g = True
                player_yc = 10
            if event.key == pygame.K_a:
                left = True
                g = True
                if bg_x <= sc_wd - bg_wd and player_x >= pstart_pos[0]:
                    player_xc = -10
                    bg_xc = 0
                    guard_xc = 0
                    grenade_xc = 0
                if player_x <= pstart_pos[0]:
                    bg_xc = 10
                    guard_xc = 10
                    grenade_xc = 1
            if event.key == pygame.K_d:
                right = True
                g = True
                if bg_x <= sc_wd - bg_wd and player_x >= pstart_pos[0]:
                    player_xc = 10
                    bg_xc = 0
                    guard_xc = 0
                    grenade_xc = 0
                if player_x <= pstart_pos[0] and bg_x <= 0:
                    bg_xc = -10
                    guard_xc = -10
                    grenade_xc = -1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                fire = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                g = False
                player_yc = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                right = False
                left = False
                g = False
                player_xc = 0
                bg_xc = 0
                guard_xc = 0
                grenade_xc = 0
        if event.type == pygame.MOUSEBUTTONUP:
            fire = False
        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
            sc_wd = event.w
            sc_ht = event.h
            screen = pygame.display.set_mode((sc_wd, sc_ht), pygame.RESIZABLE)

    if running == False:
        pygame.mixer.quit()
        pygame.quit()
        break

    if pause:
        try:
            screen.blit(pause_img, (0, 0))
            pygame.display.update()
        except:
            pass
        continue
    bg_x += bg_xc
    if bg_x >= 0:
        bg_x = 0
        grenade_xc = 0
    elif bg_x <= sc_wd - bg_wd:
        bg_x = sc_wd - bg_wd
        grenade_xc = 0

    bg(bg_x, bg_y)
    # killing enemies
    for i in enemy_list:
        index = enemy_list.index(i)
        i[1][0] += guard_xc
        if i[1][0] >= estart_pos[index][0]:
            i[1][0] = estart_pos[index][0]
        elif i[1][0] <= sc_wd - bg_wd + estart_pos[index][0]:
            i[1][0] = sc_wd - bg_wd + estart_pos[index][0]
        sprite = g_spritelist[index]
        if i[0] == 'guard':
            guard(sprite, i[1][0], i[1][1], 10)
        if i[0] == 'tguard':
            tguard(sprite, i[1][0], i[1][1], 3)
        if i[0] == 'com':
            commander(sprite, i[1][0], i[1][1], 10, 2)
        if i[0] == 'crusher':
            skull_crusher(sprite, i[1][0], i[1][1], 4, 2.4)
        if i[0] == 'grguard':
            grenade_guard(sprite, i[1][0], i[1][1], 2)
        # grenades
        for gr in g_grenade:
            index = g_grenade.index(gr)
            velx = math.cos(gr[0]) * grenade_xs
            vely = math.sin(gr[0]) * grenade_ys
            gr[1] += velx
            gr[1] += grenade_xc
            gr[2] += vely
            grenade1 = pygame.transform.rotate(gr[4], 360 - gr[0] * 57.29)
            blast = grenade(grenade1, (gr[1], gr[2]), gr[3])
            if blast:
                gr[3] += 1
        mouse_x, mouse_y = pygame.mouse.get_pos()
        point_sprite = pygame.sprite.Sprite()
        point_sprite.image = point_img
        point_sprite.rect = pygame.Rect(mouse_x, mouse_y, 64, 64)
        screen.blit(guard_img, (int(i[1][0]), int(i[1][1])))
        if i[0] == 'grguard':
            screen.blit(rot, (int(wpos[0]), int(wpos[1])))
        if i[0] == 'com':
            screen.blit(rot2, (int(wpos2[0]), int(wpos2[1])))
        if i[0] == 'crusher':
            screen.blit(rot3, (int(wpos3[0]), int(wpos3[1])))
        if pygame.sprite.collide_rect(point_sprite, sprite) and fire == True:
            if pygame.sprite.collide_mask(point_sprite, sprite):
                if bullet == True and (i[0] != 'com' or weapon == 'gun'):
                    i[2] -= agentgun_damage
                    if i[0] == 'crusher':
                        sc_health -= agentgun_damage
                if i[0] != 'crusher':
                    g_healthbar(i[1][0], i[1][1] - 20, i[2])

        if i[2] <= 0:
            player_health += 20
            index = enemy_list.index(i)
            if i[0] == 'guard':
                score_value += 10
            if i[0] == 'tguard':
                score_value += 30
            if i[0] == 'com':
                score_value += 40
            if i[0] == 'crusher':
                score_value += 100
            if i[0] == 'grguard':
                score_value += 20
            enemy_list.pop(index)
            estart_pos.pop(index)
    # restricting mouse pointer
    [pointer_x, pointer_y] = pygame.mouse.get_pos()
    dist = math.sqrt(((player_x - pointer_x) ** 2) + ((player_y - pointer_y) ** 2))
    if dist >= player_range:
        if pointer_x - player_x < 0:
            vx = -1
        else:
            vx = 1
        if pointer_y - player_y < 0:
            vy = -1
        else:
            vy = 1
        if pointer_x - player_x != 0:
            m = (pointer_y - player_y) / (pointer_x - player_x)
            a, b = player_x, player_y
            d = player_range
            x = (vx * mod(math.sqrt((d ** 2) / (1 + (m ** 2))))) + a
            y = (vy * mod(m * (x - a))) + b
        else:
            x = 0
            y = vy * player_range

        pygame.mouse.set_pos(int(x), int(y))
    player_y += player_yc
    player_x += player_xc
    if player_y <= 300:
        player_y = 300
    elif player_y >= bg_ht - player_dy:
        player_y = bg_ht - player_dy
    if player_x >= sc_wd - 32:
        player_x = sc_wd - 32
    if player_x <= pstart_pos[0]:
        player_x = pstart_pos[0]
    if boss:
        if player_y < 443 or player_y + player_dy > 605:
            if player_x + player_dx / 2 >= 465 and player_x + player_dx / 2 <= 561:
                player_x -= player_xc
            if player_x <= 561 and player_x >= 465:
                player_x -= player_xc
        if player_y >= 315 or player_y <= 605:
            if player_x + player_dx / 2 >= 465 and player_x <= 561:
                player_y -= player_yc
        if player_x <= 465:
            if player_y >= 443 and player_y <= 605:
                agentgun_damage = 10
            else:
                agentgun_damage = 0
        sc_healthbar(1495 - 320, 60)
    # following mouse pointer
    # direction of player

    player(player_x, player_y, 10, g, fire, ammo)
    score(score_x, score_y)
    health_bar(5, 60)

    pointer()
    # after every change in display we have to update
    pygame.display.update()

import launcher
import importlib

importlib.reload(launcher)
