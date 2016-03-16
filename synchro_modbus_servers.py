#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Polyconseil SAS. All rights reserved.

"""
    Script to synchronize two modbus servers. One is the master, the second is the slave.

    command example:
    synchro_modbus_servers --master-host 127.0.0.1 --master-port 502
        --slave-host 127.0.0.1 --slave-port 503
"""

import argparse
import logging

import pylibmodbus

logger = logging.getLogger(__name__)


def registers_synchro(master_handle, slave_handle, start, end):

    for x in range(start, end, 121):
        # Read registers from master Modbus server
        master_data = master_handle.read_registers(x, 121)
        # Write registers on slave Modbus server
        slave_handle.write_registers(x, master_data)
    # Remaining registers
    master_data = master_handle.read_registers(end - (end % 121), end % 121)
    # Write registers on slave Modbus server
    slave_handle.write_registers(end - (end % 121), master_data)


def coils_synchro(master_handle, slave_handle, start, end):

    for x in range(start, end, 121):
        # Read registers from master Modbus server
        master_data = master_handle.read_bits(x, 121)
        # Write registers on slave Modbus server
        slave_handle.write_bits(x, 121, master_data)
    # Remaining registers
    master_data = master_handle.read_bits(end - (end % 121), end % 121)
    # Write registers on slave Modbus server
    slave_handle.write_bits(end - (end % 121), 121, master_data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--master-host", help="Host of master Modbus server")
    parser.add_argument("--master-port", type=int, help="Port of master Modbus server")
    parser.add_argument("--slave-host", help="Host of slave Modbus server")
    parser.add_argument("--slave-port", type=int, help="Port of slave Modbus server")
    parser.add_argument("--registers-start", type=int, help="Start Modbus registers address")
    parser.add_argument("--registers-end", type=int, help="End Modbus registers address")
    parser.add_argument("--coils-start", type=int, help="Start Modbus coils address")
    parser.add_argument("--coils-end", type=int, help="End Modbus coils address")
    args = parser.parse_args()

    # PLC handlers
    master_handle = pylibmodbus.ModbusTcp(args.master_host, args.master_port)
    master_handle.connect()

    slave_handle = pylibmodbus.ModbusTcp(args.slave_host, args.slave_port)
    slave_handle.connect()

    # Synchronization
    registers_synchro(master_handle, slave_handle, args.registers_start, args.registers_end)
    coils_synchro(master_handle, slave_handle, args.coils_start, args.coils_end)

if __name__ == '__main__':
    main()
