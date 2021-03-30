Introduction
============

.. note::
    This documentation is work in progress and far from finished. New sections will be added in the near future.
    Whenever questions or feedback is received from end users, we're trying to update this documentation on the fly.
    So don't hesitate to contact us, whenever you run into problems.

The Energy System Simulator (ESSIM) is a discrete time simulation tool and collection of models that calculates energy flows in assets and the effects thereof, in an interconnected hybrid energy system over a period of time. With the help of the energy flows ESSIM calculates, one can get insights into how well the assets in a network are dimensioned, if there is overloading in any given transport asset (like pipe, cables, etc.) and what the effect of storage is in any part of the network.

  .. figure:: ../images/ESSIM-overview.png
    :scale: 40 %  
    :align: center

    An overview of what ESSIM does

Traditionally, dimensioning of assets was assessed by looking at yearly values of energy supply and demand. In a simple network where a producer supplied 10TJ per year and a consumer consumed 10TJ, the system, under such a calculation, is in balance and the energy producer is properly dimensioned to meet the demands of the consumers in the network.

  .. figure:: ../images/system-in-balance.png
    :scale: 40 %
    :align: center

    A system that appears to have no net yearly energy imbalance

However, in reality producers do not produce a constant amount of energy every hour of every day throughout the year. Neither do demands have a constant flat line consumption pattern. These variations when captured as a profile highlight the mismatch despite the annual sums adding up.

  .. figure:: ../images/system-imbalance.png
    :align: center

    Hourly data showing imbalance

ESSIM helps the user identify such nuances as it repeatedly calculates energy flows per time step for a simulation period. It takes as inputs the energy system defined in ESDL and calculates optimal schedule of flexible producers and the effect of this schedule in terms of emissions, costs, load on the network, etc. Thanks to the easy configurability of the energy system with the help of the ESDL MapEditor, the user can use ESSIM to perform "what if?" scenario analyses on current and future energy systems. Along with the primary KPIs (Key Performance Indicator) of ESSIM (Energy mix, network imbalance, emissions, etc.), external KPI modules connected to ESSIM also allow for post-processing ESSIM data to get measurable insights into the energy system variations.

  .. figure:: ../images/ESSIM-cycle.png
    :scale: 50 %
    :align: center

    ESSIM used in the planning-design phase of Energy Transition

At the heart of the tool are:

  * A simulation engine that orchestrates a fixed discrete timestep evaluation of each commodity network’s balance in a pre-determined order,
  * A flexibility-based demand-supply matching algorithm that uses marginal costs of energy production as a means to grade desirability of producers,
  * A tree-based transport network solver that calculates the load on various transport elements based on the demand-supply solution determined above.

The tool outputs the data provided and generated during the course of the simulation into a time-series database (InfluxDB) and generates a dashboard (Grafana) to visualise the same.
ESSIM allows for connecting external asset models (via an MQTT interface) and external network (solver) models (via a REST interface), alongside its internal models and while using its own orchestration mechanism. This makes ESSIM a viable candidate for a co-simulation orchestrator.
