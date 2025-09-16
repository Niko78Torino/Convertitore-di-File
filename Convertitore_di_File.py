# Importa la libreria di Streamlit
import streamlit as st

# Imposta il titolo dell'applicazione che apparirà nel browser
st.title('La Mia Prima App Streamlit!')

# Scrive un messaggio di benvenuto
st.write("Ciao mondo! Questa è la mia prima applicazione web.")

# Aggiunge un sottotitolo
st.header("Componente Interattivo")

# Crea un pulsante. Se viene cliccato, il codice all'interno dell'if viene eseguito.
if st.button('Cliccami!'):
    # Mostra un messaggio di successo
    st.success("Hai cliccato il pulsante! Ottimo lavoro.")
    # Mostra un'animazione divertente con dei palloncini
    st.balloons()
