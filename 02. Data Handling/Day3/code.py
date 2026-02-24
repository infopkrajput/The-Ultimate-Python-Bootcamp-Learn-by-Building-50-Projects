"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import json
import os
from unittest import case

FILENAME = 'movies.json'

def load_movies():
   if not os.path.exists(FILENAME):
      return []
   with open(FILENAME, "r", encoding="utf-8") as file:
      return json.load(file)

def save_movies(movies):
   with open(FILENAME, "w", encoding="utf-8") as file:
      json.dump(movies,file,indent=2)
      
def add_movies(movies):
   title = input("Enter the movie name: ").strip().lower()
   
   if any(movie["title"].lower() == title for movie in movies):
      print("Movie already exists!")
      return
   
   genre = input("Enter Genre: ").strip().lower()
   
   try:
      rating = float(input("Enter Rating(0-10): "))
      if not (0 <= rating <=10):
         raise ValueError
   except ValueError:
      print("Please enter valid number!")
      return
   
   movies.append({"title" : title, "genre" : genre, "rating" : rating})
   save_movies(movies)
   print("Movie added successfully!")
   
def search_movies(movies):
   query = input("Enter title or genre to search: ").strip().lower()
   results = [movie for movie in movies if query in movie["title"].lower() or query in movie["genre"].lower()]
   
   if not results:
      print("No movies found!")
      return
   
   print(f"found {len(results)} movies:")
   print(f"{'Title':<30} {'Genre':<20} {'Rating':<10}")
   print("-" * 60)
   for movie in results:
      print(f"{movie['title']:<30} {movie['genre']:<20} {movie['rating']:<10}")
      
def view_movies(movies):
   if not movies:
      print("No movies in database!")
      return
   
   print(f"{'Title':<30} {'Genre':<20} {'Rating':<10}")
   print("-" * 60)
   for movie in movies:
      print(f"{movie['title']:<30} {movie['genre']:<20} {movie['rating']:<10}")

def run_movie_db():
   movies = load_movies()
   
   while True:
      print("\n1. Add Movie")
      print("2. View Movies")
      print("3. Search Movies")
      print("4. Exit")
      
      choice = input("Choose an option(1-4): ").strip()
      
      match choice:
         case "1": add_movies(movies)
         case "2": view_movies(movies)
         case "3": search_movies(movies)
         case "4": print("Goodbye!"); break
         case _ : print("Invalid option, please try again.")
         
if __name__ == "__main__":
   run_movie_db()