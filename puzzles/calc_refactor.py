from operator import add, sub, truediv, mul

MAP = {'+': add, '-': sub, '*': mul, '/': truediv}

# class Node(object):
#     def __init__(self, value):
#         self.val = value

#     def evaluate(self):
#         return self.value


# class OperationNode(object):
#     MAP = {'+': add, '-': sub, '*': mul, '/': truediv}

#     def __init__(self, operation, a, b):
#         if operation not in self.MAP:
#             raise ValueError('Unknown operation %s' % operation)
#         self.operation = operation
#         self.a = a
#         self.b = b

#     def evaluate(self):
#         res_a = self.a.evaluate()
#         res_b = self.b.evaluate()
#         return self.MAP[self.operation](res_a, res_b)

def evaluate(op, a, b):
    return MAP[op](a, b)

def check_if_operation_valid(operation):
    if operation in MAP:
        return True;
    raise ValueError('Unknown operation %s' % operation);

def parse_expr(tokens):
    next_token = tokens.pop()
    # if next_token not in OperationNode.MAP:
    if next_token not in MAP:
        value = int(next_token) if next_token.isdigit() else float(next_token)
        # return Node(value)
        return value

    op = next_token
    b = parse_expr(tokens)
    a = parse_expr(tokens)
    # return OperationNode(op, a, b)
    return evaluate(op, a, b)


def calc(expr):
    if not expr:
        return 0

    tokens = expr.split(' ')
    res = parse_expr(tokens)
    if res % 1 == 0:
        return int(res)
    return res

# print('10 2 +'.split(' '))

res1 = calc('10 2 +')
print(res1)

