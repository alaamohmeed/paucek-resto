import flet
def single_image():
  container = flet.Container(
    content=flet.Image(
      src="assets/products/logo.png",
      fit=flet.ImageFit.COVER,
      expand=True,
    ),
    padding=0,
    margin=0,
    alignment=flet.alignment.center,
  )
  return container
