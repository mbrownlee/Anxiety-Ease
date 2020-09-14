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

        # I never need a list of all resources together, only those filtered by activity type id
        # 8000/useractivityresource?activitytypeid=2
        user_resource_by_type = self.request.query_params.get('activitytypeid', None)
        # ^^ this will get me the activity type id of button clicked
        chosen_activity = ActivityType.objects.get(pk=user_resource_by_type)
        chosen_resources_by_type = UserActivityResource.objects.filter(activity_type=chosen_activity)

        serializer = UserActivityResourceSerializer(
            chosen_resources_by_type, many=True, context={'request': request})
        return Response(serializer.data)        
        
        