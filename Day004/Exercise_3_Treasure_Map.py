row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row = int(position[1])
coloum = int(position[0])

# Method 1 ----------------------
select_row = map[row-1]
select_row[coloum-1] = "X"

# Method 2 ----------------------

map[row-1][coloum-1] = "x"


print(f"{row1}\n{row2}\n{row3}")