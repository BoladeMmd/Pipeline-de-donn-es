# FONCTION D'AUTHENTIFICATION POUR SE CONNECTER A LA PLATEFORME
import streamlit as st

def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(
                rgba(0, 0, 0, 0.55),
                rgba(0, 0, 0, 0.55)
            ),
            url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def login():
    set_background(
        #"https://images.unsplash.com/photo-1520607162513-77705c0f0d4a"
        "https://amiseo.fr/wp-content/uploads/2025/05/man-using-laptop-analyze-financial-charts-1536x1024.jpg"
    )

    # ----- TITRE (SANS CADRE) -----
    st.markdown("""
    <div style="
        width: 100%;
        display: flex;
        justify-content: center;
    ">
        <h1 style="
            color: white;
            font-weight: 700;
            white-space: nowrap;
            font-size: 38px;
            margin: 0 auto;
            text-align: center;
        ">
            📊 Bienvenue sur votre Plateforme d’automatisation du SAP de la DRS
        </h1>
    </div>

    <p style="
        text-align: center;
        color: #E0E0E0;
        font-size: 18px;
        margin-bottom: 40px;
    ">
        Système automatisé de traitement et de visualisation des données
    </p>
    """, unsafe_allow_html=True)

    # ----- CARTE BLANCHE (FORMULAIRE SEULEMENT) -----
    st.markdown("""
    <div style="
        background-color: rgba(255, 255, 255, 0.95);
        padding: 3px 15px;  /* réduit verticalement et horizontalement */
        border-radius: 15px;
        max-width: 420px;
        margin: auto;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
    ">
        <!-- Texte placé à l'intérieur de la carte -->
        <h3 style='text-align:center; color:#003366; margin-bottom:15px;'>Veuillez vous connecter</h3>
    """, unsafe_allow_html=True)

    # ----- LABELS JAUNES -----
    st.markdown("""
    <style>
    label {
        color: #F5C542 !important;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

    # ----- CHAMPS UTILISATEUR -----
    username = st.text_input("👤 Nom d'utilisateur")
    password = st.text_input("🔒 Mot de passe", type="password")

    # ----- BOUTON DE CONNEXION -----
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        login_button = st.button("🔐 Se connecter", use_container_width=True)

    if login_button:
        if (
            username == st.secrets["STREAMLIT_USER"]
            and password == st.secrets["STREAMLIT_PASSWORD"]
        ):
            st.session_state.authenticated = True
            st.success("✅ Connexion réussie")
            st.rerun()
        else:
            st.error("❌ Identifiants incorrects")

    # Fermer le div de la carte blanche
    st.markdown("</div>", unsafe_allow_html=True)

def require_auth():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        login()
        st.stop()
