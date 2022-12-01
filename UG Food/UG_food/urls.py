from django.contrib import admin
from django.urls import path
from django.urls import include
from registration.backends.simple.views import RegistrationView
from UG_food_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('UG_food:register_profile')

urlpatterns = [
    path('', views.index, name='index'),
    path('UG_food/', include('UG_food_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

