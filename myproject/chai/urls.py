from os import name
from django.urls import path, re_path
from . import views


# this open as localhost:8000/chai
# we can make more views like order so it open like localhost:8000/chai/order
urlpatterns = [
    path('', views.All_chai, name='chai'),

    # using params in url
    path('order/<int:id>',views.order,name='order'),
    path('identity/<str:author>',views.identity,name='identity'),

    # to use simple slug which is same as re_path(r'^blog/(?P<slug>[a-zA-Z0-9_-]+)/$', views.Product_slug),
    # path('blog/<slug:slug>/',views.Product_slug,name='Product_slug')

    # when more authenticatio is needed like letter length, small letters and many more, any specific then use
    re_path(r'^blog/(?P<slug>[a-z0-9-]{3,50})/$', views.Product_slug, name='Product_slug'),

    path('student/',views.student_list,name='student_list'),

    path('greet/',views.greet,name='greet'),
    path('date/',views.show_date,name='show_date'),

    path('greetings/',views.g,name="g"),

    path('city',views.city,name="name"),

    path('monday/',views.monday_menu, name="views.monday_menu"),
    
    path("person/",views.office, name="office"),

    path("child/",views.child, name="child"),
    
    path("childlist/",views.childlist, name="childlist"),

    path("product/",views.product, name="product"),

  re_path(r'^contact/?$', views.contactview, name='contactform'),
  
  path('calculator/', views.calculator_view, name='calculator'),

  path('simpleForm/',views.simpleForm,name=
      'simpleForm'),

  path('formTemp/',views.formTemp,name='formTemp'),

  path('form1/',views.form1),

  path('valid/',views.validation),

  path('signup/',views.signup, name='signup'),
  path('signup1/',views.signup1, name='signup1'),
  path('signup2/',views.signup2,name="signup2"),
  path('delete/<int:id>',views.delete,name="delete"),
  path('edit/<int:id>',views.edit,name="edit"),
  path("insertBlog/",views.insertblogpost,name="insertblogpost"),
  path("showPosts/",views.blogposts,name="blogposts"),
  path("blogpost_detail/<int:id>",views.blogpost_detail,name="blogpost_detail"),
  re_path(r'^setCookie/?$', views.setCookie, name="setCookie"),
  re_path(r'^getCookie/?$', views.getCookie, name="getCookie"),
  re_path(r'^deleteCookie/?$', views.deleteCookie, name="deleteCookie"),

  path('post/<int:id>',views.me),
  path('greet/<str:name>/<int:age>',views.ad),
  path('<str:weather>/<str:city>',views.we)
]