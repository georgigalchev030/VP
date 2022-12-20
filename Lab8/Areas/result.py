type_figure = input("Enter type: ")
if type_figure == "triangle":
    from triangle import triangleArea
    print(triangleArea(int(input("a: ")), int(input("ha: "))))

elif type_figure == "square":
    from square import areaSquare
    print(areaSquare(int(input("a: "))))

elif type_figure == "romb":
    from romb import areaRomb
    print(areaRomb(int(input("a: ")), int(input("ha: "))))

elif type_figure == "trapec":
    from trapec import areaTrapec
    print(areaTrapec(int(input("a: ")), int(input("b: ")), int(input("ha: "))))

elif type_figure == "pravougulnik":
    from pravougulnik import areaPravougulnik
    print(areaPravougulnik(int(input("a: ")), int(input("b: "))))
