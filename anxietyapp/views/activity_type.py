from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from anxietyapp.models import ActivityType

class ActivityTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ActivityType
        url = serializers.HyperlinkedIdentityField(
            view_name='activitytype-detail',
            lookup_field='id'
        )
        fields = ('id', 'name', 'url')

class ActivityTypeView(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            activity_type = ActivityType.objects.get(pk=pk)
            serializer = ActivityTypeSerializer(activity_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

        
    def list(self, request):
        
        activity_type = ActivityType.objects.all()

        serializer = ActivityTypeSerializer(
            activity_type, many=True, context={'request': request})
        return Response(serializer.data)