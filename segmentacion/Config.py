# Datos de configuracion do adestramento
SEMENTE=None
RUTA_DATASET="../../Datasets/segmentacion/DS_Estradas_1"
IMX_ALTO=512
IMX_ANCHO=512
NUM_ITERACIONS=3
NUM_DIM_ULTCAPA=1
BASE_ROUTE=""
LEARNING_RATE=0.002
EPOCHS=30
BATCH_TAM=2 # Pot de 2
TRAIN_SPLIT=0.8
VALIDACION_SPLIT=0.1
TEST_SPLIT=0.1
MIN_DELTA=0.01
PACIENCIA=8
NUM_CLASES=["Libre", "Estradas"]