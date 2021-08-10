from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainPage.as_view(), name='mainpage'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('sign-up/', views.CustomSignUpView.as_view(), name='sign-up'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create-card/', views.PassCardCreateView.as_view(), name='create-card'),
    path('edit/<slug:slug>/', views.EditCardView.as_view(), name='edit-card'),
    path('delete/<slug:slug>/', views.DeleteCardView.as_view(), name='delete-card'),
    path('<slug:slug>/', views.CardView.as_view(), name='card-info'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
