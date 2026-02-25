<mxfile host="app.diagrams.net" modified="2026-02-25T10:40:00.000Z" agent="Mozilla/5.0" version="24.7.8" type="device">
  <diagram id="dotnetKafkaArch" name="Page-1">
    <mxGraphModel dx="1400" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="900" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- ===== Groups (dashed containers) ===== -->
        <mxCell id="gClients" value="Clients" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeWidth=2;container=1;collapsible=0;fillColor=#ffffff;" vertex="1" parent="1">
          <mxGeometry x="30" y="80" width="260" height="340" as="geometry"/>
        </mxCell>

        <mxCell id="gHost" value="ASP.NET Core Host (.NET)" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeWidth=2;container=1;collapsible=0;fillColor=#ffffff;" vertex="1" parent="1">
          <mxGeometry x="320" y="40" width="780" height="700" as="geometry"/>
        </mxCell>

        <mxCell id="gKafka" value="Kafka" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeWidth=2;container=1;collapsible=0;fillColor=#ffffff;" vertex="1" parent="1">
          <mxGeometry x="1140" y="120" width="420" height="380" as="geometry"/>
        </mxCell>

        <mxCell id="gStore" value="State Store (Cache/DB) - optional" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeWidth=2;container=1;collapsible=0;fillColor=#ffffff;" vertex="1" parent="1">
          <mxGeometry x="1140" y="540" width="420" height="200" as="geometry"/>
        </mxCell>

        <!-- ===== Clients ===== -->
        <mxCell id="cWeb" value="Web Client" style="shape=mxgraph.mockup.containers.browserWindow;whiteSpace=wrap;html=1;fillColor=#f8f8f8;strokeWidth=2;" vertex="1" parent="gClients">
          <mxGeometry x="30" y="60" width="200" height="110" as="geometry"/>
        </mxCell>

        <mxCell id="cMobile" value="Mobile Client" style="shape=mxgraph.mockup.containers.mobile;whiteSpace=wrap;html=1;fillColor=#f8f8f8;strokeWidth=2;" vertex="1" parent="gClients">
          <mxGeometry x="70" y="200" width="120" height="170" as="geometry"/>
        </mxCell>

        <!-- ===== Host components ===== -->
        <mxCell id="ws" value="WebSocket Endpoint&#10;real-time streaming" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#fff2cc;" vertex="1" parent="gHost">
          <mxGeometry x="40" y="70" width="230" height="90" as="geometry"/>
        </mxCell>

        <mxCell id="rest" value="REST / Health" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#dae8fc;" vertex="1" parent="gHost">
          <mxGeometry x="40" y="180" width="230" height="70" as="geometry"/>
        </mxCell>

        <mxCell id="router" value="Message Router" style="shape=rhombus;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#e1d5e7;" vertex="1" parent="gHost">
          <mxGeometry x="330" y="105" width="150" height="110" as="geometry"/>
        </mxCell>

        <mxCell id="channel" value="Bounded In-Memory Queue&#10;System.Threading.Channels&#10;(backpressure)" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#d5e8d4;" vertex="1" parent="gHost">
          <mxGeometry x="290" y="270" width="260" height="110" as="geometry"/>
        </mxCell>

        <mxCell id="bg" value="Background Worker(s)&#10;IHostedService / BackgroundService" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#f8cecc;" vertex="1" parent="gHost">
          <mxGeometry x="310" y="420" width="240" height="90" as="geometry"/>
        </mxCell>

        <mxCell id="pool" value="Worker Pool&#10;Tasks + async/await" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#f5f5f5;" vertex="1" parent="gHost">
          <mxGeometry x="590" y="420" width="230" height="90" as="geometry"/>
        </mxCell>

        <mxCell id="serde" value="Serializer/Deserializer&#10;JSON / Avro / Protobuf" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#fff2cc;" vertex="1" parent="gHost">
          <mxGeometry x="590" y="540" width="230" height="80" as="geometry"/>
        </mxCell>

        <mxCell id="obs" value="Observability&#10;Metrics / Tracing / Logs" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#dae8fc;" vertex="1" parent="gHost">
          <mxGeometry x="40" y="560" width="230" height="90" as="geometry"/>
        </mxCell>

        <!-- ===== Kafka side ===== -->
        <mxCell id="kTopics" value="Kafka Topics" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#fff2cc;" vertex="1" parent="gKafka">
          <mxGeometry x="120" y="140" width="180" height="70" as="geometry"/>
        </mxCell>

        <mxCell id="kProd" value="Confluent.Kafka Producer" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#d5e8d4;" vertex="1" parent="gKafka">
          <mxGeometry x="40" y="40" width="220" height="70" as="geometry"/>
        </mxCell>

        <mxCell id="kCons" value="Confluent.Kafka Consumer" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#f8cecc;" vertex="1" parent="gKafka">
          <mxGeometry x="40" y="250" width="220" height="70" as="geometry"/>
        </mxCell>

        <!-- ===== State store ===== -->
        <mxCell id="storeDb" value="Cache / DB" style="shape=cylinder;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#f5f5f5;" vertex="1" parent="gStore">
          <mxGeometry x="140" y="70" width="160" height="90" as="geometry"/>
        </mxCell>

        <!-- ===== Edges (arrows) ===== -->
        <mxCell id="e1" value="WebSocket" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="cWeb" target="ws">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e2" value="WebSocket" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="cMobile" target="ws">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e3" value="HTTP" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="cWeb" target="rest">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e4" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="ws" target="router">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e5" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="router" target="channel">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="channel" target="bg">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="bg" target="pool">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e8" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="pool" target="serde">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e9" value="produce" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="pool" target="kProd">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e10" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="kProd" target="kTopics">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e11" value="poll" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="kTopics" target="kCons">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e12" value="poll" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="kCons" target="channel">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e13" value="push updates" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="pool" target="ws">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e14" value="read/write" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;" edge="1" parent="1" source="pool" target="storeDb">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Observability fan-in -->
        <mxCell id="e15" value="metrics/traces/logs" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;dashed=1;strokeWidth=2;" edge="1" parent="1" source="ws" target="obs">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e16" value="metrics/traces/logs" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;dashed=1;strokeWidth=2;" edge="1" parent="1" source="bg" target="obs">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e17" value="metrics/traces/logs" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;dashed=1;strokeWidth=2;" edge="1" parent="1" source="kProd" target="obs">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e18" value="metrics/traces/logs" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;dashed=1;strokeWidth=2;" edge="1" parent="1" source="kCons" target="obs">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
