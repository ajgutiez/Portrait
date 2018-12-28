# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from photos.models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')

    def owner_name(self,obj):
        return obj.owner.first_name + u' ' + obj.owner.last_name
    #listado
    owner_name.short_description = u'Photo owner'
    owner_name.admin_order_field = 'owner'

    #detalle
    fieldsets = (
        (None,{
            'fields': ('name',),
            'classes': ('wide',)
        }),
        ('Description & Author', {
            'fields': ('description', 'owner'),
            'classes': ('wide',)
        }),
        ('Extra', {
            'fields': ('url', 'license', 'visibility'),
            'classes': ('wide', 'collapse')
        })
    )

admin.site.register(Photo, PhotoAdmin)
