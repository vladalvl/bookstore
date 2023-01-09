from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Book, Category, Genre
from .forms import ReviewForm
from cart.forms import CartAddProductForm
from django.db.models import Q


class GenresCategories:
    """Жанры и категории книг """
    model = Book
    slug_field = 'url'

    def get_genres(self):
        return Genre.objects.all()

    def get_categories(self):
        return Category.objects.all()


class BooksView(GenresCategories, ListView):
    """Список книг"""
    model = Book
    queryset = Book.objects.all()
    template_name = 'books/books_list.html'
    paginate_by = 4


class BooksDetailsView(GenresCategories, DetailView):
    """Полное описание книги"""
    model = Book
    slug_field = 'url'

    def book_detail(self, pk, slug):
        book = get_object_or_404(Book,
                                 id=pk,
                                 slug=slug,
                                 available=True)
        cart_product_form = CartAddProductForm()
        return render(self, 'books/book_detail.html', {'product': book,
                                                          'cart_product_form': cart_product_form})


class AddReview(View):
    """Отзывы без регистрации"""
    def post(self, request, pk):
        # print(request.POST)
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.save()
        return redirect('/')


class FilterBooksView(GenresCategories, ListView):
    """Фильтр книг"""
    template_name = 'books/books_list.html'

    def get_queryset(self):
        queryset = Book.objects.filter(
            Q(category__in=self.request.GET.getlist('category')) |
            Q(genre__in=self.request.GET.getlist('genre'))
        )
        return queryset


class Search(ListView):
    """Поиск книг"""
    # template_name = 'books/search.html'
    paginate_by = 4

    def get_queryset(self):
        q = self.request.GET.get('q').capitalize()
        return Book.objects.filter(title__icontains=q)
        # return Book.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


def delivery(request):
    return render(request, 'books/delivery.html')


def about(request):
    return render(request, 'books/about.html')





