# Utilitários de tempo
def str_to_minutos(hora):
    h, m = map(int, hora.split(":"))
    return h * 60 + m

def minutos_to_str(mins):
    return f"{mins//60:02d}:{mins%60:02d}"