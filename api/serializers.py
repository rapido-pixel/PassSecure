from rest_framework import serializers
from pass_manager.models import PassCard, Folder


class PassCardSerializer(serializers.ModelSerializer):
    folder = serializers.CharField(allow_blank=True)

    class Meta:
        model = PassCard
        fields = ['folder', 'id', 'name', 'username', 'password', 'site']


class FolderSerializer(serializers.HyperlinkedModelSerializer):
    cards_in_folder = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Folder
        fields = ['id', 'name', 'cards_in_folder']
