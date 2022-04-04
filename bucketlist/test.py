import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor
}

def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return ops[oper](op1, op2)

print(eval_binary_expr(*("1 + 3".split())))
print(eval_binary_expr(*("1 * 3".split())))
print(eval_binary_expr(*("1 % 3".split())))
print(eval_binary_expr(*("1 ^ 3".split())))