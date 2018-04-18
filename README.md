ECStemplate
===========

Example of an [Entity Component System](https://en.wikipedia.org/wiki/Entity–component–system) project, using [esper](https://github.com/benmoran56/esper) + [pygame](https://github.com/pygame/pygame).

Entity-Component-Systems *(Systems a.k.a. Processors)*, are helpful in data-driven architectures, where a high separation of concerns is desirable.

About
-----
Under `./e` are **Entities**; they are made out of **Components**.
An Entity is nothing more than a general `.yml` specification that defines a collection of arbitrary **Components** and their properties.

Under `./c` are **Components**, that can constitute an **Entity** *(think classes specifications)*.

Under `./p` are **Processors**; they hold the "logic" behind each entity.
Each **Processor** can act upon all **Entities** that have a specific set of **Components**.
That basically means that *processing* is loosely coupled with *entity instances*.

Additionally, `w.py` should hold the "global" state, if needed.


How to use
----------

Running `ECStemplate.py` will dynamically create classes + instances, based on specifications written in the `./e/*.yml` files.
This allows you to create new **Entities** from arbitrary **Components**, that adhere to specific behaviors defined in the **Processors**.


todo
----
* make import system more dynamic.
* work out the [event system](https://stackoverflow.com/questions/1092531/event-system-in-python#16192256) so entities can better notify each other of their actions.
