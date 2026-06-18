class Options:

    def __init__(self):
        self.path_parameters = None
        self.folder_path_out = None
        self.path_simulator = None
        self.cuttof_planning = 0
        self.cuttof_planning_h = None
        self.type_of_cuttof_planning = None
        self.stop_criteria = 0.0
        self.path_to_simulator_result_file = None

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

    def get_cuttof_planning(self):
        return self.cuttof_planning

    def set_cuttof_planning(self, cuttof_planning):
        self.cuttof_planning = cuttof_planning

    def get_cuttof_planning_h(self):
        return self.cuttof_planning_h

    def set_cuttof_planning_h(self, cuttof_planning_h):
        self.cuttof_planning_h = cuttof_planning_h

    def get_type_of_cuttof_planning(self):
        return self.type_of_cuttof_planning

    def set_type_of_cuttof_planning(self, type_of_cuttof_planning):
        self.type_of_cuttof_planning = type_of_cuttof_planning

    def get_stop_criteria(self):
        return self.stop_criteria

    def set_stop_criteria(self, stop_criteria):
        self.stop_criteria = stop_criteria

    def get_path_to_simulator_result_file(self):
        return self.path_to_simulator_result_file

    def set_path_to_simulator_result_file(self, path_to_simulator_result_file):
        self.path_to_simulator_result_file = path_to_simulator_result_file
