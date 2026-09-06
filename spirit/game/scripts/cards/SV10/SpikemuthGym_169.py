from spirit.game.data_utils import StadiumCardDef, Ability, Activations, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_pokemon_card


def _is_marnies_pokemon_card(card) -> bool:
    if not is_pokemon_card(card):
        return False
    definition = def_for(card.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Marnie's ")


card = StadiumCardDef(
    guid="1732c541-809d-518c-8a72-55d96a921581",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpikemuthGym.Name",
    display_name="Spikemuth Gym",
    searchable_by=["Spikemuth Gym", "Stadium", "SpikemuthGym"],
    subtypes=["Stadium"],
    collector_number=169,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Spikemuth Gym",
        game_text="Once during each player's turn, that player may search their deck for a Marnie's Pokémon, reveal it, and put it into their hand. Then, that player shuffles their deck.",
        activation=Activations.ONCE_PER_TURN,
        condition=deck_nonempty,
        effect=search_to_hand(
            _is_marnies_pokemon_card, count=1, minimum=0,
            prompt="Choose a Marnie's Pokémon to put into your hand.",
        ),
    ),
)
