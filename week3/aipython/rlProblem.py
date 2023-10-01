# rlProblem.py - Representations for Reinforcement Learning
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
from agents import Agent, Environment
from utilities import pick_from_dist, argmaxe, argmaxd, flip

class RL_env(Environment):
    def __init__(self, name, actions, state):
        """creates an environment given name, list of actions, and initial state"""
        self.name = name         # the role for an agent 
        self.actions = actions   # list of all actions
        self.state = state       # initial state

    # must implement do(action)->(reward,state)
    

class RL_agent(Agent):
    """An RL_Agent 
    has percepts (s, r) for some state s and real reward r
    """
    def __init__(self, actions):
       self.actions = actions

    def initial_action(self, env_state):
        """return the initial action, and remember the state and action
        Act randomly initially
        Could be overridden to initialize data structures (as the agent now knows about one state)
        """
        self.state = env_state
        self.action = random.choice(self.actions)
        return self.action

    def select_action(self, reward, state):
        """ 
        Select the action given the reward and next state
        Remember the action in self.action
        This implements "Act randomly" and should  be overridden!
        """
        self.action = random.choice(self.actions)
        return self.action
        
import matplotlib.pyplot as plt

class Simulate(Displayable):
    """simulate the interaction between the agent and the environment
    for n time steps.
    Returns a pair of the agent state and the environment state.
    """
    def __init__(self, agent, environment):
        self.agent = agent
        self.env = environment
        self.action = agent.initial_action(self.env.state)
        self.reward_history = []  # for plotting
        
    def go(self, n):
        for i in range(n):
            (reward,state) = self.env.do(self.action)
            self.display(2,f"i={i} reward={reward}, state={state}")
            self.reward_history.append(reward)
            self.action = self.agent.select_action(reward,state)
            self.display(2,f"      action={self.action}")
        return self

    def plot(self, label=None, step_size=None, xscale='linear'):
        """
        plots the rewards history in the simulation
        label is the label for the plot
        step_size is the number of steps between each point plotted
        xscale is 'log' or 'linear'

        returns sum of rewards
        """
        if step_size is None: #for long simulations (> 999), only plot some points
            step_size = max(1,len(self.reward_history)//500)
        if label is None:
            label = self.agent.method
        plt.ion()
        plt.xscale(xscale)
        plt.xlabel("step")
        plt.ylabel("Sum of rewards")
        sum_history, sum_rewards = acc_rews(self.reward_history, step_size)
        plt.plot(range(0,len(self.reward_history),step_size), sum_history, label=label)
        plt.legend()
        plt.draw()
        return sum_rewards

def acc_rews(rews,step_size):
    """returns the rolling sum of the values, sampled each step_size, and the sum
    """
    acc = []
    sumr = 0; i=0
    for e in rews:
       sumr += e
       i += 1
       if (i%step_size == 0): acc.append(sumr)
    return acc, sumr


class Env_from_MDP(RL_env):
    def __init__(self, mdp):
        initial_state = random.choice(mdp.states)
        RL_env.__init__(self, "From MDP", mdp.actions, initial_state)
        self.mdp = mdp

    def do(self, action):
        """updates the state based on the agent doing action.
        returns state,reward
        """
        reward = self.mdp.R(self.state,action)
        self.state = pick_from_dist(self.mdp.P(self.state,action))
        return reward,self.state

def epsilon_greedy(Qs, Vs={}, epsilon=0.1):
        """select action given epsilon greedy
        Qs is the {action:Q-value} dictionary for current state
        Vs is ignored
        """
        if flip(epsilon):
            return random.choice(list(Qs.keys())) # act randomly
        else:
            return argmaxd(Qs)

def ucb(Qs, Vs, c=1.4):
        """select action given upper-confidence bound
        Qs is the  {action:Q-value} dictionary for current state
        Vs is the {action:visits} dictionary for current state

        0.01 is to prevent divide-by zero (could just be infinity)
        """
        Ns = sum(Vs.values())
        ucb1 = {a:Qs[a]+c*math.sqrt(Ns/(0.01+Vs[a]))
                    for a in Qs.keys()}
        action = argmaxd(ucb1)
        return action

