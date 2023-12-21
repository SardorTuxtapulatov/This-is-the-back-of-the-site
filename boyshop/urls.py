from django.urls import path
from .views import HomeView, ServiceView, AboutView, PortfolioView, ContactView

app_name = 'boyshop'

urlpatterns = [
    path('', HomeView.as_view(), name="home_page"),
    path('service/', ServiceView.as_view(), name="service_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('portfolio/', PortfolioView.as_view(), name='portfolio_page'),
    path('contact/', ContactView.as_view(), name='contact_page')

]