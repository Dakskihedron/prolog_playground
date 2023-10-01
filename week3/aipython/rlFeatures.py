# rlFeatures.py - Feature-based Reinforcement Learner
# AIFCA Python3 code Version 0.9.6 Documentation at http://aipython.org
# Download the zip file and read aipython.pdf for documentation

# Artificial Intelligence: Foundations of Computational Agents http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2023.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

import random
from rlProblem import RL_agent, epsilon_greedy, ucb
from display import Displayable
from utilities import argmaxe, flip

class SARSA_LFA_learner(RL_agent):
    """A SARSA with linear function approximation (LFA) learning agent has
    """
    def __init__(self, role, actions, discount, get_features,
                     exploration_strategy=epsilon_greedy, es_kwargs={},
                     step_size=0.01, winit=0, method="SARSA_LFA"):
        """role is the role of the agent (e.g., in a game)
        actions is the set of actions the agent can do
        discount is the discount factor
        get_features is a function get_features(state,action) -> list of feature values
        exploration_strategy is the exploration function, default "epsilon_greedy"
        es_kwargs is extra keyword arguments of the exploration_strategy 
        step_size is gradient descent step size
        winit is the initial value of the weights
        method gives the method used to implement the role (for plotting)
        """
        RL_agent.__init__(self, actions)
        self.role = role
        self.discount = discount
        self.exploration_strategy = exploration_strategy
        self.es_kwargs = es_kwargs
        self.get_features = get_features
        self.step_size = step_size
        self.winit = winit
        self.method = method

    def initial_action(self, state):
        """ Returns the initial action; selected at random
        Initialize Data Structures
        """
        self.action = random.choice(self.actions)
        self.features = self.get_features(state, self.action)
        self.weights = [self.winit for f in self.features]
        self.state = state
        self.display(2, f"Initial State: {state} Action {self.action}")
        self.display(2,"s\ta\tr\ts'\tQ")
        return self.action


    def Q(self, state,action):
        """returns Q-value of the state and action for current weights
        """
        return dot_product(self.weights, self.get_features(state,action))
        
    def select_action(self, reward, next_state):
        """do num_steps of interaction with the environment"""
        feature_values = self.get_features(self.state,self.action)
        oldQ = self.Q(self.state,self.action)
        next_action = self.exploration_strategy({a:self.Q(next_state,a)
                                                     for a in self.actions}, {})
        nextQ = self.Q(next_state,next_action)
        delta = reward + self.discount * nextQ - oldQ
        for i in range(len(self.weights)):
            self.weights[i] += self.step_size * delta * feature_values[i]
        self.display(2,self.state, self.action, reward, next_state,
                     self.Q(self.state,self.action), delta, sep='\t')
        self.state = next_state
        self.action = next_action
        return self.action

    def show_actions(self,state=None):
        """prints the value for each action in a state.
        This may be useful for debugging.
        """
        if state is None:
            state = self.state
        for next_act in self.actions:
            print(next_act,dot_product(self.weights, self.get_features(state,next_act)))

def dot_product(l1,l2):
    return sum(e1*e2 for (e1,e2) in zip(l1,l2))

from rlProblem import Simulate
from rlExamples import Monster_game_env   # monster game environment
import rlMonsterGameFeatures

mon_env = Monster_game_env()
fa1 = SARSA_LFA_learner(mon_env.name, mon_env.actions, 0.9, rlMonsterGameFeatures.get_features)
# Simulate(fa1,mon_env).go(100000).plot()
fas1 = SARSA_LFA_learner(mon_env.name, mon_env.actions, 0.9, rlMonsterGameFeatures.simp_features, method="LFA (simp features)")
#Simulate(fas1,mon_env).go(100000).plot()

