from django.shortcuts import render
from . thirdparty_native_sdk import ThirdPartyNativeSDK

# Create your views here.



def process_data(request):
    sdk = ThirdPartyNativeSDK()
    sdk.initialize()
    sdk.process()
    return render(request, 'process_data.html')