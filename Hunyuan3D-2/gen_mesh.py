#import trimesh

from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline

pipeline = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained('tencent/Hunyuan3D-2').to("cuda:0")
mesh = pipeline(image='assets/mugcup.png')[0]


mesh.export('results/output_mesh.glb')  
mesh.export('results/output_mesh.obj')  