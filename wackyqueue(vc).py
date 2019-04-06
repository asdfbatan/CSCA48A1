"""
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
"""

from wackynode import WackyNode

# Do not add import statements or change the one above.
# Write your WackyQueue class code below.


class WackyQueue():

    def __init__(self):
        self._oddlist = WackyNode(None, None) # dummy node
        self._evenlist = WackyNode(None, None)

    def __str__(self):
        result = ""
        curr = self._oddlist.get_next()
        while curr:
            result += str(curr.get_item())
            result += " -> "
            curr = curr.get_next()
        result += "None (odd) \n"

        curr = self._evenlist.get_next()
        while curr:
            result += str(curr.get_item())
            result += " -> "
            curr = curr.get_next()
        return result + "None (even)\n"


    def insert(self, obj, pri, node=None, curr=None, next=None):
        if not node: # for changepriority (in case you check for same node)
            node = WackyNode(obj, pri)
        if not curr: # for changepriority (avoid starting from head)
            curr, next = self._oddlist, self._evenlist

        while curr.get_next() and curr.get_next().get_priority() >= pri:
            next, curr = curr.get_next(), next

        node.set_next(next.get_next())
        next.set_next(curr.get_next())
        curr.set_next(node)


    def extracthigh(self):
        remove_node = self._oddlist.get_next()
        self._oddlist.set_next(self._evenlist.get_next())
        self._evenlist.set_next(remove_node.get_next())
        remove_node.set_next(None)
        return remove_node

    def isempty(self):
        return not self._oddlist.get_next()

    def changepriority(self, obj, pri):
        curr, next = self._oddlist, self._evenlist
        while curr.get_next() and curr.get_next().get_item() != obj:
            next, curr = curr.get_next(), next

        if curr.get_next() and curr.get_next().get_priority() != pri:
            old_pri = curr.get_next().get_priority()      # optional
            curr.get_next().set_priority(pri)
            node = curr.get_next()                        # optional
            temp = curr.get_next().get_next()
            curr.set_next(next.get_next())
            next.set_next(temp)

            if pri < old_pri:                             # optional
        	    self.insert(obj, pri, node, curr, next)   # optional
            else:
                self.insert(obj, pri, node)


    def _reverse(self, head):
        num_node = 0
        prev = None
        curr = head.get_next()
        while curr:
            curr.set_priority(-curr.get_priority())
            temp = curr.get_next()
            curr.set_next(prev)
            prev = curr
            curr = temp
            num_node += 1
        head.set_next(prev)
        return num_node

    def negateall(self):
        if (self._reverse(self._oddlist) + self._reverse(self._evenlist)) % 2 == 0:
        	temp = self._oddlist.get_next()
        	self._oddlist.set_next(self._evenlist.get_next())
        	self._evenlist.set_next(temp)


    def getoddlist(self):
        return self._oddlist.get_next()

    def getevenlist(self):
        return self._evenlist.get_next()


print("\n\n\n\n\n\n\n")





if __name__ == "__main__":

    wq = WackyQueue()
    wq.insert('6', 6)
    wq.insert('6', 6)
    wq.insert('A', 1)
    wq.insert('A', 0)
    wq.insert('A', 1)
    wq.insert('A', 0)
    wq.insert('B', 0)
    wq.insert('B', 0)
    wq.insert('Z', -2)
    wq.insert('P', -2)
    print(wq)

    print(wq.isempty())
    wq.changepriority('B', -100)
    wq.changepriority('6', 4)
    wq.insert('5', 5)
    print(wq)

    wq.negateall()
    print(wq)

    wq.changepriority('A', 100)
    wq.insert('C', -1)
    print("---")
    print(wq)
    wq.negateall()
    print(wq)
    wq.changepriority('P', -0.5)
    wq.changepriority('KYLE', 100)
    wq.negateall()
    print(wq)



    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.extracthigh())
    print(wq.isempty())
    # print(wq.extracthigh())
    # wq = WackyQueue()

    # wq.insert("A", 1)
    # wq.insert("B", 3)
    # wq.insert("C", 2)
    # wq.insert("D", 1)
    # wq.insert("E", 3)
    # wq.insert("F", 0)
    # wq.insert("G", -1)
    # wq.insert("H", -2)
    # print(wq)

    # wq.negateall()
    # print("negatall")
    # print(wq)

    # wq.insert("I", 3)
    # print("insert('I', 3)")
    # print(wq)

    # wq.negateall()
    # print("negatall")
    # print(wq)






    # print("removed: ", wq.extracthigh().get_item())
    # print(wq)

    # wq.changepriority("D", 4)
    # print(wq)
    # # wq.changepriority("E", 4)
    # # print(wq, "changepriority('E', 4)\n")
    # # wq.changepriority("F", 3)
    # # print(wq, "changepriority('F', 3)\n")
    # # wq.changepriority("E", 1)
    # # print(wq, "changepriority('E', 1)\n")
    # wq.insert("Z", -3)
    # wq.negateall()
    # print("negatall\n", wq)

    # print("\n\n\n\n\n")