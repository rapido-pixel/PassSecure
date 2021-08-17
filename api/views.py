from rest_framework import generics
from api.serializers import PassCardSerializer, FolderSerializer
from pass_manager.models import PassCard, Folder
from django.core.exceptions import ObjectDoesNotExist


class FolderList(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class FolderDetail(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class PassCardList(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = PassCard.objects.all()
    serializer_class = PassCardSerializer

    def perform_create(self, serializer):
        folder_name = serializer.validated_data['folder']
        try:
            folder_name = Folder.objects.get(name=folder_name)
            serializer.save(folder=folder_name)
        except ObjectDoesNotExist:
            Folder.objects.create(name=folder_name)
            folder_name = Folder.objects.get(name=folder_name)
            serializer.save(folder=folder_name)


class PassCardDetail(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = PassCard.objects.all()
    serializer_class = PassCardSerializer

    def perform_update(self, serializer):
        folder_name = serializer.validated_data['folder']
        try:
            folder_name = Folder.objects.get(name=folder_name)
            serializer.save(folder=folder_name)
        except ObjectDoesNotExist:
            Folder.objects.create(name=folder_name)
            folder_name = Folder.objects.get(name=folder_name)
            serializer.save(folder=folder_name)

