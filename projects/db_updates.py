from .models import Post, District
posts = Post.objects.all()
districts = District.objects.all()

for post in posts:
    if '_' in post.post:
        name = post.post.replace('_', ' ')
        post.post = name
        post.save()
        print('Post name updated')
    
    if '_' in post.province:
        name = post.province.replace('_', ' ')
        post.province = name
        post.save()
        print('Post province name updated')

    if '_' in post.district:
        name = post.district.replace('_', ' ')
        post.district = name
        post.save()
        print('Post district name updated')

for district in districts:
    
    if '_' in district.province:
        name = district.province.replace('_', ' ')
        district.province = name
        district.save()
        print('District province name updated')

    if '_' in district.district:
        name = district.district.replace('_', ' ')
        district.district = name
        district.save()
        print('District name updated')