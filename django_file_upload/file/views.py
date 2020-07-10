from django.shortcuts import render,redirect
from .models import MyPost

# Create your views here.
def create_post(request):
    if request.method == 'POST':
        post_data = request.POST
        file_data = request.FILES
        login_user = request.user

        print("##########")
        print(file_data)
        print("##########")
        mypost = MyPost(
            title = post_data.get('title'),
            post = post_data.get('post'),
            upload_user = login_user,
            file = file_data.get('file'),
        )
        mypost.save()
        return redirect('filehome')
