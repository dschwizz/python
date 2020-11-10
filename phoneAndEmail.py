#! python3

import re, pyperclip


# create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, (x12345
(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-)        # seperator
\d\d\d        # first 3 digits
-        # seperator
\d\d\d\d        # last 4 digits
(((ext(\.)?\s)|x)       # extension word part(optional)
 (\d{2,5}))?        # extension number part(optional)
 )
''',re.VERBOSE)

# create a regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@(

[a-zA-z0-9_.+]+        # name part
@        # @ symbol
[a-zA-z0-9_.+]+        # domain name part

''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
