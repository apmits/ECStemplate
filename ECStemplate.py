#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

import c
import p
import e
import w


FPS = 60
RESOLUTION = 720, 480


##################################
#  Define some Components:
##################################
#
# in ./c/
#


################################
#  Define some Processors:
################################
#
# in ./p/
#


################################
#  main program:
################################
def run():
    # Initialize Pygame stuff
    pygame.init()
    window = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("Entity Component System using esper + pygame.")
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)

    # Initialize Esper world:
    # world = esper.World()  # moved in w.

    # Create entities:
    #   I could define the entities in here, but then I'd had to call
    #   "player" instead of "e.player" in main loop below, and I don't like it's non explicitness.
    #   Instead, I use e.__init__ to instanciate the objects from.

    # Create some Processor instances, and assign them to be processed.
    render_processor = p.RenderProcessor(window=window)
    print_processor = p.PrintProcessor(window=window)
    movement_processor = p.MovementProcessor(minx=0, maxx=RESOLUTION[0], miny=0, maxy=RESOLUTION[1])
    w.world.add_processor(render_processor)  # todo: figure out proc priorities (.add_processor accepts optional args)
    w.world.add_processor(print_processor)
    w.world.add_processor(movement_processor)
    w.world.add_processor(p.ClickProcessor())  # instanciate & add to world.
    #
    # mouse "Processor" is separate from the Event System, due to speed reasons.
    #                   is instanciated in w., so it's "globally" accessible.
    #

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Here is a way to directly access a specific Entity's
                    # Velocity Component's attribute (y) without making a
                    # temporary variable.
                    w.world.component_for_entity(e.player, c.Velocity).x = -3
                elif event.key == pygame.K_RIGHT:
                    # For clarity, here is an alternate way in which a
                    # temporary variable is created and modified. The previous
                    # way above is recommended instead.
                    player_velocity_component = w.world.component_for_entity(e.player, c.Velocity)
                    player_velocity_component.x = 3
                elif event.key == pygame.K_UP:
                    w.world.component_for_entity(e.player, c.Velocity).y = -3
                elif event.key == pygame.K_DOWN:
                    w.world.component_for_entity(e.player, c.Velocity).y = 3
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    w.world.component_for_entity(e.player, c.Velocity).x = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    w.world.component_for_entity(e.player, c.Velocity).y = 0
            # Mouse handling:   https://www.pygame.org/docs/ref/mouse.html
            elif event.type == pygame.MOUSEMOTION:  # update mouse status (separately from the event system)
                w.mouse.x, w.mouse.y = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    w.mouse.clicked_L = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    w.mouse.clicked_L = False
            elif event.type == pygame.ACTIVEEVENT:
                dbgtext = 'ACTIVEEVENT: {} | event.state: {} | event.gain: {}'.format(
                    pygame.ACTIVEEVENT, event.state, event.gain)
                w.world.component_for_entity(e.sample_text_entity, c.Printable).text = dbgtext

            dbgtext2 = 'w.mouse.x: {:4d} | w.mouse.y: {:4d} | w.mouse.clicked_L: {}'.format(
                w.mouse.x, w.mouse.y, w.mouse.clicked_L)
            w.world.component_for_entity(e.sample_text_entity2, c.Printable).y = 70  # > than default value (in yaml)
            w.world.component_for_entity(e.sample_text_entity2, c.Printable).text = str(dbgtext2)

        # A single call to world.process() will update all Processors:
        w.world.process()

        clock.tick(FPS)


if __name__ == "__main__":
    run()
    pygame.quit()
