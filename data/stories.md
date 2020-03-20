## greet_part
* greet
   - utter_greet
> greet_part

## qa_happy_1
> greet_part
* faq
   - action_get_answer
   - utter_helpful
* affirm{"accept": "yes"}
   - utter_goodbye

## qa_happy_3
> greet_part
* faq
   - action_get_answer
   - utter_helpful
* affirm{"accept": "yes"}
   - utter_goodbye

## qa_happy_4
> greet_part
* faq
   - action_get_answer
   - utter_helpful
* deny{"reject":"No"}
   - utter_not_helpful
* faq
   - action_get_answer
   - utter_helpful
* affirm{"accept": "yes"}
   - utter_goodbye

## qa_not_happy_2
> greet_part
* faq
   - action_get_answer
   - utter_helpful
* deny{"reject":"No"}
   - utter_not_helpful
* faq
   - action_get_answer
   - utter_helpful
* deny{"reject":"No"}
   - utter_sorry

## qa_not_happy_2
> greet_part
* faq
   - action_get_answer
   - utter_helpful
* deny{"reject":"No"}
   - utter_not_helpful
* faq
   - action_get_answer
   - utter_helpful
* deny{"reject":"No"}
   - utter_sorry

## qa_not_happy_2
> greet_part
* faq
   - action_get_answer
   - utter_helpful
* deny{"reject":"No"}
   - utter_not_helpful
* faq
   - action_get_answer
   - utter_helpful
* deny{"reject":"No"}
   - utter_sorry

## New Story

* greet
    - utter_greet
* faq
    - action_get_answer
    - utter_helpful
* affirm{"accept": "yes"}
    - utter_goodbye

## New Story

* greet
    - utter_greet
* faq
    - action_get_answer
    - utter_helpful
* affirm
    - utter_goodbye
