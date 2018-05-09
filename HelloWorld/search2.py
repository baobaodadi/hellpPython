# -*- coding: utf-8 -*-

from django.shortcuts import render

# 接收POST请求数据
def search_post(request):
   ctx ={}
   return render(request, "post.html", ctx)