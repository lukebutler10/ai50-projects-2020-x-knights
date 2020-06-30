from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

AInfo = None
BInfo = None
CInfo = None

ATruth = Symbol("A told truth")
ALie = Symbol("A told lie")
BTruth = Symbol("B told truth")
BLie = Symbol("B told lie")

# Puzzle 0
# A says "I am both a knight and a knave."


knowledge0 = And(
    Or(AKnight,AKnave),Not(And(AKnight,AKnave)),    #A must be a knight or a knave but he must not be both
    
    Implication(AKnight,And(AKnight,AKnave))
    
    )



# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    Or(AKnight,AKnave),Not(And(AKnight,AKnave)),    #A must be a knight or a knave but he must not be both
    Or(BKnave,BKnight),Not(And(BKnight,BKnave)), 

    Biconditional(AKnight,And(AKnave, BKnave))
    
)

# Puzzle 2
# A says "We are the same kind."        A is a knave, B is a knight
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight,AKnave),Not(And(AKnight,AKnave)),    
    Or(BKnave,BKnight),Not(And(BKnight,BKnave)), 

    Biconditional(AKnight, Or(And(AKnight,BKnight),And(AKnave,BKnave)) ),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)) )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.  note: A can't say he's a knave 
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

#i think the trick here is to get AI to understand B is lying by saying "A said 'I am a knave'"
knowledge3 = And(
    Or(AKnight,AKnave),Not(And(AKnight,AKnave)),    
    Or(BKnave,BKnight),Not(And(BKnight,BKnave)),  
    Or(CKnave,CKnight),Not(And(CKnight,CKnave)), 

    Biconditional(BKnight, Or( Biconditional(AKnight,AKnave), Biconditional(AKnave,AKnight))),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
