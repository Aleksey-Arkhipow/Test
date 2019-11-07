from django.urls import path 

from .views import BBLoginView

app_name = 'main'
urlpatterns = [
	path('accounts/login/', BBLoginView.as_view(), name='login'),
	
]