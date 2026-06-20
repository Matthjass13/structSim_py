import os
import subprocess
import sys

folders = [
    # "transpiler",
    # "zeroShot/onlyTask",
    # "zeroShot/persona",
    # "zeroShot/withContext",
    # "zeroShot/negativeConstraint",
    # "chainOfThought/perClass",
    # "oneShot/aSimulationSystemHandler", # 31/44
    "oneShot/concreteModifier",
    # "oneShot/experimentPlanGenerator",
    # "chainOfThought/lenient",
    # "chainOfThought/strict",
    # "chainOfThought/riskFirst/structuredsim"
    # "chainOfThought/perClass",
]


tests_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(tests_dir)

for folder in folders:
    folder_path = os.path.join(project_root, folder)

    print(f"\n{'=' * 60}")
    print(f"Running tests against: {folder_path}")
    print('=' * 60)

    env = os.environ.copy()
    env["PYTHONPATH"] = folder_path
    env["STRUCTSIM_PROJECT_DIR"] = folder_path

    result = subprocess.run(
        [sys.executable, "-m", "pytest", tests_dir, "-v"],
        env=env,
    )

    print(f"\nResult for '{folder}': {'PASSED' if result.returncode == 0 else 'FAILED'} (exit code {result.returncode})")
