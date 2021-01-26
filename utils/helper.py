from datetime import date, datetime


# ---------------------------- FUNÇÕES AUXILIARES ----------------------------------------------------------------------
def date_para_str(data: date) -> str:
    """Formata uma data (tipo date) em uma string"""
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str) -> date:
    """Formata uma data (string) em uma date"""
    return datetime.strptime(data, '%d/%m/%Y')


def formata_moeda(valor: float) -> str:
    """Retorna uma string contendo um valor float de acordo com a formatação da moeda brasileira"""
    return f'R$ {valor:,.2f}'
