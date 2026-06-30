
def diagnose_error(error_message, code_context=""):
    """
    Analyzes an error message and returns a Socratic question instead of a fix.
    
    Args:
        error_message (str): The Python error string.
        code_context (str): Optional context about what code was running.
        
    Returns:
        str: A pedagogical hint/question.
    """
    error = error_message.lower()
    
    if "kinetic energy" in error or "negative" in code_context and "energy" in code_context:
        return "Observe your Kinetic Energy. In classical physics, K = 0.5 * m * v^2. Can this value ever be negative? What does a negative K imply about velocity?"
        
    if "valueerror" in error and "dimension" in error:
        return "Dimensional Mismatch. Are you trying to multiply a [3x1] vector by a [3x3] matrix? Recall linear algebra rules: (M x N) * (N x P) = (M x P)."
        
    if "zerodivisionerror" in error:
        return "Singularity detected. In potentials like Lennard-Jones (1/r^12), what happens when atoms get infinitely close (r -> 0)?"
        
    if "nameerror" in error and "not defined" in error:
        return "It seems a variable is missing. Did you execute the cell above where this variable was defined?"

    # Default generic
    return f"Interesting error: '{error_message}'. If you were the Python interpreter, why would you be confused here?"
