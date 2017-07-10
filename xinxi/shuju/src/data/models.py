# -*-coding:utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django import forms
from django.forms import ModelForm



class BlogUser(models.Model):
    user_name = models.CharField(db_column='user_Name', primary_key=True, max_length=15)  # Field name made lowercase.
    user_password = models.CharField(db_column='user_Password', max_length=15)  # Field name made lowercase.
    user_emial = models.CharField(unique=True, max_length=20)
    
    class Meta:
       managed = False
       db_table = 'test3.3'


class BlogUserAdmin(admin.ModelAdmin):
    list_display=('user_name','user_password','user_emial')
    
#admin.site.register(BlogUser, BlogUserAdmin)

class data(models.Model):
    data_applicant=models.CharField(u'申请人',db_column='applicant',primary_key=True,max_length=60)
    data_department=models.CharField(u'申请部门',db_column='department',max_length=60)
    data_application_time =models.CharField(u'申请时间',db_column='application_time',max_length=60)
    data_application_brief=models.CharField(u'用途说明',db_column='application_brief',max_length=60)
    data_internal_ip=models.CharField(u'内部ip',db_column='internal_ip',max_length=60)
    data_external_ip=models.CharField(u'外部ip',db_column='external_ip',max_length=60)
    nei_ip=models.CharField(u'内部ip',db_column='nei_ip',max_length=60)
    wai_ip=models.CharField(u'外部ip',db_column='wai_ip',max_length=60)
    checkbox_stat=models.CharField(u'用途类型',db_column='checkbox',max_length=60)
    yont_tu=models.CharField(u'用途说明',db_column='yong_tu',max_length=60)
    white_list=models.CharField(u'外部访问ip白名单限制',db_column='white_list',max_length=60)
    url=models.CharField(u'url地址',db_column='url',max_length=60)
    agent=models.CharField(u'代理或中间件ip',db_column='agent',max_length=60)
    
    class Meta:
        verbose_name='资产信息'
        verbose_name_plural='资产信息'
        managed = False
        db_table = 'test3.3'

#class data_nei(models.Model):
#    nei_ip=models.CharField(db_column='nei_ip',primary_key=True,max_length=20)
#    wai_ip=models.CharField(db_column='wai_ip',max_length=20)
    
#    class Meta:
#        managed = False
#        db_table = 'data_data_test'
        
#class data_neiAdmin(admin.ModelAdmin): 
#    list_display=('nei_ip','wai_ip')  

#admin.site.register(data_nei,data_neiAdmin)
#class data_test_1(ModelForm):
#    class Meta:
#        model=data
#        fields=['user_name','user_password','last_login']
class dataAdmin(admin.ModelAdmin):
    list_display=('data_applicant','data_department','data_application_time','yont_tu','nei_ip','wai_ip','url','agent','white_list')
    
#class dataAdmin(admin.ModelAdmin):
#    list_display=('data_applicant','data_department','data_application_time','data_internal_ip','data_external_ip','data_application_brief','nei_ip','wai_ip')
    
admin.site.register(data,dataAdmin)




