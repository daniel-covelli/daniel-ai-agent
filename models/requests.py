from dataclasses import dataclass, field
from typing import Any, Deque, Dict, List, Literal, Optional, TypedDict, Union

from models.core import AgentGoal

Message = Dict[str, Union[str, Dict[str, Any]]]
ConversationHistory = Dict[str, List[Message]]
NextStep = Literal["confirm", "question", "done"]
CurrentTool = str

@dataclass
class AgentGoalWorkflowParams:
    conversation_summary: Optional[str] = None
    prompt_queue: Optional[Deque[str]] = None


@dataclass
class CombinedInput:
    agent_goal: AgentGoal
    tool_params: AgentGoalWorkflowParams

@dataclass
class ToolPromptInput:
    prompt: str
    context_instructions: str

@dataclass
class ValidationInput:
    prompt: str
    conversation_history: ConversationHistory
    agent_goal: AgentGoal


@dataclass
class ValidationResult:
    validationResult: bool
    validationFailedReason: Dict[str, Any] = field(default_factory=dict)