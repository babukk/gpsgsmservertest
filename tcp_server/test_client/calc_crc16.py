#! /usr/bin/env python
#----------------------------------------------------------------------------------

import libscrc
import sys

print(format(libscrc.modbus(sys.argv[1].encode()), '04X'))
