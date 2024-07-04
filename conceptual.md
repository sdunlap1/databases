# Conceptual Exercise

### Answer the following questions below:

- What is PostgreSQL?
    - PostgreSQL is an open-source, object-relational database management system, supporting both SQL and JSON.

- What is the difference between SQL and PostgreSQL?
    - `SQL` A standardized language used to manage and manipulate relational databases.
    - `Postgres` A specific implementation of a relational database management system that uses SQL as its querying language, offering additional features like advanced data types, full text search, and custom functions.

- In `psql`, how do you connect to a database?
    - `\c database_name`. Or, `psql -d database_name`.

- What is the difference between `HAVING` and `WHERE`?
    - `HAVING` is used to filter groups with `GROUP BY`.
    - `WHERE` is used to filter rows before groupings are made.

- What is the difference between an `INNER` and `OUTER` join?
    - `INNER` returns the rows where there is a match in both tables.
    - `OUTER` returns all rows from on table and the matched rows from the other table. No match = `NULL`.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
    - `LEFT OUTER` returns all rows from the left table and the matched rows from the right table. No match = `NULL`.
    - `RIGHT OUTER` returns all rows from the right table and the matched rows from the left table. No match = `NULL`.

- What is an ORM? What do they do?
    - `ORM` is object relational mapping. This is a programming technique that allows you to query and manipulate data from a database using an object oriented paradigm. `ORMs` map database tables to classes and rows to objects. This simplifies database interactions and maintainability and readability of code.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
    - `AJAX` used to make requests from the client side.
    - `Requests` used to fetch data, e.g. APIs, web scraping, or communicating with other services.

- What is CSRF? What is the purpose of the CSRF token?
    - `CSRF` is a type of attack where a malicious website tricks a user's browser into performing an unwanted action on a trusted site where the user is authenticated.
    - `CSRF token` is used to verify a request comes from an authenticated user.

- What is the purpose of `form.hidden_tag()`?
    - `form.hidden_tag()` is a method to insert hidden fields into a form. This is a great way to include a `CSRF token`.
