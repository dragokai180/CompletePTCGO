from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="5dc14669-ef5f-50e3-851b-e29179de92dc",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torterraex.Name",
    display_name="Torterra ex",
    searchable_by=["Torterra ex", "Stage 2", "ex", "Torterraex"],
    subtypes=["Stage 2", "ex"],
    collector_number=12,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    family_id=387,
    abilities=[
        Attack(
            title="Forest March",
            game_text="This attack does 30 damage for each of your Grass Pokémon in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Jungle Hammer",
            game_text="Heal 50 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
