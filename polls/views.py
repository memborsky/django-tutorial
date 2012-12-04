# Our database model to the polls so we can render some dynamic content.
from polls.models import Poll

# This allows us to skip having to import context and template here so we can
# make our code a little cleaner.
from django.shortcuts import render_to_response

# Allow us to spit out 404 errors.
from django.http import Http404

# Raw HTTP response.
from django.http import HttpResponse

# The /polls/ view.
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

# The /polls/<id>/ view.
def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk = poll_id)

    except Poll.DoesNotExist:
        raise Http404

    return render_to_response('polls/detail.html', {'poll': p})

# The /polls/<id>/results/ view.
def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

# The /polls/<id>/vote/ view.
def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
