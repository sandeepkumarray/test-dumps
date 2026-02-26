<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0" version="29.5.4">
  <diagram id="dotnetKafkaLowLatency" name="Architecture">
    <mxGraphModel dx="2236" dy="1038" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="900" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="gClients" parent="1" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeWidth=2;strokeColor=#4D4D4D;fillColor=#FFFFFF;" value="Clients" vertex="1">
          <mxGeometry height="320" width="250" x="40" y="120" as="geometry" />
        </mxCell>
        <mxCell id="gHost" parent="1" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeWidth=2;strokeColor=#4D4D4D;fillColor=#FFFFFF;" value="ASP.NET Core Host (.NET)" vertex="1">
          <mxGeometry height="520" width="800" x="330" y="70" as="geometry" />
        </mxCell>
        <mxCell id="gKafka" parent="1" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeWidth=2;strokeColor=#4D4D4D;fillColor=#FFFFFF;" value="Kafka" vertex="1">
          <mxGeometry height="360" width="440" x="1170" y="80" as="geometry" />
        </mxCell>
        <mxCell id="cWeb" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#1F4E79;fillColor=#EAF2FF;" value="Web Client" vertex="1">
          <mxGeometry height="90" width="190" x="70" y="170" as="geometry" />
        </mxCell>
        <mxCell id="ws" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#2E7D32;fillColor=#E9F7EF;" value="WebSocket Endpoint&#xa;real-time streaming" vertex="1">
          <mxGeometry height="90" width="220" x="370" y="130" as="geometry" />
        </mxCell>
        <mxCell id="rest" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#2E7D32;fillColor=#E9F7EF;" value="REST / Health" vertex="1">
          <mxGeometry height="70" width="220" x="370" y="240" as="geometry" />
        </mxCell>
        <mxCell id="router" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#6A1B9A;fillColor=#F3E8FF;" value="Message Router" vertex="1">
          <mxGeometry height="70" width="230" x="630" y="150" as="geometry" />
        </mxCell>
        <mxCell id="channel" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#6A1B9A;fillColor=#F3E8FF;" value="Bounded In-Memory Queue&#xa;(System.Threading.Channels)&#xa;backpressure" vertex="1">
          <mxGeometry height="110" width="230" x="630" y="270" as="geometry" />
        </mxCell>
        <mxCell id="bg" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#B26A00;fillColor=#FFF3E0;" value="Background Worker(s)&#xa;(IHostedService)" vertex="1">
          <mxGeometry height="80" width="230" x="630" y="430" as="geometry" />
        </mxCell>
        <mxCell id="pool" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#B26A00;fillColor=#FFF3E0;" value="Worker Pool&#xa;(Tasks, async/await)" vertex="1">
          <mxGeometry height="80" width="230" x="890" y="430" as="geometry" />
        </mxCell>
        <mxCell id="serde" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#1565C0;fillColor=#E3F2FD;" value="Serializer / Deserializer&#xa;(JSON / Avro / Proto)" vertex="1">
          <mxGeometry height="90" width="230" x="890" y="250" as="geometry" />
        </mxCell>
        <mxCell id="obs" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#455A64;fillColor=#ECEFF1;" value="Observability&#xa;(Metrics / Tracing / Logs)" vertex="1">
          <mxGeometry height="90" width="230" x="890" y="130" as="geometry" />
        </mxCell>
        <mxCell id="kProducer" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#C62828;fillColor=#FFEBEE;" value="Confluent.Kafka Producer" vertex="1">
          <mxGeometry height="70" width="200" x="1200" y="160" as="geometry" />
        </mxCell>
        <mxCell id="LbipYH2ER2oLmsX_pBrb-1" edge="1" parent="1" source="kTopics" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.75;entryY=0;entryDx=0;entryDy=0;" target="kConsumer">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="kTopics" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#C62828;fillColor=#FFEBEE;" value="Kafka Topics" vertex="1">
          <mxGeometry height="70" width="170" x="1420" y="160" as="geometry" />
        </mxCell>
        <mxCell id="kConsumer" parent="1" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=2;strokeColor=#C62828;fillColor=#FFEBEE;" value="Confluent.Kafka Consumer" vertex="1">
          <mxGeometry height="70" width="200" x="1280" y="270" as="geometry" />
        </mxCell>
        <mxCell id="store" parent="1" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;strokeWidth=2;strokeColor=#37474F;fillColor=#FFFFFF;" value="State Store&#xa;(Cache / DB)" vertex="1">
          <mxGeometry height="110" width="90" x="1240" y="510" as="geometry" />
        </mxCell>
        <mxCell id="eWebWs" edge="1" parent="1" source="cWeb" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;startArrow=blockThin;startFill=1;strokeWidth=2;" target="ws" value="WebSocket">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="215" />
              <mxPoint x="350" y="175" />
            </Array>
            <mxPoint x="300" y="215" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="eWebRest" edge="1" parent="1" source="cWeb" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;" target="rest" value="HTTP">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="215" />
              <mxPoint x="350" y="275" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="eWsRouter" edge="1" parent="1" source="ws" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;entryX=0.001;entryY=0.365;entryDx=0;entryDy=0;entryPerimeter=0;" target="router" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points" />
          </mxGeometry>
        </mxCell>
        <mxCell id="eRouterChannel" edge="1" parent="1" source="router" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;" target="channel" value="enqueue">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="745" y="235" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="eKConsumerChannel" edge="1" parent="1" source="kConsumer" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" value="poll">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1380" y="360" />
            </Array>
            <mxPoint x="1280" y="360" as="sourcePoint" />
            <mxPoint x="860.0000000000002" y="360" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="eChannelBg" edge="1" parent="1" source="channel" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;" target="bg" value="dequeue">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="745" y="375" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="eBgPool" edge="1" parent="1" source="bg" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;" target="pool" value="dispatch">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="875" y="430" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ePoolSerde" edge="1" parent="1" source="pool" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;" target="serde" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1005" y="365" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ePoolProd" edge="1" parent="1" source="pool" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;" target="kProducer" value="produce">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1160" y="430" />
              <mxPoint x="1160" y="195" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="eProdTopics" edge="1" parent="1" source="kProducer" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;" target="kTopics" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="ePoolWs" edge="1" parent="1" source="pool" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;" target="ws" value="push updates">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1005" y="540" />
              <mxPoint x="610" y="540" />
              <mxPoint x="610" y="200" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ePoolStore" edge="1" parent="1" source="pool" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=blockThin;endFill=1;strokeWidth=2;" target="store" value="read/write">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1285" y="480" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="eWsObs" edge="1" parent="1" source="ws" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;endArrow=open;endFill=0;strokeWidth=2;strokeColor=#455A64;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0.639;exitY=-0.003;exitDx=0;exitDy=0;exitPerimeter=0;" target="obs" value="metrics/traces/logs">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="610" y="100" as="sourcePoint" />
            <mxPoint x="910.0000000000002" y="100" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="eBgObs" edge="1" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;endArrow=open;endFill=0;strokeWidth=2;strokeColor=#455A64;" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="830" y="400" />
              <mxPoint x="880" y="400" />
              <mxPoint x="880" y="150" />
            </Array>
            <mxPoint x="830" y="429.9999999999999" as="sourcePoint" />
            <mxPoint x="890" y="150" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="eKafkaObs" edge="1" parent="1" source="kProducer" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;endArrow=open;endFill=0;strokeWidth=2;strokeColor=#455A64;" target="obs" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1300" y="140" />
            </Array>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
