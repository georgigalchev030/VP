def get_collection_builder(col_type):
    if not type(col_type) == str:
        return

    if col_type == "tuple":
        def tuple_builder(a, b, c, d):
            tup_lst = (a, b, c, d)
            return tup_lst
        return tuple_builder
    if col_type == "list":
        def list_builder(a, b, c, d):
            lst = [a, b, c, d]
            return lst
        return list_builder
    if col_type == "set":
        def set_builder(a, b, c, d):
            set_ls = {a,b,c,d}
            return set_ls
        return set_builder


tup_build = get_collection_builder("tuple")
tup = tup_build(1, 2.23, 3, "hi")
print(tup)