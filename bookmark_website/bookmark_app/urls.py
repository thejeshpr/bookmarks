from django.urls import path

from . import views

app_name = 'bookmark_app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('new-bookmark', views.BookmarkCreateView.as_view(), name='bookmark-create'),
    path('category', views.CategoryListView.as_view(), name='category-list'),
    path('new-catgory', views.CategoryCreateView.as_view(), name='category-add'),
    # path('car/<int:pk>', views.CarDetailView.as_view(), name='car-details'),
    # path('car/<int:pk>/update', views.CarUpdateView.as_view(), name='car-update'),
    # path('car/<int:pk>/delete', views.CarDeleteView.as_view(), name='car-delete'),
    
    # path('listing/add', views.ListingCreateView.as_view(), name='listing-add'),
    # path('car/<int:cpk>/listing/add', views.ListingCreateView.as_view(), name='listing-add'),
    # path('car/<int:cpk>/listing/<int:pk>', views.ListingDetailView.as_view(), name='listing-details'),
    # path('car/<int:cpk>/listing/<int:pk>/update', views.ListingUpdateView.as_view(), name='listing-update'),
    # path('car/<int:cpk>/listing/<int:pk>/delete', views.ListingDeleteView.as_view(), name='listing-delete'),

    # path('car/<int:cpk>/booking/add', views.BookingCreateView.as_view(), name='booking-add'),
    # path('car/<int:cpk>/booking/<int:pk>', views.BookingDetailView.as_view(), name='booking-details'),
    # path('car/<int:cpk>/booking/<int:pk>/update', views.BookingUpdateView.as_view(), name='booking-update'),
    # path('car/<int:cpk>/booking/<int:pk>/delete', views.BookingDeleteView.as_view(), name='booking-delete'),
    
    # path('car/<int:cpk>/downtime/add', views.DowntimeCreateView.as_view(), name='downtime-add'),
    # path('car/<int:cpk>/downtime/<int:pk>', views.DowntimeDetailView.as_view(), name='downtime-details'),
    # path('car/<int:cpk>/downtime/<int:pk>/update', views.DowntimeUpdateView.as_view(), name='downtime-update'),
    # path('car/<int:cpk>/downtime/<int:pk>/delete', views.DowntimeDeleteView.as_view(), name='downtime-delete'),
]