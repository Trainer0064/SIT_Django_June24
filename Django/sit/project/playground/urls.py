from django.urls import path
from .views import first_api,json_api,dynamic_api,student_api,test_html,portfolio_home,portfolio_about,portfolio_projects,portfolio_skills,portfolio_details

urlpatterns = [
    path('first-api/',first_api,name='first-api'),
    path('json-api/',json_api,name='json-api'),
    path('dynamic-api/<str:name>/',dynamic_api,name='dynamic_api'),
    path('student-api/<int:roll_no>/',student_api,name='student_api'),
    # path('student-api/<str:str_data>/',student_api2,name='student_api2'),
    path('test-html/<int:attendance>/',test_html,name='test_html'),
    # Portfolio URL patterns
    path('portfolio-home/',portfolio_home,name="portfolio_home1"),
    path('portfolio-about/',portfolio_about,name="portfolio_about"),
    path('portfolio-projects/',portfolio_projects,name="portfolio_projects"),  
    path('portfolio-skills/',portfolio_skills,name="portfolio_skills"),
    path('portfolio-details/',portfolio_details,name = "portfolio_details") ,
]