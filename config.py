class Args:
    data_root = r'E:\Industrial_defect_detection\dataset'
    train_list = r'E:\Industrial_defect_detection\dataset/train.txt'
    val_list = r'E:\Industrial_defect_detection\dataset/test.txt'
    arch = 'resnet50'  # 网络架构, resnet50或se_resnet50
    num_classes = 7  # 类别数
    batch_size = 32
    lr = 0.001
    momentum = 0.9
    weight_decay = 1e-5
    warm_up = 100  # lr warm_up step
    epoch = 150
    start_epoch = 0
    num_workers = 1
    print_freq = 5
    gpus = '0'  # 使用的GPU, 例如0,1,2,3
    checkpoint = None
    checkpoint_dir = './checkpoint' 
