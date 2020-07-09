from django.shortcuts import render,redirect
from .models import Notebook
import datetime

# Create your views here.
def note_list(request):
    notes = Notebook.objects.all().order_by('-created_at')
    return render(request, 'note/note_list.html', {'notes':notes})

def note_create(request):

    if request.method == 'POST':
        note_data = request.POST
        login_user = request.user

        data = Notebook(draft_user=login_user,note_data=note_data.get('note_data'),created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())
        data.save()
        return redirect('notepage')

def note_update(request,pk):
    if request.method == 'POST':
        note_data = request.POST
        login_user = request.user

        my_note = Notebook.objects.get(id=pk)
        if my_note.draft_user != login_user:
            return redirect('notepage')
        else:
            my_note.updated_at = datetime.datetime.now()
            my_note.note_data = note_data.get('note_data')
            my_note.save()
            return redirect('notepage')
    else:
        my_note = Notebook.objects.get(id=pk)

        return render(request,'note/note_update.html',{'note':my_note})

def note_delete(request,pk):
    note = Notebook.objects.get(id=pk)
    note.delete()
    return redirect('notepage')
