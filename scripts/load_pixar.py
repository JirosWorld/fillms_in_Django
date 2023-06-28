from films.models import Film, Genre
import csv


def run():
    with open('films/pixar.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Film.objects.all().delete()
        Genre.objects.all().delete()

        for row in reader:
            print(row)

            genre, _ = Genre.objects.get_or_create(name=row[-1])

            film = Film(title=row[0],
                        year=row[2],
                        genre=genre)
            film.save()

            # ABOUT THE SCRIPT CODE

# The scripts/load_pixar.py code has only one function in it, with no dunder call at its end. As stated in the django-extensions documentation, “This file must implement a run() function. This is what gets called when you run the script. You can import any models or other parts of your Django project to use in these scripts”.

# So, we import both the Films and Genre models and the csv Python builtin module in the script. Next, inside the run() function, we use the with context management structure and open the pixar.csv file by using not a relative path, but the pattern app_name/csv_file.

# Then we pass the file variable to the csv.reader() function, call next(reader) to skip the CSV headers, and finally use Django’s ORM method .delete() to remove any instances that might be in the models tables. If you don’t want to delete the existing rows from the tables, remove these lines of code.

# The next step is to loop over all rows in the CSV. And in this part of the code we find the important method .get_or_create() for the first time. It returns a tuple, where the object at the first index is the Django model object that was created (if it didn’t exist in the database yet) or retrieved (if it already existed). The second element in the tuple is a boolean that returns True if the object was created and False otherwise.

# Notice how we create (or get) the Genre object first, and then use it, together with other information taken from every CSV row, to create a new Film object and save it to the database.