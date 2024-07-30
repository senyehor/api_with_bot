from rest_framework.serializers import ModelSerializer

from .models import Breed, Cat


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class CatSerializer(ModelSerializer):
    breed = BreedSerializer()

    class Meta:
        model = Cat
        fields = ('id', 'name', 'breed', 'description_from_owner')
        read_only_fields = ('id', 'breed',)
