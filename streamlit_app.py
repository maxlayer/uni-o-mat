import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-cplor:
#FFFF00;
    }
    .logo {
        width: 200px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("uni.png", use_column_width=False, width=200)

# Titel der App
st.title("Uni-O-Mat")

# Einführungstext
st.write("""
Willkommen beim Uni-O-Mat! Diese App hilft dir dabei, die richtige Entscheidung bezüglich deiner Universitätswahl oder Kurswahl zu treffen. 
Bitte wähle eine der folgenden Optionen aus:
""")

# Auswahl ob die Person bereits studiert
study_status = st.radio(
    "Bist du bereits Student/in?",
    ("Noch nicht", "Bachelor-Student/in", "Master-Student/in")
)

# Funktion zur Anzeige des Fragenkatalogs für neue Studenten
def new_student_questions():
    st.header("Persönliche Informationen")
    name = st.text_input("Wie heißt du?")
    age = st.number_input("Wie alt bist du?", min_value=16, max_value=100)

    st.header("Akademische Interessen")
    st.write("Welche Studienfächer interessieren dich am meisten? (Mehrfachauswahl möglich)")
    subjects = st.multiselect(
        "",
        ["Informatik", "Maschinenbau", "Medizin", "Rechtswissenschaften", "Psychologie", "Betriebswirtschaft", "Biologie", "Chemie", "Physik", "Literatur", "Philosophie"]
    )

    st.header("Präferenzen")
    st.write("Beantworte die folgenden Fragen zu deinen Präferenzen.")
    location_preference = st.selectbox("Bevorzugst du eine bestimmte Region oder Stadt?", ["Keine Präferenz", "Großstadt", "Kleinstadt", "ländliche Gegend", "spezifische Region/Stadt"])
    university_type = st.selectbox("Bevorzugst du eine bestimmte Art von Universität?", ["Keine Präferenz", "Technische Universität", "Fachhochschule", "Kunsthochschule", "Universität mit starkem Forschungsfokus"])
    cost_concern = st.slider("Wie wichtig sind dir die Studienkosten?", 0, 10, 5)

    st.header("Sonstige Überlegungen")
    extracurriculars = st.text_area("Gibt es bestimmte außerschulische Aktivitäten, die dir wichtig sind? (z.B. Sport, Musik, ehrenamtliches Engagement)")
    future_goals = st.text_area("Welche beruflichen Ziele verfolgst du nach deinem Studium?")

    return {
        "name": name,
        "age": age,
        "subjects": subjects,
        "location_preference": location_preference,
        "university_type": university_type,
        "cost_concern": cost_concern,
        "extracurriculars": extracurriculars,
        "future_goals": future_goals
    }

# Funktion zur Anzeige des Fragenkatalogs für bestehende Studenten
def current_student_questions():
    st.header("Aktuelle Studiensituation")
    current_study_field = st.text_input("In welchem Fach studierst du derzeit?")
    current_university = st.text_input("An welcher Universität studierst du?")
    current_degree_level = st.selectbox("Welchen Abschluss strebst du derzeit an?", ["Bachelor", "Master", "Promotion"])

    st.header("Akademische Interessen")
    st.write("Welche Vertiefungsrichtungen oder Zusatzqualifikationen interessieren dich? (Mehrfachauswahl möglich)")
    interests = st.multiselect(
        "",
        ["Data Science", "Künstliche Intelligenz", "Nachhaltigkeit", "Entrepreneurship", "Medizinische Forschung", "Technologiemanagement"]
    )

    st.header("Präferenzen für den nächsten Schritt")
    preferred_next_step = st.selectbox("Was ist dein bevorzugter nächster Schritt?", ["Weiteres Studium", "Berufseinstieg", "Forschungsprojekt", "Start eines eigenen Unternehmens"])

    return {
        "current_study_field": current_study_field,
        "current_university": current_university,
        "current_degree_level": current_degree_level,
        "interests": interests,
        "preferred_next_step": preferred_next_step
    }

# Funktion zur Abfrage des Social-Media-Profils
def social_media_profile():
    st.header("Social-Media-Profil")
    linkedin_profile = st.text_input("Gib deinen LinkedIn-Profil-URL ein")
    twitter_profile = st.text_input("Gib deinen Twitter-Profil-URL ein (optional)")

    return {
        "linkedin_profile": linkedin_profile,
        "twitter_profile": twitter_profile
    }

# Funktion zur Ähnlichkeitserkennung
def analyze_similarity(profile_data, social_media_data):
    st.subheader("Analyse der Ähnlichkeiten")
    # Platzhalter für die Analyse, die die Ähnlichkeit mit erfolgreichen Personen anhand von Social-Media-Profilen bewertet
    st.write("Deine Profile werden analysiert und mit denen erfolgreicher Personen verglichen...")
    # Beispielausgabe
    st.write(f"Dein LinkedIn-Profil: {social_media_data['linkedin_profile']}")
    st.write("Ähnlichkeiten mit erfolgreichen Personen: 85%")
    st.write("Empfohlene Kontakte: [Prof. Dr. Max Mustermann](https://www.linkedin.com/in/maxmustermann), [Dr. Maria Musterfrau](https://www.linkedin.com/in/mariamusterfrau)")

# Hauptlogik zur Anzeige der Fragenkataloge basierend auf der Auswahl
if study_status == "Noch nicht":
    profile_data = new_student_questions()
    social_media_data = social_media_profile()
elif study_status in ["Bachelor-Student/in", "Master-Student/in"]:
    profile_data = current_student_questions()
    social_media_data = social_media_profile()

# Button zur Ergebnisauswertung
if st.button("Ergebnisse anzeigen"):
    st.subheader("Dein Profil")
    for key, value in profile_data.items():
        st.write(f"**{key.replace('_', ' ').title()}:** {value}")

    if social_media_data:
        analyze_similarity(profile_data, social_media_data)

    # Hinweis auf nächste Schritte (optional)
    st.write("""
    Danke für das Ausfüllen des Fragebogens! Basierend auf deinen Antworten werden wir dir bald personalisierte Empfehlungen für Universitäten oder Kurse geben.
    """)

# Optional: Informationen über die App und Entwickler
st.sidebar.header("Über diese App")
st.sidebar.write("""
Diese App wurde entwickelt, um jungen Menschen bei der Wahl der richtigen Universität oder des richtigen Kurses zu helfen. 
Sie berücksichtigt persönliche Vorlieben, akademische Interessen und andere wichtige Faktoren.
""")

st.sidebar.header("Kontakt")
st.sidebar.write("""
Falls du Fragen oder Feedback hast, kontaktiere uns bitte unter:
- **E-Mail:** info@uni-o-mat.de
- **Telefon:** +49 123 456 789
""")