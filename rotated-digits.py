# Rotated Digits
# https://leetcode.com/problems/rotated-digits/description/

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        number_status = False
        good_numbers = 0
        for number in range(1, N+ 1):
            number_str = str(number)
            digit_count = len(number_str)
            count = 0
            for digit in range(len(number_str)):
                if number_str[digit] == '0' or number_str[digit] == '1' or number_str[digit] == '8' or number_str[
                    digit] == '2' or number_str[digit] == '5' or number_str[digit] == '6' or number_str[digit] == '9':
                    count = count + 1
            if count == digit_count:
                char_list = list(number_str)
                for digit in range(len(number_str)):
                    if number_str[digit] == '2':
                        char_list[digit] = '5'
                    if number_str[digit] == '5':
                        char_list[digit] = '2'
                    if number_str[digit] == '6':
                        char_list[digit] = '9'
                    if number_str[digit] == '9':
                        char_list[digit] = '6'
                    if number_str[digit] == '0':
                        char_list[digit] = '0'
                    if number_str[digit] == '1':
                        char_list[digit] = '1'
                    if number_str[digit] == '8':
                        char_list[digit] = '8'
                if ''.join(char_list) != number_str:
                    good_numbers = good_numbers + 1
        return good_numbers
