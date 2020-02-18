from django.conf.urls import url, include
from accounts.views import logout, login, user_registration, personal_profile
from accounts import url_reset

# account related urls here then imported into main url. 

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', user_registration, name="registration"),
    url(r'^personal_profile/', personal_profile, name="personal_profile"),
    url(r'^password-reset/', include(url_reset))
]
