book_to_update = Book.objects.get(title="Django for Beginners")
book_to_update.title = "Django for Professionals"
book_to_update.save()
