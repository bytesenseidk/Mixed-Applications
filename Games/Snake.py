import random
import curses

def main(stdscr):
    # Setup
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()
    window = curses.newwin(height, width, 0, 0)
    window.keypad(1)
    window.timeout(100)

    # Initial snake position
    snake_x = width // 4
    snake_y = height // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    # Initial food position
    food = [height // 2, width // 2]
    window.addch(food[0], food[1], curses.ACS_PI)

    # Initial direction and score
    key = curses.KEY_RIGHT
    score = 0

    # Direction map for reverse direction detection
    opposite_directions = {
        curses.KEY_UP: curses.KEY_DOWN,
        curses.KEY_DOWN: curses.KEY_UP,
        curses.KEY_LEFT: curses.KEY_RIGHT,
        curses.KEY_RIGHT: curses.KEY_LEFT,
    }

    while True:
        # Display the score
        window.addstr(0, 2, f"Score: {score} ")

        # Get user input
        next_key = window.getch()
        # Ignore reverse direction
        if next_key != -1 and next_key != opposite_directions.get(key, None):
            key = next_key

        # Calculate new head position
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Check for collisions
        if (
            new_head[0] in [0, height] or  # Collides with top/bottom border
            new_head[1] in [0, width] or   # Collides with left/right border
            new_head in snake              # Collides with itself
        ):
            break

        # Insert new head to the snake
        snake.insert(0, new_head)

        # Check if the snake eats the food
        if snake[0] == food:
            score += 10  # Increase score
            food = None
            while food is None:
                new_food = [
                    random.randint(1, height - 2),
                    random.randint(1, width - 2)
                ]
                food = new_food if new_food not in snake else None
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            # Remove the tail piece if no food is eaten
            tail = snake.pop()
            window.addch(int(tail[0]), int(tail[1]), ' ')

        # Render the snake
        window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

# Run the game
curses.wrapper(main)
