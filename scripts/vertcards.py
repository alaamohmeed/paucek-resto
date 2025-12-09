import flet

def creat_food_cards():
  items = [
    {"image":"assets/products/p5.png","name":"Chicken Fries","price":"$7.99","rating":"4"},
    {"image":"assets/products/p6.png","name":" Burger","price":"$3.99","rating":"5"},
    {"image":"assets/products/p7.png","name":"French Fries","price":"$2.99","rating":"6"},
  ]
  card_list = []
  
  for item in items:
    stars = flet.Row(
      [flet.Icon(flet.Icons.STAR, color="yellow", size=16) for _ in range(int(item["rating"]))],
      spacing=2
    )
    
    card = flet.Container(
      padding=5,margin=5,bgcolor="#1B1B1B",
      border_radius=6,shadow=flet.BoxShadow(blur_radius=4),
      content=flet.Row(
        [
          flet.Column(
            [
              flet.Text(f"Name: {item['name']}", color="white", size=14, weight=flet.FontWeight.BOLD),
              flet.Text(f"Price: {item['price']}", color="green", size=14, weight=flet.FontWeight.BOLD),
              flet.Row([flet.Text("Rating: ", color='white'), stars],)
            ],
            alignment=flet.MainAxisAlignment.START,
            horizontal_alignment=flet.CrossAxisAlignment.START,
            spacing=4,expand=True
          ),
          flet.Container(
            content=flet.Image(src=item["image"], width=100, height=70, fit=flet.ImageFit.COVER),
            alignment=flet.alignment.center,
          )
        ],
        vertical_alignment=flet.CrossAxisAlignment.CENTER,
      )
    )
    card_list.append(card)
  column = flet.Container(
    content= flet.Column(
      card_list,spacing=5,horizontal_alignment=flet.CrossAxisAlignment.CENTER,
    ),
    padding=5
  )
  return column
    