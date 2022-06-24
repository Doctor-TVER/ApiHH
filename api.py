import hhparser
'''
!ID - id вакансии (восклицательный знак обязателен)
NAME - название вакансии
!COMPANY_ID - id компании (восклицательный знак обязателен)
COMPANY_NAME - название компании
DESCRIPTION - описание вакансии
'''
vacancy = input('введите вакансию: ')
city = hhparser.id_name(input('введите город: '))
keywords = input('введите ключевые слова через , : ')
#получаем вакансии с сайта по заданным параметрам
res_all, vacancy_count = hhparser.api_hh(vacancy, city)
#средняя зп по всем найденым вакансиям по поиску
salary_mean = hhparser.salary_mean(res_all)
#требования к найденных вакансий
requirements = hhparser.requirements(res_all)
#вакансии по ключевым словам и количесвто этих вакансий
requirement_count, count_key_words = hhparser.requirement_count(requirements, keywords)
#новый словарь с нужными нам данными
new_dict = hhparser.merged_dict(vacancy, keywords, requirement_count, vacancy_count, salary_mean, count_key_words)
#заливаем в json файл
api_hh = hhparser.save_file(new_dict)
