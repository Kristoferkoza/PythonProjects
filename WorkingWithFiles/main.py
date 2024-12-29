# with open("100_Days_Bootcamp\WorkingWithFiles\my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("100_Days_Bootcamp\WorkingWithFiles\my_file.txt", mode="w") as file:
#     file.write("New text.")

with open("100_Days_Bootcamp\WorkingWithFiles\my_file.txt", mode="a") as file:
    file.write("\nNew text2.")