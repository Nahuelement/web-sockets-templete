from django.shortcuts import render, get_object_or_404
from .forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from .models import Product, Category


def home(request, category_slug=None):
    category = True
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        "base.html",
        {
            "page": "pages/home.html",
            'category': category,
            'products': products
        },
    )


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    category = product.category
    # categories = Category.objects.all()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'category': category,
                #    'categories': categories,
                #   'cart_product_form': cart_product_form

                   })

def login(request):
    return render(
        request,
        "base.html",
        {"page": "pages/login.html", "active_nav": "login", "form": LoginForm()},
    )


def signup(request):
    return render(
        request,
        "base.html",
        {"page": "pages/signup.html", "active_nav": "signup", "form": SignupForm()},
    )


@login_required
def profile(request):
    return render(
        request, "base.html", {"page": "pages/profile.html", "active_nav": "profile"}
    )


def page_not_found(request, exception):
    return render(request, "base.html", {"page": "pages/404.html"})
