import streamlit as st
from transformers import pipeline

# Konfiguracja strony
st.set_page_config(page_title="Text analysis & translation app - ML", page_icon=":earth_africa:")

# Tytuł strony
st.title("Aplikacja do Analizy i Tłumaczeń Tekstu")

# Instrukcja i informacje dodatkowe
st.markdown("""
### 📌 O aplikacji
Aplikacja wykorzystuje modele z Hugging Face do:
- analizy sentymentu tekstu
- tłumaczenia tekstu z angielskiego na niemiecki

### 📝 Instrukcja
1. Wybierz opcję z listy
2. Wpisz tekst po angielsku
3. Poczekaj na wynik
""")

st.success("Aplikacja uruchomiła się poprawnie!")

# Menu
st.header('Przetwarzanie języka naturalnego')

option = st.selectbox(
    "Wybierz funkcję:",
    [
        "Wydźwięk emocjonalny tekstu (ENG)",
        "Tłumaczenie ENG -> DE",
    ],
)

# Formularz
with st.form(key="my_form"):
    text = st.text_area("Wpisz tekst po angielsku", height=150)
    submit_button = st.form_submit_button(label="Wykonaj")

if submit_button and text:
    # Analiza tekstu
    if option == "Wydźwięk emocjonalny tekstu (ENG)":
        with st.spinner("Trwa analiza tekstu..."):
            try:
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)[0]
                label = answer["label"]
                score = answer["score"]

                st.success("Analiza zakończona suckesem!")
                st.metric(label="Sentyment", value=label, delta=f"{score:.1%} pewności")
                st.progress(float(score))

                st.subheader("Dokładny wynik:")
                st.code(answer, language="json")
            except Exception as e:
                st.error(f"Wystąpił błąd podczas analizy tekstu... Błąd: {e}")

    # Tłumaczenie tekstu
    elif option == "Tłumaczenie ENG -> DE":
        with st.spinner("Tłumaczę tekst..."):
            try:
                translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
                result = translator(text)
                translation = result[0].get("translation_text")

                st.success("Tłumaczenie zakończone!")
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Angielski")
                    st.info(text)
                with col2:
                    st.subheader("Niemiecki")
                    st.success(translation)

                st.subheader("Dokładny wynik:")
                st.code(result, language="json")
            except Exception as e:
                st.error(f"Wystąpił błąd podczas tłumaczenia tekstu... Błąd: {e}")


# Stopka
st.markdown("---")
st.info("Autor: s27531")
