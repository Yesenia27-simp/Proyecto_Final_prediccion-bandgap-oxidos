from external_skills.agent_warmup.context_loader import SKILL_METADATA as context_loader_meta

REGISTRY = {
    "agent_warmup.context_loader": {
        "module": "external_skills.agent_warmup.context_loader",
        "description": context_loader_meta["description"],
        "input": context_loader_meta["input"],
        "output": context_loader_meta["output"],
        "domains": context_loader_meta["domain"],
        "version": context_loader_meta["version"],
    }
}

def load_skill(skill_name):
    return REGISTRY.get(skill_name)
