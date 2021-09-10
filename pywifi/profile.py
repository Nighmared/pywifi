#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Define WiFi Profile."""

from .const import *


class Profile():

    def __init__(self):

        self.id = 0
        self.auth = Auth.OPEN
        self.akm = [AKM.NONE]
        self.cipher = Cipher.NONE
        self.ssid: str = None
        self.bssid: str = None
        self.key: str = None
        self.signal: int = None
        self.freq: int = None


    def process_akm(self):

        if len(self.akm) > 1:
            self.akm = self.akm[-1:]

    def __eq__(self, profile):

        if profile.ssid:
            if profile.ssid != self.ssid:
                return False

        if profile.bssid:
            if profile.bssid != self.bssid:
                return False

        if profile.auth:
            if profile.auth!= self.auth:
                return False

        if profile.cipher:
            if profile.cipher != self.cipher:
                return False

        if profile.akm:
            if set(profile.akm).isdisjoint(set(self.akm)):
                return False

        return True
