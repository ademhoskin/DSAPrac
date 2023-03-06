def print_items(n):
    # o(n^2)
    for i in range(n):
        print(i)
        for j in range(n):
            print(j)
    # + o(n) -- simplify to o(n^2) due to non dominance dropping
    for k in range(n):
        print(k)

print_items(10)
