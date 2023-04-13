class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
      # Start with the first number or operand.
      # If the next symbol is a number or operand, add it to your current calculation.
      # If the next symbol is an operator, apply that operator to the previous two operands.
      # Continue this process until you reach the end of the expression
        operands = []
        for c in tokens:
            if c == "+":
                operands.append(operands.pop() + operands.pop())
            elif c == "-":
                a = operands.pop()
                b = operands.pop()
                operands.append(b - a)
            elif c == "*":
                operands.append(operands.pop() * operands.pop())
            elif c == "/":
                a = operands.pop()
                b = operands.pop()
                operands.append(int(b / a))
            else:
                operands.append(int(c))
        return operands[0]


obj = Solution()
# print(obj.evalRPN(["2", "1", "+", "3", "*"]))
print(obj.evalRPN(["4", "13", "5", "/", "+"]))
