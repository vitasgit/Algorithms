 def sm(lst, index=0):
    if index == len(lst):
        return 0

    return lst[index] + sm(lst, index + 1)

print(sm([1, 2, 3]))
