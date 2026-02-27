{
  "name": "MLProject",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "category": {
      "type": "string",
      "enum": [
        "NLP",
        "Computer Vision",
        "Tabular Data",
        "Time Series",
        "Reinforcement Learning",
        "Generative AI"
      ]
    },
    "difficulty": {
      "type": "string",
      "enum": [
        "Beginner",
        "Intermediate",
        "Advanced"
      ]
    },
    "tech_stack": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "dataset": {
      "type": "string"
    },
    "dataset_url": {
      "type": "string"
    },
    "github_url": {
      "type": "string"
    },
    "estimated_hours": {
      "type": "number"
    },
    "key_concepts": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "title",
    "description",
    "category",
    "difficulty"
  ]
}