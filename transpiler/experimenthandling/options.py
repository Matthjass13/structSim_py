class Options:

    def __init__(self):
        self.path_parameters = None
        self.folder_path_out = None
        self.path_simulator = None
        self.cutoff_planning = 0
        # For time-based cutoffs, stores the integer value (days/hours/minutes)
        self.cutoff_planning_time_value = 0
        self.type_of_cutoff_planning = None
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

    def get_cutoff_planning(self):
        return self.cutoff_planning

    def set_cutoff_planning(self, cutoff_planning):
        self.cutoff_planning = cutoff_planning

    def get_cutoff_planning_time_value(self):
        return self.cutoff_planning_time_value

    def set_cutoff_planning_time_value(self, value):
        self.cutoff_planning_time_value = value

    def get_type_of_cutoff_planning(self):
        return self.type_of_cutoff_planning

    def set_type_of_cutoff_planning(self, type_of_cutoff_planning):
        self.type_of_cutoff_planning = type_of_cutoff_planning

    def get_type_of_cuttof_planning(self):
        return self.type_of_cutoff_planning

    def get_cuttof_planning(self):
        return self.cutoff_planning

    def get_cuttof_planning_h(self):
        import datetime
        type_ = self.type_of_cutoff_planning
        val = self.cutoff_planning_time_value or self.cutoff_planning
        if type_ == "DAY":
            return datetime.datetime(1, 1, val)
        elif type_ == "HOURS":
            return datetime.datetime(1, 1, 1, val)
        elif type_ == "MINUTES":
            return datetime.datetime(1, 1, 1, 0, val)
        return None

    def get_stop_criteria(self):
        return self.stop_criteria

    def set_stop_criteria(self, stop_criteria):
        self.stop_criteria = stop_criteria

    def get_path_to_simulator_result_file(self):
        return self.path_to_simulator_result_file

    def set_path_to_simulator_result_file(self, path_to_simulator_result_file):
        self.path_to_simulator_result_file = path_to_simulator_result_file
