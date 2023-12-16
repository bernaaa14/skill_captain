# Day 7 Django model Relationships

### Tasks:

1. Create three models: Book, Author, and Genre.



2. Define the fields for each model:
- Book model: title (CharField), author (ForeignKey to Author model), genre (ManyToManyField to Genre model), publication_date (DateField), price (DecimalField).
- Author model: name (CharField), birth_date (DateField), nationality (CharField).
- Genre model: name (CharField).

![Alt text](<Screenshots/Screenshot from 2023-12-16 16-32-12.png>)


3.Create at least three instances of each model and populate them with sample data.
![Alt text](<Screenshots/Screenshot from 2023-12-14 10-39-03.png>)
![Alt text](<Screenshots/Screenshot from 2023-12-14 10-38-50.png>)
![Alt text](<Screenshots/Screenshot from 2023-12-14 10-38-58.png>)




4. Write Django queries to perform the following operations:
- Retrieve all books written by a specific author.
![Alt text](<Screenshots/Screenshot from 2023-12-14 21-17-01.png>)

- Retrieve all authors of a specific genre.
![Alt text](<Screenshots/Screenshot from 2023-12-16 08-04-23.png>)

- Add a new book with its corresponding author and genres.
![Alt text](<Screenshots/Screenshot from 2023-12-16 10-41-53.png>)

- Update the price of a specific book.
![Alt text](<Screenshots/Screenshot from 2023-12-16 11-06-32.png>)

- Remove a genre from a specific book.
![Alt text](<Screenshots/Screenshot from 2023-12-16 16-23-50.png>)

![Alt text](<Screenshots/Screenshot from 2023-12-16 16-26-51.png>)
![Alt text](<Screenshots/Screenshot from 2023-12-16 16-27-03.png>)



5. Create Django views and templates to display the book details, author information, and genre list.
![Alt text](<Screenshots/Screenshot from 2023-12-16 19-07-32.png>)
![Alt text](<Screenshots/Screenshot from 2023-12-16 19-05-00.png>)
![Alt text](<Screenshots/Screenshot from 2023-12-16 19-05-30.png>)
![Alt text](<Screenshots/Screenshot from 2023-12-16 19-05-55.png>)
![Alt text](<Screenshots/Screenshot from 2023-12-16 19-06-14.png>)
![Alt text](<Screenshots/Screenshot from 2023-12-16 18-35-15.png>)
![Alt text](<Screenshots/Screenshot from 2023-12-16 19-04-19.png>)

Challenge/s faced:
-Spent reasonable amount of time in terms of many to many fields and its associative identity.

Change/s made:


