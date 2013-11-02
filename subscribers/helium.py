import requests
try:
    import json
except ImportError:
    import simplejson as json

class Helium:
    def __init__(self, api_key):
    
        self.api_key = api_key
        
        self.api_endpoints = {
            'items': 'https://gethelium.com/api/v1/items/',
            'item': 'https://gethelium.com/api/v1/items/%s/',
            'charges': 'https://gethelium.com/api/v1/charges/',
            'charge': 'https://gethelium.com/api/v1/charges/%s/',
        }
        

    def get_items(self):
        r = requests.get(self.api_endpoints['items'], auth=(self.api_key, ''))
        return json.loads(r.content)

    def get_item(self, sku):
        r = requests.get(self.api_endpoints['item'] % sku, auth=(self.api_key, ''))
        return json.loads(r.content)

    def get_charges(self):
        r = requests.get(self.api_endpoints['charges'], auth=(self.api_key, ''), verify=False)
        return json.loads(r.content)

    def get_charge(self, charge_id):
        r = requests.get(self.api_endpoints['charge'] % charge_id, auth=(self.api_key, ''))
        return json.loads(r.content) 
        
    def put_item(self, **kwargs):
        """
        to create a product:
        usage: put_item(sku='mysku',price=1111,type='general',name='myname',require_address=True)
        to update a product:
        put_item(sku='mysku',price=9999)
        
        """
        url = self.api_endpoints['items'] + kwargs.get('sku')
        r = requests.put(url, data=kwargs, auth=(self.api_key, ''))
        if r.status_code == 200:
          return json.loads(r.content)
        else:
          return r.status_code