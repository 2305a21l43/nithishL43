import streamlit as st
P=0
Q=0
S=0

def Elec_Power(V, I, PF):
    P = V * I * PF
    Q = V * I * ((1 - PF*2) * 0.5)
    S = V * I
    return P, Q, S

st.title("2305a21l43-PS2")
st.write("this application is useful for calculating the active power(p),reactive power(q) and apparent power(s) based on input parameters such as voltage,current,and poer factor")

col=st.columns(2)
with col[0]:
    V = st.number_input("Input Voltage (V):", min_value=0.0, value=0.0)
    I = st.number_input("Input Current (I):", min_value=0.0, value=0.0)
    PF = st.number_input("Power Factor (PF):", min_value=0.0, max_value=1.0, value=0.0)
    if st.button("Compute"):
         P, Q, S = Elec_Power(V, I, PF)

with col[1]:
   
    
    st.write("Active Power (P):", P,"W")
    st.write("Reactive Power (Q):", Q," VARs")
    st.write("Apparent Power (S):" ,S ,"VA")
