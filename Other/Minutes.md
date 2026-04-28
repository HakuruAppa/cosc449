# Meeting Minutes

## 10 September 2025

deadlines

thesis document - last day of second semester
presentation - tbd

LLM research - last day of second semester

literature review

- google scholar to see what others have done
- spreadsheet with name of paper, publish date, summary, method, results, any other columns
- write a literature review summarizing what was found
- use the literature review to see how to approach the thesis

spreadsheet this week (17th), report 1st of october

come up with project timeline this week to avoid term 2 rush

pick each LLM and why they were chosen for analysis

coming up with what prompts makes sense

coming up with survey questions

domain of questions used for LLMs with justifications

## 17 September 2025

domains - cooking? sustainibility? every day questions?

google scholar - create date range, specific search terms, other site (iee, acm, web of science, pubmed, scopus)

restrict articles to last 5 years, or maybe 2-3, where it was published? journal vs conference

## 1 October 2025

domains - cooking, financial advise, general knowledge, emotional help/opinions (therapy?), industry knowledge

methodolgy, literature review draft, find more studies on llm misinformation,

salto key - sci 200, doreen (?) , key for asc 306, go in through 310

## 8 October 2025

Other possible domains? - coding?

investigate how bad inputs affect how LLMs output is truthful or if they try to correct the user

draft literature review

come up with prompts

## 15 October 2025

Should we prompt LLMS for source? repeat prompt asking for source

check existing studies on how to directly compare llm output and search engine output

look into which LLMs are allowed to use

maybe not use apple intelligence if not available to non-apple users

prompt list

survey questions

literature review draft

consult experts in the domains to doublecheck prompts

## 22 October 2025

DeepSeek application restricted but model itself is not

Apple Intelligence uses ChatGPT (gpt-4o)

Output neither good or bad like if an image is generated or misunderstands prompt logically

finding domain experts

literature review draft in progress

existing studies compare llm output and search engines by task success rather than directly comparing output

establish a reproducable pattern for converting a good input to a bad input?

Separate prompts asking for source as own dataset for comparison in output, further check if sources are good

Change bad inputs to be misinformation rather than simple grammar errors

Check deepseek requirements

Finish misinformation list

Finish survey questions

Finish expert consulting on prompts

## 29 October 2025

"bad" input just misinfo or also false logic?

instead of converting inputs, separate category with common myths?

making thesis topic more specific

- sri lanka? sri lankan perception of LLMs? rate of llm hallucinations in sri lankan cultural contexts?
- kelowna? compare sri lankan context to interior bc context?
- undergraduate students? academia?
- LLM hallucinations in academic information gathering?
- llm hallucination per domain quantification? comparing hallucinating per domains?
- justification for domains? what people complain about most?

make new category of prompts within domains as misconceptions/myths

can still do bad inputs since it is a area to test

check with experts on misconception prompts

for perception can still check comparison with sri lankan and inner bc

solidify thesis topic

## 5 November

vectara used a data set of cnn news articles with human generated summaries to compare to

hallucinations are asymmetric (a is b but b is not always a)

move focus to evaluation framework

see if can find large datasets rather than manually creating

hallucination types: prompt induced, model intrinsic

prompt engineering standard?

survey questions make sure participants can distinguish domains (domain you used most)

collect demographic data

UBC guidelines on data collection

ethics approval so questions needed soon

use qualtrics

nigeria as well for survey?

finish getting experts

## 19 November

remove section 2 until approval

start prompting models

## 26 November

Questionnaire approved?

possible weaknesses listed

fixng prompts to be objective

bad prompt = logic tests

defining niche, defining elaborate

paid models?

microsoft copilot - model not given

No meeting

## 3 December

update thesis topic

remove paid LLMs?

chatgpt - no way to select model without subscription

bad prompt into search engines

carry out study without bad prompts until can figure out method to make them

elaborate questions do not feel necessary, keep niche questions and add to quantity?

hosting: together.ai, openrouter

agree to change topic

send to prof:
<https://privacymatters.ubc.ca/i-want/safe-deepseek-ubc>

make a rough budget for paid LLMs

decide on free LLMs

double check deep reputable source

finish all prompts except 'bad prompts' until its figured out - wasting time

see if there is existing way to make logically flawed prompts

keeping personal advice until new domain can be figured out

questionnaire is good - if dont

ethics backup - online search for each prompt question, see if theres existing online data that answers prompt questions

could do both together, online search while waiting for ethics approval

