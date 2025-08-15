from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from eventia_app import views

urlpatterns = [path('events-by-category/<str:category>/', views.events_by_category, name='events_by_category'),
               path('all-events/', views.all_events, name='all_events'),
               path('event/<int:pk>/', views.event_detail, name='event_detail'),]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
