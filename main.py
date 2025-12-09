import flet
from scripts.appbar import creat_appbar
from scripts.singleimg import single_image
from scripts.card import create_cards
from scripts.vertcards import creat_food_cards
from scripts.navbar import creat_navbar
from scripts.theme import creat_theme

def main(page:flet.Page):
  page.title = "Paucek Resto"
  page.window.width = 370
  page.window.height = 800
  page.bgcolor = "#121212"
  page.theme_mode = flet.ThemeMode.LIGHT
  page.padding = 0
  page.vertical_alignment = flet.MainAxisAlignment.CENTER
  page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
  page.window.resizable = True
  page.window.maximizable = False
  page.window.maximizable = False
  page.scroll = flet.ScrollMode.AUTO
  ### start theme ###
  page.appbar= creat_appbar()
  page.navigation_bar= creat_navbar()
  page.theme= creat_theme()
  ### end theme ###
  page.add(
    single_image(),
    flet.Text("Paucek Resto Food",color="white",size=22,weight=flet.FontWeight.BOLD),
    create_cards(),
    creat_food_cards(),
  )
  page.update()
flet.app(target=main)