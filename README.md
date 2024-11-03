Advanced Legal Document Drafting System
This application is a Streamlit-based tool for generating legal documents and providing legal assistance, tailored for Indian law. It allows users to specify various legal document parameters, and the system leverages OpenAI's API to generate legally accurate drafts. Users can interact with the application to generate documents, download them as PDFs, and get answers to legal queries.

Features
Document Generation: Generate legal documents like plaints, petitions, affidavits, and more by entering details such as case information, parties involved, court details, relevant clauses, and applicable laws.
Clause Selection: Includes predefined sample clauses (specific to Indian legal contexts), with an option to add custom clauses.
PDF Export: Download generated documents as PDF files.
AI-Powered Legal Assistance: Ask questions about Indian law related to the generated document and receive responses from an AI legal assistant.
Setup
Prerequisites
Python 3.7 or higher
Required libraries: streamlit, openai, reportlab
Installation
Clone the repository.
Install the required libraries:
bash
Copy code
pip install streamlit openai reportlab
Obtain an API key from OpenAI and add it to the code.
Usage
Run the application:
bash
Copy code
streamlit run app.py
Open the application in your browser.
Use the sidebar to enter details for document generation:
Document Type: Select the type of document (e.g., Plaint, Petition).
Case Details: Provide comprehensive case information.
Parties: List all parties involved.
Court Details: Specify court information.
Relevant Clauses: Choose from sample clauses or add custom ones.
Applicable Laws: List the relevant Indian laws for the case.
Click Generate Document to create the legal draft.
View the generated document in the main section and download it as a PDF.
Interact with the AI assistant by asking legal questions related to the document.
PDF Generation
The generated legal document is saved as a PDF file using the reportlab library. Text is wrapped automatically based on page margins and formatted to ensure readability.

Code Structure
create_pdf: Generates a PDF of the drafted document.
generate_document: Calls the OpenAI API to generate a legal draft based on provided parameters.
generate_sample_clauses: Supplies sample legal clauses specific to Indian law.
main: The main function, managing the Streamlit interface, document generation, and interactions with the AI assistant.
Notes
Ensure a valid OpenAI API key is provided in the code.
Generated PDFs include only formatted text; additional graphics or tables are not supported in this version.
This application is designed for Indian legal contexts and may require adjustments for other jurisdictions.
