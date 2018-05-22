import config


class Table:

    def __init__(self):
        self.dict = {}

    def order(self,msg,time):
        for key in self.dict:
            if self.dict[key]['IP'] == msg['IP']:
                del self.dict[key]

                break

        dictData = {'Mem_Available': msg['Mem_Available'],
                    'Load': msg['Load'],
                    'IP_Addr': msg['IP_Addr'],
                    'Port': msg['Port'],
                    'RTT': time
                   }

        load = msg['Load']
        mem = msg['Mem_Available']

        k = ((1-config.factor)*(mem - load)) + 1
        self.dict[k] = dictData

        self.dict = "{" + ", ".join("%r: %r" % (key, self.dict[key]) for key in sorted(self.dict)) + "}"

    def top_server(self):
        addr = self.dict[max(self.dict, key=float)]['IP_Addr']
        return addr

    def printable(self):
        print(self.dict)
