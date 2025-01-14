from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.models import Page  # Updated import for Wagtail 6
from wagtail.contrib.search_promotions.models import Query  # Updated import for Query

def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        # Use Wagtail's live page search functionality
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record a search hit for analytics
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)  # Show 10 results per page
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    # Render the search results page
    return TemplateResponse(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
