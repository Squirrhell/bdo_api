from classes.Log import Log
from classes.API import API
from classes.BDO_API import BDO_API

Log('Set log level', 0).setLevel(1)

# response = API().post("https://eu-trade.naeu.playblackdesert.com/Trademarket/GetWorldMarketWaitList")
bdo = BDO_API()
#response = bdo.GetWorldMarketSearchList([10286,10210])
# response = bdo.GetWorldMarketWaitList()
# response = bdo.GetWorldMarketSubList(10286)
#response = bdo.GetWorldMarketList(1)
response = bdo.GetWorldMarketHotList()
print(response)