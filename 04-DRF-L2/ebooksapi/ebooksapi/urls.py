from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),  #for log IN & OUT functionality{by default}
    path("api/", include("ebooks.api.urls"))
]
