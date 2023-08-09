import re

with open('steps.log', 'r') as f:
    content = f.read()
    pattern = re.compile(r"\"[01]+\"")
    result = pattern.sub(lambda x: str(len(x.group())-2), content)

with open('steps2.log', 'w') as f:
    f.write(result)