from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from anxietyapp.mixins import PaginationMixin
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from django.contrib.auth.models import User
from anxietyapp.models import ActivityType, ActivityDetail




class ActivityDetailSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ActivityDetail
        url = serializers.HyperlinkedIdentityField(
            view_name='activitydetail',
            lookup_field='id'
        )
        fields = ('id', 'user_id', 'activity_type', 'rating', 'note', 'created_at')
        depth = 1



class ActivityDetailView(ViewSet):
   
    

    def create(self, request):

        # user = User.objects.get(pk=request.data["user_id"])
        activity_type = ActivityType.objects.get(
            pk=request.data["activity_type_id"])

        new_activity_detail = ActivityDetail()
        new_activity_detail.activity_type = activity_type
        new_activity_detail.user = request.auth.user
        if "note" in request.data:
            new_activity_detail.note = request.data["note"]
        if "rating" in request.data:
            new_activity_detail.rating = request.data["rating"]

        new_activity_detail.save()

        serializer = ActivityDetailSerializer(
            new_activity_detail, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
       
        try:
            activity_detail = ActivityDetail.objects.get(pk=pk)
            serializer = ActivityDetailSerializer(
                activity_detail, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        
        activity_detail = ActivityDetail.objects.filter(user=request.auth.user)
        serializer = ActivityDetailSerializer(
            activity_detail,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


    def destroy(self, request, pk=None):
       
        try:
            activity_detail = ActivityDetail.objects.get(pk=pk)
            activity_detail.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ActivityDetail.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        
        activity_detail = ActivityDetail.objects.get(pk=pk)
        activity_detail.note = request.data["note"]
        activity_detail.rating = request.data["rating"]
        activity_detail.save()

        return Response({}, status=status.HTTP_202_ACCEPTED)

    
class LimitedActivityListView(APIView, PaginationMixin):
    serializer_class = ActivityDetailSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 
    def get(self, request):
        
        queryset = ActivityDetail.objects.filter(user=request.auth.user).order_by("-created_at")
        page = self.paginate_queryset(queryset)
        if page is not None:

            serializer = self.serializer_class(
                page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
