import requests

config={
    'webservice_url': 'http://localhost:3000/api'
}

class StockDataProvider():
    
    url = config['webservice_url']+'/stocks'

    @staticmethod
    def get_all():
        r = requests.get(url = StockDataProvider.url)
        data = r.json()
        return data
    
    @staticmethod
    def get_filtered(filter):
      pass

    @staticmethod
    def get_one(id):
        pass

    @staticmethod
    def add(obj):
        r = requests.post(url = StockDataProvider.url, json=obj)
        response = r.json()
        # Check the response status code
        if response.status_code == 200:
            # Request successful
            print('POST request successful')
        else:
            # Request failed
            print(f'POST request failed with status code: {response.status_code}')

        # Get the response content
        print('Response:', response.text)

        return response

    @staticmethod
    def delete(id):
        pass

    @staticmethod
    def update(obj):
        pass