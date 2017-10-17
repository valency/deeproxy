import urllib.request

from django.http import HttpResponse
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from deeproxy.serializers import *


class ProxyHtmlView(APIView):
    """
    get:
        **Load HTML from Remote Host**

        - <span class='badge'>R</span> `url` Request URL
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request):
        pp = ProxyHtmlGetViewSerializer(data=request.GET)
        if pp.is_valid():
            url = pp.validated_data['url']
            response = urllib.request.urlopen(url)
            html = response.read()
            return Response({
                'url': url,
                'data': html
            })
        else:
            raise ParseError(pp.errors)


class ProxyImageView(APIView):
    """
    get:
        **Load Image from Remote Host**

        - <span class='badge'>R</span> `url` Request URL
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request):
        pp = ProxyImageGetViewSerializer(data=request.GET)
        if pp.is_valid():
            url = pp.validated_data['url']
            response = urllib.request.urlopen(url)
            img = response.read()
            content_type = response.info().get_content_type()
            return HttpResponse(img, content_type=content_type)
        else:
            raise ParseError(pp.errors)
