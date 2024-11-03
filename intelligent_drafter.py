import streamlit as st
from openai import OpenAI
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

# Initialize the OpenAI client
client = OpenAI(api_key='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')

# Create PDF
def create_pdf(content):
    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter  # Get width and height of the page
    pdf_canvas.setFont("Helvetica", 12)

    # Set margins and initial line height
    margin_left = 40
    margin_right = 40
    margin_bottom = 40
    margin_top = 40
    line_height = 14  # Space between each line of text
    max_width = width - margin_left - margin_right  # Maximum width for text lines
    max_lines_per_page = int((height - margin_top - margin_bottom) / line_height)  # Max lines per page
    
    # Function to wrap text based on max width
    def wrap_text(text, canvas, max_width):
        wrapped_lines = []
        words = text.split()
        current_line = ""
        for word in words:
            # Check the width of the current line with the new word added
            test_line = current_line + word + " "
            if canvas.stringWidth(test_line, "Helvetica", 12) < max_width:
                current_line = test_line
            else:
                # If it exceeds the width, add the current line to the wrapped lines
                wrapped_lines.append(current_line.strip())
                current_line = word + " "
        # Add the last line
        if current_line:
            wrapped_lines.append(current_line.strip())
        return wrapped_lines

    lines = content.split('\n')

    text_object = pdf_canvas.beginText(margin_left, height - margin_top)  # Starting position
    
    line_count = 0
    for line in lines:
        # Wrap the text if necessary
        wrapped_lines = wrap_text(line, pdf_canvas, max_width)
        for wrapped_line in wrapped_lines:
            if line_count < max_lines_per_page:
                text_object.textLine(wrapped_line)
                line_count += 1
            else:
                # If max lines for this page is reached, draw the text object and create a new page
                pdf_canvas.drawText(text_object)
                pdf_canvas.showPage()  # Start a new page
                text_object = pdf_canvas.beginText(margin_left, height - margin_top)  # Reset the position
                text_object.setFont("Helvetica", 12)  # Reset the font
                text_object.textLine(wrapped_line)  # Add the wrapped line to the new page
                line_count = 1  # Reset line count

    # Draw the last page's content
    pdf_canvas.drawText(text_object)
    pdf_canvas.save()

    # Get the PDF data from memory
    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data

