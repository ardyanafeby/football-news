from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406398274',
        'name': 'Ardyana Feby Pratiwi',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)