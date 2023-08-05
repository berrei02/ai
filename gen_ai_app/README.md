# 🦜🔗  LangChain

[LangChain](https://python.langchain.com/docs/get_started/introduction) is a framework for developing applications powered by language models. It enables applications that are agentic and data-ware.

This simplistict fastapi & LangChain project builds a suggestion engine that brainstorms product improvement hypotheses for a user-provided SaaS product. The suggestions can easily be requested from a `POST` api endpoint.

Why hypotheses you might ask? I wanted to check out in how far an api could be built that acts as a Product Manager or Product Designer co-pilot for hypothesis generation about potential product features.

You simply provide a Product Context and the API responds with a set of 5 different hypotheses how you could improve your Software Product.

## Reproduce

```shell
    virtualenv venv
    source venv/bin/activate
    > (venv) pip install -r requirements.txt
    > (venv) make api
```

## Prerequisites

You need to have an OPEN API Key that's working and stored in a `.env` file with the key: `OPEN_API_KEY`.

As of Aug 2023, you need to sign up for a Free Trial to get your credits.
Don't forget to set up a reasonable max budget per month (e.g. 10$).

## Testing

hit the `POST` api at `http://127.0.0.1:8000/suggestion` with this payload below: 
```json
{
    "product_context": "In general, we are helping users to book a Mental Health meeting with a certified psychologist to improve their Mental Health goals. This area of the product deals with finding a suitable psychologist which is a good fit for the user (language, age, background, ...)."
}
```

The API wraps LangChain functionality and delivers a result with
5 product improvement hypotheses (for each category of Google's HEART framework).

```json
[
    {
        "hypothesis": "IF we improve the algorithm for matching users with suitable psychologists based on their language, age, and background, THEN there will be an improvement in adoption."
    },
    {
        "hypothesis": "IF we provide users with personalized recommendations for psychologists based on their previous sessions and ratings, THEN there will be an improvement in engagement."
    },
    {
        "hypothesis": "IF we simplify the process of booking a mental health meeting with a certified psychologist, THEN there will be an improvement in task_success."
    },
    {
        "hypothesis": "IF we implement automated reminders for upcoming mental health meetings, THEN there will be an improvement in retention."
    },
    {
        "hypothesis": "IF we introduce a feature for users to track their progress and set mental health goals, THEN there will be an improvement in happiness."
    }
]
```

## Caveats
- For sure this MVP API is not production-ready
- Depending on your machine, you might need to upgrade langchain after installation with: `pip install --upgrade langchain`

