#!/usr/bin/env python3
"""
    Dump the content of a plc to a file
"""

import argparse
import pickle
import pylibmodbus

def dump(args):
    plc_handle = pylibmodbus.ModbusTcp(ip=args.host, port=args.port)
    plc_handle.connect()

    data = []
    for address in range(0, 0xFFFF, 121):
        try:
            raw = plc_handle.read_registers(address, 121)
        except:
            print("Can't read at addr %d", address)
            break
        pyobj = list(raw)
        data.append(pyobj)


    with open(args.file, 'wb') as f:
        print(data)
        pickle.dump(data, f)


def main():
    parser = argparse.ArgumentParser(description='Dump data into a pickled file.')
    parser.add_argument('--port', default=502, type=int)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--file', required=True)

    args = parser.parse_args()
    dump(args)

if __name__ == '__main__':
    main()
