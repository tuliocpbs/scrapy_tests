#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import scrapy
import urllib

DIR = 'Downloads/'

class DownloadEnemSpider(scrapy.Spider):
    name = 'downloadEnem'
    start_urls = ['http://portal.inep.gov.br/web/enem/edicoes-anteriores/provas-e-gabaritos']

    def parse(self, response):

        for link_element in response.css('div.journal-content-article > ul > li > a'):
            download_link = link_element.css('a ::attr(href)').extract_first()

            # Optendo o nome do arquivo através do link do download
            file_name = download_link.split('/')[-1]
            dir_file = os.path.join(DIR, file_name)

            # Baixando o arquivo
            download_file = urllib.URLopener()
            download_file.retrieve(download_link, dir_file)
