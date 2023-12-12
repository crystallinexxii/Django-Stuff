
from django.urls import path
from . import views
from django.conf import settings   
from django.conf.urls.static import static



urlpatterns=[
    path('',views.main),
    path('projects/<slug:project_id>', views.project_details, name='project_details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)