from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import CalcFunding
from .forms import CalcFundingForm


def calc(request):
    if request.method == 'POST':
        form = CalcFundingForm(request.POST, request.FILES)
        if form.is_valid():
            calc_funding = form.save()
    else:
        form = CalcFundingForm()    

    extra = calc_funding.salary_post - calc_funding.expences

    if calc_funding.
