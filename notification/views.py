from django.shortcuts import render


def user_list(request):
    return render(request, 'notification/user_list.html')


def reports(request):
    return render(request, 'notification/report.html')