# Robot Return to Origin #
# https://leetcode.com/problems/robot-return-to-origin/description/

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        move_dict = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        for move in range(len(moves)):
            if moves[move] == 'L':
                move_dict['L'] = move_dict['L'] + 1
            if moves[move] == 'R':
                move_dict['R'] = move_dict['R'] + 1
            if moves[move] == 'U':
                move_dict['U'] = move_dict['U'] + 1
            if moves[move] == 'D':
                move_dict['D'] = move_dict['D'] + 1

        if move_dict['L'] == move_dict['R'] and move_dict['U'] == move_dict['D']:
            return True
        else:
            return False