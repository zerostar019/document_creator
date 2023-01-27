from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT


doc = Document(docx="сведения 2 таблицы.docx")


def change_table_text(dict):
    table = doc.tables[0]

    table.rows[2].cells[2].text = f"{dict.get('Наименование объекта')}"
    table.rows[3].cells[2].text = f"{dict.get('Адрес размещения')}"
    table.rows[4].cells[2].text = f"{dict.get('Сфера деятельности')}"
    table.rows[5].cells[2].text = f"{dict.get('Назначение объекта')}"
    table.rows[6].cells[2].text = f"{dict.get('Тип объекта')}"
    table.rows[7].cells[2].text = f"{dict.get('Архитектура объекта')}"
    table.rows[8].cells[2].text = f"{dict.get('Наименование ЭВМ')}"
    table.rows[9].cells[2].text = f"{dict.get('Наименование ПО')}"
    table.rows[10].cells[2].text = f"{dict.get('Наименование прикладных ПО')}"
    table.rows[11].cells[2].text = f"{dict.get('Категория сети электросвязи')}"
    table.rows[13].cells[2].text = f"{dict.get('Наименование оператора связи')}"
    table.rows[14].cells[2].text = f"{dict.get('Основные угрозы безопасности')}"
    table.rows[15].cells[2].text = f"{dict.get('Типы компьютерных инцидентов')}"
    table.rows[17].cells[2].text = f"{dict.get('Реализованные меры защиты')}"
    table.rows[18].cells[2].text = f"{dict.get('Применяемые средства защиты')}"
    table.rows[20].cells[2].text = f"{dict.get('Категория нарушителя')}"
    table.rows[22].cells[2].text = f"{dict.get('Организационные меры')}"

    doc.save("Таблица категорирования.docx")


def create_order():
    pass
