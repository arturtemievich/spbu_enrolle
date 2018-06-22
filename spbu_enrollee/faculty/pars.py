import requests
import bs4

__URL = "https://timetable.spbu.ru"


class FacultyItem:
    """
    Один факультет с вложенными направлениями
    """
    
    def __init__(self):
        self.name, self.directions = None, []


def __parse_faculties():
    """
    Парсим все факультеты
    :return:
    """
    response = requests.get(__URL)
    content = bs4.BeautifulSoup(response.text, "html.parser")
    first_column = content.select(".col-sm-6")
    faculties = first_column[0].select('.list-group-item')
    
    return faculties


def __parse_directions(page):
    """
    По факультету парсим все направления
    :param page: str() url страницы с которой парсим направления
    :return
    """

    resp = requests.get(__URL + page)
    directions = bs4.BeautifulSoup(resp.text, 'html.parser')
    
    return directions.select(".panel-default")


def get_all_faculties():
    
    ret = list()
    
    for row in __parse_faculties():
        
        page = row.select("a")[0].get("href", "")
        faculty = FacultyItem()
        faculty.name = row.select("a")[0].getText().replace("  ", "").replace("\r\n", "")
        
        # Игнорируем Академическую гимназию
        if page == '/AGSM':
            continue
    
        for _ in __parse_directions(page):
            
            h4 = _.select(".panel-heading")
            level = h4[0].select("h4")[0].select("a")[0].getText()
            level = level.replace(" ", "").replace("\r\n", "")
            
            # Парсим только направления бакалавриата
            if level != "Бакалавриат":
                continue
        
            direction = _.select(".col-sm-5")
            for item in direction[1:len(direction)]:
                dir_name = item.getText().replace("  ", "").replace("\r\n", "")
                faculty.directions.append(dir_name)
        
        ret.append(faculty)
    
    return ret
