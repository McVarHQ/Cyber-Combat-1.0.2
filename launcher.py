import pygame, time, importlib, pickle, os, os.path, cv2
from pygame import mixer
from tkinter import *
from tkinter.ttk import *
from tkinter import Button

# initialize
pygame.init()
pygame.mixer.init()
filepath = os.path.dirname(__file__)
img = pygame.image.load(os.path.join(filepath, r'icons\cr.png'))
audio = pygame.mixer.Sound(os.path.join(filepath, 'music/intro-audio.wav'))
bgm = pygame.mixer.Sound(os.path.join(filepath, 'music/gt.wav'))
intro_music = pygame.mixer.Sound(os.path.join(filepath, 'music/pvz.wav'))

def title():
    filepath = os.path.dirname(__file__)
    audio = pygame.mixer.Sound(os.path.join(filepath, 'music\intro-audio.wav'))
    cap = cv2.VideoCapture(os.path.join(filepath, 'icons\game-title2.mp4'))
    audio.play()
    while (cap.isOpened()):
        t1 = time.time()
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('CYBER COMBAT', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                audio.stop()
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()



def game_intro():
    l_root = Tk()
    load = Progressbar(l_root, orient=HORIZONTAL, length=500, mode='determinate')
    l_root.geometry('1920x1080')
    l_root.configure(background='black')
    intro_music.play()

    def controls():
        running = True
        screen = pygame.display.set_mode((1500, 750), pygame.RESIZABLE)
        pygame.display.set_caption('INSTRUCTIONS')
        img = pygame.image.load(os.path.join(filepath, 'icons/ins.png'))
        while running:
            screen.blit(img, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.init()
                    intro_music.play()
                    running = False

    def copyrights():
        running = True

        screen = pygame.display.set_mode((1500, 750), pygame.RESIZABLE)
        pygame.display.set_caption('COPYRIGHTS')
        img = pygame.image.load(os.path.join(filepath, 'icons/cr.png'))
        while running:
            screen.blit(img, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.init()
                    intro_music.play()
                    running = False

    def close():
        l_root.destroy

    def levels():
        pygame.init()
        pygame.mixer.init()
        intro_music.stop()

        def close_levels():
            sts.destroy

        def level1():
            sts.destroy()
            import level1
            importlib.reload(level1)

        def level2():
            import level2

            importlib.reload(level2)

        def level3():
            import level3

            importlib.reload(level3)

        def level4():
            import level4

            importlib.reload(level4)

        def level5():
            import level5

            importlib.reload(level5)

        def level6():
            import level6

            importlib.reload(level6)

        sts = Tk()
        sts.geometry('1920x1080')
        sts.configure(background='black')
        b1 = Button(sts, text='LEVEL-1', command=level1, padx=93, pady=20, bg='GREEN', activebackground='white')
        try:
            with open((os.path.join(filepath, 'score1.dat')), 'rb') as file:
                hs = pickle.load(file)
        except:
            hs = 0

        if hs >= 120:
            b2 = Button(sts, text='LEVEL-2', command=level2, padx=93, pady=20, bg='GREEN', activebackground='white')
        else:
            b2 = Button(sts, text='LEVEL-2', command=level2, padx=93, pady=20, bg='YELLOW', activebackground='white',
                        state=DISABLED)
        try:
            with open((os.path.join(filepath, 'score2.dat')), 'rb') as file:
                hs = pickle.load(file)
        except:
            hs = 0
        if hs >= 140:
            b3 = Button(sts, text='LEVEL-3', command=level3, padx=93, pady=20, bg='GREEN', activebackground='white')
        else:
            b3 = Button(sts, text='LEVEL-3', command=level3, padx=93, pady=20, bg='YELLOW', activebackground='white',
                        state=DISABLED)

        try:
            with open((os.path.join(filepath, 'score3.dat')), 'rb') as file:
                hs = pickle.load(file)
        except:
            hs = 0
        if hs >= 180:
            b4 = Button(sts, text='LEVEL-4', command=level4, padx=93, pady=20, bg='GREEN', activebackground='white')
        else:
            b4 = Button(sts, text='LEVEL-4', command=level4, padx=93, pady=20, bg='YELLOW', activebackground='white',
                        state=DISABLED)

        try:
            with open((os.path.join(filepath, 'score4.dat')), 'rb') as file:
                hs = pickle.load(file)
        except:
            hs = 0
        if hs >= 200:
            b5 = Button(sts, text='LEVEL-5', command=level5, padx=93, pady=20, bg='GREEN', activebackground='white')
        else:
            b5 = Button(sts, text='LEVEL-5', command=level5, padx=93, pady=20, bg='YELLOW', activebackground='white',
                        state=DISABLED)

        try:
            with open((os.path.join(filepath, 'score5.dat')), 'rb') as file:
                hs = pickle.load(file)
        except:
            hs = 0
        if hs >= 250:
            b6 = Button(sts, text='LEVEL-6', command=level6, padx=93, pady=20, bg='GREEN', activebackground='white')
        else:
            b6 = Button(sts, text='LEVEL-6', command=level6, padx=93, pady=20, bg='YELLOW', activebackground='white',
                        state=DISABLED)
        b1.pack(pady=10)
        b2.pack(pady=10)
        b3.pack(pady=10)
        b4.pack(pady=10)
        b5.pack(pady=10)
        b6.pack(pady=10)
        sts.protocol('WM_DESTROY WINDOW', close_levels())
        mainloop()

    def bar():
        load.place(relx=0.5, rely=0.2, anchor=CENTER)
        load['value'] = 50
        l_root.update_idletasks()
        time.sleep(1)
        load['value'] = 100
        l_root.update_idletasks()
        time.sleep(1)
        load['value'] = 150
        l_root.update_idletasks()
        time.sleep(1)
        load['value'] = 200
        l_root.update_idletasks()
        time.sleep(1)
        load['value'] = 250
        l_root.update_idletasks()
        time.sleep(1)
        load['value'] = 300
        l_root.update_idletasks()
        time.sleep(1)
        load['value'] = 350
        l_root.update_idletasks()
        time.sleep(1)
        load['value'] = 400
        l_root.update_idletasks()
        time.sleep(1)
        load['value'] = 450
        l_root.update_idletasks()
        time.sleep(1)
        load['value'] = 500
        l_root.update_idletasks()
        l_root.destroy()
        intro_music.stop()
        levels()

    def new():
        try:
            f = open((os.path.join(filepath, 'admin.txt')), 'r')
            r = f.read()
        except:
            r = 'player'
        if r in ['maintanance-Raki7766', 'maintanance-Kd664', 'maintanance-McVar69420']:
            hs = 500
        else:
            hs = 0
        with open((os.path.join(filepath, 'score1.dat')), 'wb') as file1:
            pickle.dump(hs, file1)
        with open((os.path.join(filepath, 'score2.dat')), 'wb') as file2:
            pickle.dump(hs, file2)
        with open((os.path.join(filepath, 'score3.dat')), 'wb') as file3:
            pickle.dump(hs, file3)
        with open((os.path.join(filepath, 'score4.dat')), 'wb') as file4:
            pickle.dump(hs, file4)
        with open((os.path.join(filepath, 'score5.dat')), 'wb') as file5:
            pickle.dump(hs, file5)
        with open((os.path.join(filepath, 'score6.dat')), 'wb') as file6:
            pickle.dump(hs, file6)
        bar()

    def quit():
        sys.exit()

    b1 = Button(l_root, text="CONTINUE", command=bar, padx=75, pady=20, bg='WHITE', activebackground='yellow',
                relief=RAISED)
    b2 = Button(l_root, text='QUIT', command=quit, padx=93, pady=20, bg='BLACK', fg='WHITE', activebackground='yellow',
                relief=RAISED)
    b3 = Button(l_root, text='CONTROLS', command=controls, padx=65, pady=20, bg='WHITE',
                activebackground='yellow', relief=RAISED)
    b4 = Button(l_root, text='COPYRIGHTS', command=copyrights, padx=71, pady=20, bg='WHITE', activebackground='yellow',
                relief=RAISED)
    b5 = Button(l_root, text='ALMANAC', command=almanac, padx=85, pady=20, bg='BLACK', fg='WHITE',
                activebackground='yellow', relief=RAISED)
    b6 = Button(l_root, text="NEW GAME", command=new, padx=75, pady=20, bg='BLACK', fg='WHITE',
                activebackground='yellow', relief=RAISED)

    b1.place(relx=0.4, rely=0.3, anchor=CENTER)
    b2.place(relx=0.4, rely=0.4, anchor=CENTER)
    b3.place(relx=0.6, rely=0.4, anchor=CENTER)
    b4.place(relx=0.4, rely=0.5, anchor=CENTER)
    b5.place(relx=0.6, rely=0.5, anchor=CENTER)
    b6.place(relx=0.6, rely=0.3, anchor=CENTER)
    l_root.protocol('WM_DELETE_WINDOW', close())

    mainloop()


def almanac():
    def jacob():
        running = True
        screen = pygame.display.set_mode((1500, 750), pygame.RESIZABLE)
        pygame.display.set_caption('JACOB')
        img = pygame.image.load(os.path.join(filepath, 'icons/character.png'))
        while running:
            screen.blit(img, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.init()
                    intro_music.play()
                    running = False

    def guard():
        running = True

        screen = pygame.display.set_mode((1500, 750), pygame.RESIZABLE)
        pygame.display.set_caption('GUARD')
        img = pygame.image.load(os.path.join(filepath, 'icons/enemy_1.png'))
        while running:
            screen.blit(img, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.init()
                    intro_music.play()
                    running = False

    def grenade_guard():
        running = True

        screen = pygame.display.set_mode((1500, 750), pygame.RESIZABLE)
        pygame.display.set_caption('GRENADE GUARD')
        img = pygame.image.load(os.path.join(filepath, 'icons/enemy_2.png'))
        while running:
            screen.blit(img, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.init()
                    intro_music.play()
                    running = False

    def auto_turret():
        running = True

        screen = pygame.display.set_mode((1500, 750), pygame.RESIZABLE)
        pygame.display.set_caption('AUTO TURRET')
        img = pygame.image.load(os.path.join(filepath, 'icons/enemy_3.png'))
        while running:
            screen.blit(img, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.init()
                    intro_music.play()
                    running = False

    def commander():
        running = True

        screen = pygame.display.set_mode((1500, 750), pygame.RESIZABLE)
        pygame.display.set_caption('COMMANDER')
        img = pygame.image.load(os.path.join(filepath, 'icons/enemy_4.png'))
        while running:
            screen.blit(img, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.init()
                    intro_music.play()
                    running = False

    def skull_crusher():
        running = True

        screen = pygame.display.set_mode((1500, 750), pygame.RESIZABLE)
        pygame.display.set_caption('SKULL CRUSHER')
        img = pygame.image.load(os.path.join(filepath, 'icons/enemy_5.png'))
        while running:
            screen.blit(img, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.init()
                    intro_music.play()
                    running = False

    tr = Tk()
    tr.geometry('1920x1080')
    tr.configure(background='black')
    lvl = 1
    try:
        with open((os.path.join(filepath, 'score1.dat')), 'rb') as file:
            hs = pickle.load(file)
    except:
        hs = 0

    if hs >= 120:
        lvl = 2
    try:
        with open((os.path.join(filepath, 'score2.dat')), 'rb') as file:
            hs = pickle.load(file)
    except:
        hs = 0
    if hs >= 140:
        lvl = 3

    try:
        with open((os.path.join(filepath, 'score3.dat')), 'rb') as file:
            hs = pickle.load(file)
    except:
        hs = 0
    if hs >= 180:
        lvl = 4

    try:
        with open((os.path.join(filepath, 'score4.dat')), 'rb') as file:
            hs = pickle.load(file)
    except:
        hs = 0
    if hs >= 200:
        lvl = 5

    try:
        with open((os.path.join(filepath, 'score5.dat')), 'rb') as file:
            hs = pickle.load(file)
    except:
        hs = 0
    if hs >= 250:
        lvl = 6

    if lvl <= 2:
        b1 = Button(tr, text="JACOB", command=jacob, padx=90, pady=20, bg='WHITE', activebackground='yellow',
                    relief=RAISED)
        b2 = Button(tr, text='GUARD', command=guard, padx=90, pady=20, bg='BLACK', fg='WHITE',
                    activebackground='yellow',
                    relief=RAISED)
        b3 = Button(tr, text='GRENADE GUARD', command=grenade_guard, padx=60, pady=20, bg='WHITE',
                    activebackground='yellow', relief=RAISED)
        b1.place(relx=0.5, rely=0.3, anchor=CENTER)
        b2.place(relx=0.4, rely=0.4, anchor=CENTER)
        b3.place(relx=0.6, rely=0.4, anchor=CENTER)

    elif lvl<=4:
        b1 = Button(tr, text="JACOB", command=jacob, padx=90, pady=20, bg='WHITE', activebackground='yellow',
                    relief=RAISED)
        b2 = Button(tr, text='GUARD', command=guard, padx=90, pady=20, bg='BLACK', fg='WHITE',
                    activebackground='yellow',
                    relief=RAISED)
        b3 = Button(tr, text='GRENADE GUARD', command=grenade_guard, padx=60, pady=20, bg='WHITE',
                    activebackground='yellow', relief=RAISED)
        b4 = Button(tr, text='AUTO TURRET', command=auto_turret, padx=71, pady=20, bg='WHITE',
                    activebackground='yellow',
                    relief=RAISED)
        b1.place(relx=0.4, rely=0.3, anchor=CENTER)
        b2.place(relx=0.6, rely=0.3, anchor=CENTER)
        b3.place(relx=0.6, rely=0.4, anchor=CENTER)
        b4.place(relx=0.4, rely=0.4, anchor=CENTER)
    elif lvl<=5:
        b1 = Button(tr, text="JACOB", command=jacob, padx=90, pady=20, bg='WHITE', activebackground='yellow',
                    relief=RAISED)
        b2 = Button(tr, text='GUARD', command=guard, padx=90, pady=20, bg='BLACK', fg='WHITE',
                    activebackground='yellow',
                    relief=RAISED)
        b3 = Button(tr, text='GRENADE GUARD', command=grenade_guard, padx=60, pady=20, bg='WHITE',
                    activebackground='yellow', relief=RAISED)
        b4 = Button(tr, text='AUTO TURRET', command=auto_turret, padx=71, pady=20, bg='WHITE',
                    activebackground='yellow',
                    relief=RAISED)
        b5 = Button(tr, text='COMMANDER', command=commander, padx=70, pady=20, bg='BLACK', fg='WHITE',
                    activebackground='yellow', relief=RAISED)
        b1.place(relx=0.4, rely=0.3, anchor=CENTER)
        b2.place(relx=0.4, rely=0.4, anchor=CENTER)
        b3.place(relx=0.6, rely=0.4, anchor=CENTER)
        b4.place(relx=0.4, rely=0.5, anchor=CENTER)
        b5.place(relx=0.5, rely=0.5, anchor=CENTER)

    elif lvl==6:

        b1 = Button(tr, text="JACOB", command=jacob, padx=90, pady=20, bg='WHITE', activebackground='yellow', relief=RAISED)
        b2 = Button(tr, text='GUARD', command=guard, padx=90, pady=20, bg='BLACK', fg='WHITE', activebackground='yellow',
                    relief=RAISED)
        b3 = Button(tr, text='GRENADE GUARD', command=grenade_guard, padx=60, pady=20, bg='WHITE',
                    activebackground='yellow', relief=RAISED)
        b4 = Button(tr, text='AUTO TURRET', command=auto_turret, padx=71, pady=20, bg='WHITE', activebackground='yellow',
                    relief=RAISED)
        b5 = Button(tr, text='COMMANDER', command=commander, padx=70, pady=20, bg='BLACK', fg='WHITE',
                    activebackground='yellow', relief=RAISED)
        b6 = Button(tr, text='SKULL CRUSHER', command=skull_crusher, padx=67, pady=20, bg='BLACK', fg='WHITE',
                    activebackground='yellow', relief=RAISED)

        b1.place(relx=0.4, rely=0.3, anchor=CENTER)
        b2.place(relx=0.4, rely=0.4, anchor=CENTER)
        b3.place(relx=0.6, rely=0.4, anchor=CENTER)
        b4.place(relx=0.4, rely=0.5, anchor=CENTER)
        b5.place(relx=0.6, rely=0.5, anchor=CENTER)
        b6.place(relx=0.6, rely=0.3, anchor=CENTER)
    mainloop()


ins = '''HELLO
'''

game_value = True
title()
game_intro()
