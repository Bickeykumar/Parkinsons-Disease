import os
import pickle # pre trained model loading
import streamlit as st    # web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")
parkinsons_model= pickle.load(open(r"C:\Users\bicke\Desktop\parkinson disease\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Parkinsons Prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
    
if selected == 'Parkinsons Prediction':
        st.title('Parkinsons Prediction')

        col1, col2, col3, col4, col5=st.columns(5)

        with col1:
            fo=st.text_input('MDVP:Fo(Hz)')

        with col2:
            fhi=st.text_input('MDVP:Fhi(Hz)')

        with col3:
            flo=st.text_input('MDVP:Flo(Hz)')

        with col4:
            Jitter_percent=st.text_input('MDVP:Jitter(%)')

        with col5:
            Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
        
        with col1:
            RAP=st.text_input('MDVP:RAP')

        with col2:
            PPQ=st.text_input('MDVP:PPQ')

        with col3:
            DDP=st.text_input('Jitter:DDP')

        with col4:
            Shimmer=st.text_input('MDVP:Shimmer')

        with col5:
            Shimmer_dB=st.text_input('MDVP:Shimmer(dB)') 

        with col1:
            APQ3=st.text_input('Shimmer:APQ3')

        with col2:
            APQ5=st.text_input('MDVP:APQ5')

        with col3:
            APQ=st.text_input('MDVP:APQ')

        with col4:
            DDA=st.text_input('Shimmer:DDA')

        with col5:
            NHR=st.text_input('NHR')   
        
        with col1:
            HNR=st.text_input('HNR')
        
        with col2:
            RDPE=st.text_input('RDPE')
        
        with col3:
            DFA=st.text_input('DFA')
        
        with col4:
            spread1=st.text_input('spread1')
        
        with col5:
            spread2=st.text_input('spread2')
        
        with col1:
            D2=st.text_input('D2')
        
        with col2:
            PPE=st.text_input('PPE')

        parkinsons_diagnosis=''

        if st.button("Parkinson's Test Result"):

            user_input=[fo, fhi, flo, Jitter_percent,Jitter_Abs, RAP, 
                        PPQ, DDP, Shimmer,Shimmer_dB, APQ3, APQ5,
                        APQ, DDA, NHR,HNR,RDPE,DFA,spread1,spread2,D2,PPE]  

            user_input=[float(x) for x in user_input]

            parkinsons_prediction=parkinsons_model.predict([user_input])

            if parkinsons_prediction[0]==1:
                parkinsons_diagnosis='Parkinson\'s  Disease'
            else:
                parkinsons_diagnosis='No Parkinson\'s Disease'
        
        st.success(parkinsons_diagnosis)


