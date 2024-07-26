import streamlit as st

def right():
    st.title("Hackathon Management")

    # List of image filenames (assuming they are in the same directory as this script)
    images = [
        "1.png",
        "2.png",
        "3.png",
        "4.png",
        "5.png"
    ]

    # Index to track current image
    index = st.session_state.get('index', 0)

    if index < 5:
        # Display the current image with larger dimensions
        st.image(images[index], width=600)

        # Button for navigation
        if index == 0:
            if st.button('Start'):
                index += 1
                st.session_state['index'] = index
        elif index < 4:
            if st.button('Next'):
                index += 1
                st.session_state['index'] = index
        elif index == 4:
            # Change the "Get Started" button to link to the external website
            if st.button('Get Started'):
                # Update the index to reset the session state for future use
                st.session_state['index'] = 0
                st.write('')  # Clear the UI

                # Redirect to the external website
                st.markdown(
                    """
                    <meta http-equiv="refresh" content="0; url=https://hackathandbms.com" />
                    """,
                    unsafe_allow_html=True
                )

if __name__ == "__main__":
    right()
