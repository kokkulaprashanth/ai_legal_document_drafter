
# Advanced Legal Document Drafting System

This application is a Streamlit-based tool for generating legal documents and providing legal assistance, tailored for Indian law. It allows users to specify various legal document parameters, and the system leverages OpenAI's API to generate legally accurate drafts. Users can interact with the application to generate documents, download them as PDFs, and get answers to legal queries.

## Features

1. **Document Generation**: Generate legal documents like plaints, petitions, affidavits, and more by entering details such as case information, parties involved, court details, relevant clauses, and applicable laws.
2. **Clause Selection**: Includes predefined sample clauses (specific to Indian legal contexts), with an option to add custom clauses.
3. **PDF Export**: Download generated documents as PDF files.
4. **AI-Powered Legal Assistance**: Ask questions about Indian law related to the generated document and receive responses from an AI legal assistant.

## Setup

### Prerequisites

- Python 3.7 or higher
- Required libraries: `streamlit`, `openai`, `reportlab`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```
3. Install the required libraries:
   ```bash
   pip install streamlit openai reportlab
   ```
4. Obtain an API key from OpenAI and add it to the code.

### Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```
2. Open the application in your browser.
3. Use the sidebar to enter details for document generation:
   - **Document Type**: Select the type of document (e.g., Plaint, Petition).
   - **Case Details**: Provide comprehensive case information.
   - **Parties**: List all parties involved.
   - **Court Details**: Specify court information.
   - **Relevant Clauses**: Choose from sample clauses or add custom ones.
   - **Applicable Laws**: List the relevant Indian laws for the case.
4. Click **Generate Document** to create the legal draft.
5. View the generated document in the main section and download it as a PDF.
6. Interact with the AI assistant by asking legal questions related to the document.

### PDF Generation

The generated legal document is saved as a PDF file using the `reportlab` library. Text is wrapped automatically based on page margins and formatted to ensure readability.

## Code Structure

- **create_pdf**: Generates a PDF of the drafted document.
- **generate_document**: Calls the OpenAI API to generate a legal draft based on provided parameters.
- **generate_sample_clauses**: Supplies sample legal clauses specific to Indian law.
- **main**: The main function, managing the Streamlit interface, document generation, and interactions with the AI assistant.

## Notes

- Ensure a valid OpenAI API key is provided in the code.
- Generated PDFs include only formatted text; additional graphics or tables are not supported in this version.
- This application is designed for Indian legal contexts and may require adjustments for other jurisdictions.

