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

        # I never need a list of all resources together, only those filtered by activity type id
        # 8000/staticactivityresource?activitytypeid=2
        static_resource_by_type = self.request.query_params.get('activitytypeid', None)
        # ^^ this will get me the activity type id of button clicked
        chosen_activity = ActivityType.objects.get(pk=static_resource_by_type)
        chosen_resources_by_type = StaticActivityResource.objects.filter(activity_type=chosen_activity)

        serializer = StaticActivityResourceSerializer(
            chosen_resources_by_type, many=True, context={'request': request})
        return Response(serializer.data)

       