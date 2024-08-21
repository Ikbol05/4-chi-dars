from rest_framework import serializers
from OnlineShop.Goods.models import Category, Product, Cart

from OnlineShop.Goods.models import CustomUser



from rest_framework import serializers
from OnlineShop.Goods.models import Banner, Category, ProductImg, FeatureProduct, RecentArticles, SideMenu, FooterBottom, FooterBottomImg

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = '__all__'

class FeatureProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureProduct
        fields = '__all__'

class RecentArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentArticles
        fields = '__all__'

class SideMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideMenu
        fields = '__all__'


class FooterBottomSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterBottom
        fields = '__all__'

class FooterBottomImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterBottomImg
        fields = '__all__'




#============================

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'img']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'category', 'description']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'author', 'is_active', 'shopping_date']
