import re

text = open('data.txt', 'r').read()

# Expression régulière pour extraire des emails valides
email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
emails = re.findall(email_regex, text)

print("Emails valides :", emails)
# Expression régulière pour les numéros de téléphone
phone_regex = r'(\+?\d{1,3}[-.\s]?)?(\(?\d{1,4}\)?[-.\s]?)?(\d{2,4}[-.\s]?){2,4}'
phones = re.findall(phone_regex, text)

print("Numéros de téléphone :", phones)
# Expression régulière pour les dates
date_regex = r'\b(?:\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}|\d{4}[\/\-\.]\d{1,2}[\/\-\.]\d{1,2})\b'
dates = re.findall(date_regex, text)

print("Dates extraites :", dates)

# Expression régulière pour les URLs
url_regex = r'\b(?:http|https|ftp):\/\/[^\s\/$.?#][^\s]*\b'
urls = re.findall(url_regex, text)



print("URLs trouvées :", urls)
