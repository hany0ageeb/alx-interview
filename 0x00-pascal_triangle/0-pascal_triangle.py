"""
pla pla pla
"""
def pascal_triangle(n):
    """
    Pla pla pla
    """
    if (n <= 0):
        return []
    elif (n == 1):
        return [[1]]
    elif (n == 2):
        return [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for row in range(2, n):
            rw = []
            for col in range(0, row + 1):
                if(col == 0 or col == row):
                    rw.append(1)
                else:
                    rw.append(result[row - 1][col - 1] + result[row - 1][col])
            result.append(rw)
        return result
if __name__ == '__main__':
    print(pascal_triangle(0))
    print(pascal_triangle(1))
    print(pascal_triangle(2))
    print(pascal_triangle(3))
    print(pascal_triangle(4))
    print(pascal_triangle(5))
    print(pascal_triangle(6))
    print(pascal_triangle(7))
    print(pascal_triangle(8))