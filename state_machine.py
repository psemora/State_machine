"""
Semestrální projekt do VZI
Deterministický konečný automat
Petr Šemora, 4pAIŘ/1
"""
from collections import defaultdict
from pyvis.network import Network

class StateMachine:
    def __init__(self): 
        self.init_state=None
        self.final_states=[]
        self.states=[]
        self.alphabet=[]
        self.current_state=None
        self.edges = []
        self.tranzition=defaultdict(dict)
        
    def add_tranzition(self, from_state, to_state,c): #Přidání přechodové funkce 
        self.test_state(from_state)
        self.test_state(to_state)
        self.test_char(c)
        self.edges.append([from_state,to_state,c])
        self.tranzition[from_state][c] = to_state

    def tranzit(self,c): #Průchod automatem
        self.test_char(c)
        try:
            self.current_state=self.tranzition[self.current_state][c]
        except:
            raise ValueError("This tranzit is not in tranzition !")

    def is_final_state(self): #Testování, zda jsme v koncovém stavu
        return self.current_state in self.final_states
            
    def reset(self): #Vrátí automat do počátečního stau
        self.current_state=self.init_state

    def test_state(self,state): #Testování, zda existuje stav, který jsme zadali v přechodové funkci
        if state not in self.states:
            raise ValueError("State is not defined in states !")

    def test_char(self,c): #Testování, zda existuje znak v abecedě, který jsme zadali v přechodové funkci
        if c not in self.alphabet:
            raise ValueError("Char is not in alphabet !") 

    def print_automat(self): #Vykreslení konečného automatu
        g = Network("600px", "1500px", directed=True, heading = "Deterministic finite automaton")
             
        for x in range(len(self.states)):
            if self.states[x] == self.init_state:
                g.add_node(self.states[x], label = self.states[x], physics = False, shape = "circle",size = 10, color = "lightgreen", title = "INIT STATE") 
            elif self.states[x] in self.final_states:
                g.add_node(self.states[x], label = self.states[x], physics = False, shape = "circle", color = "red", title = "FINAL STATE") 
            else: 
                g.add_node(self.states[x], label = self.states[x], physics = False, shape = "circle", color = "lightblue") 
            
        for row in self.edges:
            src_node = row[0]
            dest_node = row[1]
            weight = row[2]
            g.add_edge(src_node, dest_node, weight = weight, label = weight, width=2, color ="black")
        g.set_edge_smooth('dynamic')
        g.show('StateMachine.html')


if __name__ == "__main__":
    sm=StateMachine()
    #Množina stavů
    sm.states=["A","B","C","D","E"]
    #Počátečná stav
    sm.init_state="A"
    #Množina koncových stavů
    sm.final_states=["D","E"]
    #Množina vstupních symbolů - abeceda
    sm.alphabet=["0","1"]
    #Přechodová funkce
    sm.add_tranzition("A","A","0")
    sm.add_tranzition("A","B","1")
    sm.add_tranzition("B","C","0")
    sm.add_tranzition("B","A","1")
    sm.add_tranzition("C","D","0")
    sm.add_tranzition("C","B","1")
    sm.add_tranzition("D","E","0")
    sm.add_tranzition("D","C","1")
    sm.add_tranzition("E","E","0")
    sm.add_tranzition("E","D","1")
    
    sm.reset()
    #Určení průchodu automatem
    input=["1","0","0","0","0","1"]

    #Cyklus zajištující průchod automatem
    for c in input:
        sm.tranzit(c)
    print("State Machine is in position: {}".format(sm.current_state))
    if sm.is_final_state():
        print("Awesome, SM is in final state !")
    else:
        print ("Too bad, SM is not in final state :( ")
    
    #Zobrazení konečnýho automatu
    sm.print_automat()
    
    