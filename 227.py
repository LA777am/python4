class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'

        for i in range(len(s)):
            c = s[i]

            if c.isdigit():
                num = num * 10 + int(c)

            if (not c.isdigit() and not c.isspace()) or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    a = stack.pop()
                    stack.append(a * num)

                elif sign == '/':
                    a = stack.pop()
                    stack.append(int(a / num))

                sign = c
                num = 0

        return sum(stack)