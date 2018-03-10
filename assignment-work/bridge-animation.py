from time import sleep
import bridge

is_playing = True

def run():
  while(is_playing):
    update()
    render()
    
def update():
  if (bridge.is_finished()):
    bridge.reset()
  else:
    bridge.update()

def render():
  print("\n" * 100)
  bridge.render()
  sleep(1)
  
run()