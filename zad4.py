def doors(n):
    door = [False] * (n + 1)
    i = j = 1
    while i < len(door):
        while j < len(door):
            door[j] = not door[j]
            j = j + i
        i = i + 1
        j = i
    i = 1
    opened = 0
    while i < len(door):
        if door[i]: opened = opened + 1
        i = i + 1
    return opened

print(doors(5))