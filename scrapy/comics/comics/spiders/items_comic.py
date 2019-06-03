# -*- coding: utf-8 -*-
import scrapy

class ItemsComicSpider(scrapy.Spider):
    name = 'items-comic'    
    start_urls = ['https://www.starwars.com/films']
    
    def parse(self, response):
        movies = response.css('article')                
        for libro in movies:            
            comic = libro.css('section.module.links_list > .bound > .module_header.has-list.has-dropdown > ul.drop-container > li.has-linknoselect')            
            for link in comic:                
                link_detalle = link.css('span > a::attr(href)').extract_first()
                nombre_pelicula = link.css('span > a::text').extract_first()
                print(nombre_pelicula,link_detalle)
                next_page = response.urljoin(link_detalle)
                yield scrapy.Request(next_page, callback=self.parse_author)
                # yield response.follow(link_detalle, self.parse_author)

    def parse_author(self,response):
        movies = response.css('article > .module.catalog.content-span-full-screen > .bound > .description-container.films-content')
        for movie in movies:
            nombre_movie = response.css('h1::text').extract_first()
            descripcion_movie = response.css('.desc::text').extract_first() 
            lanzamiento_movie = response.css('p.meta > span::text').extract_first()
            # print(lanzamiento_movie)

        # lanzamiento_movie = response.css('article > .module.catalog.content-span-full-screen > .bound > .description-container.films-content > p.meta > span::text').extract_first()
        # nombre_movie = response.css('article > .module.catalog.content-span-full-screen > .bound > .description-container.films-content > h1::text').extract_first()
        # movie = response.css('article > .module.catalog.content-span-full-screen > .bound > .description-container.films-content > .desc::text').extract_first() 

        # poster_movie = response.css('article > .module.catalog.content-span-full-screen > .bound > .poster-container > .poster-box').extract_first()                         
        poster_movie = response.css('.building-block-wrapper > .content-wrapper    > .content-bumper > .content-info > h3 > a > span' ).extract_first()
        print(poster_movie)
