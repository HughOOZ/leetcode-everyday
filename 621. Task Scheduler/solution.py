def leastInterval(self, tasks, N):
    task_counts = collections.Counter(tasks).values()
    M = max(task_counts)
    Mct = task_counts.count(M)
    return max(len(tasks), (M - 1) * (N + 1) + Mct)

'''Let's say the most frequent tasks occur M times, and there are Mct of them.

When N > Mct, let's make our scheduling constraint strictly stronger by choosing N = Mct. So from now on, let's suppose Mct <= N, and the most frequent tasks are denoted #A, #B, #C, ... #K.

Then we could schedule say, ABC...K__...ABC...K_...ABC...K_....., where A...K occurs Mct times, _ denotes idle time, and there is N space between A's. This partial schedule would have length L = (M-1) * (N+1) + Mct. Clearly, we need at least L intervals of time in our schedule to fit our given tasks. Let's show this is enough.

Start inserting the remaining similar tasks in the following 'writing' order:

The first space to the right of the first K
The first space to the right of the second K
...
The first space to the right of the last K
The second space to the right of the first K
...
The second space to the right of the last K
The third space to the right of the first K
....
For example, say we have A B C 1 4 7 10 A B C 2 5 8 11 A B C 3 6 9 12 A B C D.
The numbers denote idle time in the order we will insert.
If we have EEEFFGGHHJJK left, we would insert:
A B C E F G J A B C E F H J A B C E G H K A B C D

Say two tasks of the same type collide if they are scheduled within N time of each other. After we have inserted all tasks of frequency M - 1 (which clearly will not collide), other tasks of frequency lower than M - 1 will never have any task written collide with it's left-neighbor (because of the writing order), and the last task written does not collide with the first task written as they are at least 2N - 1 apart.

If len(tasks) <= L, this proves that an L-length schedule satisfies.

When len(tasks) > L, clearly we need at least len(tasks) intervals of time to schedule all tasks - one interval for each task. Let's insert remaining tasks as before, possibly having one task incomplete. For example, we might have A B C E F G J A B C E F H J A B C E G H K A B C D, with KLLMMNNOO left to insert - and K is incomplete. Our strategy will now be to insert these tasks into our compact schedule.

Our incomplete task (K in our example) can be completed by inserting tasks K in the writing order spots that preceded it. For example, if we wrote J 10th, J 11th, and K 12th, then the positions 11 and 10 are suitable to add K without collision (and numerous enough to permit adding them all). Now with our remaining tasks, say LL, we will insert in the 1st, N+1th, (and 2N+1th, 3N+1th, etc. if necessary) positions in schedule order.

So we've shown that the answer is max(len(tasks), L).'''