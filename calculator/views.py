from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import CalcFunding
from .forms import CalcFundingForm
from user_profile.models import UserProfile
import random

successes = [
    "If you really need to then I really can't stop you.",
    "Can I borrow some of all that cash you are going around with?",
    "I can see you do got the money for this but are you sure that this is what you want?",
    "Hey go for it! When you have it go for it!"
]

warnings = [
    'Brain oh brain where art thou brain. Did you really think you could afford that?',
    'Oh that sounds cool, but of wait what is that... You are broke think again. Or try and think at all next time.',
    'Did your broke ass actullay think you could afford that. You make me laugh.',
    "I don't think I could say this with any more respect, no that is a lie and you are a dumbass."
]

errors = [
    "I can not believe this... Calling you for an idiot would be an insult to all of the stupid people.",
    "Try and put on your glass and actully read you pay check.",
    "Do you want me to dum this down for you? If you don't get your act together you are sleeping on the streets in a week.",
    "You must be the younger sibling, because you clearly got none of the brain cells."
]



class LoadHomePage(View):
    def get(self, request):
        return render(request, 'index.html')


def calc(request):
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            form = CalcFundingForm(initial={
                'cost':  '0',
                'savings': profile.savings,
                'salary_pre': profile.salary_pre,
                'salary_post': profile.salary_post,
                'expences': profile.expences,

            })
        except UserProfile.DoesNotExist:
            form = CalcFundingForm()
    else:
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
            if calc_funding.expences > calc_funding.salary_post:
                messages.error(request, 'income error meaasge')
            else:
                if calc_funding.fund == 'SV':
                    if (calc_funding.savings - calc_funding.salary_pre * 3) > calc_funding.cost:
                        print("success")
                        messages.success(request, random.choice(successes))
                    else:
                        print("error")
                        messages.warning(request, random.choice(warnings))
                    print("post")
                else:
                    if calc_funding.cost < (extra * 0.7):
                        print(calc_funding.cost, (extra*0.7))
                        print("success")
                        messages.success(request, random.choice(successes))
                    else:
                        print("error")
                        messages.warning(request, random.choice(errors))
                    print("post")
        else:
            messages.info(request, 'info meaasge')
    else:
        form = CalcFundingForm()
    return redirect(reverse('calc'))
