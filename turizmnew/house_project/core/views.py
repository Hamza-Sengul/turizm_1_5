from django.views.generic import TemplateView, DetailView
from .models import SiteSettings, Category, House

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        context['houses'] = House.objects.all()
        return context

class HouseDetailView(DetailView):
    model = House
    template_name = 'house_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        context['houses'] = House.objects.all()
        return context

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Dinamik içerik eklemek isterseniz:
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        return context
    

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        return context

class PrivacySecurityView(TemplateView):
    template_name = "privacy_security.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        return context

class TermsView(TemplateView):
    template_name = "terms.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        return context

class CancellationRefundView(TemplateView):
    template_name = "cancellation_refund.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        return context
    

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        return context

class RefundRequestView(TemplateView):
    template_name = "refund_request.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        return context

class FAQView(TemplateView):
    template_name = "faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['categories'] = Category.objects.all()
        return context

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Category, House
# Admin Paneli Dashboard
class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "dashboard.html"

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_count'] = Category.objects.count()
        context['houses_count'] = House.objects.count()
        return context

# Kategori Yönetimi
class CategoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['name', 'photo']  # forms.py kullanmadan, bu alanlar üzerinden form oluşturulur.
    template_name = "category_form.html"
    success_url = reverse_lazy('admin_category_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = ['name', 'photo']
    template_name = "category_form.html"
    success_url = reverse_lazy('admin_category_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = "category_confirm_delete.html"
    success_url = reverse_lazy('admin_category_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

# Ev Yönetimi
class HouseListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = House
    template_name = "house_list.html"
    context_object_name = "houses"

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser
from django.forms import inlineformset_factory
from .models import House, HouseImage 
class HouseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = House
    fields = ['category', 'name', 'price', 'description']
    template_name = "house_form.html"
    success_url = reverse_lazy('admin_house_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        HouseImageFormSet = inlineformset_factory(House, HouseImage, fields=('image',), extra=1, can_delete=True)
        if self.request.POST:
            data['images'] = HouseImageFormSet(self.request.POST, self.request.FILES)
        else:
            data['images'] = HouseImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        self.object = form.save()
        if images.is_valid():
            images.instance = self.object
            images.save()
        return super().form_valid(form)


class HouseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = House
    fields = ['category', 'name', 'price', 'description']
    template_name = "house_form.html"
    success_url = reverse_lazy('admin_house_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        HouseImageFormSet = inlineformset_factory(House, HouseImage, fields=('image',), extra=1, can_delete=True)
        if self.request.POST:
            data['images'] = HouseImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['images'] = HouseImageFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        self.object = form.save()
        if images.is_valid():
            images.instance = self.object
            images.save()
        return super().form_valid(form)

class HouseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = House
    template_name = "house_confirm_delete.html"
    success_url = reverse_lazy('admin_house_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser