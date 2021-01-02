# Automatic file organizer

A simple python script that organizes your files automatically, through their extension or regular expression.

## Prerequisites

For run this project you'll will need python3.

## Running

You can run the project using the following command:

```shell
python3 app.py
```

## Editing the rules

To organize the files the way you want, you need to edit the rules on [rules.json.](rules.json)

```json
{
  "source": "/path-to-source/",
  "rules": [
    {
      "regex": "regular-expression",
      "moveTo": "/path-to-destination/"
    },
    {
      "extensions": ["extension1", "extension2"],
      "moveTo": "/path-to-destination/"
    },
  ]
}
```

You can create as many rules as you want, following the example above.