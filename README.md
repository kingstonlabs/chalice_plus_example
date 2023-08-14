# Example `chalice_plus` project

This is an example project to demonstrate how the [`chalice_plus`](https://github.com/kingstonlabs/chalice-plus) framework can be used.

To set up run:

`pip install -r local_requirements.txt`


## Running locally
Update the environment variables in the "local" stage of `.chalice/config.json` to point to your database, then run:

`$ alembic upgrade head`

The local server can then be run with:

`$ chalice local --stage local`


## Deploying to AWS
Add the following SSM parameters:
* `chalice_plus_example.dev.DATABASE_USER`
* `chalice_plus_example.dev.DATABASE_PASSWORD`
* `chalice_plus_example.dev.DATABASE_HOST`
* `chalice_plus_example.dev.DATABASE_NAME`

Then deploy with:

`$ chalice_plus deploy`


## Try the API

Create a user:
```
$ curl 127.0.0.1:8000/users -H "Content-Type: application/json" -d '{"username": "me", "email": "me@example.com"}'
```

Create an author:
```
$ curl 127.0.0.1:8000/authors -H "Content-Type: application/json" -d '{"name":"Eric Carle", "description": "American author, designer and illustrator of children'\''s books"}'
```

Create a book:
```
$ curl 127.0.0.1:8000/books -H "Content-Type: application/json" -d '{"title":"The Very Hungry Caterpillar", "description": "The story of a very hungry caterpillar that eats a variety of foods before pupating and emerging as a butterfly, and incorporates elements that contribute to juvenile education, such as counting, the days of the week, food, and a butterfly’s life cycle.", "author_id": "<author_id>"}'
```

List books, including their author:
```
$ curl 127.0.0.1:8000/books -H "X-Fields: {title,author{name}}"
[{"title":"The Shining","author":{"name":"Stephen King"}},{"title":"Carrie","author":{"name":"Stephen King"}},{"title":"The Very Hungry Caterpillar","author":{"name":"Eric Carle"}}]
```

List authors, including their books:
```
$ curl 127.0.0.1:8000/authors -H "X-Fields: {name,books{title}}"
[{"name":"Stephen King","books":[{"title":"The Shining"},{"title":"Carrie"}]},{"name":"Eric Carle","books":[{"title":"The Very Hungry Caterpillar"}]}]
```
