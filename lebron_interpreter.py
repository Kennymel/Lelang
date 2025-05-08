
def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
        elif expr[i].isdigit():
            num = ""
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(('NUM', int(num)))
        elif expr[i].isalpha():
            ident = ""
            while i < len(expr) and expr[i].isalnum():
                ident += expr[i]
                i += 1
            tokens.append(('ID', ident))
        elif expr[i] in "+-*/%()":
            tokens.append(('OP', expr[i]))
            i += 1
        else:
            i += 1
    return tokens

def eval_expr(tokens, variables):
    def parse_primary():
        token = tokens.pop(0)
        if token[0] == 'NUM':
            return token[1]
        elif token[0] == 'ID':
            return variables.get(token[1], 0)
        elif token[1] == '(':
            val = parse_expression()
            tokens.pop(0)  
            return val

    def parse_term():
        val = parse_primary()
        while tokens and tokens[0][1] in ('*', '/', '%'):
            op = tokens.pop(0)[1]
            next_val = parse_primary()
            if op == '*':
                val *= next_val
            elif op == '/':
                val //= next_val
            elif op == '%':
                val %= next_val
        return val

    def parse_expression():
        val = parse_term()
        while tokens and tokens[0][1] in ('+', '-'):
            op = tokens.pop(0)[1]
            next_val = parse_term()
            if op == '+':
                val += next_val
            elif op == '-':
                val -= next_val
        return val

    return parse_expression()

def run_lelang(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    variables = {}
    i = 0
    while i < len(lines):
        line = lines[i]

        if " = " in line:
            var, expr = line.split(" = ", 1)
            tokens = tokenize(expr)
            variables[var.strip()] = eval_expr(tokens[:], variables)

        elif line.startswith("goat"):
            loop_condition = line[len("goat"):].strip()
            loop_var = loop_condition.split("<=")[0].strip()
            loop_end_var = loop_condition.split("<=")[1].strip()
            i += 1

            loop_block = []
            depth = 1
            while i < len(lines):
                l = lines[i].strip()
                if l.startswith("goat"):
                    depth += 1
                elif l == "strive for greatness":
                    depth -= 1
                    if depth == 0:
                        break
                loop_block.append(lines[i])
                i += 1

            while True:
                end_val_tokens = tokenize(loop_end_var)
                end_val = eval_expr(end_val_tokens, variables)
                current_val = variables.get(loop_var, 0)

                if current_val > end_val:
                    break

                suppress_number = False
                for stmt in loop_block:
                    stmt = stmt.strip()

                    if " = " in stmt:
                        var, expr = stmt.split(" = ", 1)
                        tokens = tokenize(expr.strip())
                        variables[var.strip()] = eval_expr(tokens[:], variables)

                    elif stmt == "lakers":
                        val = variables.get(loop_var, 0)
                        if val % 3 == 0 and val % 5 == 0:
                            print("lebron")
                            suppress_number = True
                        elif val % 3 == 0:
                            print("le")
                            suppress_number = True
                        elif val % 5 == 0:
                            print("bron")
                            suppress_number = True

                    elif stmt.startswith("it's our ball ain't it"):
                        expr = stmt[len("it's our ball ain't it"):].strip()
                        tokens = tokenize(expr)
                        val = eval_expr(tokens[:], variables)
                        if not suppress_number:
                            print(val)

                    elif stmt.startswith("king me"):
                        var = stmt[len("king me"):].strip()
                        if var in variables:
                            variables[var] += 1
                        else:
                            variables[var] = 1


        elif line == "smiling through it all, can't believe this my life":
            break

        elif line.startswith("it's our ball ain't it"):
            expr = line[len("it's our ball ain't it"):].strip()
            tokens = tokenize(expr)
            val = eval_expr(tokens[:], variables)
            print(val)

        elif line.startswith("king me"):
            var = line[len("king me"):].strip()
            if var in variables:
                variables[var] += 1
            else:
                variables[var] = 1

        i += 1

if __name__ == "__main__":
    run_lelang("sample2.lelang")


