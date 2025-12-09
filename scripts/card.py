import flet
def create_cards():
  items = [
    {"image":"assets/products/p1.png"},
    {"image":"assets/products/p2.png"},
    {"image":"assets/products/p3.png"},
    {"image":"assets/products/p4.png"},
  ]
  card_list = []
  
  for item in items:
      card = flet.Container(
        width=90,padding=0,margin=5,bgcolor="white",
        border_radius=6,shadow=flet.BoxShadow(blur_radius=3),
        ### start card content ###
        content=flet.Container(
          content=flet.Image(
            src=item["image"],
            width=90,height=70,fit=flet.ImageFit.COVER
          ),
          alignment=flet.alignment.center,
          border=flet.border.all(2, color="#1B1B1B"),
        )
        ### end card content ###
      )
      card_list.append(card)
  row_content = flet.Container(
    flet.Row(
      card_list,spacing=8,alignment=flet.MainAxisAlignment.START,
      scroll=flet.ScrollMode.AUTO,height=80      
    ),
    padding=20
  )
  return row_content
    