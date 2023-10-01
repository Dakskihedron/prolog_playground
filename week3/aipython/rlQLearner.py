# rlQLearner.py - Q Learning
# AIFCA Python3 code Version 0.9.6 Documentation at http://aipython.org
# Download the zip file and read aipython.pdf for documentation

# Artificial Intelligence: Foundations of Computational Agents http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2023.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

import random
import math
from display import Displayable
from utilities import argmaxe, argmaxd, flip
from rlProblem import RL_agent, epsilon_greedy, ucb

class Q_learner(RL_agent):
    """A Q-learning agent has
    belief-state consisting of
        state is the previous state (initialized by RL_agent
        q is a {(state,action):value} dict
        visits is a {(state,action):n} dict.  n is how many times action was done in state
        acc_rewards is the accumulated reward

    """

    def __init__(self, role, actions, discount,
                 exploration_strategy=epsilon_greedy, es_kwargs={},
                 alpha_fun=lambda _:0.2,
                 Qinit=0, method="Q_learner"):
        """
        role is the role of the agent (e.g., in a game)
        actions is the set of actions the agent can do
        discount is the discount factor
        exploration_strategy is the exploration function, default "epsilon_greedy"
        es_kwargs is extra arguments of exploration_strategy 
        alpha_fun is a function that computes alpha from the number of visits
        Qinit is the initial q-value
        method gives the method used to implement the role (for plotting)
        """
        RL_agent.__init__(self, actions)
        self.role = role
        self.discount = discount
        self.exploration_strategy = exploration_strategy
        self.es_kwargs = es_kwargs
        self.alpha_fun = alpha_fun
        self.Qinit = Qinit
        self.method = method
        self.acc_rewards = 0
        self.Q = {}
        self.visits = {}

    def initial_action(self, state):
        """ Returns the initial action; selected at random
        Initialize Data Structures
        """
        self.Q[state] = {act:self.Qinit for act in self.actions}
        self.action = random.choice(self.actions)
        self.visits[state] = {act:0 for act in self.actions}
        self.state = state
        self.display(2, f"Initial State: {state} Action {self.action}")
        self.display(2,"s\ta\tr\ts'\tQ")
        return self.action
        
    def select_action(self, reward, next_state):
        """give reward and next state, select next action to be carried out"""
        if next_state not in self.visits:  # next state not seen before
            self.Q[next_state] = {act:self.Qinit for act in self.actions}
            self.visits[next_state] = {act:0 for act in self.actions}
        self.visits[self.state][self.action] +=1
        alpha = self.alpha_fun(self.visits[self.state][self.action])
        self.Q[self.state][self.action] += alpha*(
                            reward
                            + self.discount * max(self.Q[next_state].values())
                            - self.Q[self.state][self.action])
        self.display(2,self.state, self.action, reward, next_state, 
                     self.Q[self.state][self.action], sep='\t')
        self.state = next_state
        self.action = self.exploration_strategy(self.Q[next_state],
                                     self.visits[next_state],**self.es_kwargs)
        self.display(3,f"Agent {self.role} doing {self.action} in state {self.state}")
        return self.action

####### TEST CASES ########
from rlProblem import Simulate,epsilon_greedy, ucb
from rlExamples import Healthy_env, Monster_game_env
from rlQLearner import Q_learner

env = Healthy_env()
# Some RL agents with different parameters:
ag = Q_learner(env.name, env.actions, 0.7)
ag_ucb = Q_learner(env.name, env.actions, 0.7, exploration_strategy = ucb, es_kwargs={'c':0.1}, method="ucb")
ag_opt = Q_learner(env.name, env.actions, 0.7, Qinit=100, method="optimistic" )
ag_exp_m = Q_learner(env.name, env.actions, 0.7, es_kwargs={'epsilon':0.5}, method="more explore")
ag_greedy = Q_learner(env.name, env.actions, 0.1, Qinit=100, method="disc 0.1")

sim_ag = Simulate(ag,env)

# sim_ag.go(100)
# ag.Q    # get the learned Q-values
# sim_ag.plot()
# Simulate(ag_ucb,env).go(100).plot()
# Simulate(ag_opt,env).go(100).plot()
# Simulate(ag_exp_m,env).go(100).plot()
# Simulate(ag_greedy,env).go(100).plot()


from mdpExamples import MDPtiny
from rlProblem import Env_from_MDP
envt = Env_from_MDP(MDPtiny())
agt = Q_learner(envt.name, envt.actions, 0.8)
#Simulate(agt, envt).go(1000).plot()

mon_env = Monster_game_env()
mag1 = Q_learner(mon_env.name, mon_env.actions,0.9)
#Simulate(mag1,mon_env).go(100000).plot()
mag_ucb = Q_learner(mon_env.name, mon_env.actions,0.9,exploration_strategy = ucb,es_kwargs={'c':0.1},method="UCB(0.1)")
#Simulate(mag_ucb,mon_env).go(100000).plot()

mag2 = Q_learner(mon_env.name, mon_env.actions, 0.9,es_kwargs={'epsilon':0.2},alpha_fun=lambda k:1/k,method="alpha=1/k")
#Simulate(mag2,mon_env).go(100000).plot()
mag3 = Q_learner(mon_env.name, mon_env.actions, 0.9,alpha_fun=lambda k:10/(9+k),method="alpha=10/(9+k)")
#Simulate(mag3,mon_env).go(100000).plot()

