class QuizBrain:
    
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        

    def next_question(self):
        current_question = self.question_list[0]
        self.question_number += 1
        print(current_question.text[2], current_question.answer[1])
        input(f" Q.{self.question_number} {current_question.text}")

qb= QuizBrain              
print(qb.next_question(0))


        