from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Include your app URLs
    path('', RedirectView.as_view(url='/myapp/')),  # Redirect root URL to your app
]
