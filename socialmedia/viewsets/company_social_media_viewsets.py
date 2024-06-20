from ..models import CompanySocialMedia
from ..serializers.company_social_media_serializers import CompanySocialMediaListSerializers,CompanySocialMediaRetrieveSerializers,CompanySocialMediaWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

class CompanySocialMediaViewset(viewsets.ModelViewSet):
    serializer_class = CompanySocialMediaListSerializers
    permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = CompanySocialMedia.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {
    #     'user':['exact'],
    # }
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update','CompanySocialMediasCreate']:
            return CompanySocialMediaWriteSerializers #please implement permissions, not secure
        elif self.action == "CompanySocialMediasCreate":
            return CompanySocialMediaWriteSerializers
        elif self.action in ['retrieve']:
            return CompanySocialMediaRetrieveSerializers
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
        partial=kwargs.get('partial', False)
        if is_many:
            instances = []
            for item in request.data:
                serializer = self.update_from_CompanySocialMediasCreate(request,item,partial)
                instances.append(serializer)

            for serializer in instances:
                self.perform_update(serializer)

            return Response({'message':"saved"})
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
    
    @action(detail=False, methods=['post'], name="CompanySocialMediasCreate", url_path="bulk-save")
    def CompanySocialMediasCreate(self, request, *args, **kwargs):
        instances = []
        partial=kwargs.get('partial', False)
        for item in request.data:
            if item.get('id'):
                serializer = self.update_from_CompanySocialMediasCreate(request,item,partial)
            else:
                serializer = self.get_serializer(data=item)
                serializer.is_valid(raise_exception=True)
                serializer = self.perform_create(serializer)

            instances.append(serializer)

        return Response({'message':"saved"})


    def update_from_CompanySocialMediasCreate(self,request,item,partial):
        instance = self.get_queryset().get(id=item.get('id'),user = request.user)
        serializer = self.get_serializer(instance, data=item, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return serializer
    
