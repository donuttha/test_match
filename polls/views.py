# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from .models import Question
import json


def index(request):
    #No.1
    input_text = 'i like to read'
    return_text = reverse_words(input_text)
    #No.2
    print_seq = print_seq_fn(a=4, b=1)
    #No.3
    dog, bird = cal_bird_dog(head=35, leg=92)
    #No.4
    find_solution_return = find_solution()

    context = {'input_text': input_text, 'return_text': return_text, 'dog': dog, 'bird':bird, 'print_seq': print_seq, 'find_solution_return': find_solution_return}
    return render(request, 'poll.html', context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):

    user_id = request.POST.get('UserID', '')
    if user_id == '':
        context = {'ErrorCode': '10', 'ListData': []}
        return HttpResponse(json.dumps(context))

    import random
    test_list = range(1,17)
    for i in range(len(test_list) - 1, 0, -1):
        j = random.randint(0, i + 1)
        test_list[i], test_list[j] = test_list[j], test_list[i]
    context = {'ErrorCode': 0, 'ListData': test_list}
    save_render(user_id, test_list)
    return HttpResponse(json.dumps(context))


def save_render(user_id, table):
    from polls.models import TableRender
    try:
        render_table = TableRender.objects.filter(user_id=user_id)[0]
    except:
        render_table = TableRender(user_id=user_id)

    render_table.table = table
    render_table.save()

def reverse_words(text_input):
    result = ''
    for a in reversed(text_input): result += a
    return result


def print_seq_fn(a=0, b=0):
    return_data = ''
    count_a = 0
    count_b = 0
    for i in range(a):
        return_data += 'a'
        count_a += 1
        if count_a == 2:
            count_a = 0
            for i in range(b):
                return_data += 'b'
                count_b += 1
                if count_b == 2:
                    b -= 2
                    count_b = 0
                    break
    return return_data


def cal_bird_dog(head= 0, leg=0):
    dog, bird = 0,0
    for dog in range(head):
        bird = head - dog
        leg_sum = (dog*4) + ((head-dog)*2)
        if leg_sum == leg:
            break
    return dog, bird


def find_solution():
    return_solution = []
    for i in range(9):
        break
    return return_solution