import flet
def creat_navbar():
  return flet.NavigationBar(
    bgcolor= "#1F1F1F",
    indicator_color='white',
    label_behavior=flet.NavigationBarLabelBehavior.ALWAYS_SHOW,
    selected_index=0,
    destinations=[
      flet.NavigationBarDestination(icon=flet.Icons.HOME,label="Home"),
      flet.NavigationBarDestination(icon=flet.Icons.SEARCH,label="Search"),
      flet.NavigationBarDestination(icon=flet.Icons.PERSON,label="About"),
    ]
  )