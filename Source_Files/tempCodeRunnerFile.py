 # Combobox dropdown menu
        self.param_value = StringVar(value=' Root mean square deviation')
        self.param_combo = ttk.Combobox(self.f1, width = 24, textvariable = self.param_value)

        self.param_combo['values'] = (' Root mean square deviation', 
                          ' Radius of gyration',
                          ' Potential energy',
                          ' Temperature')