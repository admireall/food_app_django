from . import views
from django.urls import path
app_name='food'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
   # path('<int:item_id>/',views.detail,name='details'),
    path('add/',views.create_class.as_view(),name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    path('<int:pk>/',views.Detail_class.as_view(),name='details'),
]