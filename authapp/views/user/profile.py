from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

def userInfo(req):
    context = {}

    if req.user.is_authenticated:
        # SocialAccount(id, user, provider, uid, last_login, date_joined, extra_data)

        user = SocialAccount.objects.get(user = req.user)
        profile_pic = user.extra_data['picture']
        print('user=>',user)


        return render(req, 'authapp/auth/profile.html', context)


