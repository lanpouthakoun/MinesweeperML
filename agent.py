import numpy as np
import torch
from collections import deque
import screen_interaction
import random
MAX_MEMORY = 100000
BATCH_SIZE = 1000
class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamme = 0
        self.memory = deque(maxlen= MAX_MEMORY)
        self.model = None
        self.trainer = None
        self.left, self.right, self.width, self.height = screen_interaction.get_region()


    def get_state(self, game):
        return screen_interaction.screen_grab(topleft, topright, bottomleft,bottomright)
    
    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self):
        self.epsilon = 80 - self.n_games
        if random.randint(0,200) < self.epsilon:
            move = random.randint(0,2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model.predict(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    #game
    while True:
        state_old = agent.get_state(game)

        final_move = agent.get_action(state_old)

        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)


        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games +=1
            agent.train_long_memory(state_old, final_move, reward, state_new, done)

            if score > record:
                record = score

            print('Game', agent.n_games, 'Score', score, 'Record:', record)


            

if name == '__main__':
    