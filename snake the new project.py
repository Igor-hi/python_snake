import time
import random
from collections import deque
import os

WIDTH = 30
HEIGHT = 15
SPEED = 0.12

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_field(snake, food, score):
    clear()
    field = [['  ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    for i, (x, y) in enumerate(snake):
        if i == 0:
            field[y][x] = '▓▓'
        else:
            field[y][x] = '██'
    
    field[food[1]][food[0]] = '🍎'
    
    print('╔' + '══' * WIDTH + '╗')
    for row in field:
        print('║' + ''.join(row) + '║')
    print('╚' + '══' * WIDTH + '╝')
    
    print(f"\nСчёт: {score}    Управление: WASD / Стрелки    Q — выход")

def main():
    snake = deque([(WIDTH//2, HEIGHT//2)])
    direction = (1, 0)      # начинаем движение вправо
    score = 0
    
    food = (random.randint(2, WIDTH-3), random.randint(2, HEIGHT-3))
    
    time.sleep(0.5)
    
    while True:
        draw_field(snake, food, score)
        
        # === НЕБЛОКИРУЮЩЕЕ чтение клавиш ===
        try:
            import msvcrt
            if msvcrt.kbhit():                      # если нажата клавиша
                key = msvcrt.getch()
                
                if key == b'\xe0':                  # стрелки
                    key = msvcrt.getch()
                    if key == b'H': new_dir = (0, -1)
                    elif key == b'P': new_dir = (0, 1)
                    elif key == b'K': new_dir = (-1, 0)
                    elif key == b'M': new_dir = (1, 0)
                    else: new_dir = direction
                else:
                    k = key.decode('utf-8').lower()
                    dirs = {'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)}
                    new_dir = dirs.get(k, direction)
                
                # запрещаем разворот на 180°
                if (new_dir[0] != -direction[0] or new_dir[1] != -direction[1]):
                    direction = new_dir
                    
        except:
            pass   # на других системах просто продолжаем
        
        # Двигаем змейку
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        new_head = (head_x, head_y)
        
        # Проверка столкновений
        if (head_x < 0 or head_x >= WIDTH or 
            head_y < 0 or head_y >= HEIGHT or 
            new_head in snake):
            print(f"\nИГРА ОКОНЧЕНА! Твой счёт: {score}")
            break
        
        snake.appendleft(new_head)
        
        # Съели еду
        if new_head == food:
            score += 10
            while True:
                food = (random.randint(2, WIDTH-3), random.randint(2, HEIGHT-3))
                if food not in snake:
                    break
        else:
            snake.pop()
        
        time.sleep(SPEED)

if __name__ == "__main__":
    main()
    