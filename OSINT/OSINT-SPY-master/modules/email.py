from modules.config import *
import json, requests

def fetchData(email_id):
    url = 'https://api.fullcontact.com/v3/person.enrich'
    headers = {"Authorization": f"Bearer {fullcontact_api_key}"}
    data = json.dumps({"email": email_id})
    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 404:
        print('Profile not found')
        return

    print('General Details:')
    print(('-'*20))
    attributes = ['fullName', 'ageRange', 'gender', 'location', 'title', 
                'organization', 'twitter', 'linkedin', 'facebook', 'bio', 'avatar', 'website']
    response = response.json()
    for attribute in attributes:
        try:
            value = response[attribute]
            if value is not None:
                print(f'{attribute.capitalize()}: {value}')
        except:
            pass
    
    print('\nMore details:')
    print(('-'*20))
    details = ['emails', 'phones', 'employment', 'education', 'interests']
    for attribute in details:
        try:
            value_list = response['details'][attribute]
            if value_list:
                print(f'{attribute.capitalize()}: ')
                print(('-'*20))
                for value in value_list:
                    if isinstance(value, str):
                        print(value, end=' ')
                    else:
                        for data in value:
                            print(f'{data.capitalize()}: {value[data]}')
                        print()
                print()
        except:
            pass

