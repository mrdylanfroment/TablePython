'''mermaid
classDiagram
    %% -----------------------------
    %% Top Level
    %% -----------------------------
    class Workshop {
        +jobs : List~Job~
        --
        +load_job(path)
        +build_in_freecad(job)
        +evaluate_expressions(context)
    }

    class Job {
        +id : str
        +client : str
        +parameters : dict
        +products : List~Product~
        --
        +add_product(product)
        +get_product(name)
    }

    class Product {
        +name : str
        +description : str
        +components : List~Component~
        --
        +add_component(component)
    }

    class Component {
        +name : str
        +type : str
        +dimensions : dict
        +transform : dict   %% may contain expressions
        --
        +resolve_transform(context)
    }



    Workshop "1" --> "1..*" Job : manages
    Job "1" --> "1..*" Product : contains
    Product "1" --> "1..*" Component : includes
# TablePython
Script to create a table in FreeCAD

mermaid'''