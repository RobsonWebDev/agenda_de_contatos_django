from django.shortcuts import render, get_object_or_404
from contact.models import Contact



def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
    }

    return render(request, 'contact/index.html', context)

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    if single_contact is None:
        raise Http404

    context = {
        'contacts': single_contact,
    }

    return render(request, 'contact/contact.html', context)