# Define the left and right columns
right_column, left_column = st.columns([1, 2])
with right_column:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(r"images/profile.png", use_column_width=True)

with left_column:
    st.title("About Me")
    st.markdown(
        "<div style='text-align: justify'>"
        "Hello! I'm Rishi Raj Sharma, a tech enthusiast with a passion for Cloud, Security, and AI. With a solid IT background, I thrive on tackling challenges and discovering innovative solutions."
        "<br>"
        "I love working in teams and always had a blast participating in hackathons and developer clubs. Staying calm under pressure and paying attention to the little details help me deliver quality results every time."
        "<br>"
        "Cybersecurity and AI are my passions, and I'm constantly exploring ways to enhance security frameworks and develop smart AI solutions.🕵️‍♂️ My goal is to contribute to the development of secure, cutting-edge technologies that make a difference."
        "<br>"
        "When I'm not into tech, you'll find me playing football ⚽, trekking ⛰️,hitting the gym 💪or enjoying good food🍴. I believe in keeping a healthy balance between work and life to stay inspired."
        "<br>"
        "Thanks for visiting my portfolio! Let's connect and explore the exciting world of technology together🚀"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://linkedin.com/in/rishirajsharma231'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/Rishiraj01'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='mailto:rishirajsharma231@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )
