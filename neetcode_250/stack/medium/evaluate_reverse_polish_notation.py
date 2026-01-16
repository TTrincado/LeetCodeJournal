class Solution:
    """
    Reverse Polish Notation (Postfix) places operators AFTER their operands.

    If we see a number, we push it to the stack (waiting for an operator).
    If we see an operator (+, -, *, /), we know it applies to the LAST TWO numbers seen.

    Time Complexity: O(N) - Single pass through tokens.
    Space Complexity: O(N) - Stack stores operands.
    """

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))

        return stack[0]
