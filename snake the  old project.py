import time
import random
from collections import deque

# ===================== НАСТРОЙКИ =====================
WIDTH = 20      # ширина поля
HEIGHT = 10     # высота поля
SPEED = 0.15    # скорость игры (меньше = быстрее)
# ====================================================


directions = {
    'w': (0, -1),   
    's': (0, 1),    
    'a': (-1, 0),   
    'd': (1, 0)     
}

def draw_field(snake, food, score):
    field = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    
    for x, y in snake:
        field[y][x] = '█'
    
    
    field[food[1]][food[0]] = '●'
    
    
    print('═' * (WIDTH * 2 + 2))
    for row in field:
        print('║' + ''.join(row).replace(' ', '  ') + '║')
    print('═' * (WIDTH * 2 + 2))
    print(f' Счёт: {score}   Управление: WASD   (Q — выход)')

def main():
    
    snake = deque([(WIDTH//2, HEIGHT//2)])
    direction = (1, 0)        
    score = 0
    
    
    food = (random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2))
    
    print("=== ИГРА ЗМЕЙКА ===\n")
    
    while True:
        draw_field(snake, food, score)
        
        try:
            import msvcrt
            key = msvcrt.getch().decode('utf-8').lower()
        except ImportError:  
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                key = sys.stdin.read(1).lower()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        if key == 'q':
            print("Игра окончена. Ваш счёт:", score)
            break
        
        
        if key in directions:
            new_dir = directions[key]
            
            if (new_dir[0] != -direction[0] or new_dir[1] != -direction[1]):
                direction = new_dir
        
        
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        new_head = (head_x, head_y)
        
        
        if (head_x < 0 or head_x >= WIDTH or 
            head_y < 0 or head_y >= HEIGHT):
            print(f"\nИГРА ОКОНЧЕНА! Ваш счёт: {score}")
            break
        
        
        if new_head in snake:
            print(f"\nИГРА ОКОНЧЕНА! Ваш счёт: {score}")
            break
        
        
        snake.appendleft(new_head)
        
        
        if new_head == food:
            score += 10
            
            while True:
                food = (random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2))
                if food not in snake:
                    break
        else:
            
            snake.pop()
        
        time.sleep(SPEED)

if __name__ == "__main__":
    main()
    