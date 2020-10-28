#pip install instagram-explore

import instagram_explore as ie
import json

#search user name
result = ie.user(input('Enter user name: '))
parsed_data = json.dumps(result, indent=4, sort_keys = True)

#displaying the data
print(parsed_data)