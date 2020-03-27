from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('workload/', include('workload.urls')),
    path('admin/', admin.site.urls),
]
