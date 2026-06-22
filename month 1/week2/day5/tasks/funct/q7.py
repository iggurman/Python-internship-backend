def reverse(S):
    rev=""
    for char in S:
        rev=char+rev
    return rev

print(reverse("gurman garg"))