# backend.py - FastAPI application to validate pipelines

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List, Dict, Any, Optional
import networkx as nx
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected structure of the request body
class Node(BaseModel):
    id: str
    type: str
    position: Dict[str, Any]
    data: Dict[str, Any]

class Edge(BaseModel):
    source: str
    target: str
    sourceHandle: Optional[str] = None
    targetHandle: Optional[str] = None

class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]  # Expecting edges with 'source' and 'target'

@app.post("/pipelines/parse")
def parse_pipeline(pipeline: Pipeline):
    # Extract nodes and edges
    nodes = pipeline.nodes
    edges = pipeline.edges

    # Create a directed graph using NetworkX
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    G.add_nodes_from([node.id for node in nodes])
    G.add_edges_from([(edge.source, edge.target) for edge in edges])

    # Calculate the number of nodes and edges
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    # Check if the graph is a DAG
    is_dag = nx.is_directed_acyclic_graph(G)

    # Return the response
    return {
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "is_dag": is_dag
    }
