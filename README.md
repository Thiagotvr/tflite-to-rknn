Nesse repositório estão os arquivos necessários para transformar os arquivos tflite para rknn. O objetivo dessa transformação é para usar os arquivos no Radxa Rock3C, visto que os arquivos do mediapipe não rodam diretamente na NPU da placa de desenvolvimento. 

Vale lembrar que deve-se ter o tensorflow instalado. Depois disso é necessário instalar o RKNN Toolkit2 para conseguirmos usar o script 'transform.py'.

	Comando para instalar o RKNN Toolkit: 
		pip install rknn-toolkit2

Nesse repositório já estão os arquivos depois de rodar o script. Mas caso queira usa-los de maneira diferente, basta baixa-los daqui mesmo ou do próprio endereço do github do MediaPipe:

https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/models.md

