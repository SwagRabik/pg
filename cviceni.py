from typing import Set, Hashable

def jaccard_distance_sets(a: Set[Hashable], b: Set[Hashable]) -> float:
    """
    Jaccardova vzdálenost pro dvě množiny.
    Vrací 0.0 pokud jsou obě množiny prázdné.
    """
    union_size = len(a | b)
    if union_size == 0:
        return 0.0
    inter_size = len(a & b)
    return 1.0 - (inter_size / union_size)

if __name__ == "__main__":
    
    print(jaccard_distance_sets({1, 2, 3}, {2, 3, 4}))  
    print(jaccard_distance_sets(set(), set()))          # oček. 0.0
    print(jaccard_distance_sets({"a", "b"}, {"b", "c"}))# oček. ~0.666...
# 


Tato funkce spocita jaccardovu vzdalenost a levensteinovu vzdalenost a vyradi z seznamu dotazy, ktere budou mit jaccardovu vzdalenost mensi nez 0.5 a levensteinovu vzdalenost vetsi nebo rovno 1.