"""
external_skills — pytest test suite

Tests cover all skill modules using only stdlib + numpy.
No API keys or external services required.
"""
import sys
import os
import pytest
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from external_skills.agent_warmup import context_loader
from external_skills.ai_mining import toxicity_predictor
from external_skills.orchestration import librarian_rag
from external_skills.pedagogy import socratic_debugger
from external_skills.routing import task_classifier
from external_skills.evaluation import output_scorer
from external_skills.numerical import stability_guardian, basis_set_architect
from external_skills.memory import episodic_retriever
from external_skills.observability import trace_annotator
from external_skills.apis import token_budget_guard
from external_skills import registry


# ── context_loader ───────────────────────────────────────────────────────────

class TestContextLoader:
    def test_warm_up_returns_required_keys(self):
        result = context_loader.warm_up("research")
        assert "system_context" in result
        assert "messages" in result
        assert "domain" in result

    def test_domain_is_preserved(self):
        for domain in ["research", "engineering", "teaching", "nanotechnology", "data_analysis"]:
            result = context_loader.warm_up(domain)
            assert result["domain"] == domain

    def test_messages_have_system_role(self):
        result = context_loader.warm_up("nanotechnology")
        assert result["messages"][0]["role"] == "system"

    def test_custom_domain_requires_config(self):
        with pytest.raises(ValueError):
            context_loader.warm_up("custom")

    def test_custom_domain_with_config(self):
        result = context_loader.warm_up("custom", {"system_prompt": "Eres un experto."})
        assert result["system_context"] == "Eres un experto."

    def test_unknown_domain_raises(self):
        with pytest.raises(ValueError):
            context_loader.warm_up("dominio_inexistente")

    def test_list_available_domains(self):
        domains = context_loader.list_available_domains()
        assert "research" in domains
        assert "custom" in domains
        assert len(domains) >= 6

    def test_apply_to_agent_with_system_message(self):
        class FakeAgent:
            system_message = ""
        agent = context_loader.apply_to_agent(FakeAgent(), "teaching")
        assert len(agent.system_message) > 10

    def test_apply_to_agent_with_backstory(self):
        class FakeAgent:
            backstory = "Experto inicial."
        agent = context_loader.apply_to_agent(FakeAgent(), "engineering")
        assert "Experto inicial." in agent.backstory


# ── task_classifier ──────────────────────────────────────────────────────────

class TestTaskClassifier:
    def test_returns_required_keys(self):
        result = task_classifier.classify("analiza este dataset de nanoparticulas")
        for key in ("category", "recommended_agent", "confidence", "reasoning", "all_scores"):
            assert key in result

    def test_data_analysis_routing(self):
        result = task_classifier.classify("analiza el dataset y visualiza los datos con estadistica")
        assert result["category"] == "data_analysis"
        assert result["confidence"] > 0.0

    def test_code_generation_routing(self):
        result = task_classifier.classify("genera una funcion de Python para calcular el RMSE")
        assert result["category"] == "code_generation"

    def test_unknown_task_low_confidence(self):
        result = task_classifier.classify("xyz abc def")
        assert result["category"] == "unknown"
        assert result["confidence"] < 0.15

    def test_available_agents_constraint(self):
        result = task_classifier.classify(
            "escribe el codigo para preprocesar datos",
            available_agents=["my_code_agent", "my_data_agent"]
        )
        assert result["recommended_agent"] in ["my_code_agent", "my_data_agent"]

    def test_classify_task_alias(self):
        assert task_classifier.classify_task is task_classifier.classify

    def test_all_scores_have_all_categories(self):
        result = task_classifier.classify("investiga el estado del arte")
        for cat in task_classifier.ROUTING_RULES:
            assert cat in result["all_scores"]


# ── output_scorer ────────────────────────────────────────────────────────────

