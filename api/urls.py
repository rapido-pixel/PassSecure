from django.urls import path
import api.views as views

urlpatterns = [
    path('folders/', views.FolderList.as_view()),
    path('folders/<int:pk>/', views.FolderDetail.as_view()),
    path('passcards/', views.PassCardList.as_view()),
    path('passcards/<int:pk>/', views.PassCardDetail.as_view()),

]
