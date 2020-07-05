#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:26:52 2020

@author: apandeya
"""
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
]