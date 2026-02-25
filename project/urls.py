
from django.contrib import admin
from django.urls import path, include
# def LPU(req):
#     return HttpResponse("LPU is the best university in the world!")

# def aboutLPU(req):
#     return HttpResponse("Lovely Professional University, located in Punjab.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("app.urls"))        
]
