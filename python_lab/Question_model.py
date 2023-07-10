import data

class Question:
    
    def __init__(self, qtext, qanswer):
        self.text = qtext
        self.answer = qanswer



question = Question("what is India Capital", "Delhi")       
print(question.text)
print(question.answer)