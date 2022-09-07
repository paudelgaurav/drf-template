"""
Taken from SmileyChris' post @ https://djangosnippets.org/snippets/690/
"""
import re

from django.template.defaultfilters import slugify


def unique_slugify(
    instance, value, slug_field_name="slug", queryset=None, slug_separator="-"
):
    """
    Calculates a unique slug of ``value`` for an instance.
    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).
    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)
    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug
    if not queryset:
        queryset = instance.__class__._default_manager.all()
        if instance.pk:
            queryset = queryset.exclude(pk=instance.pk)
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = f"-{next}"
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[: slug_len - len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = f"{slug}{end}"
        next += 1
    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator=None):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.
    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    if separator == "-" or not separator:
        re_sep = "-"
    else:
        re_sep = f"(?:-|{re.escape(separator)})"
        value = re.sub(f"{re_sep}+", separator, value)
    return re.sub(f"^{re_sep}+|{re_sep}+$", "", value)
