from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


def _basic_psychic_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.PSYCHIC.value in types


card = PokemonCardDef(
    guid="c7d1a144-0a5c-57bc-9c6d-974d5dc46c62",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum",
    searchable_by=["Smoochum","Basic","Smoochum"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    family_id=238,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Delightful Kiss",
            game_text="Search your deck for up to 2 Basic Psychic Energy cards and attach them to 1 of your Benched Pokémon. Then, shuffle your deck.",
            cost={},
            effect=search_attach_energy(
                predicate=_basic_psychic_energy, count=2, distribute=False,
                target_pred=lambda p: not is_in_active_spot(p),
                prompt="Choose up to 2 Basic Psychic Energy cards to attach.",
            ),
        ),
    ],
)
