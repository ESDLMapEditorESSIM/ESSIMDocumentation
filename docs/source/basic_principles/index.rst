Basic principles
================

.. note::
    This documentation is work in progress and far from finished. New sections will be added in the near future.
    Whenever questions or feedback is received from end users, we're trying to update this documentation on the fly.
    So don't hesitate to contact us, whenever you run into problems.

Energy Assets
-------------
ESSIM follows the ESDL principle of classifying energy system assets into Producers, Consumers, Storages, Conversions and Transports. Each asset (except for Transport assets) can either have a pre-determined behaviour (*inflexible*) programmed into it with the help of a profile, or let ESSIM calculate its energy allocation (*flexible*) based on its flexibility, some control strategy and the behaviour of other assets in its network. ESSIM contains models for each of these five classes of assets and thanks to ESDL's hierarchical data structure, model behaviour can also be inherited from parent models. E.g. With a generic Consumer behaviour implementation, all existing ESDL Consumers such as ElectricityDemand, HeatingDemand, etc. and any ESDL Consumers added in the future can be supported within ESSIM. Additionally, implemented within ESSIM are also some specific asset models that have certain peculiarities. E.g. A co-generation plant is a conversion asset with two output ports with one output effecting the other.

  .. figure:: ../images/ESSIM-asset-models.png
    :scale: 40 %
    :align: center

    All implemented asset models in ESSIM

Transport Network
-----------------
In ESSIM, a transport network is an atomic network of connected energy assets perusing the same energy carrier. This means ESSIM treats isolated assets physically connected only to each other but using the same energy carrier as separate transport networks. Internally ESSIM creates a tree of such a network where the Producer/Consumer/Conversion/Storage assets are the leaf nodes and the Transport assets are the branches. Conversion assets appear in multiple transport networks as consumers of some energy carriers and producers of some others. Based on the provided ESDL description and configured behaviour, each transport network attempts to balance itself in each time step.

The transport network trees are created in the pre-processing step in ESSIM and cannot be changed during the simulation. In addition to creating the trees, ESSIM also pre-determines the order and parallelisation in computing the network tree balances.

  .. figure:: ../images/TransportNetworks.png
    :align: center

    Splitting of an energy system into constituent transport networks