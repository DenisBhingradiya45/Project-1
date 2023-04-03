from django.utils.text import slugify
import string
import random

def generate_random_string(N):
    result = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    return result

def generate_slug(text):
    new_slug = slugify(text)
    from .models import Blog_Model

    if Blog_Model.objects.filter(slug = new_slug).exists():
        return generate_slug(text + generate_random_string(5))
    return new_slug