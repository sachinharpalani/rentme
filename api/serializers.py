from rest_framework import serializers
from api.models import Customer,Item,Category

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('user_id','cat_id','title','description','terms','location','delivery','deposit','cost_per_week')
