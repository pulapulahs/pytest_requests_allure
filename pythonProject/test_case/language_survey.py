from survey import AnonymousSurvey

# 定义一个问题，并创建对象
question = "你的母语是啥"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit. \n")
while True:
    response = input("语言")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\n 谢谢您嘻嘻")
my_survey.show_results()
