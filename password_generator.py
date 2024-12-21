import secrets
import pyperclip


def main(length: int):
    nums, upper, lower, chrs = "0123456789", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", \
                               "abcdefghijklmnopqrstuvwxyz", r" !@#$%^&*()\")[]{}"
    while True:
        string = ''.join(secrets.choice(nums + upper + lower + chrs) for _ in range(length))
        string_as_set = set(string)
        if all((len(set(nums) & string_as_set),
                len(set(upper) & string_as_set),
                len(set(lower) & string_as_set),
                len(set(chrs) & string_as_set))):
            print(string)
            return string


if __name__ == "__main__":
    pyperclip.copy(main(64))
