import hashlib

import win32clipboard

from .hwid import *
from .encryption import *

import requests

from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import binascii
from uuid import uuid4

import win32api

import os

import datetime

import ssl
import socket


class api:
    name = ownerid = secret = version = ""

    def __init__(self, version):
        self.name = ""

        self.ownerid = ""

        self.secret = ""

        # TO AVOID CRACK, GET KEYAUTH OR YOUR AUTH SHA256 HASH
        self.sha256KeyAuth = "d5671326587478d7ea68acd412f8f4263803b333ac9b58dbad04fb66f7d4a895"

        self.version = str(version)
        self.init()

    sessionid = enckey = ""
    initialized = False

    def init(self):

        if self.sessionid != "":
            time.sleep(2)
            exit(0)
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        self.enckey = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify(("init").encode()),
            "ver": Encryption.encrypt(self.version, self.secret, init_iv),
            "hash": "",
            "enckey": Encryption.encrypt(self.enckey, self.secret, init_iv),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv
        }

        response = self.__do_request(post_data)

        if response == "KeyAuth_Invalid":
            win32api.MessageBox(0, 'Error!\n\nThis app does not exist.',
                                'Alert', 0x00000040)
            os._exit(1)
        response = Encryption.decrypt(response, self.secret, init_iv)

        if response["message"] == "invalidver":
            if response["download"] != "":
                win32api.MessageBox(0, 'New Version Available!\n\n Click OK to download it.',
                                    'Alert', 0x00000010)
                download_link = response["download"]
                os.system(f"start {download_link}")

            else:
                win32api.MessageBox(0, 'New Version Available!\n\nPlease, check discord.',
                                    'Alert', 0x00000040)
            os._exit(1)

        if not response["success"]:
            win32api.MessageBox(0, f'Error!\n\n{response["message"]}',
                                'Alert', 0x00000040)
            os._exit(1)

        self.sessionid = response["sessionid"]
        self.initialized = True
        self.__load_app_data(response["appinfo"])

    def license(self, key):
        self.checkinit()
        hwid = getHWID()

        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify(("license").encode()),
            "key": Encryption.encrypt(key, self.enckey, init_iv),
            "hwid": Encryption.encrypt(hwid, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv
        }

        response = self.__do_request(post_data)
        response = Encryption.decrypt(response, self.enckey, init_iv)

        if not response["success"]:
            if response["message"] == "This program hash does not match, make sure you're using latest version":
                return {"new_version": True}
            elif response["message"] == "VPNs are blocked on this application":
                return {"vpn": True}
            elif response["message"] == "Invalid license key":
                return {"invalid_token": True}
            elif response["message"] == "License key has already been used":
                return {"key_used": True}
            elif response["message"] == "Your license is banned":
                return {"license_banned": True}
            elif response["message"] == "HWID doesn't match. Ask for a HWID reset":
                return {"hwid": True}
            elif response["message"] == "There is no subscription created for your key level. Contact application developer.":
                return {"expired": True}
            elif response["message"] == "The user is banned":
                return {"license_banned": True}
            elif response["message"] == "Your subscription is paused and can't be used right now":
                return {"key_paused": True}
            elif response["message"] == "VPNs are disallowed on this application":
                return {"vpn": True}
            elif response["message"] == "VPNs are disallowed on this application":
                return {"vpn": True}
            else:
                return {"error": True}

        elif response["success"]:
            timeleft = int(response["info"]["subscriptions"][0]["timeleft"])
            if timeleft > 99999999:
                timeleft = "Lifetime"

            expiry = response["info"]["subscriptions"][0]["expiry"]

            return {"expiry": timeleft, "expiry_date": float(expiry)}

    def var(self, name):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify(("var").encode()),
            "varid": Encryption.encrypt(name, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv
        }

        response = self.__do_request(post_data)

        response = Encryption.decrypt(response, self.enckey, init_iv)

        if response["success"]:
            return response["message"]
        else:
            win32api.MessageBox(0, f'Error!\n\n{response["message"]}',
                                'Alert', 0x00000040)
            os._exit(1)

    def getvar(self, var_name):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify(("getvar").encode()),
            "var": Encryption.encrypt(var_name, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv
        }
        response = self.__do_request(post_data)
        response = Encryption.decrypt(response, self.enckey, init_iv)

        if response["success"]:
            content = response["response"]
            if content == "true" or content == "false":
                content = json.loads(content)
            return content
        else:
            return False

    def setvar(self, var_name, var_data):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {
            "type": binascii.hexlify(("setvar").encode()),
            "var": Encryption.encrypt(var_name, self.enckey, init_iv),
            "data": Encryption.encrypt(var_data, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv
        }
        response = self.__do_request(post_data)
        response = Encryption.decrypt(response, self.enckey, init_iv)

        if response["success"]:
            return True
        else:
            win32api.MessageBox(0, f'Error!\n\n{response["message"]}',
                                'Alert', 0x00000040)
            os._exit(1)

    def checkinit(self):
        if not self.initialized:
            win32api.MessageBox(0, f'Error!\n\nInitialize first, in order to use the functions',
                                'Alert', 0x00000040)
            os._exit(1)

    def __do_request(self, post_data):
        hostname = 'keyauth.win'
        port = 443

        context = ssl.create_default_context()
        try:
            with socket.create_connection((hostname, port)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                    cert = secure_sock.getpeercert(binary_form=True)
                    sha256_fingerprint = hashlib.sha256(cert).hexdigest()

                    if sha256_fingerprint != self.sha256KeyAuth:
                        # Save the new hash to clipboard
                        win32clipboard.OpenClipboard()
                        win32clipboard.EmptyClipboard()
                        win32clipboard.SetClipboardText(sha256_fingerprint)
                        win32clipboard.CloseClipboard()

                        # Improved error message
                        error_message = (
                            "SSL Certificate Error: The server's certificate fingerprint has changed.\n\n"
                            "New fingerprint: {}\n\n"
                            "The new fingerprint has been copied to your clipboard. "
                            "Please verify with an administrator and update the application if necessary."
                        ).format(sha256_fingerprint)

                        win32api.MessageBox(0, error_message, 'Security Alert', 0x00000010 | 0x00000001)
                        raise ssl.SSLCertVerificationError("SSL certificate verification failed")

            rq_out = requests.post(
                "https://keyauth.win/api/1.0/", data=post_data
            )

            return rq_out.text

        except Exception as e:
            # Handle other potential errors
            error_message = "An error occurred: {}".format(str(e))
            win32api.MessageBox(0, error_message, 'Error', 0x00000010)
            raise

    class application_data_class:
        numUsers = numKeys = app_ver = customer_panel = onlineUsers = ""

    # region user_data
    class user_data_class:
        username = ip = hwid = expires = createdate = lastlogin = subscription = ""

    user_data = user_data_class()
    app_data = application_data_class()

    def __load_app_data(self, data):
        self.app_data.numUsers = data["numUsers"]
        self.app_data.numKeys = data["numKeys"]
        self.app_data.app_ver = data["version"]
        self.app_data.customer_panel = data["customerPanelLink"]
        self.app_data.onlineUsers = data["numOnlineUsers"]

    def __load_user_data(self, data):
        self.user_data.username = data["username"]
        self.user_data.ip = data["ip"]
        self.user_data.hwid = data["hwid"]
        self.user_data.expires = data["subscriptions"][0]["expiry"]
        self.user_data.createdate = data["createdate"]
        self.user_data.lastlogin = data["lastlogin"]
        self.user_data.subscription = data["subscriptions"][0]["subscription"]
        self.user_data.subscriptions = data["subscriptions"]
