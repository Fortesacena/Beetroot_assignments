#---------------------------Other-----------------------------
"""Task 1"""
def cmimi_peshes(pesha, cmimi_per_gram):
    cmimi = pesha * cmimi_per_gram
    return cmimi

def percentage_error(percentage):
    def decorator(func):
        def wrapper(pesha, cmimi_per_gram):
            result = func(pesha, cmimi_per_gram)
            result_w_percentage = result * percentage  
            return result_w_percentage
        return wrapper
    return decorator

@percentage_error(0.99)
def cmimi_peshes_me_dekor(pesha, cmimi_per_gram):
    return cmimi_peshes(pesha, cmimi_per_gram)


pesha = 200 
cmimi_per_gram = 0.5  

final_price = cmimi_peshes_me_dekor(pesha, cmimi_per_gram)/100
print(f"Cmimi i peshes {pesha} gram me cmim per gram {cmimi_per_gram} eshte: {final_price:.2f} euro")