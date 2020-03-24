from django.urls import path
from JobBoard.api.views import Jobdetail_Create_API_view,Joblist_Create_API_view
urlpatterns = [
                    #function based api view
    path("jobs/", Joblist_Create_API_view, name="job-list"),
    path("jobs/<int:pk>", Jobdetail_Create_API_view, name="job-detail")
]