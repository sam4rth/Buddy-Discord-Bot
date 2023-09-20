def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    def is_operator(token):
        return token in '+-*/'

    for token in infix_expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            output.append(token)
        elif is_operator(token):
            while (stack and is_operator(stack[-1]) and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                raise ValueError("Mismatched parentheses")

    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return ' '.join(output)

def evaluate_postfix(postfix_expression):
    stack = []

    for token in postfix_expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(float(token))
        elif token in '+-*/':
            if len(stack) < 2:
                raise ValueError("Insufficient operands for operator")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            stack.append(result)
        else:
            raise ValueError(f"Invalid token: {token}")

    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Invalid expression")