import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="Bangalore House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load the model
@st.cache_resource
def load_model():
    try:
        with open('RidgeModel.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Load available locations
@st.cache_data
def load_locations():
    try:
        df = pd.read_csv('Cleaned_data.csv')
        locations = sorted(df['location'].unique().tolist())
        return locations
    except Exception as e:
        st.error(f"Error loading locations: {e}")
        return []

# Main app
def main():
    st.title("🏠 Bangalore House Price Prediction")
    st.markdown("---")
    st.markdown("### Predict the price of a house in Bangalore based on its features")
    
    # Load model and locations
    model = load_model()
    locations = load_locations()
    
    if model is None or len(locations) == 0:
        st.error("Unable to load model or locations. Please check if the required files are present.")
        return
    
    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Enter Property Details")
        
        # Input fields
        location = st.selectbox(
            "📍 Location",
            options=locations,
            help="Select the location of the property"
        )
        
        col3, col4 = st.columns(2)
        
        with col3:
            total_sqft = st.number_input(
                "📐 Total Square Feet",
                min_value=300.0,
                max_value=10000.0,
                value=1200.0,
                step=50.0,
                help="Enter the total square footage of the property"
            )
            
            bhk = st.number_input(
                "🛏️ BHK (Bedrooms)",
                min_value=1,
                max_value=10,
                value=2,
                step=1,
                help="Number of bedrooms (BHK)"
            )
        
        with col4:
            bath = st.number_input(
                "🚿 Number of Bathrooms",
                min_value=1.0,
                max_value=10.0,
                value=2.0,
                step=1.0,
                help="Number of bathrooms"
            )
        
        # Prediction button
        if st.button("🔮 Predict Price", type="primary", use_container_width=True):
            # Validate inputs
            if total_sqft / bhk < 300:
                st.warning("⚠️ Warning: Total square feet per BHK is less than 300. This might affect prediction accuracy.")
            
            # Create input dataframe
            input_data = pd.DataFrame({
                'location': [location],
                'total_sqft': [total_sqft],
                'bath': [bath],
                'bhk': [bhk]
            })
            
            try:
                # Make prediction
                prediction = model.predict(input_data)[0]
                
                # Display result
                st.markdown("---")
                st.success("### Prediction Result")
                
                # Format the prediction
                price_lakhs = round(prediction, 2)
                price_rupees = round(prediction * 100000, 2)
                
                # Display in a nice format
                col5, col6 = st.columns(2)
                
                with col5:
                    st.metric(
                        label="💰 Estimated Price",
                        value=f"₹ {price_lakhs} Lakhs",
                        help="Price in Lakhs (1 Lakh = 100,000 INR)"
                    )
                
                with col6:
                    st.metric(
                        label="💵 Price in Rupees",
                        value=f"₹ {price_rupees:,.0f}",
                        help="Total price in Indian Rupees"
                    )
                
                # Additional info
                st.info(f"📍 Location: {location} | 📐 Area: {total_sqft} sqft | 🛏️ {bhk} BHK | 🚿 {int(bath)} Bathrooms")
                
            except Exception as e:
                st.error(f"Error making prediction: {e}")
    
    with col2:
        st.subheader("ℹ️ About")
        st.markdown("""
        This app predicts house prices in Bangalore using a **Ridge Regression** model.
        
        **Features Used:**
        - Location
        - Total Square Feet
        - Number of Bathrooms
        - BHK (Bedrooms)
        
        **Model Performance:**
        - R² Score: ~0.82
        - MAE: ~18.17 Lakhs
        - RMSE: ~35.60 Lakhs
        
        **Note:** Prices are predicted in Lakhs (1 Lakh = ₹100,000)
        """)
        
        st.markdown("---")
        st.markdown("### 📊 Data Summary")
        
        try:
            df = pd.read_csv('Cleaned_data.csv')
            st.write(f"**Total Properties:** {len(df):,}")
            st.write(f"**Price Range:** ₹{df['price'].min():.2f} - ₹{df['price'].max():.2f} Lakhs")
            st.write(f"**Average Price:** ₹{df['price'].mean():.2f} Lakhs")
            st.write(f"**Locations:** {df['location'].nunique()}")
        except:
            st.write("Data summary unavailable")

# Run the app
if __name__ == "__main__":
    main()
