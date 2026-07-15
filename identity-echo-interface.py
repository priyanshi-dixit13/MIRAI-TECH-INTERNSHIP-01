import streamlit as st # Load streamlit , short name 'st' for convenience 

# TASK 1 : The UI Shell-------------
st.title("The Void ")
st.write("Whisper your identity and your  message into abyss It's listening... and billing you per token.")

# TASK 2 : Multi-Data Collection-------------
user_name  = st.text_input("Who dares speak?")
user_message = st.text_input("What message echoes into the dark?")

# TASK 3 : The Action Gate--------------
if st.button("Send into the void "):

    # TASK 4 : Conditional  Routing (Edge Cases)-------------
    if user_name == "":
        st.error("The Void doesn't knoww who's speaking . Please provide your name.")
    elif user_message == "":
        st.warning("Silence isn't  a message.Please type something to transmit.")
    else:

        # TASK 5 : The Formatted Output------------ 
        st.success(f"Transmission successful! Greetings,{user_name}. We received your message:{user_message}")
        
        # Advanced Challenge : Token  Cost Estimator
        char_count = len(user_message)
        token_count = char_count //4
        st.info(f"System Check: Your  message will consume approximately {token_count} tokens from our content window.")

        st.caption(f"{char_count} characters whispered into the abyss.")  
    



        