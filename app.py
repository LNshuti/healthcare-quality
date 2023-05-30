import streamlit as st 

def main():

     st.set_page_config(layout="wide")
     st.title('**Healthcare Quality Measures** between hospitals and accross states in the United States')

     st.write(
          '''We track the following six measures of healthcare quality : 

                1. Mortality - Death rate for heart attack patients

                2. Safety of Care - Serious complications

                3. Readmission - 30-day readmission rate for heart attack patients

                4. Patient Experience - Patient experience survey results

                5. Effectiveness of Care - Timeliness of care for heart attack patients

                6. Timeliness of Care - Timeliness of care for heart attack patients
        '''
            )


main()
