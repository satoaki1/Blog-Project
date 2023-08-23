from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage


# Create your views here.
# def index_view(request):
#     records = BlogPost.objects.order_by('-posted_at')
#     paginator = Paginator(records, 4)
#     page_number = request.GET.get('page', 1)
#     pages = paginator.page(page_number)
#     return render(request, 'index.html', {'orderby_records': pages})
#
#
# def blog_detail(request, pk):
#     record = BlogPost.objects.get(id=pk)
#     return render(request, 'post.html', {'object': record})

class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "orderby_records"
    queryset = BlogPost.objects.order_by("-posted_at")
    paginate_by = 4


class BlogDetail(DetailView):
    template_name = "post.html"
    model = BlogPost


class TechnoView(ListView):
    template_name = "techno_list.html"
    model = BlogPost
    context_object_name = "techno_records"
    queryset = BlogPost.objects.filter(category="technology").order_by("-posted_at")
    paginate_by = 2


class DailyLifeView(ListView):
    template_name = "dailylife_list.html"
    model = BlogPost
    context_object_name = "dailylife_records"
    queryset = BlogPost.objects.filter(category="dailylife").order_by("-posted_at")
    paginate_by = 2


class MusicView(ListView):
    template_name = "music_list.html"
    model = BlogPost
    context_object_name = "music_records"
    queryset = BlogPost.objects.filter(category="music").order_by("-posted_at")
    paginate_by = 2


class PortfolioView(ListView):
    template_name = "portfolio_list.html"
    model = BlogPost
    context_object_name = "portfolio_records"
    queryset = BlogPost.objects.filter(category="portfolio").order_by("-posted_at")
    paginate_by = 2


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blogapp:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        subject = "Contact: {}".format(title)

        message = 'Sender: {0}\n Email Address: {1}\n Title: {2}\n Message: \n{3}'.format(name, email, title, message)
        from_email = 'nsark821@gmail.com'
        to_list = ['nsark821@gmail.com']

        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,)

        message.send()
        messages.success(self.request, 'The email has been successfully sent.')

        return super().form_valid(form)
