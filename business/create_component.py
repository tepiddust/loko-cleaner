from loko_extensions.model.components import Arg, Component, save_extensions, Input, Output, Dynamic, Select

# Component parameters
input1 = Input(id='json_input', label='JSON Input', service='clean_input', to='cleaned_output')
output1 = Output(id='cleaned_output', label='Cleaned Output')

data_type = Select(name="data_type", label="Input data format",
                   options=["JSON", "List"],
                   required=True)

key = Dynamic(name="key", label="Key", dynamicType="text",
              parent="data_type", description="The specified key will be used to check for duplicates",
              required=True,
              condition="{parent}===\"JSON\"")

ignore_err = Dynamic(name="ignore_err", label="Ignor Error", parent="data_type", dynamicType="boolean",
                     condition="{parent}===\"JSON\"",
                     description="Ignore missing key errors")

# Component creation
comp1 = Component(name="Cleaner", args=[data_type, key, ignore_err], inputs=[input1],
                  outputs=[output1], configured=False, icon="RiBrush2Fill")
save_extensions([comp1])