class TestOutputScorer:
    def test_returns_score_result(self):
        result = output_scorer.score_heuristic("Instala numpy con pip install numpy.")
        assert hasattr(result, "score")
        assert hasattr(result, "breakdown")
        assert hasattr(result, "feedback")
        assert hasattr(result, "passed")

    def test_score_in_range(self):
        result = output_scorer.score_heuristic("Texto de prueba con contenido.")
        assert 0.0 <= result.score <= 1.0

    def test_empty_output_low_score(self):
        result = output_scorer.score_heuristic("")
        assert result.score < 0.3

    def test_rich_output_higher_score(self):
        rich = (
            "# Guia de instalacion\n\n"
            "Para instalar el entorno ejecuta:\n\n"
            "```bash\nconda create -n ia_nano python=3.11\nconda activate ia_nano\npip install numpy\n```\n\n"
            "El paquete tiene 3 modulos principales con 42 funciones totales.\n"
            "- Modulo A: procesamiento\n- Modulo B: visualizacion\n- Modulo C: exportacion"
        )
        result = output_scorer.score_heuristic(rich)
        assert result.score > 0.4

    def test_custom_criteria(self):
        criteria = {"length": 0.5, "structure": 0.5}
        result = output_scorer.score_heuristic("texto corto", criteria=criteria)
        assert set(result.breakdown.keys()) == {"length", "structure"}

    def test_llm_none_fallback_to_heuristic(self):
        result = output_scorer.score_with_llm("Texto de prueba.", llm=None)
        assert isinstance(result, output_scorer.ScoreResult)

    def test_passing_threshold(self):
        result = output_scorer.score_heuristic("x", passing_threshold=0.99)
        assert result.passed is False


# ── stability_guardian ───────────────────────────────────────────────────────

class TestStabilityGuardian:
    def test_safe_timestep(self):
        result = stability_guardian.analyze_timestep(1.0, "MD", ["C-C", "C-H"])
        assert "safe" in result
        assert result["safe"] is True

    def test_dangerous_timestep(self):
        result = stability_guardian.analyze_timestep(100.0, "MD", ["O-H"])
        assert result["safe"] is False

    def test_returns_message(self):
        result = stability_guardian.analyze_timestep(2.0, "MD", ["C-C"])
        assert "message" in result
        assert isinstance(result["message"], str)


# ── basis_set_architect ──────────────────────────────────────────────────────

class TestBasisSetArchitect:
    def test_returns_basis(self):
        result = basis_set_architect.select_basis("Au")
        assert "basis" in result
        assert isinstance(result["basis"], str)

    def test_returns_reason(self):
        result = basis_set_architect.select_basis("C")
        assert "reason" in result

    def test_high_precision(self):
        result = basis_set_architect.select_basis("Fe", accuracy_level="high_precision")
        assert "basis" in result


# ── episodic_retriever ───────────────────────────────────────────────────────

class TestEpisodicRetriever:
    def test_add_and_retrieve(self):
        episodic_retriever.add_episode(
            content="Simulacion DFT de Au nanoclusters",
            user_id="user_test",
            metadata={"tags": ["DFT", "Au"]}
        )
        results = episodic_retriever.retrieve(query="Au", user_id="user_test")
        assert isinstance(results, list)

    def test_retrieve_returns_list(self):
        results = episodic_retriever.retrieve(query="inexistente_xyz", user_id="user_new")
        assert isinstance(results, list)


# ── trace_annotator ──────────────────────────────────────────────────────────

class TestTraceAnnotator:
    def test_traced_decorator(self):
        @trace_annotator.traced(notebook="test_nb", concept="test_concept")
        def my_func(x):
            return x * 2

        result = my_func(5)
        assert result == 10

    def test_traced_captures_exception(self):
        @trace_annotator.traced(notebook="test_nb", concept="error_concept")
        def failing_func():
            raise ValueError("error de prueba")

        with pytest.raises(ValueError):
            failing_func()


# ── token_budget_guard ───────────────────────────────────────────────────────

class TestTokenBudgetGuard:
    def test_record_call_within_budget(self):
        guard = token_budget_guard.BudgetGuard(budget_usd=10.0, model="gpt-4o-mini")
        guard.record_call(tokens_input=100, tokens_output=50, label="test")
        assert guard.cost_usd > 0
        assert guard.circuit_open is False

    def test_exceeds_budget_opens_circuit(self):
        guard = token_budget_guard.BudgetGuard(budget_usd=0.000001, model="gpt-4o")
        guard.record_call(tokens_input=1000, tokens_output=1000, label="test")
        assert guard.circuit_open is True

    def test_circuit_open_raises(self):
        guard = token_budget_guard.BudgetGuard(budget_usd=0.000001, model="gpt-4o")
        guard.record_call(tokens_input=1000, tokens_output=1000, label="first")
        with pytest.raises(token_budget_guard.BudgetExceededError):
            guard.record_call(tokens_input=1, tokens_output=1, label="second")

    def test_estimate_tokens(self):
        count = token_budget_guard.estimate_tokens("hola mundo esta es una prueba")
        assert count >= 1

    def test_reset_clears_state(self):
        guard = token_budget_guard.BudgetGuard(budget_usd=0.000001, model="gpt-4o")
        guard.record_call(tokens_input=1000, tokens_output=1000, label="test")
        guard.reset()
        assert guard.circuit_open is False
        assert guard.cost_usd == 0.0


