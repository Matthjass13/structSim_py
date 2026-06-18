class Options:
    def __init__(self):
        self.path_parameters = None          # str
        self.folder_path_out = None          # str
        self.path_simulator = None           # str
        self.cutt_of_planning = 0            # int
        self.cutt_of_planning_h = None       # datetime.datetime (replaces Calendar)
        self.type_of_cutt_of_planning = None # str
        self.stop_criteria = 0.0             # double
        self.path_to_simulator_result_file = None  # str

    def get_path_parameters(self):
        return self.path_parameters

    def set_path_parameters(self, path_parameters):
        self.path_parameters = path_parameters

    def get_folder_path_out(self):
        return self.folder_path_out

    def set_folder_path_out(self, folder_path_out):
        self.folder_path_out = folder_path_out

    def get_path_simulator(self):
        return self.path_simulator

    def set_path_simulator(self, path_simulator):
        self.path_simulator = path_simulator

    def get_cutt_of_planning(self):
        return self.cutt_of_planning

    def set_cutt_of_planning(self, cutt_of_planning):
        self.cutt_of_planning = cutt_of_planning

    def get_cutt_of_planning_h(self):
        return self.cutt_of_planning_h

    def set_cutt_of_planning_h(self, cutt_of_planning_h):
        self.cutt_of_planning_h = cutt_of_planning_h

    def get_type_of_cutt_of_planning(self):
        return self.type_of_cutt_of_planning

    def set_type_of_cutt_of_planning(self, type_of_cutt_of_planning):
        self.type_of_cutt_of_planning = type_of_cutt_of_planning

    def get_stop_criteria(self):
        return self.stop_criteria

    def set_stop_criteria(self, stop_criteria):
        self.stop_criteria = stop_criteria

    def get_path_to_simulator_result_file(self):
        return self.path_to_simulator_result_file

    def set_path_to_simulator_result_file(self, path_to_simulator_result_file):
        self.path_to_simulator_result_file = path_to_simulator_result_file
