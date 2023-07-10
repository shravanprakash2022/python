from Question_model import Question
from  data import question_data

question_bank = []

for i in question_data:
    i_text = i["q"]
    i_answer = i["a"]
    new_i = Question(i_text, i_answer)
    question_bank.append(new_i)

print(question_bank)
print(question_bank[6].text, "it is ", question_bank[6].answer)

