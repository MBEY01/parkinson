import streamlit as st
import joblib

# Load SVM model from joblib file
parkinsons_model = joblib.load('svm_clf.pkl')

# Parkinson's Prediction Page
st.title("Prediksi Penyakit Parkinson Menggunakan SVM")

fo = st.text_input('MDVP Fo(Hz)', help="Range: 88 to 260")
fhi = st.text_input('MDVP Fhi(Hz)', help="Range: 102 to 592")
flo = st.text_input('MDVP Flo(Hz)', help="Range: 65 to 240")
Jitter_percent = st.text_input('MDVP Jitter(%)', help="Range: 0.001 to 0.033")
Jitter_Abs = st.text_input('MDVP Jitter(Abs)', help="Range: 0.00002 to 0.0002")
APQ = st.text_input('MDVP APQ', help="Range: 0.007 to 0.14")
NHR = st.text_input('NHR', help="Range: 0.0006 to 0.31")
spread1 = st.text_input('Spread1', help="Range: -7 to -2")
spread2 = st.text_input('Spread2', help="Range: 0.006 to 0.45")
PPE = st.text_input('PPE', help="Range: 0.04 to 0.5")

# code for Prediction
parkinsons_diagnosis = ''

# creating a button for Prediction
if st.button("Hasil Tes Parkinson"):
    # Convert input values to float
    features = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
               float(APQ), float(NHR), float(spread1), float(spread2), float(PPE)]

    # Predict using the loaded model
    parkinsons_prediction = parkinsons_model.predict([features])

    if parkinsons_prediction[0] == 1:
        parkinsons_diagnosis = "Pasien Memiliki Penyakit Parkinson"
    else:
        parkinsons_diagnosis = "Pasien Tidak Memiliki Penyakit Parkinson"

st.success(parkinsons_diagnosis)
