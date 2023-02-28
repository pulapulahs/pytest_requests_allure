from nametest import get_formatted_name

print("Enter 'q' at time to quit.")
while True:
    first = input("\nPlease give me your favorite man's first name:")
    if first == 'q':
        break
    last = input("\nPlease give me your favorite man's last name:")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name:" + formatted_name + '.')


