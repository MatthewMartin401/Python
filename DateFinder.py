# Date Detect

import re

'''
re.compile() # Pattern Object
    .match()
        .group()
        .start()
        .start()
        .end()
        .span()
    .search("", "")
    .findall()
    .finditer()
'''

text = "Its 05/05/2023 or 5/5/2023 or 5/5/23 or 5523"
#p = re.compile(("\D\D\?|\D?"+"\D\D?|\D?"+"\D\D|\D\D\D\D"))
#p = re.compile(("\d\d\d?\d\d?\d\d\d\d"))
# p = re.compile(r"\d+\W?\d+\W?\d+")
p = re.compile(r"\d+\W\d+\W\d+")
print(p)
m = p.findall(text)
print(m)
print(p.match(text))
    
