import scrapy


class QuotesSpider(scrapy.Spider):
    name = "courses"
    start_urls = ['https://qa.auth.gr/x/studyguide/600000438/current']

    def parse(self, response):
        courses_container = response.css("div.qa_study_guide_lev_1:last-child")
        courses = courses_container.css("tbody a")
        yield from response.follow_all(courses, callback=self.parseCourse)
        
    # selects elemtns with css selectors
    def parseCourse(self, response):
        yield {
            "title": response.css("table.qa_general_data:last-child tbody tr:first-child td:last-child::text").get(),
            "ects": response.css("table.qa_course-orientation-info tbody td:last-child::text").get(),
            "type": response.css("table.qa_course-orientation-info tbody td:nth-child(2)::text").get(),
            "content": response.css("#course-elem-course-content-syllabus .value::text").get()
        }
