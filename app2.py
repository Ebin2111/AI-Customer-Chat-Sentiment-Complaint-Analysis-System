import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Customer Chat Analysis Dashboard",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

FILE_PATH = r"C:\Users\EBIN BABU\Downloads\customer_chats_500_business_quality.csv"

df = pd.read_csv(FILE_PATH)

# =====================================
# TITLE
# =====================================

st.title(" Customer Chat Analysis Dashboard")

# =====================================
# DATA PREVIEW
# =====================================

st.subheader("Dataset Preview")

st.dataframe(df.head())

# =====================================
# SHOW COLUMN NAMES
# =====================================

st.subheader("Available Columns")

st.write(df.columns.tolist())

# =====================================
# SUMMARY METRICS
# =====================================

positive = len(df[df["expected_sentiment"] == "Positive"])
negative = len(df[df["expected_sentiment"] == "Negative"])
neutral = len(df[df["expected_sentiment"] == "Neutral"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Chats", len(df))
col2.metric("Positive", positive)
col3.metric("Negative", negative)
col4.metric("Neutral", neutral)

# =====================================
# SENTIMENT BAR CHART
# =====================================

st.subheader("Sentiment Distribution")

sentiment_counts = df["expected_sentiment"].value_counts()

st.bar_chart(sentiment_counts)

# =====================================
# PIE CHART
# =====================================

st.subheader("Sentiment Percentage")

fig, ax = plt.subplots(figsize=(6, 6))

ax.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    autopct="%1.1f%%"
)

ax.set_title("Customer Sentiment")

st.pyplot(fig)

# =====================================
# SENTIMENT TABLE
# =====================================

st.subheader("Sentiment Counts")

st.dataframe(
    sentiment_counts.reset_index().rename(
        columns={
            "index": "Sentiment",
            "expected_sentiment": "Count"
        }
    )
)

# =====================================
# CUSTOMER MESSAGES
# =====================================

st.subheader("Customer Messages")

selected_sentiment = st.selectbox(
    "Filter by Sentiment",
    ["All", "Positive", "Negative", "Neutral"]
)

if selected_sentiment == "All":
    filtered_df = df
else:
    filtered_df = df[
        df["expected_sentiment"] == selected_sentiment
    ]

st.dataframe(filtered_df)

# =====================================
# REPORT
# =====================================

summary = f"""
Total Chats: {len(df)}

Positive Chats: {positive}

Negative Chats: {negative}

Neutral Chats: {neutral}
"""

st.subheader("Analysis Report")

st.text(summary)