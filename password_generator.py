#!/usr/bin/env python
import random
import clipboard

nums, upper, lower, chrs = "0123456789", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", r"!@#$%^&*()\")"
all_chars = nums + upper + lower + chrs


def main():  # this is used to make sure that the password fits the requirements for most websites 
	while True:
		string = ''
		string = string.join(random.choices(all_chars, k=64))  # k is the length of the password
		print(string)
		b_nums = False
		b_upper = False
		b_lower = False
		b_chrs = False
		for i in string:  # makes sure there is atleast one of each type of char in the password
			if i in nums:
				b_nums = True
			elif i in upper:
				b_upper = True
			elif i in lower:
				b_lower = True
			elif i in chrs:
				b_chrs = True
			if all((b_nums, b_upper, b_lower, b_chrs)):
				clipboard.copy(string)
				return None


main()
