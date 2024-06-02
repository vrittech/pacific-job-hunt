from ..models import MySocialMedia
from ..serializers.my_social_media_serializers import MySocialMediaListSerializers,MySocialMediaRetrieveSerializers,MySocialMediaWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class MySocialMediaViewset(viewsets.ModelViewSet):
    serializer_class = MySocialMediaListSerializers
    # permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = MySocialMedia.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {
    #     'user':['exact'],
    # }
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)
    
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return MySocialMediaWriteSerializers
        elif self.action in ['retrieve']:
            return MySocialMediaRetrieveSerializers
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if is_many:
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        if is_many:
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if is_many:
            instances = []
            for item in request.data:
                instance = self.get_object_from_data(item)
                serializer = self.get_serializer(instance, data=item, partial=kwargs.get('partial', False))
                serializer.is_valid(raise_exception=True)
                instances.append(serializer)

            for serializer in instances:
                self.perform_update(serializer)

            return Response([serializer.data for serializer in instances])
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)

    def get_object_from_data(self, data):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup_value = data.get(self.lookup_field)
        filter_kwargs = {self.lookup_field: lookup_value}
        obj = self.queryset.filter(**filter_kwargs).first()
        if not obj:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_update(self, serializer):
        serializer.save()

    
    # @action(detail=False, methods=['get'], name="MySocialMedias", url_path="job-seekers")
    # def MySocialMedias(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    