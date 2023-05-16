from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NewFolderForm
from .models import Folder


@login_required
def home(request):
    folders = request.user.allfolders.all
    print(folders)
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
            form.save()
            # print(f'\nAfter save' * request.META, '\n', sep='\n')
            # print(f'\n {form.user} \n')
            return HttpResponseRedirect(request.session['redirected_from'])
    else:  # get data
        request.session['redirected_from'] = request.META.get('HTTP_REFERER')
        for i in request.META.items():
            print(f'\nGET:', i, '\n')
        form = NewFolderForm()
    return render(request, 'new_folder_form.html', {'form': form})


def open_folder(request, pk):
    folders = get_object_or_404(Folder, pk=pk)
    return render(request, 'open_folder.html', {'folders': folders})
