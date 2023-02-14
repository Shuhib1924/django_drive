from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewFolderForm
from .models import Folder
from django.contrib import messages


@login_required
def home(request):
    # look into the models under 'folder'
    folders = request.user.allfolders.filter(folder=None)
    return render(request, 'index.html', {'folders': folders})


def new_folder(request):
    if request.method == 'POST':
        form = NewFolderForm(request.POST)
        # print(form)
        if form.is_valid():
            # print(f'\n before save {request.user} \n')
            form = form.save(commit=False)
            # print(f'\nAfter save.commit' * request.META, '\n', sep='\n')
            form.user = request.user
            # print(f'\nAfter save' * request.META, '\n', sep='\n')
            # print(f'\n {form.user} \n')
            # we split the url into 4 pieces #! 0='http' 1='' [-2]=2='127.0.0.1:8000 3='' 4=nr1 5='' 5=nr1  6=''
            redirected_from = request.session['redirected_from'].split('/')
            if redirected_from[3] != '':
                # we write like that... #*because it's the warranty of creating file into the right folder!
                pk = redirected_from[-2]
                form.folder = get_object_or_404(Folder, pk=pk)
            form.save()
            return HttpResponseRedirect(request.session['redirected_from'])
    else:  # get data
        request.session['redirected_from'] = request.META.get('HTTP_REFERER')
        for i in request.META.items():
            print(f'\nGET:', i, '\n')
        form = NewFolderForm()
    return render(request, 'new_folder_form.html', {'form': form})


def open_folder(request, pk):
    try:
        folders = get_object_or_404(Folder, pk=pk)
    except:
        messages.error(request, 'folder not exist')
        return redirect('home')
    return render(request, 'open_folder.html', {'folders': folders})
