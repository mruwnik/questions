from django import template


register = template.Library()


@register.filter(name='print_path')
def print_path(item):
    """Return a string description of the path to the given item."""
    if not item:
        return 'Questions'

    items = [parent.title for parent in item.path] + [item.title]
    return item.question.content + ': ' + ' -> '.join(items)
