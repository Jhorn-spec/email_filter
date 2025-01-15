import streamlit as st
import pandas as pd
import io 

# App Title
st.title("Email Filtering App")

# Upload files
st.sidebar.header("Upload Files")
file1 = st.sidebar.file_uploader("Upload the first Excel file (bad emails)", type=["xlsx"])
file2 = st.sidebar.file_uploader("Upload the second Excel file (clean emails)", type=["xlsx"])

if file1 and file2:
    # Read the uploaded files into DataFrames
    try:
        bad_emails_df = pd.read_excel(file1)
        clean_emails_df = pd.read_excel(file2)

        st.subheader("Preview of Uploaded Data")
        st.write("Bad Emails (Sheet 1):")
        st.dataframe(bad_emails_df)

        st.write("Clean Emails (Sheet 2):")
        st.dataframe(clean_emails_df)

        # Ensure the 'Email' column exists in both files
        if "Email" not in bad_emails_df.columns or "Email" not in clean_emails_df.columns:
            st.error("Both sheets must have an 'Email' column.")
        else:
            # Filter clean emails
            filtered_emails_df = clean_emails_df[
                ~clean_emails_df["Email"].str.lower().isin(bad_emails_df["Email"].str.lower())
            ]

            st.subheader("Filtered Emails")
            st.dataframe(filtered_emails_df)

            # Download filtered emails
            @st.cache_data
            def convert_df_to_excel(df):
                output = io.BytesIO()  # Create a BytesIO buffer
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False, sheet_name='Filtered Emails')
                processed_data = output.getvalue()
                return processed_data

            filtered_file = convert_df_to_excel(filtered_emails_df)
            st.download_button(
                label="Download Filtered Emails",
                data=filtered_file,
                file_name="filtered_emails.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

    except Exception as e:
        st.error(f"Error reading the uploaded files: {e}")
else:
    st.write("Please upload both Excel files to start.")
