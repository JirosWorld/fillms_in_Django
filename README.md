### https://towardsdatascience.com/django-first-steps-for-the-total-beginners-a-quick-tutorial-5f1e5e7e9a8c

`$ python manage.py shell`

= you can run Django commands here using your project files, such as the models.

(InteractiveConsole)

> > > from films.models import Film, Genre
> > > animation_genre = Genre(name='animation')
> > > animation_genre.save()
> > > finding_nemo = Film(title='Finding Nemo', year=2003, genre-animation_genre)
> > > finding_nemo.save()
> > > all_films = Film.objects.all()
> > > all_films
> > > <QuerySet [<Film: The Matrix>, <Film: The Matrix Reloaded>, <Film: The Matrix Revolutions>, <Film: The Matrix Ressurections>, <Film: Fi nding Nemo>]>
> > > the_matrix = all_films[0]
> > > the_matrix.id
> > > 1
> > > the_matrix.genre
> > > <Genre: action>
> > > the_matrix.title
> > > 'The Matrix'
> > > the_matrix.year 1999

## Plotly graphs and Django.

- Use the `.to_html()` method from a Plotly Figure object and save it in a context dictionary with a name such as `fig`.
- In the Django template, use the tag `{{fig | safe}}` to render the graph.
- http://localhost:8000/gapminder/2007
