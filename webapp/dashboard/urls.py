from django.urls import path

from webapp.dashboard.views.dashboard import DashboardView

urlpatterns = {
    path('', DashboardView.as_view()),
}