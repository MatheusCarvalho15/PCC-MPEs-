
from django.contrib import admin
from django.contrib.auth import urls
from django.urls import include, path

urlpatterns = [
    path('accounts/', include("accounts.urls")),
    path('accounts/', include(urls)),
    path("despesas/", include("despesas.urls")),
    path("admin/", admin.site.urls),

]