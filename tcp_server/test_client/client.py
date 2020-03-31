
import sys
import getopt
import asyncio
import libscrc
import time

# --------------------------------------------------------------------------------------------------
class ClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        msgs = self.message.split('\\n')
        for _msg in msgs:
            if len(_msg) == 0:
                continue
            # print("_msg = |" + _msg + "|")
            _msg += '\n'
            transport.write(_msg.encode())
            print('Data sent: {}'.format(_msg))
            time.sleep(1)

    def data_received(self, data):
        print('Data received: {}'.format(data.decode()))
        self.loop.stop()

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()

# --------------------------------------------------------------------------------------------------
def run_command(host, port, msg):
    loop = asyncio.get_event_loop()

    coro = loop.create_connection(
        lambda: ClientProtocol(msg, loop),
        host, port
    )

    try:
        loop.run_until_complete(coro)
        loop.run_forever()
    except ConnectionRefusedError as e:
        print(str(e))
        sys.exit(1)

# --------------------------------------------------------------------------------------------------
def main():

    _command = None
    _host = None
    _port = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:h:p:", ["command=", "host=", "port=",])
    except Exception as e:
        print("Error: ", str(e))
        sys.exit(1)

    for oo, a in opts:
        if oo in ("-c", "--command"):
            _command = a
        elif oo in ("-h", "--host"):
            _host = a
        elif oo in ("-p", "--port"):
            _port = a
        else:
            print("Undefined option(s).")
            sys.exit(1)

    if _host is None:
        print("Параметр host не определен.")
        sys.exit(1)

    if _port is None:
        print("Параметр port не определен.")
        sys.exit(1)

    run_command(_host, _port, _command)


if __name__ == "__main__":
    main()
