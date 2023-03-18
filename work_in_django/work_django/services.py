from work_django.models import Profile, Product


def load_profile(user):
    try:
        return user.profile
    except:
        profile = Profile.objects.get_or_create(user=user)
        return profile
