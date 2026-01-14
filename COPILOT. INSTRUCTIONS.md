<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

- [X] Verify that the copilot-instructions.md file in the .github directory is created.
- [X] Clarify Project Requirements
- [X] Scaffold the Project
- [X] Customize the Project
- [X] Create and Run Task
- [X] Launch the Project
- [X] Ensure Documentation is Complete

## Objective

Understand the complex structure of this repository with some core modules that feeds services that goes to an ui and focus in solving transversaly the problems or bug reported. Focus on code optimitzation, mantinabilty, readable and not redundat. If you think there is some code already done that can be used to fix the bug use it and just créate new functions if necessary. Scientific robustness must be guaranteed in the computations as this code is part of a research. Always test new funcionalities. You can Access differents read.me that can help you understand the workflow of the code. IF a major imporvemnet is added or a relevant funcionality the update read.me and or requirements.

## Testing Guidelines

- Ensure that all tests must continue to pass, except in cases where syntax changes directly affect the tests.
- After any code edit or refactor, briefly validate in 1-2 lines whether the changes achieve the intended effect, and specify the next action or course-correct if validation fails.

## Execution Guidelines

- Prioritize impactful, large-scale changes over small, trivial optimizations.
- Do not compromise on maintainability or code clarity when reducing code size.
- Validate that the refactor maintains all existing functionality and workflows.
- The resultant overall changes will have reduced the amount of code lines
- If changing something in the frontend check how other pages are strucutred in order to mantain a similar style with the user-firendly focus always.
- When fixing previous problems an approach that deletes more code than adds it is a Good aproaching in order to ensure readability, always if posible and reaches to a excellent result.
  PROGRESS TRACKING:
- Start with the assumption that the code needed to complete the task is already written, if the user proviedes some guide try to find it. If not create the code.
- If any tools are available to manage the above todo list, use it to track progress through this checklist.
- After completing each step, mark it complete and add a summary.
- Read current todo list status before starting each new step.
- After understanding the problem make a checklist (max 10 bullets) outlining your planned approach.
- When executing activate the .venv

## COMMUNICATION RULES:

- Avoid verbose explanations or printing full command outputs.
- If a step is skipped, state that briefly (e.g. "No extensions needed").
- Do not explain project structure unless asked.
- Keep explanations concise and focused.

## DEVELOPMENT RULES:

- Use '.' as the working directory unless user specifies otherwise.
- Avoid adding media or external links unless explicitly requested.
- Use placeholders only with a note that they should be replaced.
- Use VS Code API tool only for VS Code extension projects.
- Once the project is created, it is already opened in Visual Studio Code—do not suggest commands to open this project in Visual Studio again.
- If the project setup information has additional rules, follow them strictly.

## FOLDER CREATION RULES:ºº

- Always use the current directory as the project root.
- If you are running any terminal commands, use the '.' argument to ensure that the current working directory is used ALWAYS.
- Do not create a new folder unless the user explicitly requests it besides a .vscode folder for a tasks.json file.
- If any of the scaffolding commands mention that the folder name is not correct, let the user know to create a new folder with the correct name and then reopen it again in vscode.

## EXTENSION INSTALLATION RULES:

- Only install extension specified by the get_project_setup_info tool. DO NOT INSTALL any other extensions.

##PROJECT CONTENT RULES:

- Avoid adding links of any type (URLs, files, folders, etc.) or integrations that are not explicitly required.
- Avoid generating images, videos, or any other media files unless explicitly requested.
- If you need to use any media assets as placeholders, let the user know that these are placeholders and should be replaced with the actual assets later.
- Ensure all generated components serve a clear purpose within the user's requested workflow.
- If a feature is assumed but not confirmed, prompt the user for clarification before including it.
- If you are working on a VS Code extension, use the VS Code API tool with a query to find relevant VS Code API references and samples related to that query.

## TASK COMPLETION RULES:

- Your task is complete when:
  - Project is successfully scaffolded and compiled without errors
  - copilot-instructions.md file in the .github directory exists in the project
  - README.md file exists and is up to date
  - User is provided with clear instructions to debug/launch the project
  - New tests cover the new functionality added

Before starting a new task in the above plan, update progress in the plan.

- Work through each checklist item systematically.
- Keep communication concise and focused.
- Follow development best practices.

## Code Structure

* Explica com tens organitzat el repo
