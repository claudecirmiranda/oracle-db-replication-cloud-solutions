from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.database import Oracle
from diagrams.aws.database import Aurora
from diagrams.aws.migration import DMS
from diagrams.aws.network import VpnGateway
from diagrams.aws.network import DirectConnect
from diagrams.aws.network import Privatelink
from diagrams.aws.security import SecretsManager
from diagrams.custom import Custom

with Diagram("AWS Database Migration Service", show=False):
    with Cluster("On-Premises"):
        onpremises = Oracle("Banco de Dados\nOracle\nOn-Premises")

    with Cluster("AWS"):
        with Cluster("Soluções de\nConectividade"):
            vpngateway = VpnGateway("VPN Gateway")
            directconnect = DirectConnect("AWS Direct Connect")
            privatelink = Privatelink("AWS PrivateLink")

        with Cluster("Banco de Dados\nDestino"):
            target = Aurora("Banco de Dados\nAurora\nAWS")
            replication = DMS("Processo de\nReplicação de Dados")

        secretsmanager = SecretsManager("Secrets Manager")

    secretsmanager - Edge(label="Autenticação") - vpngateway
    onpremises - Edge(label="VPN") - vpngateway - Edge(label="Direct Connect") - directconnect - Edge(label="AWS PrivateLink") - privatelink - replication
    replication << Edge(label="Extração de dados") >> onpremises
    replication >> Edge(label="Replicação de dados") >> target
