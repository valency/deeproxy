from rest_framework import serializers


# View serializers

class ProxyHtmlGetViewSerializer(serializers.Serializer):
    url = serializers.URLField()


class ProxyImageGetViewSerializer(serializers.Serializer):
    url = serializers.URLField()
