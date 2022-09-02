
from django.http import HttpResponse

# Create your views here.
def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    resp = HttpResponse(f'View Count={num_visits} d7e7bd5d')
    resp.set_cookie('dj4e_cookie', 'd7e7bd5d', max_age=1000)
    return resp  # ← return the response itself
