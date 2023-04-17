from diagrams import Cluster, Diagram, Edge
from diagrams.azure.database import SQLDatabases, DatabaseForPostgresqlServers
from diagrams.azure.migration import DatabaseMigrationServices
from diagrams.onprem.database import Oracle
from diagrams.onprem.compute import Server
from diagrams.azure.security import KeyVaults
from diagrams.custom import Custom

with Diagram("Azure Database Migration Service", show=False):
    with Cluster("On-Premises"):
        oracle = Oracle("Banco de Dados\nOracle\nOn-Premises")
        agent = Server("Agente de Migração\nDMS")

    with Cluster("Azure"):
        with Cluster("Banco de Dados\nde Destino"):
            sqldb = SQLDatabases("Azure SQL\nDatabase")
            migrator = DatabaseMigrationServices("Azure Database\nMigration Service")
        
        secrets = KeyVaults("Azure Key\nVault")
    
    oracle >> Edge(label="Conexão do Agente de Migração") >> agent
    agent >> Edge(label="Conexão do Agente de Migração") >> migrator
    migrator >> Edge(label="Conexão do Banco de Dados de Destino") >> sqldb
    secrets >> Edge(label="Autenticação") >> migrator
