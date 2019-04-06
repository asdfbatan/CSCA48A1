'''
# Zhang Ti zhan5263
# Copyright Nick Cheng, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
'''

from wackynode import WackyNode


# Do not add import statements or change the one above.
# Write your WackyQueue class code below.
class WackyQueue():
    '''This is the class object of wacky queue'''

    def __init__(self):
        '''
        (WackyQueue) -> NoneType
        REQ: oddlist and evenlist must be link list
        '''
        self._oddlist = WackyNode(None, None)  # dummy node
        self._evenlist = WackyNode(None, None)  # dummy node

    def insert(self, obj, pri):
        '''
        (WackyQueue, obj, int) -> NoneType
        This function takes in an object with a priority
        and insert it into the proper position of the two link list
        REQ: the pri must be an integer
        '''
        # set the new node
        new_node = WackyNode(obj, pri)
        # set the basic pointers for the odd list
        prev = None
        curr = self._oddlist.get_next()
        # set the basic pointer for the even list
        prev_even = None
        curr_even = self._evenlist.get_next()
        # loop through every obj to find a place to insert
        while curr and curr_even and curr.get_priority() >= pri and\
              curr_even.get_priority() >= pri:
            # move forward the pointer on the odd list
            prev = curr
            curr = curr.get_next()
            # move forward the pointer on the even list
            prev_even = curr_even
            curr_even = curr_even.get_next()
        if not curr:
            if self._oddlist._next is None:
                self._oddlist.set_next(new_node)
            else:
                # if curr is none, then the new node is smaller than
                # both prev and prev_even
                prev.set_next(new_node)
        elif not curr_even:
            # if curr is not none but curr_even is none
            # there are two occations:
            if self._evenlist._next is None:
                if pri <= self._oddlist.get_next().get_priority():
                    self._evenlist.set_next(new_node)
                else:
                    self._evenlist.set_next(self._oddlist.get_next())
                    self._oddlist.set_next(new_node)
            else:
                if pri <= curr.get_priority():
                    # if pri is less than odd curr value
                    # then it is inserted into the even list at last
                    prev_even.set_next(new_node)
                else:
                    # if pri is bigger than curr value
                    # of course less or equal to prev_even value
                    # then the new node is inserted after the prev
                    prev.set_next(new_node)
                    prev_even.set_next(curr)
        elif pri > curr_even.get_priority() and pri <= curr.get_priority():
            # if pri is between the value of curr and curr_even
            # then the new node is inserted after the prev_even
            # link the new node with the curr position in even list
            if prev_even is None:
                self._evenlist.set_next(new_node)
            else:
                prev_even.set_next(new_node)
            # link the new node with the next object in odd list
            new_node.set_next(curr.get_next())
            # link the curr position in odd list
            # with the next object in even list
            curr.set_next(curr_even)
        elif pri > curr.get_priority():
            # if pri's value is bigger than curr's value
            # of course less or equal to prev_even value
            # link prev in odd list with new node
            if prev is None:
                self._oddlist.set_next(new_node)
            else:
                prev.set_next(new_node)
            # link the new node with the curr obj in even list
            new_node.set_next(curr_even)
            # link the prev position in even list with curr position in odd
            if prev_even is None:
                self._evenlist.set_next(curr)
            else:
                prev_even.set_next(curr)

    def extracthigh(self):
        '''
        (WackyQueue) -> obj
        This function remove and return the first item in the wacky queue
        REQ: the wacky queue is not empty
        '''
        # store the first item in another variable for retrn
        return_item = self._oddlist.get_next()
        # set the first of the even list be the head of the oddlist
        self._oddlist.set_next(self._evenlist.get_next())
        # set the second of the odd list be the head of the even list
        self._evenlist.set_next(self._oddlist.get_next().get_next())
        # return the item that was removed
        return return_item

    def changepriority(self, obj, pri):
        '''
        (WackyQueue, obj, int) -> NoneType
        This func change the priority of the first copy of object obj to pri
        REQ: the pri must be a integer
        '''
        # main idea: find the obj (if exist), restore it and remove it
        #            then take it as a new node with new pri and insert it
        # set the original pointers
        curr = self._oddlist
        curr_even = self._evenlist
        # while the next item is not none and is not the target
        # use the next item so that moving forward pointers
        # without nonetype error
        while curr.get_next() and curr.get_next().get_item() != obj:
            # move forward the pointers
            temp = curr
            curr = curr_even
            curr_even = temp.get_next()
        # if find the target and the priority is different
        if curr.get_next() and curr.get_next().get_priority() != pri:
            # restore the target item
            item = curr.get_next()
            # reset the priority of the target
            item.set_priority(pri)
            # restore the next of the item for link
            temp = item.get_next()
            # link the curr on odd list with the next on even list
            curr.set_next(curr_even.get_next())
            # link the curr on even list with next of the item
            curr_even.set_next(temp)
            # insert the new node with new priority
            self.insert(obj, pri)

    def _reverse(self, dummy):
        '''
        (WackyQueue, LLNode) -> int
        This is a helper function that negate the priority of each item
        revese the whole link list
        and return the length of the list
        REQ: dummy must be a link list
        '''
        # set the original pointers
        prev = None
        curr = dummy.get_next()
        # set the length counter
        length = 0
        # loop through every node, reverse the pointer between each node
        while curr:
            # negate the priority
            curr.set_priority(-curr.get_priority())
            # move forward the pointers
            temp = curr.get_next()
            curr.set_next(prev)
            prev = curr
            curr = temp
            # count the length
            length += 1
        # set the next of the head be the tail of the original
        dummy.set_next(prev)
        return length

    def negateall(self):
        '''
        (WackyQueue) -> NoneType
        This function negates the priority of every object in the wacky queue
        '''
        if self._reverse(self._oddlist) == self._reverse(self._evenlist):
            # if the two list has the same length
            # reverse the odd list with the even list
            temp = self._oddlist.get_next()
            self._oddlist.set_next(self._evenlist.get_next())
            self._evenlist.set_next(temp)
        else:
            # if odd list has one more item
            # then the two list are the same except the order inside each list
            pass

    def isempty(self):
        '''
        (WackyQueue) -> bool
        This functon returns if the link is empty
        '''
        return self._oddlist.get_next() is None

    def getoddlist(self):
        '''
        (WackyQueue) -> LLNode
        This function returns the odd list
        '''
        return self._oddlist.get_next()

    def getevenlist(self):
        '''
        (WackyQueue) -> LLNode
        This function returns the even list
        '''
        return self._evenlist.get_next()
