# Models

 - Doctor 
    - id        (integer, primary key)
    - name      (string, not null)
    - specialty (string, not null)
 - Appointment
    - id         (integer, primary key)
    - date       (datetime, not null)
    - doctor_id  (integer, not null)
    - patient_id (integer, not null)
 - Patient
    - id   (primary key)
    - name (string, not null)
    - 
# Validation

  - Doctor
    - names must start with 'Dr.'
  - Appointment
    - date must be in the future
    
# Routes

  - GET /doctors
  - GET /doctors/<int:id>
  - POST /doctors
  - PATCH /patients/<int:id>
  - DELETE /appointments/<int:id>
    

# Response Formats

  - GET /doctors
  ```json
  [
      {
          id
          name
          specialty
      }
  ]
  ```
  - GET /doctors/<int:id>
  ```json
  [
      {
          id
          name
          specialty
          appointments: [
            {
                id
                date
                patient: {
                    id
                    name
                }
            }
          ]
      }
  ]
  ```
  - POST /doctors
  ```json
      {
          id
          name
          specialty
      }
  ```
  - PATCH /patients/<int:id>
  ```json
      {
          id
          name
      }
  ```