#Email Slicer

email_id = input('Enter your email id: ').strip() #leading and trailing whitespaces are removed;

username = email_id[:email_id.index('@')]

domain = email_id[email_id.index('@')+1:]

print(f"User Name: {username}\nDomain Name: {domain}")