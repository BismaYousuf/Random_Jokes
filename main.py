import streamlit as st
import requests

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .title {
            text-align: center;
            color: #ff5733;
            font-size: 36px;
            font-weight: bold;
        }
        .button {
            background-color: #ff5733;
            color: white;
            padding: 12px 24px;
            font-size: 20px;
            border-radius: 10px;
            transition: all 0.3s;
        }
        .button:hover {
            background-color: #ff3300;
            transform: scale(1.05);
        }
        .footer {
            text-align: center;
            font-size: 16px;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)


def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"😂 {joke_data['setup']} \n\n👉 {joke_data['punchline']}"
        else:
            return "⚠️ Failed to fetch a joke. Please try again later."
    except requests.exceptions.RequestException:
        return "🤖 Why did the programmer quit his job?\n\nBecause he didn't get arrays!"


def main():
    st.markdown("<h1 class='title'>😂 Random Joke Generator 😂</h1>", unsafe_allow_html=True)
    st.write("Click the button below to get a random joke!")

    # Centering the button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎭 Tell me a joke!"):
            joke = get_random_joke()
            st.success(joke)

    st.divider()

    st.markdown("""
    <div class="footer">
        <p>Joke from <b>Official Joke API</b></p>
        <p>💖 Built with love by <b>Bisma Yousuf</b></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
