from collections import deque

def bfs(matrix, visited, start, band_char):
    """BFS to identify all cells in the same band"""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    component = []
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y = queue.popleft()
        component.append((x, y))
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix) and not visited[nx][ny]:
                if matrix[nx][ny] == band_char:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    return component

def find_bands_and_overlaps(matrix):
    """Identify bands and overlaps"""
    visited = [[False] * len(matrix) for _ in range(len(matrix))]
    band_1, band_2 = [], []
    overlaps = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "1" and not visited[i][j]:
                band_1.extend(bfs(matrix, visited, (i, j), "1"))
            elif matrix[i][j] == "2" and not visited[i][j]:
                band_2.extend(bfs(matrix, visited, (i, j), "2"))
    
    overlap_positions = set(band_1) & set(band_2)
    overlaps = len(overlap_positions)
    return band_1, band_2, overlaps, overlap_positions

def is_interlocked(matrix, overlap_positions):
    """Check for interlocking using overlap positions"""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x, y in overlap_positions:
        surrounding = set()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix):
                surrounding.add(matrix[nx][ny])
        # If the surrounding includes both '1' and '2', it indicates interlocking
        if '1' in surrounding and '2' in surrounding:
            return True
    return False

def main():
    # Input
    S = int(input())
    matrix = [input().strip() for _ in range(S)]
    
    # Find bands and overlaps
    band_1, band_2, overlaps, overlap_positions = find_bands_and_overlaps(matrix)
    
    # Check for interlocking
    if is_interlocked(matrix, overlap_positions):
        print("Impossible")
    else:
        print(overlaps)

if __name__ == "__main__":
    main()
