from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="1ec62c98-a547-5ba4-886d-38691762c3f5",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluzaex.Name",
    display_name="Veluza ex",
    searchable_by=["Veluza ex", "Basic", "ex", "Veluzaex"],
    subtypes=["Basic", "ex"],
    collector_number=43,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=976,
    abilities=[
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Purging Strike",
            game_text="You may discard your hand. If you discarded any cards in this way, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
