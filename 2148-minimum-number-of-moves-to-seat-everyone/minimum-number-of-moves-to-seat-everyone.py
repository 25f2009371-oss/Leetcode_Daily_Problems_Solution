
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        s = 0
        for i in range(len(students)):
            s += abs(students[i] - seats[i])
        return s
