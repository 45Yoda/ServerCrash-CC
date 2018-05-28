import re
import config


class StatTable:

    def __init__(self):
        self.dict = {}

    def order(self, msg, time):

        for key in self.dict:
            if self.dict[key]['IP_Addr'] == msg['IP_Addr']:
                del self.dict[key]

                break

        dict_data = {'Mem_Available': msg['Mem_Available'],
                     'Load': msg['Load'],
                     'IP_Addr': msg['IP_Addr'],
                     'Port': msg['Port'],
                     'RTT': time}

        load = msg['Load']
        mem = msg['Mem_Available']

        ka = ((1-config.factor)*((float(mem)/1000)+float(load))*time)

        self.dict[ka] = dict_data

        self.dict = SortDisplay(self.dict)

    def top_server(self):
        addr = self.dict[max(self.dict, key=float)]['IP_Addr']
        return addr

    def printable(self):
        print(self.dict)


class SortDisplay(dict):
    def __str__(self):
        return "{" + ", ".join("%r: %r" % (key, self[key]) for key in sorted(self)) + "}"
