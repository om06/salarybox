from rest_framework import serializers


class FileUploadSerializer(serializers.Serializer):
    """
    Reference: https://stackoverflow.com/questions/57483114/drf-upload-csv-file-then-iterate-over-each-row
    """
    file = serializers.FileField()

    class Meta:
        fields = ('file',)