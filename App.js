// App.js
import { PipelineToolbar } from './toolbar';
import { PipelineUI } from './ui';
import PipelineForm from './submit'; // Import your modified PipelineForm

function App() {
  return (
    <div>
      <PipelineToolbar />
      <PipelineUI />
      <PipelineForm />
    </div>
  );
}

export default App;
