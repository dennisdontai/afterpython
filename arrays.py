furniture = ["table", "chair", "stool"]
print(furniture[0])

print(furniture)
for x in furniture:
    print(x)

# Adding an item in an array
furniture.append("bed")
print(furniture)


# Removing an item in ana array
furniture.remove("stool")
print(furniture)

# Length of an array
x = len(furniture)
print(x)