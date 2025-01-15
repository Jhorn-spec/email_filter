# Application for Filtering Emails
filter out lists of spam emails from a list of partially cleaned emails


This application is designed to filter out bad emails from a dataset by comparing them with a list of bad emails. It provides users with an intuitive interface to upload their datasets, filter emails, and download the cleaned dataset.

## Features

- **File Upload**: Upload two Excel files: 
  - `Sheet1`: Contains a list of bad emails.
  - `Sheet2`: Contains a list of emails to be cleaned.
- **Email Filtering**: Compares emails in `Sheet2` with those in `Sheet1` and removes any matches.
- **Download Cleaned Data**: Provides a downloadable Excel file of the cleaned email list.

## How to Use

1. **Run the App**:
   - Use `streamlit run app.py` to launch the application.

2. **Upload Files**:
   - Upload the Excel file containing bad emails (`Sheet1`) and the file with emails to be filtered (`Sheet2`).

3. **Filter Emails**:
   - The app automatically filters out emails in `Sheet2` that match any email in `Sheet1`.

4. **Download Cleaned File**:
   - Once the filtering is complete, download the cleaned file using the provided button.

## Prerequisites

- Python 3.7 or higher.
- Required Python packages:
  - `streamlit`
  - `pandas`

Install these packages using:
```bash
pip install streamlit pandas
```

## Hosting

You can deploy this app for free using platforms like [Streamlit Community Cloud](https://streamlit.io/cloud). Follow these steps:

1. Push your code to a GitHub repository.
2. Sign in to Streamlit Cloud and link your repository.
3. Deploy the app by selecting the `app.py` file as the entry point.

## File Format

Ensure that both uploaded files are in Excel format and have a sheet with the following column structure:

- `Sheet1`:
  - A column containing the bad emails.
- `Sheet2`:
  - A column containing emails to be cleaned.

## Example Usage

- **Bad Emails (Sheet1)**:
  ```
  Email
  bademail1@example.com
  bademail2@example.com
  ```

- **Emails to be Filtered (Sheet2)**:
  ```
  First Name | Last Name | Email
  John       | Doe       | johndoe@example.com
  Jane       | Smith     | bademail1@example.com
  ```

- **Result (Cleaned Sheet2)**:
  ```
  First Name | Last Name | Email
  John       | Doe       | johndoe@example.com
  ```

## Troubleshooting

- **Error: Missing Columns**:
  - Ensure both files have the correct column names.

- **Error: File Format Not Supported**:
  - Only `.xlsx` files are supported. Convert your files if necessary.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contact

For questions or issues, please contact [Your Email/Name].

