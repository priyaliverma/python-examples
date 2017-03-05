import random

questions = {
    "strong": "Do ye like yer drinks strong?(Y/N)",
    "salty": "Do ye like it with a salty tang?(Y/N)",
    "bitter": "Are ye a lubber who likes it bitter?(Y/N)",
    "sweet": "Would ye like a bit of sweetness with yer poison?(Y/N)",
    "fruity": "Are ye one for a fruity finish?(Y/N)",
}
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def ques_bool_dict(quest_dict):
    ans_lst = []
    q_lst = []
    for k, v in quest_dict.items():
        ans = True
        if str(input(quest_dict[k])) != 'Y':
            ans = False
        ans_lst.append(ans)
        q_lst.append(k)
    print ('Questions List:',q_lst)
    print ('Answers Boolean List:',ans_lst)

    ques_ans_dict = {}
    for q, a in zip(q_lst, ans_lst):
        ques_ans_dict[q] = a
    print ('Ques Ans Dict:', ques_ans_dict)

    return ques_ans_dict

question_answer_dict = ques_bool_dict(questions)

print ('Question Answer Dictionary:', question_answer_dict)

def prepare_drink(quest_ans_dict):
    taste_lst = []
    for k, v in quest_ans_dict.items():
        if quest_ans_dict[k]:
            taste_lst.append(k)

    ingred_lst = []
    for i in taste_lst:
        ingred = random.choice(ingredients[i])
        ingred_lst.append(ingred)

    drink_dict = {}
    for q, a in zip(taste_lst, ingred_lst):
        drink_dict[q] = a

    print ('Final Drink Dict:', drink_dict)
    return drink_dict

prepare_drink(question_answer_dict)


