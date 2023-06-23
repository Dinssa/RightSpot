from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('locations/index/', views.locations_index, name='locations_index'),
  path('decks/', views.decks_index, name='decks'),
  path('projects/', views.projects_index, name='projects'),
  path('compare/', views.compare, name='compare'),
  path('locations/', views.location_detail, name='location_detail'),
  path('locations/<int:location_id>/', views.saved_location_detail, name='saved_location_detail'),
  path('decks/<int:deck_id>/', views.deck_detail, name='deck_detail'),
  path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
  path('location/create/', views.LocationCreate.as_view(), name='location_create'),
  path('deck/create/', views.DeckCreate.as_view(), name='deck_create'),
  path('project/create/', views.ProjectCreate.as_view(), name='project_create'),
  path('location/<int:pk>/update/', views.LocationUpdate.as_view(), name='location_update'),
  path('deck/<int:pk>/update/', views.DeckUpdate.as_view(), name='deck_update'),
  path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
  path('location/<int:pk>/delete/', views.LocationDelete.as_view(), name='location_delete'),
  path('deck/<int:pk>/delete/', views.DeckDelete.as_view(), name='deck_delete'),
  path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('faq/', views.faq, name='faq'),
  path('legal/', views.legal, name='legal'),
  path('settings/', views.settings, name='settings'),
]