from django.urls import path
from .views import post_create, post_view, post_detail, post_list, post_update, post_delete
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('create/', post_create, name='create'),
    path('', post_list, name='list'),
    path('post/update/<int:id>',post_update,name='detailowner'),
    path('post/delete/<int:id>',post_delete,name='post_delete'),
    path("post/detail/<int:id>", post_detail, name="post_detail"),
    path("post/update/<int:id>", post_update, name="post_update"),
    path("post/view/<int:id>", post_view, name="post_view"),

    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

