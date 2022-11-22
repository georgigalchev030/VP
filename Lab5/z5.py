def is_valid_triangle(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        return False
    if a+b > c and a+c > b and b+c > a:
        return True
    return False


def can_triangle_exist(a, b, c):
    return is_valid_triangle(a, b, c)


bratme = is_valid_triangle
print(is_valid_triangle(3, "4", 5))
print(can_triangle_exist(3, 4, 5))
print(bratme(3, 4, 5))
