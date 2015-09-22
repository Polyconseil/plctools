plctools
========

Collection of tools to talk to a PLC


plc_dump
--------

`plc_dump` is used on polybox to dump the content of a PLC into a file.

Usage:

   plc_dump.py --host 192.168.0.10 --port 502 --file bollene.plc


plc_load
--------

`plc_load` is used on your own computer to load the previous dump into your `modbus-server`.

Usage:

    plc_load --host 127.0.0.1 --port 502 --file abidjan.plc



