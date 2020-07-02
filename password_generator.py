import random
import pyperclip


def main(length: int):
    nums, upper, lower, chrs = "0123456789", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", \
                               "abcdefghijklmnopqrstuvwxyz", r" !@#$%^&*()\")"
    all_chars = nums + upper + lower + chrs
    while True:
        string = ''.join(random.choices(all_chars, k=length))
        print(string)
        b_nums = False
        b_upper = False
        b_lower = False
        b_chrs = False
        for i in string:
            if i in nums:
                b_nums = True
            elif i in upper:
                b_upper = True
            elif i in lower:
                b_lower = True
            elif i in chrs:
                b_chrs = True
            if all((b_nums, b_upper, b_lower, b_chrs)):
                pyperclip.copy(string)
                return None


if __name__ == "__main__":
    main(64)
