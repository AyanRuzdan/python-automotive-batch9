# user defined modules

# builtin modules

# 3rd party modules

# package module directly containing multiple modules


# can is Control Area Network
import can

network = can.interface.Bus(bustype="virtual", channel="jio")
print(network)