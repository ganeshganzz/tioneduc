from django.shortcuts import render
def Post_list(request):
    return render(request, 'tioneduc/Post_list.html', {})

