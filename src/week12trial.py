# myTeam.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from captureAgents import CaptureAgent
import random, time, util
from game import Directions
import game
from keyboardAgents import KeyboardAgent

#################
# Team creation #
#################

def createTeam(firstIndex, secondIndex, isRed,
               first = 'SmarterAgent', second = 'SmarterAgent'):
  """
  This function should return a list of two agents that will form the
  team, initialized using firstIndex and secondIndex as their agent
  index numbers.  isRed is True if the red team is being created, and
  will be False if the blue team is being created.

  As a potentially helpful development aid, this function can take
  additional string-valued keyword arguments ("first" and "second" are
  such arguments in the case of this function), which will come from
  the --redOpts and --blueOpts command-line arguments to capture.py.
  For the nightly contest, however, your team will be created without
  any extra arguments, so you should make sure that the default
  behavior is what you want for the nightly contest.
  """

  # The following line is an example only; feel free to change it.
  return [eval(first)(firstIndex), eval(second)(secondIndex)]

##########
# Agents #
##########


class SmarterAgent(CaptureAgent):
  def registerInitialState(self, gameState):
    CaptureAgent.registerInitialState(self, gameState)
    self.home = gameState.getInitialAgentPosition(self.index)

  def chooseAction(self, gameState):
    actions = gameState.getLegalActions(self.index) 
    if gameState.getAgentState(self.index).numCarrying >= 5:
      TargetPlace = self.home
    else: 
      TargetPlace = self.getTargetPelletPosition(gameState)
        
    minDistance = 9999
    for action in actions:
      successor = gameState.generateSuccessor(self.index, action)
      NextPos = successor.getAgentState(self.index).getPosition()

      NextDistanceToFood = self.getMazeDistance(NextPos, TargetPlace)
      if NextDistanceToFood < minDistance: 
        minDistance = NextDistanceToFood
        GoodAction = action

    return GoodAction
    
  def getTargetPelletPosition(self, gameState):
    foodList = self.getFood(gameState).asList()   
    myPos = gameState.getAgentState(self.index).getPosition()

    minDistance = 9999
    if len(foodList) == 0:
      return self.home

    for food in foodList:
      DistanceToFood = self.getMazeDistance(myPos, food)
      if DistanceToFood < minDistance:
        minDistance = DistanceToFood
        FoodPosition = food

    return FoodPosition

