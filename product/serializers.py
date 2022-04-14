from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    owner = Serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Product
        fields = '__all__'
