from MouseTrap import MouseTrap, MouseAction

moves = ['mouse appears', 'mouse runs away', 'mouse appears', 'mouse enters trap',
         'mouse escapes', 'mouse appears', 'mouse enters trap', 'mouse trapped',
         'mouse removed', 'mouse appears', 'mouse runs away', 'mouse appears',
         'mouse enters trap', 'mouse trapped', 'mouse removed']

actions = map(MouseAction, moves)

mouse_trap_state_machine = MouseTrap()
mouse_trap_state_machine.run_all(actions)
