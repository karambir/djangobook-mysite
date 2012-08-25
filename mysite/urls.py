#TODO: Learn extending django-profiles to add your own form elements---> http://dewful.com/?p=70


from django.conf.urls.defaults import *
from basic.blog import views
#import satchmo_ext.productratings.models
from registration.backends.default.urls import *
from django.views.generic.simple import redirect_to
from django.contrib import admin
admin.autodiscover()

from basic.books.models import *

genre_list = {
    'queryset': Genre.objects.all(),
}
publisher_list = {
    'queryset': Publisher.objects.all(),
}
book_list = {
    'queryset': Book.objects.all(),
}


urlpatterns = patterns('mysite.views',
    (r'^$', 'hello'),
    (r'^time/$', 'current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    (r'^meta/$', 'display_meta'),
    (r'^color/$', 'set_color'),
    (r'^accounts/profile',redirect_to, {'url': '/profiles/'} ),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),
    #(r'^accounts/',redirect_to, {'url': '/accounts/login'} ),
    (r'^profiles/', include('profiles.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

"""
urlpatterns += patterns('mysite.contact.views',
    (r'^contact/$', 'contactview'),
    (r'^contact/thankyou/$', 'thankyou'),
)
"""

urlpatterns += patterns('mysite.books.views',
    (r'^search-form/$', 'search_form'),
    (r'^search/$', 'search'),
)

urlpatterns += patterns('mysite.colleges.views',
    (r'^search-page/$', 'search_page'),
    (r'^searchc/$', 'searchc'),
)


"""
from django.views.generic import DetailView, ListView
from mysite.polls.models import Poll

urlpatterns += patterns('mysite.polls.views',
    url(r'^polls/$',ListView.as_view(queryset=Poll.objects.order_by('-pub_date')[:5],context_object_name='latest_poll_list',template_name='polls/index.html')),
    url(r'^polls/(?P<pk>\d+)/$',DetailView.as_view(model=Poll,template_name='polls/detail.html')),
    url(r'^polls/(?P<pk>\d+)/results/$',DetailView.as_view(model=Poll,template_name='polls/results.html'),name='poll_results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
"""


urlpatterns += patterns('basic.blog.views',
    url(r'^blog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view='post_detail',
        name='blog_detail'
    ),
    url(r'blog/^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        view='post_archive_day',
        name='blog_archive_day'
    ),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\w{3})/$',
        view='post_archive_month',
        name='blog_archive_month'
    ),
    url(r'^blog/(?P<year>\d{4})/$',
        view='post_archive_year',
        name='blog_archive_year'
    ),
    url(r'^blog/categories/(?P<slug>[-\w]+)/$',
        view='category_detail',
        name='blog_category_detail'
    ),
    url (r'^blog/categories/$',
        view='category_list',
        name='blog_category_list'
    ),
    url(r'^blog/tags/(?P<slug>[-\w]+)/$',
        view='tag_detail',
        name='blog_tag_detail'
    ),
    url (r'^blog/search/$',
        view='search',
        name='blog_search'
    ),
    url(r'^blog/page/(?P<page>\d+)/$',
        view='post_list',
        name='blog_index_paginated'
    ),
    url(r'^blog/$',
        view='post_list',
        name='blog_index'
    ),
)


urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^books/genres/(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=genre_list,
        name='book_genre_detail',
    ),
    url (r'^books/genres/$',
        view='object_list',
        kwargs=genre_list,
        name='book_genre_list',
    ),
    url(r'^books/publishers/(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=publisher_list,
        name='book_publisher_detail',
    ),
    url (r'^books/publishers/$',
        view='object_list',
        kwargs=publisher_list,
        name='book_publisher_list',
    ),
    url(r'^books/(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=book_list,
        name='book_detail',
    ),
    url (r'^books/$',
        view='object_list',
        kwargs=book_list,
        name='book_list',
    ),
)
