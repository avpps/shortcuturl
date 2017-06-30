from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from cuturl.models import userurl


def home(request):
    return render(request, 'cuturl/home.html')

def addurl(request):
    userurltext = request.POST['userurl']
    new_url = userurl.objects.create(
        url_text = userurltext
        )
    new_url.save
    userurltext_id = new_url.id
    link_for_user = 'http://127.0.0.1:8000/cuturl/%d/' % userurltext_id

    return render(request, 'cuturl/link.html',
                  {'link_for_user': link_for_user})

def redToURL(request, userurl_id):
    print('userurl_id', userurl_id)
    user_url = get_object_or_404(userurl, pk=userurl_id)
    user_url = user_url.url_text
    return HttpResponseRedirect(user_url)

    