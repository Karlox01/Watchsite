from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from watches.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')



class CustomLoginView(LoginView):
    template_name = 'core/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def render_to_response(self, context, **response_kwargs):
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )


def signup(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html',{
        'form': form,
        'categories': categories
    })