# ── registry ────────────────────────────────────────────────────────────────

class TestRegistry:
    def test_discover_skills_returns_list(self):
        skills = registry.discover_skills()
        assert isinstance(skills, list)
        assert len(skills) > 0

    def test_load_skill_context_loader(self):
        mod = registry.load_skill("context_loader")
        assert hasattr(mod, "warm_up")

    def test_load_skill_task_classifier(self):
        mod = registry.load_skill("task_classifier")
        assert hasattr(mod, "classify")

    def test_load_unknown_skill_raises(self):
        with pytest.raises((KeyError, ValueError)):
            registry.load_skill("skill_que_no_existe")


# ── toxicity_predictor ───────────────────────────────────────────────────────

class TestToxicityPredictor:
    def test_toxic_compound_detected(self):
        result = toxicity_predictor.predict_toxicity("HgCl2")
        assert result["is_toxic"] is True
        assert result["toxicity_score"] > 0.5
        assert len(result["mechanisms"]) > 0

    def test_non_toxic_compound(self):
        result = toxicity_predictor.predict_toxicity("H2O")
        assert result["is_toxic"] is False
        assert result["toxicity_score"] < 0.5
        assert result["mechanisms"] == []

    def test_lead_is_toxic(self):
        result = toxicity_predictor.predict_toxicity("PbSO4")
        assert result["is_toxic"] is True

    def test_returns_confidence(self):
        result = toxicity_predictor.predict_toxicity("AsCl3")
        assert "confidence" in result
        assert isinstance(result["confidence"], str)

    def test_returns_required_keys(self):
        result = toxicity_predictor.predict_toxicity("C6H6")
        for key in ("is_toxic", "toxicity_score", "confidence", "mechanisms"):
            assert key in result


# ── librarian_rag ────────────────────────────────────────────────────────────

class TestLibrarianRag:
    def test_known_compound_returns_data(self):
        result = librarian_rag.fetch_properties("Au")
        assert "bandgap" in result
        assert "structure" in result
        assert result["source"] == "Materials Project (Verified)"

    def test_silicon_properties(self):
        result = librarian_rag.fetch_properties("Si")
        assert result["bandgap"] == 1.12
        assert result["structure"] == "Diamond"

    def test_unknown_compound_returns_error(self):
        result = librarian_rag.fetch_properties("CompuestoInexistente")
        assert "error" in result

    def test_tio2_is_in_db(self):
        result = librarian_rag.fetch_properties("TiO2")
        assert "bandgap" in result
        assert result["bandgap"] == 3.2

    def test_graphene_melting_point(self):
        result = librarian_rag.fetch_properties("Graphene")
        assert result["melting_point"] == 4510


# ── socratic_debugger ────────────────────────────────────────────────────────

class TestSocraticDebugger:
    def test_returns_string(self):
        result = socratic_debugger.diagnose_error("ValueError: negative kinetic energy")
        assert isinstance(result, str)
        assert len(result) > 10

    def test_kinetic_energy_error(self):
        result = socratic_debugger.diagnose_error("negative kinetic energy detected")
        assert "kinetic" in result.lower() or "?" in result

    def test_zero_division_error(self):
        result = socratic_debugger.diagnose_error("ZeroDivisionError: division by zero")
        assert "?" in result or len(result) > 20

    def test_name_error(self):
        result = socratic_debugger.diagnose_error("NameError: name 'x' is not defined")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_generic_error_fallback(self):
        result = socratic_debugger.diagnose_error("SomeObscureError: unknown issue")
        assert "SomeObscureError" in result or "?" in result

