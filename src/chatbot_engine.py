import langchain
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.schema import HumanMessage

langchain.verbose = True

def chat(message, chat_history) :
	llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

	"""
	messages = chat_history
	user_message = {"role": "user", "content": message}
	messages.append(user_message)
	bot_message = llm.invoke(messages).content
	messages.append(bot_message)
	"""
	user_message = {"role": "user", "content": message}
	chat_history.append(user_message)
	bot_message = llm.invoke(chat_history).content
	chat_history.append({"role": "assistant", "content": bot_message})

	return chat_history