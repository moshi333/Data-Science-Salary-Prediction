import pandas as pd

def shorten_categories(series, cutoff=10):
    """
    Оставляет топ-N популярных категорий, остальные заменяет на 'Other'.
    """
    top_values = series.value_counts().nlargest(cutoff).index
    return series.apply(lambda x: x if x in top_values else 'Other')

def load_data(filepath):
    """
    Загрузка данных
    """
    return pd.read_csv(filepath)