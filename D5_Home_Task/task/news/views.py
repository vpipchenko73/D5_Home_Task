# импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView  # импортируем класс получения деталей объекта
from django.views.generic import UpdateView, CreateView, \
     DeleteView  # импортируем класс создания редактирования и удаления обьектов
from .models import Post
from .filters import PostFilter  # импортируем недавно написанный фильтр
from .forms import PostForm
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin


# Новости
class PostList(ListView):
    model = Post
    template_name = 'newsall.html'
    context_object_name = 'newsall'
    # queryset = Post.objects.order_by('-dateCreation') # выводим статьи в обратном порядке
    ordering = ['-dateCreation']
    paginate_by = 10  # поставим постраничный вывод в 10 элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = f"Все новости . общее количество новостей ->>{Post.objects.all().count()}"
        return context

class PostSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news_search'
    # queryset = Post.objects.order_by('-dateCreation') # выводим статьи в обратном порядке
    ordering = ['-dateCreation']
    paginate_by = 10  # поставим постраничный вывод в 10 элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value1'] = f"Все новости . общее количество новостей ->>{Post.objects.all().count()}"
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news_detail.html'  # название шаблона будет product.html
    # context_object_name = 'news_detail'  # название объекта. в нём будет
    queryset = Post.objects.all()


class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    template_name = 'news_create.html'
    form_class = PostForm


class PostUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = ('news.change_post',)
    template_name = 'news_create.html'
    form_class = PostForm

    # делаем метод что бы получить информацию об объекте которы мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/newsall/'
