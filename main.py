import streamlit as st

POWER_PLAN = 1300
PRICE = 1444.70

st.set_page_config(layout='wide')
def count_bill(power, usage_time):
    return round(power/1000 * usage_time * 30, 2) * PRICE

# print(count_bill(230, 2))

st.title('Hitung Listrik Bulanan')

power = st.text_input('Power / Daya (Watt)')
usage_time = st.text_input('Usage Time (Hrs)/Day')

if st.button('Count'):
    st.write("Rp. " + f"{count_bill(int(power), int(usage_time)):,}" + "/month")
st.write("bernardrealino.com")