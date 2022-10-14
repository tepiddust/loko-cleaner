from loko_extensions.model.components import Arg, Component, save_extensions, Input, Output, Dynamic

# Component parameters
input1 = Input(id='json_input', label='JSON Input', service='clean_input', to='cleaned_output')
output1 = Output(id='cleaned_output', label='Cleaned Output')

output_as_a_list = Arg(name="output_as_a_list", label="Output as a list", type="boolean",
                       description="The output will be a list containing all the input elements")

remove_duplicates = Arg(name="remove_duplicates", label="Remove Duplicates", type="boolean",
                        description="Remove duplicates from a list of JSON objects or a list")

replace_null = Arg(name="replace_null", label="Replace None or empty values", type="boolean",
                   description="Remove None or Empty values from JSON objects or a list")

replacing_text = Dynamic(name="replacing_text", label="Replacing Text", dynamicType="text",
                         parent="replace_null", description="Empty or None values will be replaced by this text",
                         required=True,
                         condition="{parent}===true")

key = Dynamic(name="key", label="Key", dynamicType="text",
              parent="remove_duplicates",
              description="The specified key will be used to check for duplicates in a list of JSON objects",
              condition="{parent}===true")

ignore_err = Dynamic(name="ignore_err", label="Ignor Error", parent="remove_duplicates", dynamicType="boolean",
                     condition="{parent}===true",
                     description="Ignore missing key errors")

# Component creation
comp1 = Component(name="Cleaner", args=[output_as_a_list, remove_duplicates, key, ignore_err, replace_null, replacing_text],
                  inputs=[input1],
                  outputs=[output1], configured=False, icon="RiBrush2Fill")
save_extensions([comp1])
