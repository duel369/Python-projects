from bs4 import BeautifulSoup
import os

#opening a file('file name', 'read-only') as VARIABLE:
with open((os.path.join("WebScraping1/", "home.html")), 'r') as html_file:
    content = html_file.read()
#    print(content)

    soup = BeautifulSoup(content, 'lxml')
#    print(soup.prettify())

#    courses_html_tags = soup.find_all('h5')
    #courses_html_tags comes in a list, therefore the following block will separate it by text(.text)
#    for course in courses_html_tags:
#        print(course.text)

    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
#        print(course.prettify())
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

#        print(course_name)
#        print(course_price)
        print(f'{course_name} costs {course_price}')