# -*- coding: utf-8 -*-
from wagtail.contrib.modeladmin.helpers import WagtailBackendSearchHandler
from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup, modeladmin_register)

from home.models import NewsPage


class NewsAdmin(ModelAdmin):
    model = NewsPage
    menu_label = "News"
    list_display = ('title', 'url_path', 'date', 'first_published_at', 'is_sticky', 'is_on_index', 'live')
    list_filter = ('is_sticky', 'is_on_index', 'live')
    search_handler_class = WagtailBackendSearchHandler
    ordering = ['-date']


class ContentGroup(ModelAdminGroup):
    menu_label = 'Specific contents'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (NewsAdmin, )


modeladmin_register(ContentGroup)


