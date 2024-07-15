from django.urls import path

from .views import http_api,dynamic_api,html_api,read_all_views,create_view,update_view,delete_view
urlpatterns = [
    path('http-api/',http_api,name="http_api"),
    path('dynamic-api/<name>/',dynamic_api,name="dynamic_api"),
    path('html-api/',html_api,name="html_api"),  # render a basic HTML template
    path('course-list-api/',read_all_views,name="read_all_views"),
    path('create-course-api/',create_view,name="create_view"),  # create a new course record in the database using POST request data.
    path('update-course-api/<id>/',update_view,name="update_view"),  # update an existing course record in the database using POST request data.
    path('delete-course-api/<id>/',delete_view,name="delete_view"),  # delete a course record from the database using the provided id.
]