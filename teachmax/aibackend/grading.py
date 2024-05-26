from PyPDF2 import PdfReader 
from groq import Groq
from IPython.display import display
import pandas as pd

class Grade:
    def __init__(self, submission):
        self.submission = submission
    
    def pdfToText(self):
        reader = PdfReader(self.submission) 
        page = reader.pages[0] 
        text = page.extract_text() 
        return text
    
    def gradeTest(self):
        submissionText = self.pdfToText()
        groq_client = Groq(api_key="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")

        system_prompt=f"""
        You are an assistant that recieves a grading rubric and a student submission. 
        Using the rubric, output a score for each category in the rubric, the score out of the total with all categories added up, and provide justification for each evaluation.
        Should a student's submission reveal that that student needs additional support, please flag that student. 

        At the end, provide a summary in this format using integers:
        **SUMMARY**
        Name: Last Name, First Name
        Communication: 
        Purposeful Evidence Selection: 
        Analysis: 
        Claims/Assertions: 
        Flagged: 0 or 1
        Total Score: 

        Rubric:
        # Communication
        ## 3 points:
        Is clear and sophisticated, adheres to the conventions of academic writing, purposefully employs a variety of sentence structures, and uses language precisely with only minor lapses.
        Paragraph is cohesively organized, argumentative, and narrowly focused.
        Evidence is smoothly integrated into paragraphs.
        ## 2 points:
        Is clear and adheres to the conventions of academic writing, employs a variety of sentence structures, and uses language appropriately with only minor lapses.
        Paragraph is organized, argumentative, focused, and logically ordered.
        Evidence is integrated into paragraphs.
        ## 1 points:
        Adheres to some conventions of academic writing. May use language vaguely, incorrectly, or imprecisely. 
        Includes general idea organization, but may be less focused or logically ordered.
        Evidence is clumsily or abruptly integrated into paragraphs.
        ## 0 points:
        Strays from the conventions of academic writing. Vague or incorrect language use interferes with clarity.
        Lacks coherent organization and structure. 
        Evidence may not be integrated.

        # Purposeful Evidence Selection
        ## 3 points:
        Textual [or visual] evidence is precisely chosen to reflect the most important identified rhetorical or literary devices in support of the rhetorical goal or literary theme.
        ## 2 points:
        Textual [or visual] evidence reflects important identified rhetorical or literary devices in support of the rhetorical goal or literary theme.
        ## 1 point:
        Textual [or visual] evidence is too sparse, too plentiful, or is a poor representation of the identified rhetorical or literary device(s). Evidence may tenuously support the rhetorical goal.
        ## 0 points:
        Textual [or visual] evidence may be missing, inaccurate, or entirely unrelated to the rhetorical goal.

        # Analysis
        ## 3 points:
        Draws clear and compelling connections between claims and evidence. Identifies and thoroughly explains the function and significance of relevant details and key literary devices.
        ## 2 points:
        Draws clear connections between claims and evidence. Identifies and explains the function and/or significance of relevant details and literary devices.
        ## 1 point:
        Draws connections between claims and evidence, though they may be uneven. Identifies the function and/or significance of details and/or literary devices.Draws connections between claims and evidence, though they may be uneven. Identifies the function and/or significance of details and/or literary devices.
        ## 0 points:
        Fails to draw connections or draws unsupportable connections between claims (if present) and evidence (if present). Lacks coherence. May egregiously  misinterpret evidence or the text.

        # Claims/Assertions
        ## 3 points:
        Asserts a narrowly focused and original, insightful, clear, and complex argument about the text’s thematic meaning.
        ## 2 points:
        Asserts a focused, accurate and clear argument about the text’s thematic meaning.
        ## 1 point:
        Asserts an argument about the text’s meaning.  May reflect a minor misreading of the text and/or lack clarity or focus.
        ## 0 points:
        Lacks a coherent argument or makes an argument based on gross misreading of the text.


        """


        messages = [{"role": "system", "content": system_prompt},{"role":"user", "content":submissionText}]
        response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            temperature=0.0,
            max_tokens=4096
        )
        return(response.choices[0].message.content.strip())
    
    def parseDict(self):
        bool = False
        out = self.gradeTest()
        lines = out.strip().split('\n')
        parsed_dict = {}

        for line in lines:
            if bool:
                if ':' in line:
                    key, value = line.split(':', 1)
                    if value.isdigit():
                        parsed_dict[key.strip()] = int(value.strip())
                    else:
                        parsed_dict[key.strip()] = value.strip()
            if "Summary:" in line:
                bool = True

        return parsed_dict

    

obj1 = Grade("tylergradp.pdf")
obj2 = Grade("charlottegradp.pdf")
df = None

list = [obj1, obj2]

for obj in list:
    df2 = pd.DataFrame([obj.parseDict()])
    df2.set_index('Name', inplace=True)
    df = pd.concat([df,df2])


# # Save to Excel File
df.to_excel('output.xlsx')