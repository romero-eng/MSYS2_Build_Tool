import shutil
import traceback
from pathlib import Path

from compile import CodeBase, Dependency


if (__name__ == '__main__'):

    Add_library_codebase: CodeBase | None = None
    Add_codebase: CodeBase | None = None
    use_dynamic_library: bool = False
    clean_up_build_directories: bool = True

    try:

        Add_library_codebase = \
            CodeBase('Arithmetic',
                     Path.cwd()/f'example_C_{'dynamic' if use_dynamic_library else 'static':s}_library',
                     language_standard='C 2018',
                     preprocessor_variables=['ADD_EXPORTS'] if use_dynamic_library else [])

        Add_library: Dependency = Add_library_codebase.generate_as_dependency(use_dynamic_library)

        Add_codebase = \
            CodeBase('Arithmetic',
                     Path.cwd()/'example_C++_code_with_C_Linkage',
                     language_standard='C++ 2020')

        Add_codebase.add_dependency(Add_library)
        Add_codebase.generate_as_executable()

    except Exception:
        print(traceback.format_exc())

    else:
        Add_codebase.test_executable()

    finally:

        if clean_up_build_directories:
            if Add_library_codebase:
                if Add_library_codebase.build_directory.exists():
                    shutil.rmtree(Add_library_codebase.build_directory)
            if Add_codebase:
                if Add_codebase.build_directory.exists():
                    shutil.rmtree(Add_codebase.build_directory)
