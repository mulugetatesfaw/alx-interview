#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    stack = [0]  # Start with the first box (box 0)

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key < n:
                stack.append(key)

    return len(visited) == n

# Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes))  # Output: False

