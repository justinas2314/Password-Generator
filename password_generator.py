import random
import pyperclip


def main(length: int):
    nums, upper, lower, chrs = "0123456789", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", \
                               "abcdefghijklmnopqrstuvwxyz", r" !@#$%^&*()\")[]{}"
    while True:
        string = ''.join(random.choices(nums + upper + lower + chrs, k=length))
        string_as_set = set(string)
        if all((len(set(nums) & string_as_set),
                len(set(upper) & string_as_set),
                len(set(lower) & string_as_set),
                len(set(chrs) & string_as_set))):
            return string


if __name__ == "__main__":
    pyperclip.copy(main(64))
