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

# Analiza tekstu
if option == "Wydźwięk emocjonalny tekstu (ENG)":
    text = st.text_area(label="Wpisz tekst po angielsku")
    if text:
        with st.spinner("Trwa analiza tekstu"):
            try:
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)

                st.success("Analiza zakończona suckesem!")
                st.write(answer)
            except Exception as e:
                st.error(f"Wystąpił błąd podczas analizy tekstu... Błąd: {e}")

# Tłumaczenie tekstu
elif option == "Tłumaczenie ENG -> DE":
    text = st.text_area("Wpisz tekst po angielsku")

    if text:
        with st.spinner("Tłumaczę tekst..."):
            try:
                translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
                result = translator(text)

                st.success("Tłumaczenie tekstu zakończone!")
                st.write("Tłumaczenie:")
                st.write(result[0]["generated_text"])

            except Exception as e:
                st.error(f"Wystąpił błąd podczas tłumaczenia tekstu... Błąd: {e}")


# Stopka
st.markdown("---")
st.info("Autor: s27531")

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/docs/transformers/index')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
