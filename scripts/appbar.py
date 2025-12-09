import flet
def creat_appbar():
  return flet.AppBar(
    title=flet.Text("Paucek Resto",size=19,color='white'),
    bgcolor= "#1F1F1F",
    center_title=True,
    leading=flet.Icon(flet.Icons.HOME, color="white",tooltip="Home"),
    actions=[
      flet.IconButton(flet.Icons.NOTIFICATIONS,icon_color="white",tooltip="Notfications"),
      flet.IconButton(flet.Icons.ACCOUNT_CIRCLE,icon_color="white",tooltip="Account"),
    ]
    
  )
  
  