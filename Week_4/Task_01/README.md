# Завдання 1. 
> Написати програму, яка надсилає GET-запит до відкритого API та
виводить статус-код, заголовки і тіло відповіді. Додатково реалізувати POST-запит із
передачею даних.

# To run server

```bash
python -m uvicorn Week_4.Task_01.app:app --host 0.0.0.0 --port 8000

ngrok http 8000
```

Copy from "Forwarding  https://unbrazen-botchy-michele.ngrok-free.dev -> http://localhost:8000"
part https://unbrazen-botchy-michele.ngrok-free.dev and paste it into

```bash
curl -X POST https://api.telegram.org/bot<TOKEN>/setWebhook \ 
-d "url=<Rigth here>/telegram"
```

And it's done. You type message in the Bot and everything should work just fine.

## <div style="color: red">**The AI doesn't work, because the resources were exhausted.**</div>
