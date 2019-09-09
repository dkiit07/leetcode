# Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        part1_rx = '(?:[a-z0-9]|[.+])+@'
        part_part1_rx = '(?:[a-z0-9]|[.])+\+'
        part2_rx = '@(?:[a-z]|[.])+'

        new_list = []
        for email in emails:
            first = re.findall(part1_rx, email)
            if '+' in first[0]:
                first = re.findall(part_part1_rx, str(first))
            new_part = ""
            for ch in first[0]:
                if ch == '.' or ch == '+' or ch == '@':
                    pass
                else:
                    new_part += ch

            second = re.findall(part2_rx, email)
            new_email = new_part + second[0]
            new_list.append(new_email)

        email_set = set(new_list)
        return len(email_set)
