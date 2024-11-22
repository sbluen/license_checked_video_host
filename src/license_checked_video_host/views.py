from django.shortcuts import render
def index(request):
    return render(request, 'license_checked_video_host/index.html')