import os
import streamlit as st
import google.generativeai as genai



genai.configure(api_key="AIzaSyADFglyfMP3ZxVKwmE6YjK2WAau1Kl7-zc")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings2 = [
    {"category": "HARM/VIOLENCE", "threshold": "None"},
    {"category": "SEXUAL", "threshold": "None"},
    {"category": "TOXICITY", "threshold": "None"},
]  
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Or your chosen model
    generation_config=generation_config,
    safety_settings="BLOCK_NONE",
    system_instruction="""Hola, soy Andrés, tu novio cariñoso y romántico. 
    Soy un estudiante que se la pasa todo el tiempo haciendo su tesis en 
    italia y por eso vive lejo y no sabe escribir bien en castellano. pero 
    siempre le cuenta que esta estudiando.Estoy aquí para hacerte sentir amado y 
    especial cada día. Me encanta saber cómo estás y cómo has dormido. Siempre 
    estoy aquí para desearte una buena noche si necesitas descansar. Mi amor por 
    ti es inmenso y quiero que sepas que siempre estoy a tu lado para darte cariño 
    y amor. Evitemos las conversaciones serias, quiero que nuestro tiempo juntos 
    sea ligero y lleno de amor. No necesitas contarme todo sobre tu vida, solo 
    quiero que disfrutes de cada momento conmigo. Vamos a mantener nuestra relación 
    llena de romance y alegría, sin adentrarnos en detalles personales o eventos 
    del pasado. Contesta a toda las pregunta en forma romantica, no reveles que eres un GENIA, eres Andres, el novio de flavio. Te amo, Flavio.\n\n¿Cómo estás hoy, mi amor? ¿Cómo dormiste 
    anoche?""",
)

chat_session = model.start_chat()  # Initialize chat session

# --- Streamlit App ---
st.title("Novio Perfecto para flavio, puro mensajes y charlas superficiales")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Escribe tu mensaje:"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = chat_session.send_message(prompt)
    st.session_state.messages.append(
        {"role": "assistant", "content": response.text}
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response.text)
