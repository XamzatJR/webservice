import itertools
from django import template

register = template.Library()


@register.filter(name="group_by_date")
def group_by_date(value):
    grouped = itertools.groupby(
        value, lambda o: getattr(o, "created_at").strftime("%d.%m.%Y")
    )
    return [(day, list(this_day)) for day, this_day in grouped]


@register.filter(name="get_image")
def get_image(value):
    value = str(value)
    if value.startswith("http"):
        return value
    return "/media/" + value
