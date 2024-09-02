from util import read_yaml,load_model,load_labels,get_all_models,classify
from camera import Camera

YAML_PATH='src/config.yaml'

def print_menu():
    print('Please select one of the following options:')
    print('1. Load Model')
    print('2. Predict on Image')
    print('3. Activate Video Stream')
    print('4. Quit')
    choice=int(input('Option: '))
    return choice

def choose_model():
    print('\tSelect one of the following saved models:')
    models=get_all_models()
    for i in range(len(models)):
        print(f'\t{i+1}. {models[i]}')
    choice=int(input('\tSelect a model: '))-1
    return models[choice]

def predict_img():
    path=input('\tPlease input the path to the image: ')
    print('\tclassifying...')
    ans=classify(path=path,show=True)
    print(f'\tPrediction: {ans}')

def main():
    if read_yaml(YAML_PATH):
        print('Configurations Loaded!')
    else:
        print('Configurations failed to load. Please double check if config.yaml is present in the src folder.')
    
    if load_labels():
        print('Labels Loaded!')
    else:
        print('Labels failed to load. Please double check if labels_path is correctly defined in config.yaml file.')
    print()

    run_app=True
    
    while run_app:
        choice=print_menu()
        if choice==1:
            model_name=choose_model()
            if load_model(model_name):
                print('\tModel successfully loaded!')
            else:
                print('\tUnable to load model. Please check the error message.')
        elif choice==2:
            predict_img()
        elif choice==3:
            print('\tCamera stream opening...')
            cam=Camera('out')
            cmds=cam.get_cmds()
            for cmd,desc in cmds.items():
                print(f'\tPress \'{cmd}\' to {desc}')
            cam.start_capture()
        else:
            run_app=False
            print('\nGoodbye!')
        if run_app:
            print('\n')


if __name__ == '__main__':
    main()