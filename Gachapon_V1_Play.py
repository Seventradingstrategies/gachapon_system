import streamlit as st
import random

def gachapon(prizes_with_probabilities):
    prizes, probabilities = zip(*prizes_with_probabilities.items())
    return random.choices(prizes, probabilities)[0]

def main():
    st.set_page_config(page_title="Gachapon", page_icon=":game_die:", layout="centered")

    st.title("Gachapon Machine")
    st.markdown("Welcome to the Gachapon Machine. Click the button to get a prize!")

    # Add the link to the Telegram channel
    st.markdown(
        "Join our Telegram channel [SevenLevelCapital](https://t.me/SevenLevelCapital) for updates and discussions!"
    )

    backend_password = st.sidebar.text_input("Enter backend password for prize probabilities:", type="password")

    prizes_with_probabilities = {}

    if backend_password == "your_password":  # Set your desired password here
        st.sidebar.write("Add prizes and probabilities:")

        num_prizes = st.sidebar.number_input("Number of prizes:", min_value=1, value=1)
        for i in range(num_prizes):
            prize_name = st.sidebar.text_input(f"Prize {i+1} name:", key=f"prize{i+1}_name")
            prize_probability = st.sidebar.slider(f"Prize {i+1} probability:", 0.0, 1.0, 0.1, key=f"prize{i+1}_probability")
            if prize_name:
                prizes_with_probabilities[prize_name] = prize_probability

    if st.button("Get a Prize"):
            if prizes_with_probabilities:
                prize = gachapon(prizes_with_probabilities)
                st.success(f"Congratulations! You won a {prize}!")
            else:
                st.warning("Please add at least one prize and its probability in the backend section.")

if __name__ == "__main__":
    main()
