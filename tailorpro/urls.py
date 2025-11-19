<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # All pages + all API come from orders.urls
    path('', include('orders.urls')),
]
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # All pages + all API come from orders.urls
    path('', include('orders.urls')),
]
>>>>>>> 25ebfac29b52da4c94d0490e2f97baf08cb66efc
