def findString(w, queries):


w_count = int(input("Enter the number of strings "))
if 1 <= w_count <= 50:
    w = []

    for _ in range(w_count):
        w_item = input("Enter strings")
        if 1 <= len(w_item) <= 2000:
            w.append(w_item)
        else:
            print(F"The length of the string is less than 1 or more than 2000")
            exit()

    queries = []
    queries_count = int(input("Enter the number of queries"))
    if 1 <= queries_count <= 500:
        for _ in range(queries_count):
            queries_item = int(input("Enter k"))
            if 1 <= queries_item <= 1000000000:
                queries.append(queries_item)
            else:
                exit()
    else:
        print(F"The amount of queries should range from 1 to 500")
        exit()

    result = findString(w, queries)
else:
    print(F"Wrong number of strings.\nYou should have at lease one and no more than 50 strings")

