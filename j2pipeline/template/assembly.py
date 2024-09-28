from j2pipeline.template.load import load_template
from j2pipeline.template.vars import get_vars, substitute

def assemble(path: str, subs: dict[str, str]) -> str:
    template: str = load_template(path=path)
    vars: dict[str, str] = get_vars(j2=template)
    return substitute(j2=template, subs=subs, vars=vars)