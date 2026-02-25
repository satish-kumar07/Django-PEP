from django.urls import path
from app.views import *

urlpatterns = [
    path("",home,name="index"),
    path("home",home,name="index"),
    path("about",about,name="about"),
    path("save_data",saveDataView,name="save_data"),
    path("indexView",indexView,name="indexView"),
    path("deleteView",deleteView,name="deleteview"),
    path("deleteView/<int:id>",deleteView,name="deleteView"),
    path("editView/<int:id>",editView,name="editView"),
    path("update-note/<int:id>", updateViewpage, name="updateViewpage"),
    path("update-data/<int:id>", updateDataView, name="updateDataView"),

    

]