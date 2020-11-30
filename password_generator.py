import random
import pyperclip


def main(length: int):
    nums, upper, lower, chrs = "0123456789", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", \
                               "abcdefghijklmnopqrstuvwxyz", r" !@#$%^&*()\")[]{}"
    while True:
        string = ''.join(random.choices(nums + upper + lower + chrs, k=length))
        string_as_set = set(string)
        if all((set(nums) & string_as_set != {},
                set(upper) & string_as_set != {},
                set(lower) & string_as_set != {},
                set(chrs) & string_as_set != {})):
            pyperclip.copy(string)
            return


if __name__ == "__main__":
    main(64)
