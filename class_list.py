classes = []

class_name = input('Enter class name: ')

while class_name:
    classes.append(class_name)
    class_name = input('Enter class name OR press ENTER to quit: ')


print(classes)

# for c in classes:
#     print(c)

#fancy numbered list
for index, c in enumerate(classes):
    print(f'{index+1}: {c}')