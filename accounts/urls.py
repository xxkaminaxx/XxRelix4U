from django.conf.urls import url, include
from accounts.views import logout, login, user_registration, personal_profile
from accounts import url_reset

# account related urls here then imported into main url. 

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^user_registration/', user_registration, name="user_registration"),
    url(r'^password-reset/', include(url_reset))
]
