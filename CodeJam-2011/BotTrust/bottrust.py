#! -*- coding: utf8 -*-
# Python 2.7

class Bot(object):
    
    def __init__(self, color, seq):
        self.color = color
        self.pos = 1
        self.seq = []
        self._calc_seq(seq)

    def _calc_seq(self, seq):
        for color, pos in seq:
            if color == self.color:
                self.seq.append(pos)
    def update(self):
        if self.seq != []:
            next = self.seq[0]
            if next > self.pos:
                self.pos += 1
            elif next < self.pos:
                self.pos -= 1


# we use an instruction list

def calc_strategy(sequence):
    bot1 = Bot('O', sequence)  #the orange bot position
    bot2 = Bot('B', sequence) 
    bots = {'O': bot1, 'B': bot2}  #hacer que se genere automaticamente
    
    counter = 0
    while sequence != []:
        
        counter += 1
        bot, pos = sequence[0]
        if bots[bot].pos == pos:
            for _bot in bots.values():
                _bot.update()
            bots[bot].seq.pop(0)  #cumplio la ultima acción
            sequence.pop(0)
        else:
            for _bot in bots.values():
                _bot.update()
    
    return counter
    

if __name__ == '__main__':
    import sys
    fh = open(sys.argv[1])
    lines = fh.readlines()
    fh.close()
    cases = int(lines.pop(0))
    for case in xrange(1, cases + 1):
        line = lines.pop(0).split()
        seq_len = int(line.pop(0))
        seq = [(line.pop(0), int(line.pop(0))) for n in xrange(0, seq_len)]
        print "Case #%d: %d" % (case, calc_strategy(seq))

        







