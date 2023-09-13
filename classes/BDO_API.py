from classes.API import API
from classes.Log import Log


class BDO_API :

    url_base = "https://eu-trade.naeu.playblackdesert.com/Trademarket/"

    def __init__(self) :
        None

    def GetWorldMarketHotList(self) : # need fix
        url = self.url_base+"GetWorldMarketHotList"
        
        response = API().post(url)

        items = response['resultMsg'].split('|')
        result_list = []
        for item in items :
            if item != '' and item != '0' :
                item = item.split('-')
                new_item = {
                    "id" : item[0],
                    "enhan_min" : item[1],
                    "enhan_max" : item[2],
                    "price_base" : item[3],
                    "curr_stock" : item[4],
                    "total_trade" : item[5],
                    "price_chg_dir" : item[6],
                    "price_chg_val" : item[7],
                    "price_cap_min" : item[8],
                    "price_cap_max" : item[9],
                    "last_sale_price" : item[10],
                    "last_sale_time" : item[11],
                }
                result_list.append(new_item)
        
        return result_list

    def GetWorldMarketList(self, mainCategory, subCategory=None) :
        url = self.url_base+"GetWorldMarketList"
        
        param = {
            "keyType" : 0,
            "mainCategory" : mainCategory,
            "subCategory" : subCategory,
        }
        response = API().post(url, param)

        items = response['resultMsg'].split('|')
        result_list = []
        for item in items :
            if item != '' and item != '0' :
                item = item.split('-')
                new_item = {
                    "id" : item[0],
                    "curr_stock" : item[1],
                    "price_base" : item[3],
                    "total_trade" : item[2],
                }
                result_list.append(new_item)
        
        return result_list
    
    def GetWorldMarketSubList(self, item_id) :
        url = self.url_base+"GetWorldMarketSubList"
        
        param = {
            "keyType" : 0,
            "mainKey" : item_id,
        }
        response = API().post(url, param)
        items = response['resultMsg'].split('|')
        result_list = []
        for item in items :
            if item != '' and item != '0' :
                item = item.split('-')
                new_item = {
                    "id" : item[0],
                    "enhan_min" : item[1],
                    "enhan_max" : item[2],
                    "price_base" : item[3],
                    "curr_stock" : item[4],
                    "total_trade" : item[5],
                    "price_cap_min" : item[6],
                    "price_cap_max" : item[7],
                    "last_sale_price" : item[8],
                    "last_sale_time" : item[9],
                }
                result_list.append(new_item)
        
        return result_list

    def GetWorldMarketSearchList(self, item_ids) :
        url = self.url_base+"GetWorldMarketSearchList"

        if isinstance(item_ids, list):
            new_item_ids = ','.join(map(str, item_ids))
            item_ids = new_item_ids
        
        param = {
            "searchResult" : item_ids,
        }
        response = API().post(url, param)

        items = response['resultMsg'].split('|')
        result_list = []
        for item in items :
            if item != '' and item != '0' :
                item = item.split('-')
                new_item = {
                    "id" : item[0],
                    "curr_stock" : item[1],
                    "price_base" : item[2],
                    "total_trade" : item[3],
                }
                result_list.append(new_item)
        
        return result_list

    def GetBiddingInfoList(self, item_id) :
        url = self.url_base+"GetBiddingInfoList"

        param = {
            "keyType" : 0,
            "mainKey" : item_id,
            "subKey"  : 0, 
        }
        response = API().post(url, param)
        return response

    def GetMarketPriceInfo(self, item_id) :
        url = self.url_base+"GetMarketPriceInfo"

        param = {
            "keyType" : 0,
            "mainKey" : item_id,
            "subKey"  : 0, 
        }
        response = API().post(url, param)
        return response

    def GetWorldMarketWaitList(self) :
        url = self.url_base+"GetWorldMarketWaitList"
        response = API().post(url)

        items = response['resultMsg'].split('|')
        result_list = []
        for item in items :
            if item != '' and item != '0' :
                item = item.split('-')
                new_item = {
                    "id" : item[0],
                    "enhan_lvl" : item[1],
                    "price" : item[2],
                    "time" : item[3],
                }
                result_list.append(new_item)
        
        return result_list
