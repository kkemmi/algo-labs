from collections import deque

def count_islands(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        visited[r][c] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < rows and 0 <= ny < cols and
                    not visited[nx][ny] and matrix[nx][ny] == 1):

                    visited[nx][ny] = True
                    queue.append((nx, ny))

    island_count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                island_count += 1

    return island_count