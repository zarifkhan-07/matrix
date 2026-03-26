original_string = input("Enter a string: ")

pos_replace = int(input("Enter position to replace (0-based index): "))
new_char = input("Enter new character: ")

modified_string = (
    original_string[:pos_replace] + new_char + original_string[pos_replace + 1:]
)

pos_delete = int(input("Enter position to delete (0-based index): "))

modified_string = (
    modified_string[:pos_delete] + modified_string[pos_delete + 1:]
)

print("\nOriginal String:", original_string)
print("Modified String:", modified_string) 