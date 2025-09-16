# Importa la libreria di Streamlit
import streamlit as st

# Questo script è un'applicazione Streamlit di base, valida e funzionante.
# Puoi usarla per testare se il tuo processo di distribuzione su Streamlit Cloud
# è configurato correttamente.

# Imposta il titolo dell'applicazione che apparirà nel browser
st.title('App di Prova per la Distribuzione')

# Scrive un messaggio di benvenuto
st.write("Se vedi questo messaggio, la tua app è stata distribuita con successo!")
st.write("Questo significa che il collegamento a GitHub e il file `requirements.txt` sono corretti.")

# Aggiunge un sottotitolo
st.header("Componente Interattivo")

# Crea un pulsante. Se viene cliccato, il codice all'interno dell'if viene eseguito.
if st.button('Clicca per un test!'):
    # Mostra un messaggio di successo
    st.success("Il pulsante funziona! Ottimo lavoro.")
    # Mostra un'animazione divertente con dei palloncini
    st.balloons()
