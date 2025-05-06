import re

def run_lelang(filename):
    with open(filename) as f:
        lines = f.readlines()

    variables = {}
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not line or line.startswith("#"):
            i += 1
            continue

        if " = " in line:
            var, expr = line.split(" = ", 1)
            expr = expr.strip()
            for v in variables:
                expr = re.sub(rf'\b{v}\b', str(variables[v]), expr)
            try:
                variables[var.strip()] = eval(expr)
            except:
                variables[var.strip()] = expr

        elif line.startswith("nothing is given, everything is earned"):
            condition = line[len("nothing is given, everything is earned"):].strip()
            for var in variables:
                condition = re.sub(rf'\b{var}\b', str(variables[var]), condition)
            if not eval(condition):
                while not lines[i].strip().startswith("you are my sunshine"):
                    i += 1

        elif line.startswith("goat"):
            loop_condition = line[len("goat"):].strip()
            loop_var = loop_condition.split("<=")[0].strip()
            loop_end_expr = loop_condition.split("<=")[1].strip()
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
                cond_expr = loop_condition
                for var in variables:
                    cond_expr = re.sub(rf'\b{var}\b', str(variables[var]), cond_expr)
                if not eval(cond_expr):
                    break

                suppress_number = False

                for subline in loop_block:
                    subline = subline.strip()

                    if " = " in subline:
                        var, expr = subline.split(" = ", 1)
                        expr = expr.strip()
                        for v in variables:
                            expr = re.sub(rf'\b{v}\b', str(variables[v]), expr)
                        try:
                            variables[var.strip()] = eval(expr)
                        except:
                            variables[var.strip()] = expr

                    elif subline == "lakers":
                        current = variables.get("i", 0)
                        if current % 3 == 0 and current % 5 == 0:
                            print("lebron")
                            suppress_number = True
                        elif current % 3 == 0:
                            print("le")
                            suppress_number = True
                        elif current % 5 == 0:
                            print("bron")
                            suppress_number = True

                    elif subline.startswith("it's our ball ain't it"):
                        expr = subline[len("it's our ball ain't it"):].strip()
                        for var in variables:
                            expr = re.sub(rf'\b{var}\b', str(variables[var]), expr)
                        try:
                            val = eval(expr)
                        except:
                            val = expr.strip('"')
                        if not suppress_number:
                            print(val)

                    elif subline.startswith("king me"):
                        var = subline[len("king me"):].strip()
                        if var in variables:
                            variables[var] += 1

        elif line == "lakers":
            current = variables.get("i", 0)
            if current % 3 == 0 and current % 5 == 0:
                print("lebron")
            elif current % 3 == 0:
                print("le")
            elif current % 5 == 0:
                print("bron")
            else:
                print(current)

        elif line.startswith("it's our ball ain't it"):
            expr = line[len("it's our ball ain't it"):].strip()
            for var in variables:
                expr = re.sub(rf'\b{var}\b', str(variables[var]), expr)
            try:
                val = eval(expr)
            except:
                val = expr.strip('"')
            print(val)

        elif line == "smiling through it all, can't believe this my life":
            break

        elif line.startswith("king me"):
            var = line[len("king me"):].strip()
            if var in variables:
                variables[var] += 1

        i += 1

if __name__ == "__main__":
    run_lelang("sample2.lelang")