import random

# coded by Zenet

global num_list

def random_nums():
    global num_list
    num_list = []
    for x in range(10):
        integers = random.randint(1, 100)
        num_list.append(integers)
    print(f"You must form these numbers: {num_list}")


class NumberGame:
    def __init__(self, difficulty):
        self._difficulty = difficulty
        self._player_score = 0

    def main_game(self):
        self._welcome_message()
        self.__difficulty()
        self._expression_conversion()

    def _welcome_message(self):
        while (
                1 != 0 and
                          self._difficulty != self._player_score ):
             print("Welcome to the numbers smashing game"
                      "\nwhere you must use the numbers given to you with selective operations"
                      "\nto form the randomly generated numbers", sep="----")
             break

    def _expression_conversion(self):
        q = 2 - 5 + 3
        stack = []
        calculating_stack = []
        for expression in range(len(self._player_ans)):
            #stack.append(self._player_ans[expression])
            for x in range(len(stack)):
                if stack[x].isdigit():
                    calculating_stack.append(stack[x])
                elif stack[x] in ["+", "-", "*", "/"]:
                    self._final_expression = calculating_stack[x], stack[x], calculating_stack[x + 1]
                    self._player_ans = self._final_expression
        print(stack)
        print(calculating_stack)

    def __difficulty(self):
        if self._difficulty == "easy":
            def _easy_generate_gamemode():
                print("||-------------------------------------------------------------------||")
                self._num_list = [1, 6, 4, 2, 9, 25, 85, 190, 32, 16, 8]
                self._available_operations = ["+", "-", "*", "/"]
                print(f"Numbers You must use: {self._num_list}")
                print(f"Available Operations: {self._available_operations}")
            _easy_generate_gamemode()
            self._easy_gamemode()

        elif self._difficulty == "medium":
            def _medium_generate_gamemode():
                print("||-------------------------------------------------------------------||")
                self._num_list = [6, 2, 7, 5, 45, 193, 31, 19, 8, 99, 93]
                self._available_operations = ["+", "-", "*", "/"]
                print(f"Numbers You must use: {self._num_list}")
                print(f"Available Operations: {self._available_operations}")
            _medium_generate_gamemode()
            self._medium_gamemode()

        elif self._difficulty == "hard":
            def _hard_generate_gamemode():
                print("||-------------------------------------------------------------------||")
                self._num_list = [17, 2, 12, 5, 55, 193, 31, 19, 13, 33, 109]
                self._available_operations = ["+", "-", "*", "/"]
                print(f"Numbers You must use: {self._num_list}")
                print(f"Available Operations: {self._available_operations}")
            _hard_generate_gamemode()
            self._hard_gamemode()

    def _easy_gamemode(self):
        print("||-------------------------------------------------------------------||")
        print("\nYou have chosen the easy gamemode:")
        random_nums()
        while self._player_score != -3:
            print(f"\nPlayer Score: {self._player_score}")
            self._player_ans = input("\nExpression: ")
            self._player_ans_evaluated = eval(self._player_ans)
            if self._player_ans_evaluated in num_list:
                num_list.remove(self._player_ans_evaluated)
                print(num_list)
                self._player_score += 1

            else:
                self._player_score -= 1


    def _medium_gamemode(self):
        print("||-------------------------------------------------------------------||")
        print("\nYou have chosen the medium gamemode:")
        random_nums()
        while self._player_score != -3:
            print(f"\nPLayer score: {self._player_score}")
            self._player_ans = input("\nExpression: ")
            self._player_ans_evaluated = eval(self._player_ans)
            if self._player_ans_evaluated in num_list:
                num_list.remove(self._player_ans_evaluated)
                print(num_list)
                self._player_score += 1

            else:
                self._player_score -= 1

    def _hard_gamemode(self):
        print("||-------------------------------------------------------------------||")
        print("\nYou have chosen the hard gamemode:")
        random_nums()
        while self._player_score != -3:
            print(f"\nPlayer score: {self._player_score}")
            self._player_ans = input("\nExpression: ")
            self._player_ans_evaluated = eval(self._player_ans)
            if self._player_ans_evaluated in num_list:
                num_list.remove(self._player_ans_evaluated)
                print(num_list)
                self._player_score += 1
            else:
                self._player_score -= 1

if __name__ == '__main__':
    p = NumberGame("hard")
    print(p.main_game())
