from django.urls import path, include
from . views import (MainAPIView, contact,
     BannerListCreateAPIView,
    BannerRetrieveUpdateDestroyAPIView,
    FooterBottomListCreateAPIView,
    FooterBottomRetrieveUpdateDestroyAPIView,
    FooterBottomImgCreateAPIView,)

urlpatterns = [
    path('', MainAPIView.as_view(), name='index'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('user/', include('Goods.user.urls')),
    path('contact/', contact, name='contact'),
    

    path('api/banners/', BannerListCreateAPIView.as_view(), name='banner_list_create'),
    path('api/banners/<int:pk>/', BannerRetrieveUpdateDestroyAPIView.as_view(), name='banner_detail'),
    path('api/footer-bottom/', FooterBottomListCreateAPIView.as_view(), name='footer_bottom_list_create'),
    path('api/footer-bottom/<int:pk>/', FooterBottomRetrieveUpdateDestroyAPIView.as_view(), name='footer_bottom_detail'),
    path('api/footer-bottom-img/', FooterBottomImgCreateAPIView.as_view(), name='footer_bottom_img_create'),



    # path('banners/', views.banner_list, name='banner_list'),
    # path('banners/create/', views.banner_create, name='banner_create'),
    # path('banners/<int:pk>/update/', views.banner_update, name='banner_update'),
    # path('banners/<int:pk>/delete/', views.banner_delete, name='banner_delete'),
    #
    # path('footer', views.footer_bottom_list, name='footer_bottom_list'),
    # path('detail/<int:pk>/', views.footer_bottom_detail, name='footer_bottom_detail'),
    # path('create/', views.footer_bottom_create, name='footer_bottom_create'),
    # path('update/<int:pk>/', views.footer_bottom_update, name='footer_bottom_update'),
    # path('delete/<int:pk>/', views.footer_bottom_delete, name='footer_bottom_delete'),
    # path('img/create/', views.footer_bottom_img_create, name='footer_bottom_img_create'),
]
