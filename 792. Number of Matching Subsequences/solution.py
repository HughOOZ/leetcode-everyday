def numMatchingSubseq(self, S, words):
    'Using iterators to represent words and their progress:'
    waiting = collections.defaultdict(list)
    for w in words:
        waiting[w[0]].append(iter(w[1:]))
    for c in S:
        for it in waiting.pop(c, ()):
            waiting[next(it, None)].append(it)
    return len(waiting[None])

def numMatchingSubseq(self, S, words):
    'A version with cleaner initialization, using iterators iterating the whole word instead of a copy of the word after its first letter:'
    waiting = collections.defaultdict(list)
    for it in map(iter, words):
        waiting[next(it)].append(it)
    for c in S:
        for it in waiting.pop(c, ()):
            waiting[next(it, None)].append(it)
    return len(waiting[None])

def numMatchingSubseq(self, S, words):
    'Another version, make all words waiting for a space character and prepend a space character to S:'
    waiting = collections.defaultdict(list, {' ': map(iter, words)})
    for c in ' ' + S:
        for it in waiting.pop(c, ()):
            waiting[next(it, None)].append(it)
    return len(waiting[None])

''' go through S once, and while I'm doing that, I move through all words accordingly. That is, I keep track of how much of each word I've already seen, and with each letter of S, I advance the words waiting for that letter. To quickly find the words waiting for a certain letter, I store each word (and its progress) in a list of words waiting for that letter. Then for each of the lucky words whose current letter just occurred in S, I update their progress and store them in the list for their next letter.

Let's go through the given example:

S = "abcde"
words = ["a", "bb", "acd", "ace"]
I store that "a", "acd" and "ace" are waiting for an 'a' and "bb" is waiting for a 'b' (using parentheses to show how far I am in each word):

'a':  ["(a)", "(a)cd", "(a)ce"]
'b':  ["(b)b"]
Then I go through S. First I see 'a', so I take the list of words waiting for 'a' and store them as waiting under their next letter:

'b':  ["(b)b"]
'c':  ["a(c)d", "a(c)e"]
None: ["a"]
You see "a" is already waiting for nothing anymore, while "acd" and "ace" are now waiting for 'c'. Next I see 'b' and update accordingly:

'b':  ["b(b)"]
'c':  ["a(c)d", "a(c)e"]
None: ["a"]
Then 'c':

'b':  ["b(b)"]
'd':  ["ac(d)"]
'e':  ["ac(e)"]
None: ["a"]
Then 'd':

'b':  ["b(b)"]
'e':  ["ac(e)"]
None: ["a", "acd"]
Then 'e':

'b':  ["b(b)"]
None: ["a", "acd", "ace"]
And now I just return how many words aren't waiting for anything anymore.'''