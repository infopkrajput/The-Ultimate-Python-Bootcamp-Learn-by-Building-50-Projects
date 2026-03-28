data = [
  {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
    "description": "A powerful story about racial injustice and moral growth in the American South."
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "genre": "Dystopian",
    "description": "A chilling depiction of a totalitarian regime that uses surveillance and propaganda to control citizens."
  },
  {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "genre": "Philosophical Fiction",
    "description": "A young shepherd travels in search of treasure and discovers the importance of following dreams."
  },
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic",
    "description": "A tale of love, wealth, and illusion set in the Roaring Twenties."
  },
  {
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "genre": "Romance",
    "description": "A classic story of love and misunderstanding between Elizabeth Bennet and Mr. Darcy."
  },
  {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "genre": "Fantasy",
    "description": "Bilbo Baggins embarks on an adventurous quest filled with dragons, treasure, and self-discovery."
  },
  {
    "title": "Harry Potter and the Sorcerer's Stone",
    "author": "J.K. Rowling",
    "genre": "Fantasy",
    "description": "A young boy discovers he is a wizard and begins his journey at Hogwarts School."
  },
  {
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "genre": "Fiction",
    "description": "A teenage boy narrates his struggles with identity and alienation."
  },
  {
    "title": "The Kite Runner",
    "author": "Khaled Hosseini",
    "genre": "Drama",
    "description": "A story of friendship, betrayal, and redemption set in Afghanistan."
  },
  {
    "title": "Sapiens",
    "author": "Yuval Noah Harari",
    "genre": "Non-fiction",
    "description": "An exploration of human history from ancient times to modern society."
  },
  {
    "title": "Atomic Habits",
    "author": "James Clear",
    "genre": "Self-help",
    "description": "A guide to building good habits and breaking bad ones through small changes."
  },
  {
    "title": "The Power of Now",
    "author": "Eckhart Tolle",
    "genre": "Spiritual",
    "description": "A book that teaches living in the present moment for a peaceful life."
  },
  {
    "title": "Think and Grow Rich",
    "author": "Napoleon Hill",
    "genre": "Self-help",
    "description": "A motivational book focused on success through mindset and determination."
  },
  {
    "title": "Rich Dad Poor Dad",
    "author": "Robert Kiyosaki",
    "genre": "Finance",
    "description": "A comparison of financial philosophies that teaches wealth-building strategies."
  },
  {
    "title": "The Subtle Art of Not Giving a F*ck",
    "author": "Mark Manson",
    "genre": "Self-help",
    "description": "A bold approach to living a meaningful life by focusing on what truly matters."
  },
  {
    "title": "The Book Thief",
    "author": "Markus Zusak",
    "genre": "Historical Fiction",
    "description": "A story of a young girl in Nazi Germany who finds solace in stealing books."
  },
  {
    "title": "The Fault in Our Stars",
    "author": "John Green",
    "genre": "Romance",
    "description": "A touching love story between two teenagers battling cancer."
  },
  {
    "title": "A Brief History of Time",
    "author": "Stephen Hawking",
    "genre": "Science",
    "description": "An explanation of the universe, black holes, and time in simple language."
  },
  {
    "title": "The Silent Patient",
    "author": "Alex Michaelides",
    "genre": "Thriller",
    "description": "A psychological thriller about a woman who stops speaking after a shocking crime."
  },
  {
    "title": "Gone Girl",
    "author": "Gillian Flynn",
    "genre": "Thriller",
    "description": "A suspenseful story of a marriage filled with secrets and deception."
  },
  {
    "title": "The Da Vinci Code",
    "author": "Dan Brown",
    "genre": "Mystery",
    "description": "A fast-paced novel involving secret societies and hidden historical truths."
  },
  {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "genre": "Dystopian",
    "description": "A deadly competition in a futuristic society where survival is the ultimate goal."
  },
  {
    "title": "The Road",
    "author": "Cormac McCarthy",
    "genre": "Post-apocalyptic",
    "description": "A father and son journey through a bleak and dangerous world."
  },
  {
    "title": "Life of Pi",
    "author": "Yann Martel",
    "genre": "Adventure",
    "description": "A boy survives a shipwreck and shares a lifeboat with a Bengal tiger."
  },
  {
    "title": "The Shining",
    "author": "Stephen King",
    "genre": "Horror",
    "description": "A family becomes trapped in a haunted hotel with terrifying consequences."
  },
  {
    "title": "Dracula",
    "author": "Bram Stoker",
    "genre": "Horror",
    "description": "The classic tale of the infamous vampire Count Dracula."
  },
  {
    "title": "Frankenstein",
    "author": "Mary Shelley",
    "genre": "Science Fiction",
    "description": "A scientist creates life but must face the consequences of his actions."
  },
  {
    "title": "The Little Prince",
    "author": "Antoine de Saint-Exupéry",
    "genre": "Fable",
    "description": "A philosophical tale about love, loneliness, and human nature."
  },
  {
    "title": "Meditations",
    "author": "Marcus Aurelius",
    "genre": "Philosophy",
    "description": "Personal writings of a Roman emperor on Stoic philosophy and life."
  },
  {
    "title": "The 7 Habits of Highly Effective People",
    "author": "Stephen R. Covey",
    "genre": "Self-help",
    "description": "A guide to personal and professional effectiveness through proven principles."
  }
]

import pandas as pd

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print("Books DataFrame created and saved to books.csv")