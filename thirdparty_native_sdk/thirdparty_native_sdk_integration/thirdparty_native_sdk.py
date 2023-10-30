import ctypes

class ThirdPartyNativeSDK:
    def __init__(self):
        self.lib = ctypes.CDLL('path/to/native/sdk/library')

    def initialize(self):
        self.lib.initialize()

    def process(self):
        self.lib.process()