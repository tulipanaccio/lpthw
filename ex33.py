def make_list(num_elem, step):
    i = 0
    numbers = []

    while i < num_elem:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    return numbers

# i = 0
# numbers = []
#
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
numbers = make_list(6000, 100)


print("The numbers: ")

for num in numbers:
    print(num)
