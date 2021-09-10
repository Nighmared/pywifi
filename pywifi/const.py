#!/usr/bin/env python3
# vim: set fileencoding=utf-8
from enum import Enum
"""Constants used in pywifi library define here."""


# Define interface status.
class Iface(Enum):
    DISCONNECTED = 0
    SCANNING = 1
    INACTIVE = 2
    CONNECTING = 3
    CONNECTED = 4


# Define auth algorithms.
class Auth(Enum):
    OPEN = 0
    SHARED = 1


# Define auth key mgmt types.
class AKM(Enum):
    NONE = 0
    WPA = 1
    WPAPSK = 2
    WPA2 = 3
    WPA2PSK = 4
    UNKNOWN = 5


# Define ciphers.
class Cipher(Enum):
    NONE = 0
    WEP = 1
    TKIP = 2
    CCMP = 3
    UNKNOWN = 4


class Key(Enum):
    NETWORKKEY = 0
    PASSPHRASE = 1