"exam" send an email before 21st, what was done for 3rd december items, and next steps before the new years

availalibility for next semester send before 21st

meeting next week (10

## 10 December

understand how tokens work for budgeting

check which llama models to use

send email on 17th

## 21 December

ToDo:

- budget - done
- timeline
- availability for semester - done
- next steps
- deepseek sources

## 22 January

Logical fallacies

Personal advice to career/life-goal advice? e.g getting into university, job advice, etc

survey may not be able to do, gather answers for survey questions online/ literature

create spreadsheet for each survey questions in a mini literature-review

see if demographic information can be found

start with free model testing

find expert in life-goal domain - ask maneth worst case

## 29 January

change search to domain specific for survey lit review

reputable sources for white papers from big tech companies

## 5 February

OpenRouter enable websearch?

openrouter API keys?

recording model settings such as reasoning

look into getting API keys

look into "reasoning effort" levels
for now use medium?

maybe email prof garner

begin writing thesis

## 12 February

Reproducable design for elaborate questions

models installed - ollama 3.1, 3.2, 3.3; gemma3; qwen3; deepseekv3.2

no need for openrouter?

justify elaborate questions - see if theres any existing work or find a framework

remove unnecessary models except chatgpt

## 19 February

Academia myth - study design hierarchy?

Life advice section to be completed

## 26 February

Emailed prof garner - meeting on 27th evening

Finish elaborate questions

double check academia and programming myths

career advice prompts mostly completed

news/politics prompts mostly completed

save results in documents in addition to within spreadsheet

began thesis on overleaf

finishing up gemma3 4b prompts

read into existing popular benchmark

manual querying on ollama takes too long - solution is python script
 tested basic script, works!

academia myth: misconception

programming myth: dr ifeoma asking a colleague

possible myth - good programmers dont need to google?

justification for thesis

## 5 March

Discussed with Garner, follow up meeting

Python script done and working,

got outputs for qwen3 4b,8b, qwen3.5 4b, gemma3 4b, gemma3n e2b, e4b

using csv files for data management

adding benchmarks to lit review

have to manually review prompt results;
 suggestion for future is training network on prompts and truths to automate?

wrote justification

why is the sky blue replacing how many countries

LLMs dont have internet search function

weakness is models are selected from those i could run locally

check vscode venv between two machines

redo lit review and justification

## 19 March

Redoing lit review

"bad prompts" - discussed with garner, logical fallacies out of scope

- too many types of fallacies, easier to make new than "convert" a prompt
- bullshit bench: new benchmark that measures LLMs by domain on nonsensical questions
- bad prompts no longer novel

bullshitbench:

- domains of software, finance, legal, medical, physics
- automated judging using aggregated 3 LLMs
- 13 techniques for nonsense

simpleqa:

- similar to our research
- human ai trainers created 4326 qa pairs
- answeribility cutoff date of dec 2023
- their questions were 'challenging'
- domains of sci/tech, politics, art, other, geo, sports, music, tv, history, video games
- had 'true, false, not attempted'
performance saturation?
pertubations of prompts

suggestions for improvement

- using existing dataset and categorizing domains with a deep model

## 25 March

changed What is the highest ranked Computer Science university in Sri Lanka in 2025

analyzed more results

rather than use logical fallacies to make bad prompts, use bullshit benchmark design

set timebound to january 2026

emphasize how much things change

include link to bullshit bench as footnot, any  other links too
 <https://llm-stats.com/benchmarks?category=general>

final meeting on 9th

Finish updating lit review

Keep writing paper

Finish analysing LLM results

make github repo - add iadaji

presentation on 24th april

proper deadline on 27th april

first draft april 17th

thesis:

- answers ALL the 'why' questions
- must be able to read the thesis and understand everything, replicate without needing to talk to measures

presentation:

- summarize thesis,
- topic, outline, intro, motive, related work (1 slide, brief), methodology, results, limitations, future work/improvement, conclusion, thank you
- 15- 16 minutes per person, 4-5 QA period
- 20 slides maximum
- numbered slides
- less text more graphics
- get scored on presentation
- final presentation open to public, can invite people!

## Notes

search engine equivalent answers found in first page of results

prompt is conversational equivalent of search engine key term searches

T/F/P system does not measure per fact in one response, so not in depth per response (unsuitable for comparison purely by a single prompt)

no inter-reliability or validation by second party

could talk to school industrial liasoion office

could reach out to prof ifeoma after grad to continue
