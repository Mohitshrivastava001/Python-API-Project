import requests

def response_from_API():
    url = "https://api.freeapi.app/api/v1/public/books/39"
    response = requests.get(url)
    response_json = response.json()

    if response_json["success"] and "data" in response_json:
        Books = response_json["data"]
        Book_title = Books["volumeInfo"]["title"]
        Author = ', '.join(Books["volumeInfo"].get("authors", ["Unknown Author"]))
        return Book_title, Author
    else:
        raise Exception("Failed to get a successfull response")



def main():
    try:
        Book_title, Author = response_from_API()
        print(f"Book Title: {Book_title} \n Author: {Author}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

