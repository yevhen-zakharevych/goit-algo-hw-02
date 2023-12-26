from collections import deque


def is_palindrome(string):
    prepared_str = string.replace(" ", "").lower()
    d = deque(prepared_str)

    while len(d) > 2:
        if d.popleft() != d.pop():
            return False
    return True


def main():
    try:
        while True:
            user_input = input("Enter a string: ")

            if is_palindrome(user_input):
                print(f"{user_input} is a palindrome")
            else:
                print(f"{user_input} is not a palindrome")

    except KeyboardInterrupt:
        print('\nInterrupted!')


if __name__ == "__main__":
    main()
