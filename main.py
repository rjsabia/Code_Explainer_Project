import os
import openai
import inspect


# set ENV variables
openai.api_key = os.getenv('OPEN_AI_KEY_01')

# Python
# Funciton (OOP)

 # 2 ways to havea documentation string. allows it to be multi-line
    # """ """ <-- 3 double quotes OR 3 single quotes --> ''' '''
    # also will need a way to easily add triple quotes to the prompt
    # For this we can use break characters like this --> "is some words \"\"\" "

def hello(name):
    print(f"Hello {name}")

# hello("Luce")

# Functionlaity design
# _-_-_-_-_-_-_-_-_-_-_-_-_
# We will pass in code -->
#  def hello(name):
#       print(f"Hello {name}")

# New line with a comment --> # some text describing code

# New line --> ''' Prompt '''
# -_-_-_-_-_-_-_-_-_-_-_-_-_

def docstring_prompt(code):
    prompt = f"{code}\n # A high quality python docstring of the above Python function:\n \"\"\""
    return prompt

# Trying out more complex funciton
def create_student_view(test,num_questions):
    student_view = {1:''}
    question_number = 1
    for line in test.split("\n"):
        if not line.startswith("Correct Answer:"):
            student_view[question_number] += line+'\n'
        else:
            if question_number < num_questions:
                question_number +=1
                student_view[question_number] = ''
    return student_view

# testRun = inspect.getsource(hello)
# print(testRun)
# OR
# print(inspect.getsource(hello))
# print(docstring_prompt(inspect.getsource(hello)))

# could not use the code davinci api, this was discontinued, so swapped for text davinci
response = openai.Completion.create(
            model='text-davinci-003',
            prompt = docstring_prompt(inspect.getsource(create_student_view)),
            temperature = 0,
            max_tokens = 250,
            top_p=1.0,
            stop=["\"\"\""]
)

# print(response['choices'][0]['text'])

def merge_docstring_and_function(original_function,docstring):
    function_string = inspect.getsource(original_function)
    split = function_string.split('\n')
    first_part,second_part = split[0],split[1:]

    merged_function = first_part+'\n    """'+docstring+'    """'+'\n'+'\n'.join(second_part)

    return merged_function

print(merge_docstring_and_function(create_student_view,response['choices'][0]['text']))


























