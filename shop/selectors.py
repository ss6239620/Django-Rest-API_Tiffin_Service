from .models import Category, Subcategory, Product


def get_categories():
    return Category.objects.all()


def get_products_from_subcategory(*, subcategory_slug):
    return Product.objects.filter(subcategory__slug=subcategory_slug)