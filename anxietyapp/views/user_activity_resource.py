from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from anxietyapp.models import UserActivityResource, ActivityType

class UserActivityResourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserActivityResource
        url = serializers.HyperlinkedIdentityField(
            view_name='useractivityresource-detail',
            lookup_field='id'
        )
        fields = ('id', 'resource', 'url', 'activity_type_id', 'user_id')

class UserActivityResourceView(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            user_activity_resource = UserActivityResource.objects.get(pk=pk)
            serializer = UserActivityResourceSerializer(user_activity_resource, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

        
    def list(self, request):
        
        user_activity_resource = UserActivityResource.objects.all()

        serializer = UserActivityResourceSerializer(
            user_activity_resource, many=True, context={'request': request})
        return Response(serializer.data)