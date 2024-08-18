import streamlit as st

# Custom CSS for improved styling
st.markdown("""
    <style>
    /* General Page Styling */
   body {
    background-color: #ffffff; /* Light background for readability */
    color: #333333; /* Dark text color for contrast */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
}


    /* Title Styling */
    .title {
        text-align: center;
        color: #27ae60; /* Fresh green color for a modern look */
        font-size: 2.5rem;
        font-weight: 700;
        margin-top: 30px;
    }

    /* Subtitle Styling */
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #555555; /* Slightly darker text for subtitles */
        margin-bottom: 20px;
        line-height: 1.6;
    }

    /* Button Styling */
    .stButton button {
        background-color: #27ae60; /* Green button for primary action */
        color: white;
        border-radius: 5px;
        padding: 12px 24px;
        font-size: 1.1rem;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }

    .stButton button:hover {
        background-color: #1e8449; /* Darker green on hover */
        transform: scale(1.05); /* Slightly scale button on hover */
    }

    /* Image Styling */
    .image-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .image-container img {
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #95a5a6;
        margin-top: 40px;
        padding: 20px 0;
    }

    /* Container Styling */
    .container {
        width: 90%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    /* Link Styling */
    a {
        color: #27ae60;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Container for the content
with st.container():
    # Title with an emoji
    st.markdown('<div class="title">🌿 Welcome to the Farm Disease Detection and Recommendation System</div>', unsafe_allow_html=True)

    # Subtitle and descriptive text
    st.markdown("""
    <div class="subtitle">
        **Welcome to our advanced Plant Disease Detection and Recommendation System!** 🌱<br><br>
        This tool is designed to help you:
        <ul>
            <li><strong>Upload images</strong> of plant leaves.</li>
            <li><strong>Get precise disease predictions</strong> from the images.</li>
            <li><strong>Receive comprehensive recommendations</strong> for treatment and prevention.</li>
        </ul>
        <h3>How It Works:</h3>
        1. <strong>Navigate</strong> to the <strong>Diagnostic Tool</strong> section.<br>
        2. <strong>Upload</strong> an image of a plant leaf.<br>
        3. <strong>Receive predictions</strong> and actionable recommendations instantly.<br><br>
        We aim to support you in keeping your plants healthy and thriving. Explore the features and take advantage of our tool to maintain the best care for your plants.<br><br>
        For any questions or additional help, check out the [FAQs](#) or contact us through the [Contact](#) page.<br><br>
        **Let's get started and ensure your plants are always in their best shape!** 🌟
    </div>
    """, unsafe_allow_html=True)

    # Add an image or logo
    st.markdown('<div class="image-container"><img src="./farming-banner-with-logo.jpg" alt="Plant Disease Detection Tool" width="80%"></div>', unsafe_allow_html=True)

    # Button to start using the diagnostic tool
    if st.button("Go to Diagnostic Tool"):
        st.write("Redirecting you to the Diagnostic Tool...")
        # Navigation logic goes here

    # Optional Footer
    st.markdown('<div class="footer">© 2024 Plant Disease Detection System. All Rights Reserved.</div>', unsafe_allow_html=True)
