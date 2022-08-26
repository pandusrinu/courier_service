from django.urls import path


urlpatterns = [
    path("", path.CourierServiceListView.as_view(), name='index'),
    path('create/', path.CourierServiceListView.as_view()),
    path('update/<int:pk>', path.CourierServiceListView.as_view()),
    path('delete/<int:pk>', path.CourierServiceListView.as_view()),
    path('signup/', path.signup_view, name='signup'),
    path('login/', path.login_request, name='login'),
    path('logout/', path.logout_request, name='logout'),

]