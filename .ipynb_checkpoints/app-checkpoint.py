import streamlit as st
import pandas as pd
import joblib


# =====================================================
# 1. LOAD MODEL
# =====================================================

model = joblib.load(
    "smartphone_addiction_model.pkl"
)


# =====================================================
# 2. LOAD SELECTED FEATURES
# =====================================================

selected_features = joblib.load(
    "selected_features.pkl"
)


# =====================================================
# 3. FEATURE ENGINEERING
# =====================================================

def create_features(df):

    df = df.copy()

    # Social Media Usage Ratio
    df["Social_Media_Usage_Ratio"] = (
        df["time_on_social_media"] /
        (df["daily_usage_hours"] + 0.01)
    )

    # Gaming Usage Ratio
    df["Gaming_Usage_Ratio"] = (
        df["time_on_gaming"] /
        (df["daily_usage_hours"] + 0.01)
    )

    # Education Usage Ratio
    df["Education_Usage_Ratio"] = (
        df["time_on_education"] /
        (df["daily_usage_hours"] + 0.01)
    )

    # Total Entertainment Time
    df["Total_Entertainment_Time"] = (
        df["time_on_social_media"] +
        df["time_on_gaming"]
    )

    # Checks Per Usage Hour
    df["Checks_Per_Usage_Hour"] = (
        df["phone_checks_per_day"] /
        (df["daily_usage_hours"] + 0.01)
    )

    # Weekend Usage Difference
    df["Weekend_Usage_Difference"] = (
        df["weekend_usage_hours"] -
        df["daily_usage_hours"]
    )

    # Sleep Deficit
    df["Sleep_Deficit"] = (
        8 - df["sleep_hours"]
    )

    # Usage vs Sleep Interaction
    df["Usage_Sleep_Interaction"] = (
        df["daily_usage_hours"] *
        df["Sleep_Deficit"]
    )

    return df


# =====================================================
# 4. PREPARE INPUT
# =====================================================

def prepare_input(df):

    df = create_features(df)

    X = df[selected_features]

    return X


# =====================================================
# 5. STREAMLIT PAGE
# =====================================================

st.set_page_config(
    page_title="Smartphone Addiction Prediction",
    page_icon="📱",
    layout="centered"
)


# =====================================================
# 6. TITLE
# =====================================================

st.title("📱 Smartphone Addiction Level Prediction")

st.write(
    "Enter the user's smartphone usage and lifestyle "
    "information to predict the addiction level."
)


# =====================================================
# 7. USER INPUTS
# =====================================================

st.header("Enter User Details")


daily_usage_hours = st.number_input(
    "Daily Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0,
    step=0.1
)


sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.1
)


intellectual_performance = st.number_input(
    "Intellectual Performance",
    min_value=0,
    max_value=100,
    value=75,
    step=1
)


screen_time_before_bed = st.number_input(
    "Screen Time Before Bed",
    min_value=0.0,
    max_value=24.0,
    value=1.0,
    step=0.1
)


phone_checks_per_day = st.number_input(
    "Phone Checks Per Day",
    min_value=0,
    max_value=500,
    value=80,
    step=1
)


apps_used_daily = st.number_input(
    "Apps Used Daily",
    min_value=0,
    max_value=100,
    value=20,
    step=1
)


time_on_social_media = st.number_input(
    "Time on Social Media (Hours)",
    min_value=0.0,
    max_value=24.0,
    value=3.0,
    step=0.1
)


time_on_gaming = st.number_input(
    "Time on Gaming (Hours)",
    min_value=0.0,
    max_value=24.0,
    value=1.0,
    step=0.1
)


time_on_education = st.number_input(
    "Time on Education (Hours)",
    min_value=0.0,
    max_value=24.0,
    value=1.0,
    step=0.1
)


weekend_usage_hours = st.number_input(
    "Weekend Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=8.0,
    step=0.1
)


# =====================================================
# 8. PREDICTION BUTTON
# =====================================================

if st.button("🔮 Predict Addiction Level"):

    input_data = pd.DataFrame({

        "daily_usage_hours": [daily_usage_hours],

        "sleep_hours": [sleep_hours],

        "intellectual_performance": [
            intellectual_performance
        ],

        "screen_time_before_bed": [
            screen_time_before_bed
        ],

        "phone_checks_per_day": [
            phone_checks_per_day
        ],

        "apps_used_daily": [
            apps_used_daily
        ],

        "time_on_social_media": [
            time_on_social_media
        ],

        "time_on_gaming": [
            time_on_gaming
        ],

        "time_on_education": [
            time_on_education
        ],

        "weekend_usage_hours": [
            weekend_usage_hours
        ]
    })


    # Prepare model input

    X_input = prepare_input(input_data)


    # Predict

    prediction = model.predict(X_input)

    predicted_level = prediction[0]


    # Display result

    st.success(
        f"Predicted Smartphone Addiction Level: "
        f"{predicted_level:.2f}"
    )


X_input = prepare_input(input_data)

prediction = model.predict(X_input)