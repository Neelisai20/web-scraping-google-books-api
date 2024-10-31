import requests
import pandas as pd

def fetch_books_data(api_key, query, max_results=10):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': query,
        'key': api_key,
        'maxResults': max_results
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        books = []

        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            
            # Extract book details
            title = volume_info.get('title', 'Unknown Title')
            authors = ', '.join(volume_info.get('authors', ['Unknown Author']))
            publication_date = volume_info.get('publishedDate', 'Unknown Date')
            average_rating = volume_info.get('averageRating', 'No Rating')

            books.append({
                'Title': title,
                'Author': authors,
                'Publication Date': publication_date,
                'Average Rating': average_rating
            })

        return books

    else:
        print(f"Error: {response.status_code}")
        return []

def save_books_to_excel(books_data, filename="google_books_data.xlsx"):
    df = pd.DataFrame(books_data)
    df.to_excel(filename, index=False)
    print(f"Book data saved to {filename}")

if __name__ == "__main__":
    api_key = "YOUR_GOOGLE_API_KEY"
    search_query = "data science"
    max_books = 10

    # Fetch books data using the Google Books API
    books_data = fetch_books_data(api_key, search_query, max_books)
    
    # Save to Excel
    if books_data:
        save_books_to_excel(books_data)
    else:
        print("No book data found.")
