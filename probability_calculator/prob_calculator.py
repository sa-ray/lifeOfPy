import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for attr in kwargs.keys():
            for _ in range(kwargs[attr]):
                self.contents.append(attr)

    def draw(self, num):
        num = min(num, len(self.contents))
        balls = []
        for _ in range(num):
            index = random.randint(0, len(self.contents)-1)
            balls.append(self.contents.pop(index))
        return balls

def experiment(hat, balls_to_draw, num_balls_drawn, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        exp_hat = copy.deepcopy(hat)
        balls = exp_hat.draw(num_balls_drawn)
        num_of_correct_colors = 0
        for color in balls_to_draw.keys():
            if balls.count(color) >= balls_to_draw[color]:
                num_of_correct_colors += 1
        if num_of_correct_colors == len(balls_to_draw):
            successes += 1
    probability = float(successes)/num_experiments
    return(probability)