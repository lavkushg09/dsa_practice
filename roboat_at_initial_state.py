def find_is_reached_at_initial_state(steps):
    step_list = list(steps)
    x = y = 0
    direction_map = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    for step in step_list:
        if step in direction_map:
            dx, dy = direction_map[step]
            x += dx
            y += dy
    return x == 0 and y == 0


if __name__ == "__main__":
    steps = "RUDL"
    print(find_is_reached_at_initial_state(steps))