import random
def game:
    while True:
        computer = random.randint(0,2)
        print('Computer choose : ', computer)

        choice_index = choice
        computer_index = computer 

        result_matrix = [[0, 2, 1],
                        [1, 0, 2], 
                        [2, 1, 0],
                        [3, 3, 3]]
            
        result_idx = result_matrix[choice_index][computer_index]
        result_message = ['Tie!', 'You Win!', 'You Lose!', 'Invalid!']
        result = result_message[result_idx]

        print(result)
    