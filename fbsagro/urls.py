from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grupo_prop.urls')),  # 👈 isso faz o Django enxergar as rotas do seu app
]
