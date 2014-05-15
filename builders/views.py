from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Builder, Review
from .forms import BuilderForm, DeleteForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy

class BuilderListView(ListView):
    context_object_name = 'builders'
    model = Builder
    paginate_by = 25

class BuilderDetailView(DetailView):
    context_object_name = 'builder'
    model = Builder

    def get_context_data(self, *args, **kwargs):
        ctx = super(BuilderDetailView, self).get_context_data(*args, **kwargs)
        ctx['editable'] = self.object.can_edit(self.request.user)
        return ctx

class BuilderPermissionMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BuilderPermissionMixin, self).dispatch(request, *args, **kwargs)

    def get_object(self, *args, **kwargs):
        obj = super(BuilderPermissionMixin, self).get_object(*args, **kwargs)
        if not obj.can_edit(self.request.user):
            raise PermissionDenied()
        return obj

class BuilderUpdateView(BuilderPermissionMixin, UpdateView):
    model = Builder
    form_class = BuilderForm

class BuilderDeleteView(BuilderPermissionMixin, DeleteView):
    model = Builder
    success_url = reverse_lazy('builder.list')

    def get_context_data(self, *args, **kwargs):
        ctx = super(BuilderDeleteView, self).get_context_data(*args, **kwargs)
        ctx['form'] = DeleteForm.create_for(self.object)
        return ctx

class ReviewListView(ListView):
    context_object_name = 'reviews'
    model = Review
    paginate_by = 5

    def get_queryset(self):
        self.builder = get_object_or_404(Builder, slug=self.kwargs['builder'])
        return Review.objects.filter(builder=self.builder)

    def get_context_data(self, *args, **kwargs):
        ctx = super(ReviewListView, self).get_context_data(*args, **kwargs)
        ctx['builder'] = self.builder
        return ctx

class ReviewDetailView(DetailView):
    context_object_name = 'review'
    model = Review

    def get_queryset(self):
        self.builder = get_object_or_404(Builder, slug=self.kwargs['builder'])
        return super(ReviewDetailView, self).get_queryset().filter(builder=self.builder)

    def get_context_data(self, *args, **kwargs):
        ctx = super(ReviewDetailView, self).get_context_data(*args, **kwargs)
        ctx['builder'] = self.builder
        return ctx
