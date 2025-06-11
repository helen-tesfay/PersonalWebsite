import os
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Welcome!", page_icon=":tada:", layout="wide")

# ---- Background ----
custom_css = """
<style>
    /* Main page background */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://preview.colorkit.co/color/a66f6f.png?size=wallpaper&static=true");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;

    /* Make header transparent */
    [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0);
    }

    /* Adjust the toolbar position */
    [data-testid="stToolbar"] {
        right: 2rem;

    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Animation
def load_lottieurl(url: str):
      r = requests.get(url)
      if r.status_code != 200:
        return None
      return r.json()

# Animation
lottie_file = load_lottieurl("https://lottie.host/d7d83113-0460-40f7-b351-a61244ed9b9e/PfxGA5EEnx.json")

# Font
# st.markdown(
#    """
#    <style>
#    * {
#        font-family: "Times New Roman", serif !important;
#   }
#    </style>
#    """,
#    unsafe_allow_html=True
# )

# Images
img_joes_automotive = Image.open("joesauto.jpg")
img_parking_ticket = Image.open("parkingticket.jpg")
img_ship_image = Image.open("shipimage.jpg")

# CSS styling for "Contact Me" Section
def style_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

style_css("style.css")

def style_toml(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

style_toml("config.toml")

# ---- Intro ---- 
with st.container():
    st.subheader("Welcome!")
    st.title("Helen Tesfay – A.S. in Mathematics/Computer Science")
    st.write("Hi! I'm Helen, I recently graduated from Harrisburg Area Community College (HACC) in Harrisburg, PA.")
    st.write("I'm now a junior at Harrisburg University of Science and Technology (HU). As you can guess, I love to solve problems and create products.")
    st.write("When it came time to declare my major, it was easy for me to choose Mathematics/Computer Science at HACC and Computer and Information Sciences at HU.")
    st.write("Email: helen.h.tesfay@gmail.com")
    st.write("GitHub: https://github.com/helen-tesfay")
    st.write("LinkedIn: https://linkedin.com/in/helen-h-tesfay")

# ---- Experience ---- 
with st.container():
    left_column, right_column = st.columns(2)
    st.write("---")
    with left_column:
        st.header("Experience")
        st.write(
            
        """
        My experience includes the following key accomplishments:
        - Spring 2025 Dean's List
        - Fall 2024 Dean's List
        - Computer Science Club (CPS Club) Vice President/Secretary

        Selected highlights from my portfolio, with more available upon request:
        - ParkingTicket Simulator (Java)
        - JoesAutomotive Cost Calculator (Java, JavaFx)
        - Personal Webpage (Python, CSS, Streamlit, Pillow)

        Check these out in more detail below!
        """)
# Animation next to "Experience"
with right_column:
       st_lottie(lottie_file, height=400, key="coding")
        
# ----- PROJECTS -------
with st.container():
        st.write("----")
        st.header("Portfolio")

    # ---- PARKING TICKET -----
        image_column, text_column = st.columns([1, 2])
        with image_column:
            st.image(img_parking_ticket)
        with text_column:
            st.subheader("Parking Ticket Simulator: Be sure not to get a ticket!")
            st.write(
                """
                The parking ticket simulator GUI application is used to issue a parking ticket.
                This application has four classes, ParkedCar, ParkingMeter, ParkingTicket, and PoliceOffer. 
                The application checks how long a vehicle had been parked against any purchased time.
                If the purchased parking time is less than the time the vehicle had been parked, the PoliceOfficer class would a ticket.
                The ParkingTicket class would report the car's make, model, license plate number, officer name and fine amount.
                """
            )
            st.markdown("GitHub Repository: https://github.com/helen-tesfay/ParkingTicket")

    # ---- JOE'S ----
        image2_column, text2_column = st.columns([1, 2])
        with image2_column:
            st.image(img_joes_automotive)
        with text2_column:
            st.subheader("Joe's Automotive: Calculate your cost for a visit to Joe's!")
            st.write( 
                """
                Use my JoesAutomotive to get a quote for your visit to Joe's Automotive.
                The GUI application allows you to select from a "Routine Maintenance" dropdown
                as well as a "Repair Hours" dropdown for any repair work. It is necessary to call
                or meet with a repair technician first to get a quote for the number of hours.
                """
            )
            st.markdown("GitHub Repository: https://github.com/helen-tesfay/JoesAutomotive")

    # ---- SHIP ----
        image3_column, text3_column = st.columns([1, 2])
        with image3_column:
            st.image(img_ship_image)
        with text3_column:
            st.subheader("Ship, CruiseShip, and CargoShip Classes: Sail Today!")
            st.write(
                """
                The Ship, CruiseShip, and CargoShip classes work to store and print ship information. 
                The Ship superclass holds information about each ship's name and year built.
                The CruiseShip and CargoShip subclasses inherit the name and year built and add additional information.
                The ShipDemo class is to print each ship's information, such as CruiseShip's max. passenger capacity, and CargoShip's max. cargo capacity.
                This project encompasses inheritance, overriding methods, and honing use of arrays.
                """
            )
            st.markdown("GitHub Repository: https://github.com/helen-tesfay/Ship-CruiseShip-and-CargoShip-Classes")

# --- CONTACT ME ---
with st.container():
        st.write("----")
        st.header("Let's Be Friends")

        contact_field = """
    <form action="https://formsubmit.co/htesfay033@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
</form>
"""
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_field, unsafe_allow_html=True)
        with right_column:
            st.empty()
