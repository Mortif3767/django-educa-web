# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Subject, Course, Module


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
	model = Module
#stackedinline与tarbularinline的区别仅仅是模板渲染的区别

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'subject', 'created']
	list_filter = ['created', 'subject']
	search_fields = ['title', 'overview']
	prepopulated_fields = {'slug': ('title',)}
	inlines = [ModuleInline]
