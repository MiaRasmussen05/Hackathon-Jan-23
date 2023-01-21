from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import CalcFunding
from .forms import CalcFundingForm




class LoadHomePage(View):
    def get(self, request):
        return render(request, 'index.html')


def calc(request):
    form = CalcFundingForm()
    template = 'calculator/calc-funding.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def run_calc(request):
    """ Run calculation with given values """
    if request.method == 'POST':
        form = CalcFundingForm(request.POST, request.FILES)
        if form.is_valid():
            calc_funding = form.save()
            extra = calc_funding.salary_post - calc_funding.expences
            if calc_funding.savings > (calc_funding.salary_pre * 3):
                print("success")
            else:
                print("error")
            print("post")
    else:
        form = CalcFundingForm()

    return redirect(reverse('calc'))