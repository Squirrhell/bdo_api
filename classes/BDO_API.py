from classes.API import API
from classes.Log import Log

class BDO_API :

    url_base = "https://api.blackdesertmarket.com"
    param = {"region" : 'eu'}

    def __init__(self) :
        None

    def GetMarketHotList(self) :
        url = f"{self.url_base}/list/hot"

        response = API().get(url, self.param, json=True)
        data = response['data']
        return data
    
    def GetMarketQueueList(self) :
        url = f"{self.url_base}/list/queue"

        response = API().get(url, self.param, json=True)
        data = response['data']
        return data

    def GetMarketList(self, mainCategory, subCategory='') :
        url = f"{self.url_base}/list/{mainCategory}/{subCategory}"

        response = API().get(url, self.param, json=True)
        data = response['data']
        return data

    def GetMarketItem(self, item_id, enhan_lvl='') :
        url = f"{self.url_base}/item/{item_id}/{enhan_lvl}"
        # pas encore compris comment le niveau d'enchant fonctionne xD

        response = API().get(url, self.param, json=True)
        data = response['data']
        return data

    def GetMarketItemIcon(self, item_id) :
        url = f"{self.url_base}/item/{item_id}/icon"

        response = API().get(url, self.param)
        return response
    
    def GetMarketItemTooltip(self, item_id, enhan_lvl=1) :
        url = f"{self.url_base}/item/{item_id}/{enhan_lvl}/tooltip"
        # pas encore compris comment le niveau d'enchant fonctionne xD

        response = API().get(url, self.param, json=True)
        data = response['data']
        return data
    
    def GetMarketSearch(self, item_id) :
        url = f"{self.url_base}/search/{item_id}"

        response = API().get(url, self.param, json=True)
        data = response['data']
        return data