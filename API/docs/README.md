# HuskyLink API Docs

Base URL: https://api.tenderloin.tech

## GET /

No parameters

### Success Response

```json
{"online": true}
```

## POST /api/v1/login

| Parameter Name | Datatype | Description |
| --- | --- | --- |
| username | String |  |
| password | String |  |

### Success Response

```json
{
  "result": {
    "password": true
  }
}
```

### Error Response

```json
{
  "result": {
    "password": false,
    "returnedPassword": <String>
  }
}
```

## POST /api/v1/createAccount

| Parameter Name | Datatype | Description |
| --- | --- | --- |
| username | String |  |
| password | String |  |
| realName | String | Name of the user, if the username is “AnishSahoo39”, real name would be “Anish Sahoo” |
| createdAt | Integer | Epoch time of when user joined. |
| userType | String | User type, admin/student/professor |
| isBanned | Boolean | Has the user been banned/blocked from the service? |

### Success Response

```json
{
  "result": {
    "success": true,
    "message": "ok",
    "createdAt": <Integer>
  }
}
```

## GET /api/v1/getUserInfo/<username>

| Parameter Name | Datatype | Description |
| --- | --- | --- |
| username | String | Username to search |

### Success Response

```json
[
  [
    "trent",
    "Trent Wiles",
    1698525331,
    "student",
    "https://trentwil.es/a/FI3S64vsT4.png",
    false,
    null
  ]
]
```

### Error Response

```json
[]
```

## GET /api/v1/listAllUsers

No parameters

### Success Response

```json
[
  [
    "trent",
    "Trent Wiles",
    1698525331,
    "student",
    "https://trentwil.es/a/FI3S64vsT4.png",
    false,
    null
  ],
  [
    "trent452090",
    "Trent Wiles",
    1698525331,
    "student",
    "https://trentwil.es/a/FI3S64vsT4.png",
    false,
    null
  ],
	...
]
```

## GET /api/v1/sortByUserType/<type>

| Parameter Name | Datatype | Description |
| --- | --- | --- |
| type | String | User type, admin/student/professor |

### Success Response

```json
[
  [
    "trent",
    "Trent Wiles",
    1698525331,
    "student",
    "https://trentwil.es/a/FI3S64vsT4.png",
    false,
    null
  ],
  [
    "trent452090",
    "Trent Wiles",
    1698525331,
    "student",
    "https://trentwil.es/a/FI3S64vsT4.png",
    false,
    null
  ],
	...
]
```

### Error Response

```json
[]
```

## GET /api/v1/searchUsers

| Parameter Name | Datatype | Description |
| --- | --- | --- |
| q | String | Search query, searches usernames and realNames |

### Success Response

```json
[
  [
    "trent",
    "Trent Wiles",
    1698525331,
    "student",
    "https://trentwil.es/a/FI3S64vsT4.png",
    false,
    null
  ],
	...
]
```

### Error Response

```json
[]
```

## POST /api/v1/createNewRequest

| Parameter Name | Datatype | Description |
| --- | --- | --- |
| username | String |  |
| title | String | Title of the help request |
| description | String | Description of the help request |
| tags | JSON | tags in a JSON list, ie. [”java”, “linux”, “khoury”] |

### Success Response

```json
{"result": {"uniqueID": <Integer>}}
```

## GET /api/v1/listRequests

No parameters

### Success Response

```json
[
  [
    "None",
    "I need help with my code!",
    "None",
    [
      "reactConsole",
      "khoury"
    ],
    1698527693,
    true,
    2369180787
  ],
	...
]
```

## GET /api/v1/sortRequestsByTag

| Parameter Name | Datatype | Description |
| --- | --- | --- |
| tags | String | Comma separated list of tags. Examples: “khoury” or “khoury,java,linux” |

### Success Response

```json
[
  [
    "None",
    "I need help with my code!",
    "None",
    [
      "reactConsole",
      "khoury"
    ],
    1698527693,
    true,
    2369180787
  ],
	...
]
```

### Error Response

```json
[]
```

## GET /api/v1/searchRequests

| Parameter Name | Datatype | Description |
| --- | --- | --- |
| q | String | Search query, searches titles and descriptions |

### Success Response

```json
[
  [
    "None",
    "I need help with my code!",
    "None",
    [
      "reactConsole",
      "khoury"
    ],
    1698527693,
    true,
    2369180787
  ],
	...
]
```

### Error Response

```json
[]
```