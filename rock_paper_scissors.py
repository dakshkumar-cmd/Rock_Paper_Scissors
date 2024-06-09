import random

import streamlit as st
st.set_page_config(page_title="Rock Paper Scissors", page_icon=":tada:")
try:

        user_action = st.selectbox("Choose Your Favorite Choice",("Rock","Paper","Scissors"))
        a = st.button("Submit")
        if a:
            

            possible_actions = ["Rock","Paper","Scissor"]
            computer_action = random.choice(possible_actions)
            st.text(f"Computer Choice - {computer_action}")
            st.text(f"User Choice - {user_action}")
            if user_action == possible_actions:
                st.text("Tie")

            elif (user_action == "Paper") and (computer_action == "Rock"):
                st.text("You Win")
                st.balloons()
            elif (user_action == "Rock") and (computer_action == "Scissor"):
                st.text("You Win")
                st.balloons()

            elif (user_action == "Scissor") and (computer_action == "Paper"):
                st.text("You win")
                st.balloons()

            else:
                st.text("You Lose and Computer Win")
                st.snow()




finally:
     print("Do")