# Function to generate document using OpenAI's GPT model
def generate_document(document_type, case_details, clauses, laws, parties, court):
    prompt = f"""
As an AI legal assistant specializing in Indian law, draft a detailed {document_type} with the following comprehensive details:

    Parties Involved:
    {parties}

    Court Details:
    {court}

    Case Details:
    {case_details}

    Relevant Clauses:
    {clauses}

    Applicable Laws:
    {laws}

Please ensure the following in your draft:
1. Comply with the latest Indian laws and use appropriate Indian legal terminology.
2. Follow the standard format for {document_type}s as per Indian legal practice.
3. Include detailed citations of relevant Indian case law and statutes.
4. Use formal language suitable for Indian courts, including any standard phrases or legal jargon commonly used.
5. Structure the document clearly, using detailed sections and sub-sections with proper formatting (headings, paragraphs, etc.).
6. If this is a court document, ensure the correct court language is used (e.g., "Most respectfully showeth" for petitions).
7. Include any necessary declarations, verifications, or certifications required under Indian law.
8. Ensure thorough coverage of all legal and factual issues, including background, legal arguments, and supporting facts.
9. Provide detailed instructions or explanations for any specific actions required by the parties involved.
10. Ensure that the draft is comprehensive, leaving no ambiguities or missing sections.

Provide the document in a fully structured, detailed format with clear sections, adhering to Indian legal drafting standards, ensuring all components are complete and precise.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a legal AI assistant specialized in drafting Indian legal documents."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000
    )

    return response.choices[0].message.content.strip()

# Function to generate sample clauses (updated for Indian context)
def generate_sample_clauses():
    return {
        "Jurisdiction": "The Hon'ble Court has the jurisdiction to try and entertain the present suit/petition as per Section X of the Civil Procedure Code, 1908.",
        "Limitation": "The present suit/petition is within the period of limitation as prescribed under the Limitation Act, 1963.",
        "Cause of Action": "The cause of action for filing the present suit/petition arose on [DATE] when...",
        "Relief Sought": "In light of the facts and circumstances stated above, this Hon'ble Court may be pleased to...",
        "Interim Relief": "Pending hearing and final disposal of the present suit/petition, this Hon'ble Court may be pleased to...",
        "Affidavit": "I, [NAME], the [DESIGNATION] of the Petitioner above named, do hereby solemnly affirm and state as follows:"
    }

# Streamlit app
def main():
    st.title("Advanced Legal Document Drafting System")

    # Sidebar for inputs
    st.sidebar.header("Document Parameters")
    
    # Document type selection (updated for Indian context)
    document_type = st.sidebar.selectbox(
        "Select Document Type",
        ["Plaint", "Written Statement", "Petition", "Writ Petition", "Affidavit", "Legal Notice", "Vakalatnama"]
    )

    # Case details input
    st.sidebar.subheader("Case Details")
    case_details = st.sidebar.text_area("Enter case details:", height=150)

    # Party details input
    st.sidebar.subheader("Parties Involved")
    parties = st.sidebar.text_area("Enter details of parties involved (e.g., Plaintiff, Defendant):", height=100)

    # Court details input
    st.sidebar.subheader("Court Details")
    court = st.sidebar.text_input("Enter Court Name and Location")

    # Clauses selection
    st.sidebar.subheader("Relevant Clauses")
    if 'sample_clauses' not in st.session_state:
        st.session_state.sample_clauses = generate_sample_clauses()
    
    selected_clauses = st.sidebar.multiselect(
        "Select relevant clauses:",
        list(st.session_state.sample_clauses.keys())
    )
    
    # Option for custom clauses
    custom_clause = st.sidebar.text_area("Add Custom Clause (Optional):", height=100)

    # Laws input (updated for Indian context)
    st.sidebar.subheader("Applicable Laws")
    applicable_laws = st.sidebar.text_area("Enter applicable Indian laws and sections:", height=100,
                                           placeholder="e.g., Section 124 of Indian Contract Act, 1872")

    # Generate document button
    if st.sidebar.button("Generate Document"):
        if case_details and selected_clauses and applicable_laws and parties and court:
            with st.spinner("Generating document..."):
                # Join selected and custom clauses
                clauses_text = "\n".join([f"{clause}: {st.session_state.sample_clauses[clause]}" for clause in selected_clauses])
                if custom_clause:
                    clauses_text += f"\nCustom Clause: {custom_clause}"
                
                # Generate document
                generated_document = generate_document(document_type, case_details, clauses_text, applicable_laws, parties, court)
                
                # Store document in session state
                st.session_state.generated_document = generated_document
        else:
            st.sidebar.warning("Please fill in all required fields.")

    # Display generated document
    if 'generated_document' in st.session_state:
        st.header("Generated Document")
        st.text_area("", value=st.session_state.generated_document, height=400)

        # Download option
        pdf_data = create_pdf(st.session_state.generated_document)

        # Download option for PDF
        st.download_button(
            label="Download Document as PDF",
            data=pdf_data,
            file_name=f"{document_type.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mime="application/pdf"
        )

    # Chat interface for legal advice or questions
    st.header("Chat with AI Legal Assistant")
    user_question = st.text_input("Ask a question about Indian law or the generated document:")
    
    if user_question:
        if 'generated_document' in st.session_state:
            prompt = f"""
            You are an AI legal assistant specializing in Indian law. A {document_type} has been generated. 
            
            The user has asked the following question:
            {user_question}
            
            Please provide a helpful and insightful answer based on your knowledge of Indian legal matters and document drafting. 
            Make sure to cite relevant Indian laws, precedents, or procedures where applicable.
            """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a legal AI assistant specialized in Indian law, document drafting, and legal advice."},
                    {"role": "user", "content": prompt}
                ]
            )

            st.write(response.choices[0].message.content)
        else:
            st.write("Please generate a document first before asking questions.")

if __name__ == "__main__":
    main()
