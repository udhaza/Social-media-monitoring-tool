import instaloader
import streamlit as st
# Create an instance of Instaloader
loader = instaloader.Instaloader()

def scrape_hashtags(hashtag, count):
    posts = instaloader.Profile.from_username(loader.context, hashtag).get_posts()
    post_count = 0

    for post in posts:
        if post_count >= count:
            break

        post_count += 1
        st.write(f"Caption: {post.caption}")
        st.write(f"Likes: {post.likes}")
        st.write(f"Link: https://www.instagram.com/p/{post.shortcode}")
        st.write("---")

# Streamlit app
st.set_page_config(page_title="HackElevate", page_icon=":satellite_antenna:", layout="centered")
with st.container():
    st.subheader("Hackelevate - Social Media Monitoring")
st.title("Instagram Hashtag Scraper")
hashtag = st.text_input("Enter the hashtag to search for posts")
count = st.number_input("Enter the number of posts to retrieve", min_value=1, max_value=100, step=1, value=10)
if st.button("Search"):
    scrape_hashtags(hashtag, count)
