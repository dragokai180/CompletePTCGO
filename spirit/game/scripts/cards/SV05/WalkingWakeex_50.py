from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="81b4845d-a27d-5484-8e05-b46391940529",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WalkingWakeex.Name",
    display_name="Walking Wake ex",
    searchable_by=["Walking Wake ex", "Basic", "ex", "Ancient", "WalkingWakeex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=50,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=1009,
    abilities=[
        Ability(
            title="Azure Seas",
            game_text="Damage from attacks used by this Pokémon isn't affected by any effects on your opponent's Active Pokémon.",
            passive=standard_passive("Damage from attacks used by this Pokémon isn't affected by any effects on your opponent's Active Pokémon."),
        ),
        Attack(
            title="Catharsis Roar",
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
