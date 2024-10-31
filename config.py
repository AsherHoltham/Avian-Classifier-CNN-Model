import os

class Config:
    def __init__(self):
        self.local_path = os.path.dirname(os.path.abspath(__file__))

        #Data file path tracking
        self.data_path = os.path.join(self.local_path, 'data')
        self.train_data_path = os.path.join(self.data_path, 'train_data')
        self.test_data_path = os.path.join(self.data_path, 'test_data')

        # Output path tracking
        self.output_path = os.path.join(self.local_path, 'outputs')
        self.model_save_path = os.path.join(self.output_path, 'models')
        self.log_path = os.path.join(self.output_path, 'logs')


        self.learning_rate = 1e-3
        self.batch_size = 16
        self.epochs = 10