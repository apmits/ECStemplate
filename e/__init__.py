import yaml
import importlib

import w


def dict_from_yml(file):
    _d = {}
    _path_file = './e/{}'.format(file)
    try:
        # Opens it as stream
        _gobj = yaml.load_all(open(_path_file))  # yaml parsing returns a generator object (not a dict!).
    except IOError:
        print("Error opening {}".format(_path_file))
    else:
        for aaa in _gobj:
            _d.update(aaa)  # Note: because it's a generator, for "double" yaml entries, only the last will be kept!
    return _d


def add_components_for_entity(entity, component_spec):
    """
    :param entity:
    :param component_spec: dictionary; see example_entity_player{...}
    :return:
    """
    for entity_in_spec in component_spec:
        # Debug
        print('>>> str(entity_in_spec): {}      type(entity_in_spec): {}'.format(str(entity_in_spec),
                                                                                 type(entity_in_spec)))
        for component in component_spec[entity_in_spec]:
            # Debug
            print('>>> str(component): {}       type(component): {}'.format(str(component), type(component)))

            # create a dictionary with all component properties (for each component) - reset it.
            c_properties = {}

            for c_property in component_spec[entity_in_spec][component]:
                # Debug
                print('>>> str(c_property): {}      type(c_property): {}'.format(str(c_property), type(c_property)))

                # Case:
                #   player.yml :
                #    Clickable:
                #       - to_function : "xoxoxo"
                #       - has_selector             <--- below code should allow me to leave property <value> empty.
                # if c_property is not dict, convert it to dict:True
                if not isinstance(c_property, dict):
                    c_property = {c_property: True}
                    print('>>>                  Converted! : {}    {}'.format(str(c_property), type(c_property)))

                c_properties.update(c_property)  # if same properties have overlapping keys, the final value
                #                                  will be taken from the last

            if c_properties:
                # Create the component INSTANCE, and add it to w.world;
                #   To avoid below hard-coding, eg:
                """
                # Debug
                #   print('>>> type(component): {}'.format(type(component)))
                #   print('>>> str(component): {}'.format(str(component)))
                if component == 'Velocity':
                    #                          ** -> https://www.python-course.eu/passing_arguments.php
                    new_component = c.Velocity(**c_properties)
                elif component == 'Renderable':
                    new_component = c.Renderable(**c_properties)
                elif component == 'Printable':
                    new_component = c.Printable(**c_properties)
                elif component == 'Clickable':
                    new_component = c.Clickable(**c_properties)
                else:
                    print('Unknown component!')
                    break
                """
                #   Dynamically load a class,
                try:
                    module = importlib.import_module('c.{}'.format(component))
                    # Debug
                    print('>>> Loading module: {}   component: {}'.format(str(module), component))
                    my_class = getattr(module, component)  # component (string) Class name, should be EXACTLY
                    #                                        same with component filename! (same CamelCase)
                    # Debug
                    print('>>>                 class is: {}'.format(str(my_class)))
                    new_component = my_class(**c_properties)  # new_component instance.
                    # Debug
                    print('>>> Adding new_component: {} to entity: {} , for w.world'.format(str(new_component),
                                                                                            str(entity)))
                    print('>>>                       of type({}): {}'.format(str(new_component), type(new_component)))
                    w.world.add_component(entity,
                                          new_component)
                except Exception as e:
                    print('>>>                       Exception!: {}'.format(e))
                else:
                    print('>>>                       Done.')


#
# Examples; define some entities:
#

# Create player
player = w.world.create_entity()
#
# # Explanation:
#
# w.world.add_component(player,
#                       c.Velocity(x=0,
#                                  y=0))
#
# w.world.add_component(player,
#                       c.Renderable(image="assets/imgs/redsquare.png",
#                                    posx=100,
#                                    posy=100))
#
#                            /\_ component
#                                     /\_ c_property
#                                           /\_ c_value
#
example_entity_player = dict_from_yml('player.yml')
add_components_for_entity(player, example_entity_player)

# Create enemy
enemy = w.world.create_entity()
example_entity_enemy = dict_from_yml('enemy.yml')
add_components_for_entity(enemy, example_entity_enemy)

enemy_2 = w.world.create_entity()
add_components_for_entity(enemy_2, dict_from_yml('enemy2.yml'))

# Create sample text
sample_text_entity = w.world.create_entity()
add_components_for_entity(sample_text_entity, dict_from_yml('sample_text.yml'))

sample_text_entity2 = w.world.create_entity()
add_components_for_entity(sample_text_entity2, dict_from_yml('sample_text.yml'))

# Create clickable text
text_entity_3 = w.world.create_entity()
add_components_for_entity(text_entity_3, dict_from_yml('text_clickable.yml'))

# Make a selector (should not render immediately)
selector_1 = w.world.create_entity()
add_components_for_entity(selector_1, dict_from_yml('selector1.yml'))
