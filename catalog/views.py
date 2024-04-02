from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag


def index(request):
    """View function for the home page of the site."""
    tasks = Task.objects.all()
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "tasks": tasks,
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }

    return render(request, "catalog/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "catalog/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("catalog:tag-list")


class TaskStatusView(generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.status = not task.status
        task.save()
        return redirect("catalog:index")
