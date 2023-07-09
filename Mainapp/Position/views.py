# views.py
from django.shortcuts import render, redirect, get_object_or_404
from Position.forms import PositionForm
from Position.models import Position


def Position_Page(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('Position_List')  # Redirect to a success page
    else:
        form = PositionForm()
    return render(request, 'Position/Positions_page.html', {'form': form})



def PositionEdit_Page(request, id):
    position = get_object_or_404(Position, id=id)
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('Position_List')
    else:
        form = PositionForm(instance=position)
    return render(request, 'Position/PositionsEdit.html', {'form': form, 'positions': position})


def PositionDelete_Page(request, id):
    position = get_object_or_404(Position, id=id)
    if request.method == 'POST':
        position.delete()
        return redirect('Position_List')
    return render(request, 'Position/PositionsDelete.html', {'position': position})


def Positionlist_page(request):
    positions = Position.objects.all()
    return render(request, 'Position/Positionslist_page.html', {'positions': positions})
