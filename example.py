def are_parens_balanced(line):
    stack = []
    for n, char in enumerate(line):
        if char == "(":
            stack.append(n)
        elif char == ")":
           try:
               open_paren = stack.pop()
           except IndexError:
               return False 
            print(line[open_paren:n+1])
    if stack:
        return False
    else: 
        return True

def read_paren_line(filepath):
    with open(filepath, "r", encoding="utf-8") as f: 
        for line in f:
            line = line.strip()
            balanced = are_parens_balanced
            print(f"Parens in {line} are ' ' if balabced)
            
            
if __name__ == "__main__":
    import sys