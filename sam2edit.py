# Edit Anything trained with Stable Diffusion + ControlNet + SAM  + BLIP2
import os
import gradio as gr
from diffusers.utils import load_image
from sam2edit_lora import EditAnythingLoraModel, config_dict
from sam2edit_demo import create_demo_template
from huggingface_hub import hf_hub_download, snapshot_download


def create_demo(process, process_image_click=None):

    examples = None
    INFO = f'''
    ## EditAnything https://github.com/sail-sg/EditAnything
    '''
    WARNING_INFO = None

    demo = create_demo_template(process, process_image_click, examples=examples, 
                                    INFO=INFO, WARNING_INFO=WARNING_INFO, enable_auto_prompt_default=True)
    return demo


if __name__ == '__main__':
    model = EditAnythingLoraModel(base_model_path="stabilityai/stable-diffusion-2",
                                  controlmodel_name='LAION Pretrained(v0-4)-SD21', extra_inpaint=False,
                                  lora_model_path=None, use_blip=True)
    demo = create_demo(model.process, model.process_image_click)
    demo.queue().launch(server_name='0.0.0.0')
