// PipelineForm.js
import React from 'react';
import { useStore } from './store'; // Import the Zustand store
import axios from 'axios';

const PipelineForm = () => {
    const nodes = useStore(state => state.nodes); // Get nodes from Zustand
    const edges = useStore(state => state.edges); // Get edges from Zustand

    const handleSubmit = async () => {
        const nodes = useStore.getState().nodes; // Fetch nodes from Zustand
        const edges = useStore.getState().edges; // Fetch edges from Zustand
    
        console.log("Nodes:", nodes); // Log nodes to inspect
        console.log("Edges:", edges); // Log edges to inspect
    
        try {
            const response = await axios.post("http://localhost:8000/pipelines/parse", {
                nodes,
                edges,
            });
    
            alert(`Number of Nodes: ${response.data.num_nodes}, Number of Edges: ${response.data.num_edges}, Is DAG: ${response.data.is_dag}`);
        } catch (error) {
            console.error("Error submitting pipeline:", error);
            console.error("Response data:", error.response.data); // Log response data for more details
        }
    };
    return (
        <div>
            <button onClick={handleSubmit}>Submit Pipeline</button>
        </div>
    );
};

export default PipelineForm;
