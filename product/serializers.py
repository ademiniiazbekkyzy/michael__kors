
from rest_framework import serializers

from product.models import Product, Category, Rating, Image


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class Ratingserializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields ='rating'


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ProductImageSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'owner', 'descriprion', 'images', 'price', 'rating')

    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        product = Product.object.create(**validated_data)
        for image in images_data.getlist('images'):
            Image.objects.create(product=product, image=image)
        return product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        rating_result = 0
        for i in instance.rating.all():
            rating_result += int(i.rating)
        if instance.rating.all().count()==0:
            representation['rating'] = rating_result
        else:
            representation['rating'] = rating_result / instance.rating.all().count()
        print(rating_result)
        return representation
