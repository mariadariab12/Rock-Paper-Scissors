import random

ok = 1
nr_wins = 0

while ok == 1:
    dificultate = input("Nivel de dificultate - usor, mediu, greu: ")
    print("1 = piatra")
    print("2 = hartie")
    print("3 = foarfeca")
    mutare_jucator = int(input("Introduceti un numar de la 1 la 3 : "))

# genereaza ce alege calculatorul
    if dificultate == 'usor':
        mutare_computer = 1
    elif dificultate == 'mediu':
        mutare_computer = random.randint(2, 3)
    else:
        mutare_computer = random.randint(1, 3)

    print(mutare_computer)

    if mutare_jucator == mutare_computer :
        print("Remiza")
        ok = 0
    elif (mutare_jucator == 1 and mutare_computer == 3) or (mutare_jucator == 2 and mutare_computer == 1) or (mutare_jucator == 3 and mutare_computer == 2):
        print("Ai castigat!")
        ok = 1
    else:
        print("Ai pierdut!")
        ok = -1

    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    import pygame

# Inițializarea pygame
    pygame.init()

# Crearea unui obiect de sunet
    sunet_drums = pygame.mixer.Sound('drum.wav')
    sunet_win = pygame.mixer.Sound('win.mp3')
    sunet_lose = pygame.mixer.Sound('lose.flac')

# Citirea imaginilor
    imagine1 = mpimg.imread("rock2.jpg")
    imagine2 = mpimg.imread("carte2.jpg")
    imagine3 = mpimg.imread("ghilotina.jpg")
    img_win = mpimg.imread("winner.jpg")
    img_lose = mpimg.imread("lose.jpg")
    img_win_lose = mpimg.imread("win_lose.jpg")
    img_remiza = mpimg.imread("remiza.jpg")

    if mutare_computer == 1:
        img_comp = imagine1
    elif mutare_computer == 2:
        img_comp = imagine2
    else:
        img_comp = imagine3

    if mutare_jucator == 1:
        img_juc = imagine1
    elif mutare_jucator == 2:
        img_juc = imagine2
    else:
        img_juc = imagine3

# Afișarea imaginilor în ferestre separate
    plt.figure(1)
    plt.subplot(121)  # Subplot pentru prima imagine
    plt.imshow(img_comp)
    plt.title('Computer:')
    plt.axis('off')  # Ascunde axele de pe grafic
    plt.xticks([])   # Ascunde etichetele de pe axa x

    plt.subplot(122)  # Subplot pentru a doua imagine
    plt.imshow(img_juc)
    plt.title('Jucator:')
    plt.axis('off')  # Ascunde axele de pe grafic
    plt.xticks([])   # Ascunde etichetele de pe axa x

# Afișarea ferestrei cu imaginile
    plt.show(block=False)

# Așteaptă 5 secunde
    plt.pause(5)

# Închide fereastra
    plt.close()

# Așteaptă 1 secunda
    plt.pause(1)

# Redarea sunetului
    sunet_drums.play()

# Așteptarea până la încheierea sunetului
    pygame.time.delay(3000)  # Așteaptă 3 secunde (3000 milisecunde)

# Afișarea imaginii
    plt.imshow(img_win_lose)
    plt.axis('off')  # Ascunde axele de pe grafic

# Afișarea ferestrei cu imaginile
    plt.show(block=False)

# Așteaptă 5 secunde
    plt.pause(5)

# Închide fereastra
    plt.close()

# Oprirea sunetului
    sunet_drums.stop()

    if ok == 0:
        img_final = img_remiza
    elif ok == 1:
        img_final = img_win
        sunet_final = sunet_win
        nr_wins += 1
    else:
        img_final = img_lose
        sunet_final = sunet_lose

# Așteaptă 1 secunda
    plt.pause(1)

# Afișarea imaginii
    plt.imshow(img_final)
    plt.axis('off')  # Ascunde axele de pe grafic

# Afișarea ferestrei cu imaginile
    plt.show(block=False)

# Așteaptă 5 secunde
    plt.pause(5)

# Redarea sunetului
    sunet_final.play()

# Așteptarea până la încheierea sunetului
    pygame.time.delay(5000)

# Oprirea sunetului
    sunet_final.stop()

# Închide fereastra
    plt.close()

# Închiderea pygame
    pygame.quit()

    print("Numar meciri castigate: ", nr_wins)

    continua = input("Vrei sa continui? - da/nu: ")
    if continua == 'da':
        ok_cont = 1
    else:
        ok_cont = 0
