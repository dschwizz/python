import re
text = '''I want to buy style 503-4557.
Give me style 5467892.
My prefered SKU is 54323 from style 506-2341
'''
listText = ('I want to buy style 503-4557.','Give me style 5467892.','My prefered SKU is 54323 from style 506-2341')
styleRegex = re.compile(r'(\d\d\d(-)?\d\d\d\d)')
#loop through list using search
for i in range(3) :
    print(styleRegex.search(listText[i]))

#use findall on a large piece of text
print(styleRegex.findall(text)) 


