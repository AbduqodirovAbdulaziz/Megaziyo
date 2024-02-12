from django.contrib import admin
from django.urls import path
from oquv_markaz.views import *

urlpatterns = [
    path('batafsil/', batafsil),

    path('admin/', admin.site.urls),
    path('hamma_yonalish/', hamma_yonalish),
    path('hamma_xona/', hamma_xona),
    path('hamma_ustoz/', hamma_ustoz),
    path('hamma_guruh/', hamma_guruh),
    path('hamma_oquvchi/', hamma_oquvchi),
    path('hamma_tolov/', hamma_tolov),

    # Ma'lumot qo'shsih

    path('yonalish_add/', yonalish_add),
    path('xona_add/', xona_add),
    path('ustoz_add/', ustoz_add),
    path('guruh_add/', guruh_add),

    # forms bilan
    path('oquvchi_add/', oquvchi_add),
    path('tolov_add/', tolov_add),

    # ---------------delete qilish-------------
    path('yonalish/<int:pk>/delete/', yonalish_delete),
    path('xona/<int:pk>/delete/', xona_delete),
    path('guruh/<int:pk>/delete/', guruh_delete),
    path('ustoz/<int:pk>/delete/', ustoz_delete),
    path('oquvchi/<int:pk>/delete/', oquvchi_delete),
    path('tolov/<int:pk>/delete/', tolov_delete),

    # -----------------------Tahrirlash---------------------
    path('yonalish/<int:pk>/tahrirlash/', yonalish_edit),
    path('xona/<int:pk>/tahrirlash/', xona_edit),
    path('ustoz/<int:pk>/tahrirlash/', ustoz_edit),
    path('guruh/<int:pk>/tahrirlash/', guruh_edit),
    path('oquvchi/<int:pk>/tahrirlash/', oquvchi_edit),
    path('tolov/<int:pk>/tahrirlash/', tolov_edit),


    path('edit_or_delete/', edit_or_delete),
    path('data_add/', data_add),




]
