# TablePython Copilot Instructions

## Project Overview
TablePython is a Python project for programmatically creating tables in FreeCAD. The system uses a hierarchical data model to define table structures that can be built and rendered in FreeCAD.

## Architecture

### Core Data Model
The project follows a strict hierarchical structure (Workshop → Job → Product → Component):

- **Workshop**: Top-level container that manages multiple jobs and orchestrates FreeCAD building
  - Key methods: `load_job()`, `build_in_freecad()`, `evaluate_expressions()`
  - Responsible for expression evaluation across the entire job context

- **Job**: Represents a work order with client info and parameters
  - Contains parameters dict for job-specific configuration
  - Manages a collection of Products

- **Product**: A table product unit containing components
  - Provides container for Component definitions
  - Can have descriptions for documentation

- **Component**: The leaf-level element representing physical table parts
  - Has `type`, `dimensions`, and `transform` attributes
  - The `transform` dict may contain expressions that need resolution
  - Critical: Transforms can reference Job parameters via expressions

### Key Pattern: Expression Resolution
- Components may have expressions in their `transform` dict (e.g., `"width": "${job.parameter_name}"`)
- Expression evaluation happens at the Workshop level via `evaluate_expressions(context)`
- Always resolve transforms through the parent Job's parameter context

## Development Patterns

### Adding Features
1. **When extending the data model**: Update the corresponding class in the hierarchy, then update Workshop's `evaluate_expressions()` method
2. **When adding FreeCAD integration**: All FreeCAD operations should be routed through Workshop's `build_in_freecad()` method
3. **When working with parameters**: Always pass Job context through the evaluation pipeline

### Testing Considerations
- Test expression resolution with Job parameters of various types (strings, numbers, dicts)
- Verify FreeCAD build operations don't mutate the original Component definitions
- Test the full Workshop → Job → Product → Component chain to catch context loss

## Integration Points
- **FreeCAD**: Interfaced through Workshop's `build_in_freecad()` method
- **Expression Engine**: Custom evaluation needed for transform expressions referencing Job parameters
- **External Parameters**: Job parameters drive component dimensions and transforms

## File Structure (Expected)
When implementing:
- Core model classes should live in dedicated modules (one per class or grouped by layer)
- FreeCAD integration logic should be separate from data model logic
- Expression evaluation utilities should be reusable across all component types
