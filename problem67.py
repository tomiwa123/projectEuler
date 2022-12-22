def get_triangle(filename="p067_triangle.txt"):
    with open(filename, 'r') as file:
        triangle = [list(map(int, line.split())) for line in file]
    return triangle


def max_path_sum(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]


if __name__ == "__main__":
    print(max_path_sum(get_triangle()))
