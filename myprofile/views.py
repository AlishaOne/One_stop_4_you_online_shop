import ast

from django.contrib.auth import authenticate, views
from django.contrib.auth import login as auth_login
from django.contrib.sessions.models import Session
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

from myprofile.form import SignupForm
from myprofile.models import UserSession
from onestop4you import settings


def signup(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            new_user = authenticate(username=username, password=raw_password)
            auth_login(request, new_user)
            return redirect('/mainstore')
    else:
        user_form = SignupForm()
    return render(request, 'myprofile/signup.html', {'user_form': user_form})


def my_logout(request):
    sk = request.session.session_key
    s = Session.objects.get(pk=sk)
    userid = s.get_decoded().get('_auth_user_id')
    cartid = s.get_decoded().get('cart')

    # save the latest cart info,if exist update values with defaults dictionary's values
    user_cart_bk, created = UserSession.objects.update_or_create(
        user_id=request.user.id,
        defaults={'session_id': request.session.session_key, 'session_data': cartid},
    )

    print("  user cart backup data id is {} created? {}:".format(user_cart_bk, created))

    views.logout(request)

    request.session['user_id'] = userid
    request.session['session_key'] = sk

    return redirect('/mainstore/start')


def my_login(request):
    # ######
    # u = UserSession.objects.get(user_id=request.user.id)
    # # u = UserSession.objects.get(user_id=request.user.id).order_by('-id')[:1]
    # cartid = json.loads(u.session_data)
    # print(" cid is:",cartid)
    # request.session[settings.CART_SESSION_ID] = cartid
    ######

    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                try:
                    u = UserSession.objects.filter(user_id=request.user.id).latest('id')
                except(KeyError, UserSession.DoesNotExist):
                    return redirect('/mainstore')
                else:
                    # model(class) to dict
                    ud = model_to_dict(u)
                    c = ud.get('session_data')

                    # str to dict
                    cd = ast.literal_eval(c)
                    # if cd:
                    request.session[settings.CART_SESSION_ID] = cd
                    return redirect('/mainstore')
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Invalid login details")
            return render(request, 'myprofile/login.html', {"user": user})

    else:
        return render(request, 'myprofile/login.html', {})
