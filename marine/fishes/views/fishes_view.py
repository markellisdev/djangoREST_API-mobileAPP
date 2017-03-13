from django.views import generic
import sys
sys.path.append("../")

from fishes.models import Fish

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate

import sqlite3

class FishViewSet(TemplateView):
	template_name = "fishes/fish.html"
	#this fetches all the rows of data in the Fish table
def get_all_fish(request):
	all_fish_view = Fish.objects.all()
	print("This is all the fish ", all_fish_view)
	return render(request, 'fishes/fish.html', {"fishes": all_fish_view})