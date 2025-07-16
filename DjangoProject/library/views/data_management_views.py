import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from library.models import Book, Author


def data_management(request):
    
    if request.method == 'GET' and 'export' in request.GET:
        filename = "books.csv"
        headers = [
            'book_title',
            'book_publish_date',
            'book_isbn',
            'book_open_library_key',
            'author_name', 
            'author_birth_date', 
            'author_death_date',
            'author_country',
            'author_open_library_key'
        ]
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        writer.writerow(headers)

        for book in Book.objects.all():
            row = [
                book.title, 
                book.publish_date, 
                book.isbn,
                book.olid,
                book.author.name,
                book.author.birth_date,
                book.author.death_date,
                book.author.country,
                book.author.olid
            ]
            writer.writerow(row)

        return response
    
    
    if request.method == 'POST' and 'import' in request.POST:
        csv_file = request.FILES.get('csv_file')

        if not csv_file or not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a valid CSV file.')
            return redirect(request.path)
        
        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            next(reader)

            for row in reader:
                author_name = row[4]
                author_birth_date = row[5] if row[5] else None
                author_death_date = row[6] if row[6] else None
                author_country = row[7]
                author_open_library_key = row[8]

                author, _ = Author.objects.get_or_create(
                    name=author_name,
                    defaults={
                        'birth_date': author_birth_date,
                        'death_date': author_death_date,
                        'country': author_country,
                        'open_library_key': author_open_library_key
                    }
                )

                Book.objects.update_or_create(
                    isbn=row[2],
                    defaults={
                        'title': row[0],
                        'publish_date': row[1] if row[1] else None,
                        'open_library_key': row[3],
                        'author': author,
                    }
                )
           
            messages.success(request, 'CSV imported successfully.')
        except Exception as e:
            messages.error(request, f'Error importing data: {e}')

        return redirect('library:index')

    return render(request, 'library/data_management.html')