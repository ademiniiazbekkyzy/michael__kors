from rest_framework import serializers
from product.models import Product, Category, Rating, Image


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RatingSerializers(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Rating
        fields = ['rating', "owner"]


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ProductImageSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['owner', 'name', 'description', 'price', 'category', 'images']
        read_only_fields = ["id"]

    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        product = Product.objects.create(**validated_data)
        for image in images_data.getlist('images'):
            Image.objects.create(product=product, image=image)
        return product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        rating_result = 0
        for i in instance.rating.all():
            rating_result += int(i.rating)

        if instance.rating.all().count() == 0:
            representation['rating'] = rating_result
        else:
            representation['rating'] = rating_result / instance.rating.all().count()
        return representation


# class CommentsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Comment
#         fields = ['id', 'user', 'comment_text', 'post']
#         read_only_fields = ['user', ]
#
#     def to_representation(self, instance):
#         representation = super(CommentsSerializer, self).to_representation(instance)
#         representation['user'] = instance.user.email
#         representation['post'] = instance.post.name
#         return representation


# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = '__all__'
#         read_only_fields = ['user', ]
#
#     # def get_total_likes(self, instance):
#     #     return instance.liked_by.count()
#     def create(self, validated_data):
#         print("*****", validated_data)
#         obj, created = Like.objects.get_or_create(**validated_data)
#         return obj
#     # def to_representation(self, instance):
#     #     representation = super(LikeSerializer, self).to_representation(instance)
#     #     like_result = 0
#     #     for i in instance.likes.all():
#     #         like_result += int(i.likes)
#     #     if instance.rating.all().count() == 0:
#     #         representation['likes'] = like_result
