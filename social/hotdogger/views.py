from django.shortcuts import render, redirect
from .models import Profile, BlogPost
from .forms import BlogForm

def dashboard(request):
    if request.method == "POST":
        form = BlogForm(request.POST or None) 
        if form.is_valid() :
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect("hotdogger:dashboard")
    form = BlogForm()
    return render(request, "hotdogger/dashboard.html", {"form": form})



def profile_list(request):

    if request.user.is_anonymous:
         profiles = Profile.objects.all()
    else:
          profiles = Profile.objects.exclude(user=request.user)
 
    
    return render(request, "hotdogger/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        print(action)
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
        
    return render(request, "hotdogger/profile.html", {"profile": profile})

def blog_post(request,pk):
    blog = BlogPost.objects.get(pk=pk)
    return render(request, "hotdogger/blog_post.html", {"blog": blog})
