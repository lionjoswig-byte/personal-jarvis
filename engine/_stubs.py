class InferenceEngine:
    def query(self, prompt):
        raise NotImplementedError("Query method not implemented.")


class OllamaEngine(InferenceEngine):
    def query(self, prompt):
        return f"Ollama response to: {prompt}"


class OpenAIEngine(InferenceEngine):
    def query(self, prompt):
        return f"OpenAI response to: {prompt}"


class AnthropicEngine(InferenceEngine):
    def query(self, prompt):
        return f"Anthropic response to: {prompt}"


class EngineFactory:
    @staticmethod
    def create_engine(engine_type):
        engines = {
            'ollama': OllamaEngine,
            'openai': OpenAIEngine,
            'anthropic': AnthropicEngine,
        }
        return engines.get(engine_type.lower())() if engine_type.lower() in engines else None

