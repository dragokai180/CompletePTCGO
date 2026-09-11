from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="f234127c-6733-5e6c-9cac-241f42226e1b",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganaclex.Name",
    display_name="Garganacl ex",
    searchable_by=["Garganacl ex", "Stage 2", "ex", "Garganaclex"],
    subtypes=["Stage 2", "ex"],
    collector_number=89,
    set_code="SV07",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=934,
    abilities=[
        Ability(
            title="Salty Body",
            game_text="This Pokémon can't be affected by any Special Conditions.",
            passive=standard_passive("This Pokémon can't be affected by any Special Conditions."),
        ),
        Attack(
            title="Block Hammer",
            game_text="During your opponent's next turn, this Pokémon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
