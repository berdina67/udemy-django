from django.urls import path, include
from .views import index, contact, about, services, portfolio, blog, blog_single, pricing, team, faq

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('blog/', blog, name='blog'),
    path('blog-single/', blog_single, name='blog_single'),
    path('pricing/', pricing, name='pricing'),
    path('team/', team, name='team'),
    path('faq/', faq, name='faq'),
]

