from pyquery import PyQuery as pq
from tornado.ioloop import IOLoop


class MOMScrapper(object):
    def __init__(self, io_loop=None):
        self.io_loop = io_loop or IOLoop.instance()
        pass

    def get_scrapped_result(self, html, callback=None):

        dict_response = {}
        d = pq(html)
        title_html = pq(d.find('title').html())

        title_text = title_html.text()
        if "Not Available" in title_text:
            """
            TODO if Not available give empty dictionary 
            """
            dict_response = dict(error=408,
                                 message="စစ်ဆေးနိုင်မည့်အချိန်\nတနင်္လာနေ့ မှ သောကြာနေ့ တွင် နံနက် ၈ : ၀၀ - ည ၈ : ၀၀ အထိ : \nစနေနေ့တွင် နံနက် ၈ : ၀၀ - ညနေ ၂ : ၀၀ အထိ\nစစ်လို့ရပါတယ်")

        elif "PEPOLENQM009" in title_text:
            """
            TODO if it exists Continue scraping 
            """
            form_html = pq(d.find('form[name="enquiryForm"]').html())
            result_html = pq(form_html.find('.outerBox > table > tr'))
            result_html.each(lambda e, tb_row:
                             dict_response.update(
                                 {pq(tb_row).text().split(":")[0].strip(): pq(tb_row).text().split(":")[1].strip()})
                             )
        else:
            dict_response = dict(error=503,
                                 message="Internal Server Error")

        return callback(dict_response)
