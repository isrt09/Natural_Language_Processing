import re

text = "I was born in 1985 in Lahore, in Pakistan"

re.match(r"",         text)
re.match(r".*",       text)
re.match(r".+",       text)
re.match(r"[a-zA-Z]", text)
re.match(r"[a-zA-Z]+",text)
re.match(r"I was?",   text)
re.match(r"^1985",    text)

re.search(r"[a-zA-Z]+",text)
re.search(r"Pakistan$",text)

re.sub(r"\d+","",           text)
re.sub(r"Pakistan","India", text)
re.sub(r"[a-z]",   "#",     text)
re.sub(r"[a-zA-Z]","#",     text)

