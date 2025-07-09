from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def querystring_except_page(context):

    """
    Fix pagination problem with search
    """

    request = context["request"]
    querydict = request.GET.copy()

    querydict.pop("page", None)
    return querydict.urlencode()
