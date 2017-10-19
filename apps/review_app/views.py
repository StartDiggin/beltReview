# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect
from ..login_app.models import User
from .models import Book
from .models import Review
from django.db.models import Count

# Route to home page --> books/
def home(request):
    if not 'id' in request.session:
        messages.error(request,'Please log in again!')
        return redirect('/')
    else:
        booklist = []
        books = Book.objects.all()
        # print context['reviewed_books']
        for x in range(1,4):
            booklist.append(books[len(books)-x])

        context={
            'user': User.objects.get(id=request.session['id']), #working
            'allBooks': Book.objects.all(), #working
            'reviewed_books': booklist
        }
        print booklist
    return render(request,'review_app/home.html', context)

# Route to add a book --> /books/addBook
def addBook(request):
    context={
        'book_authors': Book.objects.all(),
    }
    return render(request,'review_app/addBook.html', context)

# Route to create a book and review --> /books/create
def create(request):
    user = User.objects.get(id=request.session['id'])
    book = Book.objects.create(title=request.POST['title'],author=request.POST['author'],rate=request.POST['rate'], user=user)
    request.session['book_id'] = book.id
    review = Review.objects.create(review=request.POST['review'], book=book, creator=user)
    return redirect('/books')

# Route to review book --> /books/reviews
def review(request, id):
    context={
    'book': Book.objects.get(id=id),
    'user': User.objects.get(id=request.session['id']),
    'userReviews': Review.objects.all(),
    }

    return render(request,'review_app/review.html',context)

# Route to user profile --> /books/user/(?P<id>\d+)
def user(request, id):
    context={
    'userInfo': User.objects.get(id=id),
    'reviewCount': Review.objects.filter(creator__id=id).count(),
    'reviewedBooks':[],
    }
    b = Review.objects.filter(book__user__id=id)
    c = Review.objects.filter(creator__id=id).count()
    print c
    for y in range(0,c):
        context['reviewedBooks'].append(b[y].book)
    return render(request,'review_app/user.html', context)

# Route to destroy a record --> /books/delete
def delete(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return redirect('/books')

# Route to add a review --> /books/addReview
def addReview(request, id):
    user = User.objects.get(id=request.session['id'])
    book = Book.objects.get(id=id)
    review = Review.objects.create(review=request.POST['review'], book=book, creator=user)
    review.save()
    return redirect('/books')
