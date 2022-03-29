from django.forms import ModelForm, BooleanField
from .models import Post

# сщздаем модельную форму

class PostForm(ModelForm):
    check_box=BooleanField(label='Подтвердите')
    # в класс мета заносим модель и нужные нам поля
    class Meta:
        model=Post
        fields=['title', 'text', 'autor','check_box']
