def count_types_letters():
    uppercase_count = 0
    lowercase_count = 0
    all_letters = 0
    word = "CostA Rica"
    for types in word:
        if types.isupper():
            uppercase_count += 1
            all_letters += 1
        elif types.islower():
            lowercase_count += 1
            all_letters += 1


    print(f"The uppercase quantity are:", uppercase_count)
    print(f"The lowercase quantity are", lowercase_count)
    print(f"The all letters quantity are", all_letters)
    return (uppercase_count, lowercase_count, all_letters)


