import streamlit as st

st.set_page_config(
    page_title="Google-Style Unit Converter",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main {
        background-color: #5F6368;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        color: #202124;
        font-size: 24px !important;
        font-weight: 400 !important;
    }
    .stSelectbox label, .stNumberInput label {
        font-size: 14px;
        color: #5F6368;
        font-weight: 500;
    }
    .conversion-result {
        font-size: 36px;
        font-weight: 400;
        color: #202124;
        margin-top: 20px;
    }
    .formula {
        color: #5F6368;
        font-size: 13px;
    }
    .stButton button {
        background-color: #4285F4;
        color: white;
        border-radius: 4px;
    }
    .header-container {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .logo {
        margin-right: 10px;
        font-size: 24px;
        color: #4285F4;
    }
</style>
""", unsafe_allow_html=True)

CONVERSION_FACTORS = {
    "Length": {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        
    },
    "Mass": {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ton": 1000.0,
    },
    "Volume": {
        "Liter": 1.0,
        "Milliliter": 0.001,
        "Cubic Meter": 1000.0,
         },
    "Area": {
        "Square Meter": 1.0,
        "Square Kilometer": 1000000.0,
        "Square Centimeter": 0.0001,
        "Square Millimeter": 0.000001,
        
    },
    "Time": {
        "Second": 1.0,
        "Millisecond": 0.001,
        "Microsecond": 0.000001,
        "Nanosecond": 1e-9,
        "Minute": 60.0,
        "Hour": 3600.0,
        "Day": 86400.0,
        "Week": 604800.0,
        "Month (30 days)": 2592000.0,
        "Year (365 days)": 31536000.0,
    },
}
    

def convert_units(value: float, from_unit: str, to_unit: str, category: str) -> float:
    """Convert a value from one unit to another within the same category."""
    if from_unit == to_unit: 
        return value
    
    
    from_factor = CONVERSION_FACTORS[category][from_unit]
    to_factor = CONVERSION_FACTORS[category][to_unit]
    
    base_value = value * from_factor
    result = base_value / to_factor
    
    return result

def main():
    """Main application function."""
    # Header with Google-like styling
    st.markdown("""
    <div class="header-container">
        <div class="logo">⚖️</div>
        <h1>Unit Converter</h1>
    </div>
    """, unsafe_allow_html=True)
    
    category = st.selectbox("Select Category", list(CONVERSION_FACTORS.keys()))
    
    units = list(CONVERSION_FACTORS[category].keys())
    
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From", units, key="from_unit")
        from_value = st.number_input("Enter value", value=1.0, format="%.10g", key="from_value")
    
    with col2:
        to_unit = st.selectbox("To", units, key="to_unit")
        
        try:
            to_value = convert_units(from_value, from_unit, to_unit, category)
            
           
            if abs(to_value) >= 1e6 or (abs(to_value) < 1e-4 and abs(to_value) > 0):
                formatted_value = "{:.6e}".format(to_value)
            else:
                formatted_value = "{:.10g}".format(to_value)
                
            st.markdown(f"<div class='conversion-result'>{formatted_value}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Conversion error: {e}")
    


if __name__ == "__main__":
    main()



