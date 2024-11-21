from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task,Invitation
from .forms import TaskForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site

def home(request):
    try:
        tasks = Task.objects.filter(user=request.user)
        return render(request, "index.html", {"tasks": tasks})
    except:
        tasks = []
        return render(request, "index.html", {"tasks": tasks})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Associate task with the logged-in user
            task.save()
            return redirect("task-list")  # Redirect to the task list after saving
    else:
        form = TaskForm()
    
    # Return the form to be rendered in the modal (if needed)
    return render(request, "tasks/task_form_modal.html", {"form": form})



@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Ensure the user owns the task
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = TaskForm(instance=task)
    return render(request, "task_form.html", {"form": form})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Ensure the user owns the task
    if request.method == "POST":
        task.delete()
        return redirect("task-list")
    return render(request, "task_confirm_delete.html", {"task": task})



def send_invitation_admin(request, pk):
    """
    Send an invitation to the user from the admin panel.
    """
    invitation = get_object_or_404(Invitation, pk=pk)
    
    if invitation.used:
        messages.warning(request, "This invitation has already been used.")
    else:
        # Generate the registration link
        current_site = get_current_site(request)
        invitation_link = f"http://{current_site.domain}/register/{invitation.token}/"

        # myemail = 'contactmoneyniti@gmail.com'
        # paswd = 'pjzyeslvgudyuctr'


        # Send the email
        send_mail(
            subject="Invitation to Join Our Platform",
            message=f"Hi,\n\nYou have been invited to join our platform. Click the following link to register: {invitation_link}",
            from_email="contactmoneyniti@gmail.com",  # Replace with your email
            recipient_list=[invitation.email]
        )

        invitation.used = False  # Keep it unused until the user registers
        invitation.save()
        messages.success(request, f"Invitation sent to {invitation.email}.")

    return redirect('/admin/mainapps/invitation/')  # Replace `app_name` with your app's name
