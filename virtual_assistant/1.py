import pyaudio
import websockets
import asyncio
import base64
import json
from api_secrets import *

frames_per_buffer = 3200
format_ = pyaudio.paInt16
channels = 1
rate = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=format_,
    channels=channels,
    rate=rate,
    input=True,
    frames_per_buffer=frames_per_buffer,

)


url = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"


async def send_receive():
    async with websockets.connect(
        url,
        ping_timeout=20,
        ping_interval=5,
        extra_headers={"Authorization": secret_key}
    ) as _ws:
        await asyncio.sleep(0.1)
        session_begins = await _ws.recv()
        print(session_begins)
        print('Sending Messages')

        async def send():
            while True:
                try:
                    data = stream.read(frames_per_buffer, exception_on_overflow=False)
                    data = base64.b64encode(data).decode('utf-8')
                    json_data  = json.dumps({'audio_data': data})
                    await _ws.send(json_data)
                    
                except websockets.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break
                except Exception as e:
                    assert False, 'Not a websocket 4008 error'
                await asyncio.sleep(0.01)
                

                    
        
        async def receive():
            while True:
                try:
                    result_str = await _ws.recv()
                    result = json.loads(result_str)
                    prompt = result['text']
                    if prompt and result['message_type'] == 'FinalTranscipt':
                        print('Me:', prompt)
                        print("Bot", "This is my answer")

                except websockets.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break 
                    
                except Exception as e:
                    assert False, 'Not a websocket 4008 error'
                
            
            
        send_result, receive_result = await asyncio.gather(send(), receive())
        
asyncio.run(send_receive())

    
    





