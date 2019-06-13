from django.views.generic import CreateView
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Create Task"""

    template_name = "task/create.html"
    form_class = TaskForm

    def get_form_kwargs(self):
        """Add request to form kwargs"""

        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        """render same view with success message instead of redirect to success url"""

        self.object = form.save()
        context = self.get_context_data(form=self.form_class(request=self.request))
        context["msg"] = "An email with task details will be sent shortly"
        return self.render_to_response(context)

