import json
import os
import streamlit as st

st.set_page_config(page_title="📚 Library Manager", page_icon="📘")

LIBRARY_FILE = "library.txt"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

def format_book(book):
    status = "Read" if book["read"] else "Unread"
    return f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}'

# Load library
library = load_library()

# Sidebar navigation
st.sidebar.title("Library Manager")
page = st.sidebar.radio("Go to", ["📚 View All Books", "➕ Add Book", "❌ Remove Book", "🔍 Search Book", "📊 Statistics"])

# Add Book
if page == "➕ Add Book":
    st.title("➕ Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
        genre = st.text_input("Genre")
        read = st.selectbox("Have you read it?", ["No", "Yes"])
        submitted = st.form_submit_button("Add Book")

        if submitted:
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": True if read == "Yes" else False
            }
            library.append(book)
            save_library(library)
            st.success("✅ Book added successfully!")

# View All Books
elif page == "📚 View All Books":
    st.title("📚 Your Library")
    if not library:
        st.warning("Your library is empty.")
    else:
        for i, book in enumerate(library, 1):
            st.markdown(f"**{i}.** {format_book(book)}")

# Remove Book
elif page == "❌ Remove Book":
    st.title("❌ Remove a Book")
    titles = [book["title"] for book in library]
    if not titles:
        st.warning("No books to remove.")
    else:
        to_remove = st.selectbox("Select a book to remove", titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != to_remove]
            save_library(library)
            st.success(f"✅ '{to_remove}' has been removed.")

# Search Book
elif page == "🔍 Search Book":
    st.title("🔍 Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    query = st.text_input("Enter search term")

    if query:
        if search_by == "Title":
            results = [book for book in library if query.lower() in book["title"].lower()]
        else:
            results = [book for book in library if query.lower() in book["author"].lower()]

        if results:
            st.subheader("Matching Books")
            for book in results:
                st.markdown(f"- {format_book(book)}")
        else:
            st.warning("❌ No matching books found.")

# Statistics
elif page == "📊 Statistics":
    st.title("📊 Library Statistics")
    total = len(library)
    read = sum(1 for book in library if book["read"])
    unread = total - read
    percent_read = (read / total) * 100 if total > 0 else 0

    st.metric("Total Books", total)
    st.metric("Read Books", read)
    st.metric("Unread Books", unread)
    st.progress(percent_read / 100)
    st.write(f"📖 **{percent_read:.1f}%** of your library has been read.")
