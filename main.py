import os
from modules.audio_capture import record_audio
from modules.speech_to_text import transcribe
from modules.keyword_engine import find_keywords
from modules.question_generator import generate_questions
from modules.journal_search import search_papers
from config import CHUNK_DURATION


def run_live_system():

    print("🚀 LIVE VIDEO ANALYZER STARTED\n")

    while True:

        try:
            # 🎧 Capture audio
            audio_file = record_audio(duration=CHUNK_DURATION)

            # 🧠 Transcribe
            text = transcribe(audio_file)
            #print("\n🧠 Heard:", text)

            # 🔎 Keyword detection
            keywords = find_keywords(text)

            if keywords:
                for word in keywords:

                    print(f"\n✅ Keyword Detected: {word}")

                    questions = generate_questions(word)
                    papers = search_papers(word)

                    print("\n❓ Questions:")
                    for q in questions:
                        print("-", q)

                    print("\n📚 Research Papers:")
                    for p in papers:
                        print("-", p)

            else:
                print("❌ No keyword found")

            # 🧹 cleanup
            os.remove(audio_file)

        except KeyboardInterrupt:
            print("\n🛑 Stopped by user")
            break

        except Exception as e:
            print("⚠️ Error:", e)


if __name__ == "__main__":
    run_live_system()
