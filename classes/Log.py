
class Log :
    lvl = 1
    # 0 : Not Displayed
    # 1 : Information
    # 2 : Warning
    # 3 : Error
    # 4 : Nothing

    color = {
        1  : '\033[92m',      # OKGREEN
        2  : '\033[93m',      # WARNING
        3  : '\033[91m',      # ERROR
        99 : '\033[0m',       # END/WHITE
    }

    def __init__(self, msg, msg_lvl):
        self.msg = msg
        self.msg_lvl = msg_lvl
        self.__call__()

    def __call__(self):
        if self.msg_lvl >= self.lvl:
            color = self.color[self.msg_lvl] if self.msg_lvl in self.color else self.color[99]
            print(color, self.msg, self.color[99])

    def setLevel(self, lvl):
        Log.lvl = lvl