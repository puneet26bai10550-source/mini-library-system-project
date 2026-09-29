# Problem Statement: Mini Library System

## Background
Managing books manually on paper or in registers can be confusing and time-consuming. It is easy to lose track of which books are available, which ones are issued to users, and who needs to return what.

## Objective
The objective of this project is to build a simple, menu-driven Python program that helps manage a small collection of books easily through a command-line interface (CLI).

## Key Requirements
1. **Store Book Details:** Keep track of book information including Book ID, Title, Author/Writer, and Issue Status (Available or Issued).
2. **Display All Books:** Show a list of all stored books along with whether they are currently available or issued.
3. **Add New Books:** Allow the user to input details for a new book and store it in the system.
4. **Search Functionality:** Enable users to find a book by typing its title (or part of its title).
5. **Issue Books:** Let users borrow a book using its unique ID, changing its status from available to issued.
6. **Return Books:** Allow users to return an issued book back to the library.
7. **Interactive Menu:** Keep the application running in a loop with clear options until the user chooses to exit.