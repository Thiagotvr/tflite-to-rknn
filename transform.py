from rknn.api import RKNN

# Caminho para o modelo
tflite_model_path = 'face_landmark.tflite'  # Substitua pelo modelo correto
rknn_model_path = 'face_landmark.rknn'      # Nome do arquivo de saída

# Inicialize o RKNN
rknn = RKNN()

# Configuração com o target_platform
print('--> Configurando o modelo para a plataforma RK3566')
rknn.config(
    mean_values=[[0, 0, 0]],
    std_values=[[1, 1, 1]],
    target_platform='rk3566'  # Defina a plataforma correta aqui
)

# Carregar o modelo .tflite
print('--> Carregando o modelo TFLite')
ret = rknn.load_tflite(model=tflite_model_path)
if ret != 0:
    print('Erro ao carregar o modelo TFLite')
    exit(ret)

# Otimizar e converter para RKNN
print('--> Otimizando e construindo o modelo RKNN')
ret = rknn.build(do_quantization=False)  # Quantização é opcional
if ret != 0:
    print('Erro ao construir o modelo RKNN')
    exit(ret)

# Exportar o modelo para um arquivo .rknn
print('--> Salvando o modelo RKNN')
ret = rknn.export_rknn(rknn_model_path)
if ret != 0:
    print('Erro ao exportar o modelo RKNN')
    exit(ret)

print('Conversão concluída para:', rknn_model_path)

