from classes.Log import Log
from classes.API import API
from classes.BDO_API import BDO_API

Log('Set log level', 0).setLevel(1)

bdo = BDO_API()

# response = bdo.GetMarketHotList()
# response = bdo.GetMarketQueueList()
# response = bdo.GetMarketList(1, 1)
response = bdo.GetMarketItem(56221)
# response = bdo.GetMarketItem(10210, 2)
# response = bdo.GetMarketItemIcon(10210)
# response = bdo.GetMarketItemTooltip(10210, 2)
# response = bdo.GetMarketSearch('Narc')


print(response)

# FUTURE
# embed = discord.Embed(title="my title",color=**discord.Color.purple()**)
# embed.set_thumbnail(url="")
# embed.add_field(name="", value="", inline=True)
# embed.set_footer(text="by squirrhell")

# pouvoir ajouter/supp/voir
#