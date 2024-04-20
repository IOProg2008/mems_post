import praw
import time
from dhooks import Webhook
import runer

def main():
  reddit = praw.Reddit(
    client_id="xo-QpLz6TJTpWK8LYTsjfQ",
    client_secret="1XXmupMu0Ghdc8Gv5HdYgIuROdoBGA",
    redirect_uri="https://github.com/IOProg2008/mems_post",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
  )

  hook_url = 'https://discord.com/api/webhooks/1229334407442337812/43VVqhvtSbj6N12PHhz8prbhz7FUy4aLdC3dxlPloClehGgOo0w2890kNpOdYaTYwkUL'
  hook = Webhook(hook_url)
  last_mem = '0'

  submissions = reddit.subreddit('programmingmemes').new(limit=10)
  for submission in submissions:
    if submission.id != last_mem:
      hook.send(submission.url)
      last_mem = submission.id
      break  # Удаляем break, если хотим отправить все 10 постов
      time.sleep(1)  # Даем задержку между отправками, чтобы избежать спама

if __name__=='__main__':
  runer.keep_alive()
  main()