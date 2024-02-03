from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Sweets, CustomUserComment
from .forms import SweetForm, UpdateSweetForm, CreateSweetForm, CommentForm, CommentUpdateForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class UpdateSweetView(LoginRequiredMixin, View):
    template_name = 'sweets/update_sweet.html'

    def get(self, request, pk):
        sweet_instance = get_object_or_404(Sweets, pk=pk)
        form = UpdateSweetForm(instance=sweet_instance)
        return render(request, self.template_name, {'form': form, 'sweet': sweet_instance})

    def post(self, request, pk):
        sweet_instance = get_object_or_404(Sweets, pk=pk)
        form = UpdateSweetForm(request.POST, request.FILES, instance=sweet_instance)
        if form.is_valid():
            form.save()
            return redirect('sweets')
        return render(request, self.template_name, {'form': form, 'sweet': sweet_instance})


class DeleteSweetView(LoginRequiredMixin, View):
    template_name = 'sweets/delete.html'

    def get(self, request, pk):
        sweet_instance = get_object_or_404(Sweets, pk=pk)
        return render(request, self.template_name, {'sweet': sweet_instance})

    def post(self, request, pk):
        sweet_instance = get_object_or_404(Sweets, pk=pk)
        sweet_instance.delete()
        return redirect('sweets')


class SweetListView(View):
    template_name = 'sweet/sweet_list.html'
    items_per_page = 10

    def get(self, request):
        search_query = request.GET.get('search', '')

        sweets = Sweets.objects.filter(name__icontains=search_query).order_by('-create_at')

        paginator = Paginator(sweets, self.items_per_page)
        page = request.GET.get('page')

        try:
            sweets = paginator.page(page)
        except PageNotAnInteger:
            sweets = paginator.page(1)
        except EmptyPage:
            sweets = paginator.page(paginator.num_pages)

        context = {
            'sweets': sweets,
            'search_query': search_query,
        }

        return render(request, template_name=self.template_name, context=context)


class AddSweetView(View):
    def post(self, request):
        form = CreateSweetForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid():
            form.save()
            return redirect("sweet_list")
        else:
            return render(request, "sweet/add_sweets.html", {"form": form})

    def get(self, request):
        form = CreateSweetForm()
        return render(request, "sweet/add_sweets.html", {"form": form})


class SweetDetailView(View):
    def get(self, request, pk):
        sweets = Sweets.objects.get(pk=pk)
        comments = CustomUserComment.objects.filter(sweet=sweets)
        comment_form = CommentForm()
        context = {
            'sweet': sweets,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, template_name='sweet/sweet_detail.html', context=context)


class AddCommentView(View):
    def get(self, request, pk):
        form = CommentForm()  # Use an empty form for GET requests
        return render(
            request, "sweet/add_comment.html", {"form": form, "pk": pk}
        )

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            sweet = get_object_or_404(Sweets, pk=pk)
            comment.sweet = sweet
            comment.user = request.user
            comment.save()
            return redirect("sweet_detail", pk=pk)
        return render(
            request, "sweet/add_comment.html", {"form": form, "pk": pk}
        )


class DeleteCommentView(View):
    def get(self, request, pk):
        comment = get_object_or_404(CustomUserComment, id=pk)
        return render(request, "sweet/delete_comment.html", {"comment": comment})

    def post(self, request, pk):
        comment = get_object_or_404(CustomUserComment, id=pk)
        pk = comment.sweet.pk
        comment.delete()
        return redirect("sweet_detail", pk=pk)





class UpdateCommentView(View):
    def get(self, request, pk):
        comment = get_object_or_404(CustomUserComment, id=pk)
        form = CommentUpdateForm(instance=comment)
        context = {"form": form, "comment": comment}
        return render(request, "sweet/update_comment.html", context=context)

    def post(self, request, pk):
        comment = get_object_or_404(CustomUserComment, id=pk)
        form = CommentUpdateForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            pk = comment.sweet.pk
            form.save()
            return redirect("sweet_detail", pk=pk)
        context = {"form": form, "comment": comment}
        return render(request, "sweet/update_comment.html", context=context)


