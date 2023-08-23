from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog-detail/<int:pk>/', views.BlogDetail.as_view(), name="blog_detail"),
    path('techno-list/', views.TechnoView.as_view(), name='techno_list'),
    path('dailylife-list/', views.DailyLifeView.as_view(), name='dailylife_list'),
    path('music-list/', views.MusicView.as_view(), name='music_list'),
    path('portfolio-list/', views.PortfolioView.as_view(), name='portfolio_list'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
