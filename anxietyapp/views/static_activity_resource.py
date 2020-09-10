from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from anxietyapp.models import StaticActivityResource, ActivityType

class StaticActivityResourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StaticActivityResource
        url = serializers.HyperlinkedIdentityField(
            view_name='staticactivityresource-detail',
            lookup_field='id'
        )
        fields = ('id', 'resource', 'url', 'activity_type_id')

class StaticActivityResourceView(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            static_activity_resource = StaticActivityResource.objects.get(pk=pk)
            serializer = StaticActivityResourceSerializer(static_activity_resource, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

        
    def list(self, request):
        
        static_activity_resource = StaticActivityResource.objects.all()

        serializer = StaticActivityResourceSerializer(
            static_activity_resource, many=True, context={'request': request})
        return Response(serializer.data)