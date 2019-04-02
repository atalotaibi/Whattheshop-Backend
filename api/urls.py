from django.urls import path
from .views import (
    UserCreateAPIView,
    CategorysList,
    CategoryDetail,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
    CartItemsList,
    CartItemDetail,
    CartItemCreate,
    CartItemUpdate,
    CartItemDelete,
)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('CategorysList', CategorysList.as_view(), name='CategorysList'),
    path('CategoryDetail/<int:Category_id>/',
         CategoryDetail.as_view(), name='CategoryDetail'),
    path('CategoryCreate/', CategoryCreate.as_view(), name='CategoryCreate'),
    path('CategoryUpdate/<int:Category_id>/',
         CategoryUpdate.as_view(), name='CategoryUpdate'),
    path('CategoryDelete/<int:Category_id>/',
         CategoryDelete.as_view(), name='CategoryDelete'),
    path('CartItemsList', CartItemsList.as_view(), name='CartItemsList'),
    path('CartItemDetail/<int:cartItem_id>/',
         CartItemDetail.as_view(), name='CartItemDetail'),
    path('CartItemCreate/', CartItemCreate.as_view(), name='CartItemCreate'),
    path('CartItemUpdate/<int:cartItem_id>/',
         CartItemUpdate.as_view(), name='CartItemUpdate'),
    path('CartItemDelete/<int:cartItem_id>/',
         CartItemDelete.as_view(), name='CartItemDelete'),

]
