import socket
import time
import json
import config
from threading import Thread


class MonitorUDP:

    def __init__(self):
        self.start = time.time()
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_DGRAM,
                                    socket.IPPROTO_UDP)

        t1 = Thread(target=self.probe)
        t2 = Thread(target=self.listen_answer)

        t1.start()
        t2.start()

    def probe(self):

        while True:
            print("Probing Agents")
            self.start = time.time()
            self.socket.sendto(bytes(json.dumps({"Type": 'request'}), "utf-8"), config.mcast_group)

            print("Probe sent")
            time.sleep(5)

    def listen_answer(self):

        while True:
            data, addr = self.socket.recvfrom(1024)
            end = time.time()
            what = end-self.start
            parsed = json.loads(data)
            print('Time: ' + str(what))
            print(json.dumps(parsed, indent=2))
            print('Address: %s' % (addr,))


def main():
    MonitorUDP()


if __name__ == "__main__":
    main()
