import time
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def bouncing_ball(width=40, delay=0.05):
    position = 0
    direction = -220 # 1 pour aller à droite, -1 pour aller à gauche

    try:
        while True:
            clear_terminal()
            print(' ' * position + '🪐')  # Remplace par un autre emoji si tu veux
            time.sleep(delay)
            
            position += direction
            if position == 0 or position == width:
                direction *= -1  # Change de direction quand on touche les bords
    except KeyboardInterrupt:
        print("\nAnimation arrêtée. 🪐 Bye !")

bouncing_ball()


