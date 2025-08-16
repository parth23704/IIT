# Automated Pet Feeder System

This project is my solution for the University of Canberra’s Introduction to Information Technology (4478/8936) Assignment 1. It’s a simple automated pet feeder for an animal shelter. The feeder gives dry food at 8 AM and 12 PM, wet food at 6 PM, and lets staff press a button for extra food. It checks if food is eaten using a weight sensor, buzzes if something’s wrong (like food not coming out or sitting for 2 hours), and logs events like “[current_time]: Gave Dry, 100g”. I used cheap parts like a motor and sensor, and kept everything easy to understand. I also used Microsoft Copilot to make the flowchart and code simpler.

## Repository Structure

Step1_Analysis: Describes the problem and how parts connect.
  - problem_statement.md`: Explains what the feeder does, inputs (e.g., current_time, bowl_weight, button_status), outputs (e.g., servo motors, buzzer), assumptions, and limits.
  - Block_Diagram.md: Mermaid code for the block diagram showing the Control Unit, Food Dispenser, etc.
  - block_diagram.png: Picture of the block diagram.
Step2_Data: Lists all data used.
  - data_description.md: Table with data (e.g., current_time, dry_schedule, bowl_weight), inputs (e.g., RTC, weight sensor), and outputs (e.g., log, buzzer).
Step3_Flowchart/: Shows the plan for how the feeder works.
  - algorithm.md: Simple steps in plain English (e.g., check time/button, give food).
  - Pet_Feeder_Flowchart.drawio: Draw.io file with the flowchart (uses oval Start/End).
  - flowchart.md: Mermaid code for the simple flowchart.
  - Pet_Feeder_Flowchart.png: Picture of the flowchart.
Step4_Word_Code/: Code in simple words.
  - word_code.md: Easy code using current_time, bowl_weight, etc., to give food, check weight, and log events.
Step5_Testing/: Tests to make sure it works.
  - test_results.md: Test cases (e.g., normal feeding, food not eaten) and fixes like checking bowl_weight > 0.
AI_Reflection/: How I used AI.
  - reflection.md: 200-word explanation of how Microsoft Copilot helped simplify the flowchart and code.

## Submission Details

- Zipped File: All files are in u3311230_Assignment1.zip for Canvas submission.
- Collaborators: Added tutor_uc and lecturer_uc to the repository.
- GitHub: This repository (pet-feeder-project) is private and contains all deliverables.

## How to View Diagrams
- Open Block_Diagram.md or flowchart.md in GitHub or [mermaid.live](https://mermaid.live) to see diagrams.
- Open Pet_Feeder_Flowchart.drawio in [app.diagrams.net](https://app.diagrams.net) to edit the flowchart.


This project is simple, uses cheap parts, and is easy for shelter staff to use. All files are organized for the tutor to check.

