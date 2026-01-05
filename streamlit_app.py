!pip install -q streamlit
    
%%writefile app.py
import streamlit as st

# --- THEME CONFIGURATION ---
st.set_page_config(page_title="Classy in Scrubs", layout="wide")

# Custom CSS for Luxury Branding
st.markdown("""
    <style>
    .main { background-color: #fdfdfd; }
    .stButton>button { background-color: #c5a059; color: white; border-radius: 5px; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #a68546; color: white; border: 1px solid #001f3f; }
    [data-testid="stSidebar"] { background-color: #001f3f; } /* Deep Navy Sidebar */
    [data-testid="stSidebar"] * { color: white !important; }
    h1, h2, h3 { color: #001f3f; font-family: 'Playfair Display', serif; }
    .motto { color: #c5a059; font-style: italic; font-size: 1.5rem; text-align: center; margin-top: -20px; }
    .gold-highlight { color: #c5a059; font-weight: bold; }
    </style>
    """, unsafe_content_allowed=True)

# --- NAVIGATION ---
st.sidebar.markdown("<h2 style='text-align: center;'>CLASSY IN SCRUBS</h2>", unsafe_content_allowed=True)
page = st.sidebar.radio("Navigation", ["Home", "The Collection", "Contact & Fittings"], label_visibility="collapsed")

# --- PAGE 1: HOME ---
if page == "Home":
    st.markdown("<h1 style='text-align: center; letter-spacing: 2px;'>CLASSY IN SCRUBS</h1>", unsafe_content_allowed=True)



import urllib
print("1. YOUR PASSWORD/IP:", urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip())
!streamlit run app.py & npx localtunnel --port 8501

    st.markdown("<p class='motto'>\"When you look good, we feel good\"</p>", unsafe_content_allowed=True)
    
    # High-end Hero Image
    st.image("https://images.unsplash.com/photo-1599493758267-c6c884c7071f?q=80&w=1200", use_container_width=True)
    
    st.markdown("<br>", unsafe_content_allowed=True)
    st.write("### Elegance in the Workplace")
    st.write("At Classy in Scrubs, we provide premium medical apparel for the modern professional who refuses to compromise on style.")

# --- PAGE 2: THE COLLECTION ---
elif page == "The Collection":
    st.title("Our Signature Collection")
    
    # Measurement Section
    with st.container():
        st.markdown("### <span class='gold-highlight'>The Bespoke Fit Assistant</span>", unsafe_content_allowed=True)
        st.write("Ensuring you look your best starts with the perfect measurement.")
        
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            bust = st.number_input("Chest/Bust (inches)", 30, 60, 38)
        with col_m2:
            waist = st.number_input("Waist (inches)", 20, 55, 30)
        with col_m3:
            hips = st.number_input("Hips (inches)", 30, 65, 40)
            
        # Refined Size Logic
        if bust < 35: size_rec = "Extra Small"
        elif bust < 38: size_rec = "Small"
        elif bust < 41: size_rec = "Medium"
        elif bust < 45: size_rec = "Large"
        else: size_rec = "Extra Large"
        
        st.success(f"Based on your profile, your recommended **Classy Fit** is: **{size_rec}**")

    st.divider()

    # Brand Display
    brand_tab1, brand_tab2 = st.tabs(["Cherokee Collections", "Infinity Performance"])
    
    with brand_tab1:
        c1, c2 = st.columns([1, 1])
        with c1:
            st.image("https://images.unsplash.com/photo-1631815589968-fdb09a223b1e?q=80&w=500")
        with c2:
            st.header("Cherokee")
            st.write("Professionalism meets peak durability. The timeless choice for every clinician.")
            st.button("View Cherokee Styles")

    with brand_tab2:
        i1, i2 = st.columns([1, 1])
        with i1:
            st.image("https://images.unsplash.com/photo-1582921017967-79d1cb6702ee?q=80&w=500")
        with i2:
            st.header("Infinity")
            st.write("Athletic-inspired design with antimicrobial fabric. Move with confidence.")
            st.button("View Infinity Styles")

# --- PAGE 3: CONTACT ---
elif page == "Contact & Fittings":
    st.title("Connect With Us")
    
    st.info("📍 **Boutique Location:** Medical Plaza, Nairobi, Kenya")
    
    with st.form("luxury_contact"):
        st.markdown("#### Inquiry Form")
        st.text_input("Name")
        st.text_input("Email")
        st.selectbox("I am interested in...", ["Personal Order", "Hospital/Clinic Bulk Order", "Sizing Consultation"])
        st.text_area("How can we help you look good?")
        st.form_submit_button("Send to Classy in Scrubs")


