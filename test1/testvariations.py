from pypdf import PdfReader 
from groq import Groq

class TestVariations:  
    def __init__(self, inputPdf, number):
        self.inputPdf = inputPdf
        self.number = number

    def pdfToText(self):
        reader = PdfReader(self.inputPdf) 
        page = reader.pages[0] 
        text = page.extract_text() 
        return text
    
    def generateTest(self):
        testText = self.pdfToText()
        groq_client = Groq(api_key="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")

        system_prompt=f"""
        You are a chat assistant that recieves a sample test and generates a variation of that test.

        """


        messages = [{"role": "system", "content": system_prompt},{"role":"user", "content":testText}]
        response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            temperature=0.0,
            max_tokens=4096
        )
        return(response.choices[0].message.content.strip())
    
    def listNewTests(self):
        mylist = []
        for i in range(self.number):
            mylist.append(self.generateTest())
        return mylist
    