__author__ = 'santhoshkumar'
import web
import json
import requests

#urls = ('/(.*)', 'API')
urls = ('/get_user_profile_pic/(.*)', 'API')
app = web.application(urls, globals())

class API():

    def GET(self,username=None):
        if username == None:
            username='sreenathkamath'
        resp = requests.get('https://graph.facebook.com/'+username)
        resp = resp.json()
        if 'id' in resp:
            id = resp['id']
        else:
            return ''
        url = 'https://graph.facebook.com/'+str(id)+'/picture?access_token=CAAQDIa0jY9kBAGl5nP9uJpumehBrvpPYiSM9ZACwILF1djCjpViX00jZCOZBrw3bpwE5ApOHl5Fst3QvABcywZAr0uwZCZC2ZANgiv2pvZCfnnyMfalyDWrUJ9xb6MO1FEf9amCr0MgZB8E1EGo7u3yiovOxoVRogFrP4RaEdLZAXsS9g9mNHpakrxv0RJmjEnu104j22cit9jdAZDZD&redirect=false&type=large'
        response = requests.get(url)
        response_json = response.json()

        if 'url' in response_json['data']:
            return response_json['data']['url']
        else:
            return ''

if __name__ == "__main__":
    app.run()
