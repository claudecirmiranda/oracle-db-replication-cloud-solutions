from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.database import Oracle
from diagrams.oci.connectivity import VPN
from diagrams.oci.connectivity import FastConnect
from diagrams.oci.network import ServiceGateway
from diagrams.oci.database import Autonomous
from diagrams.custom import Custom

with Diagram("Oracle GoldenGate na OCI", show=False):
    with Cluster("On-Premise"):
        oracle = Oracle("Banco de Dados\nde Origem")
        extract = Custom("Processo de\nCaptura de Dados","./icon/ogg.png")

    with Cluster("Oracle Cloud Infrastructure"):
        with Cluster("Banco de Dados\nDestino"):
            database = Autonomous("Banco de Dados")
            replicat = Custom("Processo de\nReplicação de Dados","./icon/ogg.png")
        
        with Cluster("Soluções\nde Conectividade"):
            vpn = VPN("Oracle Cloud \nVPN Connect")
            fastconnect = FastConnect("Oracle FastConnect")
            nsg = ServiceGateway("Network Cloud\nService Gateway")
    
    oracle >> Edge(label="Extração dos dados") >> extract >> Edge(label="Transmissão dos dados") >> vpn 
    vpn >> Edge(label="Conexão VPN") >> fastconnect >> Edge(label="Conexão FastConnect") >> nsg >> Edge(label="Gateway de Serviço de Rede") >> replicat
    replicat >> Edge(label="Replicação dos dados") >> database
