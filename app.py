import streamlit as st
import pandas as pd

# Load data
books_df = pd.read_json('data/books.json')

# Streamlit UI
st.set_page_config(
    page_title="Books to Scrape Viewer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Books to Scrape - Book Explorer")
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Search box
search = st.text_input("🔍 Search book title", "")

# Filter
if search:
    books_filtered = books_df[books_df['title'].str.contains(search, case=False)]
else:
    books_filtered = books_df

# Show data
st.write(f"Showing {len(books_filtered)} books:")
st.dataframe(books_filtered)

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ using Streamlit | Data source: [Books to Scrape](https://books.toscrape.com/)"
)
