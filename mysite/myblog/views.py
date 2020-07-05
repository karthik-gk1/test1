from django.shortcuts import render

from .models import out, get_all_video_in_channel


def index(request):
    idd = 'UC9QDA8CiJozdErmYC1PLjGQ'
    t1, li, de = list(get_all_video_in_channel(idd))
    d = []
    for i in range(len(t1)):
        dest1 = out()
        dest1.link = li[i]
        dest1.title = t1[i].replace("&#39;", "'")
        dest1.description = de[i]
        d.append(dest1)
    return render(request, 'index.html', {'d': d, 'id': idd})
