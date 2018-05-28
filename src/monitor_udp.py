import socket
import time
import json
from threading import Thread


class MonitorUDP:

    def __init__(self, stat_table):
        self.start = time.time()
        self.table = stat_table
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_DGRAM)

        t1 = Thread(target=self.probe)
        t2 = Thread(target=self.listen_answer)

        t1.start()
        t2.start()

    def probe(self):

        while True:
            print("Probing Agents")
            self.start = time.time()
            self.socket.sendto(bytes(json.dumps({"Type": 'request'}), "utf-8"), ("239.8.8.8", 8888)) #config.mcast_group

            print("Probe sent")
            time.sleep(5)

    def listen_answer(self):

        while True:
            data, addr = self.socket.recvfrom(1024)
            data = json.loads(data.decode())

            if data["Type"] == 'response':
                end = time.time()
                what = end-self.start
                self.table.order(data, what)
                self.table.printable()


def main():
    MonitorUDP()


if __name__ == "__main__":
    main()
