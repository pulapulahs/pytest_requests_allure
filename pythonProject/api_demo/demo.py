import requests

class ApiDemo:
    #POST
    def do_post(self, url, params=None, headers=None, **kwargs):
        return requests.post(url=url, params=params, headers=headers, **kwargs)

    #GET
    def do_get(self, url, params=None, headers=None, **kwargs):
        return requests.get(url=url, params=params, headers=headers, **kwargs)


    