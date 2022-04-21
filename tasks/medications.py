import pandas as pd
#print(pd.__name__)

def create_medications(names, counts):
    """
    Напишите функцию create_mediactions(names, counts), которая  создает Series medications,
    индексами которой являются названия лекарств names, а значениями - их количество в поставке counts
    """
   
    medications = pd.Series(
        data = counts,
        index = names
        )
    return medications
   

def get_percent(medications, name):
    """
    А также напишите функцию get_percent(medications, name), которая возвращает долю количества товара
    с именем name от общего количества товаров в поставке в процентах.
    """
    if name in names:
        result = medications.loc[name]*100/sum(medications)
    else: 
        result = 0
    return result

if __name__ == '__main__':
    names=['chlorhexidine', 'cyntomycin', 'afobazol']
    counts=[15, 18, 7]
    medications = create_medications(names, counts)
    print(get_percent(medications, 'chlorhexidine')) #37.5
