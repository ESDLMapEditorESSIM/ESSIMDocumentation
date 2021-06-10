<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" esdlVersion="v2102" version="3" id="ee10ca5f-a08d-4201-823c-fa7abcc1ba1b" name="Untitled EnergySystem" description="">
  <energySystemInformation xsi:type="esdl:EnergySystemInformation" id="751842b7-80e1-4e82-a222-fdebeca8a797">
    <carriers xsi:type="esdl:Carriers" id="0a3cb696-2558-48f4-9e23-aff11e1020a4">
      <carrier xsi:type="esdl:HeatCommodity" name="Heat" id="fcd62e8f-ef7a-404c-8d3f-d94e9dd48cd3" supplyTemperature="80.0" returnTemperature="40.0"/>
    </carriers>
    <quantityAndUnits xsi:type="esdl:QuantityAndUnits" id="3f1a3603-2018-4a16-97e9-67eeee195a5b">
      <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="ENERGY" unit="JOULE" multiplier="GIGA" id="eb07bccb-203f-407e-af98-e687656a221d" description="Energy in GJ"/>
    </quantityAndUnits>
  </energySystemInformation>
  <instance xsi:type="esdl:Instance" name="Untitled Instance" id="42a64855-de86-4a66-b267-b00c66b43b58">
    <area xsi:type="esdl:Area" name="Untitled Area" id="7bcf5cd9-d3fe-4626-859a-c16d89ddf552">
      <asset xsi:type="esdl:GeothermalSource" name="GeothermalSource_b572" id="b572d6cb-313e-489f-b489-a86bbd6ecd21">
        <geometry xsi:type="esdl:Point" lon="4.702792167663575" CRS="WGS84" lat="52.12170613337859"/>
        <port xsi:type="esdl:OutPort" id="15ff7099-8b7f-46af-bcc4-63e03f17722e" name="Out" connectedTo="a09857b5-5093-499c-83ce-54ecc54a7518" carrier="fcd62e8f-ef7a-404c-8d3f-d94e9dd48cd3">
          <profile xsi:type="esdl:SingleValue" value="5.0" id="a3804b62-4205-4afb-bf78-60cd73d339f2">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitReference" reference="eb07bccb-203f-407e-af98-e687656a221d"/>
          </profile>
        </port>
      </asset>
      <asset xsi:type="esdl:HeatingDemand" name="HeatingDemand_b505" id="b505c10b-bde4-4606-8d68-7f8e0188c383">
        <geometry xsi:type="esdl:Point" lon="4.712383747100831" CRS="WGS84" lat="52.12191692831886"/>
        <port xsi:type="esdl:InPort" connectedTo="15ff7099-8b7f-46af-bcc4-63e03f17722e" id="a09857b5-5093-499c-83ce-54ecc54a7518" name="In" carrier="fcd62e8f-ef7a-404c-8d3f-d94e9dd48cd3">
          <profile xsi:type="esdl:SingleValue" value="5.0" id="e19ae2d6-3ff7-494c-b8bf-86450d855838">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitReference" reference="eb07bccb-203f-407e-af98-e687656a221d"/>
          </profile>
        </port>
      </asset>
    </area>
  </instance>
</esdl:EnergySystem>
