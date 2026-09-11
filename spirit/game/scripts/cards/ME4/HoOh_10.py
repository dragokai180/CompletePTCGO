from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="46b2b5dc-b88c-5140-9b46-d8c4030b082b",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic", "HoOh"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=250,
    abilities=[
        Attack(
            title="Flames of Revival",
            game_text="Put up to 3 Basic Pokémon from your discard pile onto your Bench.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Bright Wing",
            game_text="Discard a Fire Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
