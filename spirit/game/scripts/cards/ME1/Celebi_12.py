from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


def _grass_pokemon_or_stadium(card):
    if card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value:
        return True
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.GRASS.value in types


card = PokemonCardDef(
    guid="31ed8763-c8fa-5de7-9ee1-f89295e21045",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi","Basic","Celebi"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    family_id=251,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Traverse Time",
            game_text="Search your deck for up to 3 in any combination of Grass Pokémon and Stadium cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_to_hand(
                _grass_pokemon_or_stadium, count=3, minimum=0,
                prompt="Choose up to 3 Grass Pokémon and Stadium cards.",
            ),
        ),
        Attack(
            title="Solar Cutter",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
