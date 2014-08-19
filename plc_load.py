#!/usr/bin/env python3
"""
    Load the content of a previously dumped plc
"""

import argparse
import pickle
import pylibmodbus

def load(args):
    plc_handle = pylibmodbus.ModbusTcp(ip=args.host, port=args.port)
    plc_handle.connect()

    with open(args.file, 'rb') as f:
        data = pickle.load(f)

    address = 0
    for batch in data:
        print(len(batch))
        plc_handle.write_registers(address, batch)
        address += 121

def main():
    parser = argparse.ArgumentParser(description='Load data from a pickled file.')
    parser.add_argument('--port', default=502, type=int)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--file', required=True)

    args = parser.parse_args()
    load(args)

if __name__ == '__main__':
    main()