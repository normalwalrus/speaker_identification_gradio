import gradio as gr
from utils.testing import tester
from typing import Any, List, Optional, Union

inputs: Union[str, gr.Audio] = gr.Audio(source='upload', type='filepath')
# inputs: Union[str, gr.inputs.Audio] = gr.inputs.Audio(source='upload', type='filepath')
outputs: str = 'text'

print(inputs)

if __name__ == "__main__":

    app = gr.Interface(
        tester.predict,
        inputs=inputs,
        outputs=outputs,
        title="Speech Recognition",
        description="Lmao",
    ).launch()
    
    