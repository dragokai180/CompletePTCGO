from spirit.game.data_utils import StadiumCardDef, Ability, Activations, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_bench_space
from spirit.game.card_effects.trainers import fossil_search


def _is_antique_trainer(card):
    definition = def_for(getattr(card, "archetype_id", None) or "")
    name = getattr(definition, "display_name", None) or ""
    return "Antique" in name


FOSSIL_QUARRY_ABILITY = Ability(
    title="Fossil Quarry",
    game_text="Once during each player's turn, that player may search their deck for up to 2 Trainer cards with \"Antique\" in their name, put them onto their Bench, and then shuffle their deck.",
    activation=Activations.ONCE_PER_TURN,
    effect=fossil_search(_is_antique_trainer, count=2, label="Antique Trainer"),
    condition=requires_bench_space(1),
)


card = StadiumCardDef(
    guid="969b4c1d-8cec-5939-9ffc-a80d4237debf",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilQuarry.Name",
    display_name="Fossil Quarry",
    searchable_by=["Fossil Quarry","Stadium","FossilQuarry"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    ability=FOSSIL_QUARRY_ABILITY,
)
