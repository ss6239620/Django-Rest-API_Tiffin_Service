from rest_framework.exceptions import ValidationError

from .models import Product, Subcategory, Invoice


def create_product(
    *,
    owner,
    title,
    price,
    description,
    thumbnail,
    subcategory,
    quantity_type,
    quantity
):
    if Product.objects.filter(owner=owner).filter(title=title).exists():
        raise ValidationError("You already have a Product with the same title.")

    subcategory_object = Subcategory.objects.get(slug=subcategory)

    product = Product.objects.create(
        owner=owner,
        title=title,
        price=price,
        description=description,
        thumbnail=thumbnail,
        subcategory=subcategory_object,
        quantity_type=quantity_type,
        quantity=quantity
    )

    return Product.objects.get(pk=product.pk)


def update_product(
    *,
    product_slug,
    owner=None,
    title=None,
    price=None,
    description=None,
    thumbnail=None,
    subcategory=None,
    quantity_type=None,
    quantity=None,
):
    try:
        product = Product.objects.get(owner=owner, slug=product_slug)
    except Product.DoesNotExist:
        raise ValidationError("Could not find the specified Product.")

    if title:
        if Product.objects.filter(owner=owner).filter(title=title).exists():
            raise ValidationError("You already have a Product with the same title.")
        product.title = title

    if price:
        product.price = price

    if description:
        product.description = description

    if thumbnail:
        product.thumbnail = thumbnail

    if subcategory:
        subcategory_obj = Subcategory.objects.get(slug=subcategory)
        product.subcategory = subcategory_obj

    if quantity:
        product.quantity = quantity

    if quantity_type:
        product.quantity_type = quantity_type

    product.save()

    return Product.objects.get(pk=product.id)


def create_invoice(
    *,
    user,
    summary,
    total_cost,
    shipping_address,
    card_token
):
    invoice = Invoice.objects.create(
        user=user,
        summary=summary,
        total_cost=total_cost,
        shipping_address=shipping_address,
        card_token=card_token
    )

    return invoice