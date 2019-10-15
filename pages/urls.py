from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('newsitem/<slug>', views.newsItem, name='newsitem'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('ataman/', views.ataman, name='ataman'),
    path('about/', views.about, name='about'),
    path('about/', views.about, name='about'),
    # path('portfolio/', views.portfolio, name='portfolio'),
    # path('prices/', views.prices, name='prices'),
    #
    # path('about/', views.about, name='about'),
    # path('portfolio/<nameSlug>', views.portfolio_item, name='portfolio-item'),
    # path('callback/', views.callbackForm, name='callbackForm'),
    # path('create-landing/', views.createlanding, name='createlanding'),
    # path('create-blog/', views.createlanding, name='createblog'),
    # path('create-service/', views.createlanding, name='createservice'),
    # path('create-shop/', views.createlanding, name='createshop'),
    # path('create-forum/', views.createlanding, name='createforum'),
    # path('create-crm/', views.createlanding, name='createcrm'),

    # path('login/', views.login, name='login'),
    # path('logout/', views.logout_page, name='logout'),
    # path('profile/<nickname_req>', views.profile, name='profile'),
    # path('del_message/', views.del_message, name='del_message'),
    # path('bonus_pack/', views.bonus_pack, name='bonus_pack'),
    # path('about_us/', views.about_us, name='about_us'),
    # path('rules/', views.rules, name='rules'),
    # path('add_to_player_balance/', views.add_to_player_balance, name='add_to_player_balance'),
    # path('about_bonus_pack/', views.about_bonus_pack, name='about_bonus_pack'),




    # path('statistic/', views.statistic, name='statistic'),

]
